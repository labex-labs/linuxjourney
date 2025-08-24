#!/usr/bin/env python3
"""
Linux Journey AI Localization Script

This script translates markdown files in the lessons/en directory to multiple languages
using OpenRouter's Gemini 2.5 Flash model while preserving specific formatting requirements.

Supported languages: zh, es, fr, de, ja, ru, ko, pt

Requirements:
- openai library: pip install openai
- rich library: pip install rich
- click library: pip install click
- OPENROUTER_API_KEY environment variable
- git (for incremental translation features)

Features:
- Beautiful CLI with rich formatting and progress bars
- Preserves YAML front matter structure (translates values, keeps keys)
- Keeps fixed English headings: ## Lesson Content, ## Exercise, ## Quiz Question, ## Quiz Answer
- Translates Exercise content while preserving technical terms and URLs
- Protects code blocks and commands from translation
- Preserves Quiz Answer content exactly as-is
- Enhanced validation to ensure proper Exercise translation
- Organizes translated files in correct language directories
- Git-based incremental translation (translate only changed files)

Usage Examples:
1. Translate all files: python localize_docs.py
2. Translate unstaged changes: python localize_docs.py --git-changes
3. Translate to specific languages: python localize_docs.py --lang zh es fr
4. Translate specific file: python localize_docs.py --path lessons/en/getting-started/linux-history.md
5. Translate specific file to certain languages: python localize_docs.py --path lessons/en/getting-started/linux-history.md --lang zh fr
"""

import os
import sys
import re
import subprocess
import json
import time
from pathlib import Path
from typing import List, Optional, Dict, Set, Tuple
from datetime import datetime

import click
from rich.console import Console
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
)
from openai import OpenAI

# Initialize rich console
console = Console()

# Language mappings
LANGUAGE_NAMES = {
    "zh": "Chinese (Simplified)",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "ja": "Japanese",
    "ru": "Russian",
    "ko": "Korean",
    "pt": "Portuguese",
}

# Fixed English headings that should NOT be translated
FIXED_HEADINGS = [
    "## Lesson Content",
    "## Exercise",
    "## Quiz Question",
    "## Quiz Answer",
]

# Translation model
OPENROUTER_MODEL = "google/gemini-2.5-flash"


class GitChangeDetector:
    """Class to detect changes in git repository."""

    def __init__(self, repo_path: Path):
        self.repo_path = repo_path

    def run_git_command(self, command: List[str]) -> str:
        """Run a git command and return the output."""
        try:
            result = subprocess.run(
                command,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            console.print(f"[red]Git command failed: {' '.join(command)}[/red]")
            console.print(f"[red]Error: {e.stderr}[/red]")
            raise

    def get_unstaged_files(self) -> Set[Path]:
        """Get files with unstaged changes only."""
        try:
            output = self.run_git_command(["git", "diff", "--name-only"])
            changed_files = set()

            for line in output.split("\n"):
                if line.strip():
                    file_path = self.repo_path / line.strip()
                    if file_path.exists():
                        changed_files.add(file_path)

            return changed_files
        except subprocess.CalledProcessError:
            return set()

    def filter_english_markdown_files(self, files: Set[Path]) -> List[Path]:
        """Filter files to only include English markdown files in lessons/en directory."""
        english_files = []
        lessons_en_pattern = re.compile(r"lessons[/\\]en[/\\].*\.md$")

        for file_path in files:
            try:
                relative_path = file_path.relative_to(self.repo_path)
                if lessons_en_pattern.search(str(relative_path)):
                    english_files.append(file_path)
            except ValueError:
                continue

        return sorted(english_files)

    @staticmethod
    def validate_and_filter_files(
        file_paths: List[Path], script_dir: Path
    ) -> List[Path]:
        """Validate and filter specified files to ensure they are English markdown files."""
        valid_files = []
        lessons_en_pattern = re.compile(r"lessons[/\\]en[/\\].*\.md$")

        for file_path in file_paths:
            # Convert to absolute path if relative
            if not file_path.is_absolute():
                file_path = script_dir / file_path

            # Check if file exists
            if not file_path.exists():
                console.print(
                    f"[yellow]Warning: File does not exist: {file_path}[/yellow]"
                )
                continue

            # Check if it's a markdown file
            if not file_path.suffix.lower() == ".md":
                console.print(
                    f"[yellow]Warning: Not a markdown file: {file_path}[/yellow]"
                )
                continue

            # Check if it's in the lessons/en directory
            try:
                relative_path = file_path.relative_to(script_dir)
                if not lessons_en_pattern.search(str(relative_path)):
                    console.print(
                        f"[yellow]Warning: File is not in lessons/en directory: {file_path}[/yellow]"
                    )
                    continue
            except ValueError:
                console.print(
                    f"[yellow]Warning: File is outside the project directory: {file_path}[/yellow]"
                )
                continue

            valid_files.append(file_path)

        return sorted(valid_files)


class DocumentLocalizer:
    """Class to handle document localization using OpenRouter API."""

    def __init__(
        self,
        api_key: str,
        site_url: str = "https://linuxjourney.com",
        site_name: str = "Linux Journey",
    ):
        self.client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
        self.site_url = site_url
        self.site_name = site_name
        self.max_retries = 3
        self.retry_delay = 2.0
        self.stats = {"processed": 0, "errors": 0, "skipped": 0, "validation_failed": 0}
        self.failed_files = []

    def get_translation_schema(self) -> Dict:
        """Get the JSON schema for structured translation output."""
        return {
            "type": "object",
            "properties": {
                "translated_title": {
                    "type": "string",
                    "description": "Translated title",
                },
                "translated_meta_title": {
                    "type": "string",
                    "description": "Translated meta title",
                },
                "translated_meta_description": {
                    "type": "string",
                    "description": "Translated meta description",
                },
                "translated_meta_keywords": {
                    "type": "string",
                    "description": "Translated meta keywords",
                },
                "translated_content": {
                    "type": "string",
                    "description": "Translated main content",
                },
            },
            "required": [
                "translated_title",
                "translated_meta_title",
                "translated_meta_description",
                "translated_meta_keywords",
                "translated_content",
            ],
            "additionalProperties": False,
        }

    def get_translation_prompt(self, target_language: str) -> str:
        """Get the AI prompt for translating documents."""
        return f"""Please translate this Linux learning content to {target_language} following these CRITICAL requirements:

TRANSLATION REQUIREMENTS:
1. **Meta Information**: Translate ONLY the VALUES in title, meta_title, meta_description, and meta_keywords (NOT the keys themselves)
2. **Fixed Headings**: Keep these headings in English exactly as-is:
   - ## Lesson Content
   - ## Exercise  
   - ## Quiz Question
   - ## Quiz Answer
3. **Content Translation**: Translate ALL content under each section EXCEPT where specifically noted:
   - Translate the content under "## Lesson Content" 
   - Translate the content under "## Exercise" 
   - Translate the content under "## Quiz Question"
   - Keep "## Quiz Answer" content EXACTLY as-is (do not translate)
4. **Code Protection**: ABSOLUTELY DO NOT translate ANY content inside:
   - Code blocks (```...```)
   - Inline code (`...`)
   - Linux commands and paths
   - File names and directories
   - Command line examples
   - Configuration file contents
   - URLs and web links (keep URLs exactly as they are - DO NOT modify them)
5. **Quiz Answer**: Keep ALL content under "## Quiz Answer" section EXACTLY as-is - ABSOLUTELY DO NOT translate, modify, or change anything in Quiz Answer sections
6. **Technical Terms**: Keep ALL Linux-specific terms, commands, file names, and technical keywords in English
7. **Natural Translation**: Make the translation sound natural and educational in {target_language} while preserving all technical accuracy

CONTENT STRUCTURE:
- You will receive ONLY the main content WITHOUT YAML front matter
- Main content sections with the fixed headings mentioned above
- Code examples and commands that must remain unchanged
- Exercise content should be translated while preserving any URLs, commands, or technical references
- Quiz content where ONLY the question should be translated (Quiz Answer sections must remain unchanged)

IMPORTANT: 
- Do NOT include YAML front matter (---) in your translated_content output
- Only translate the main content body
- Exercise sections contain instructional content that should be translated to help users understand what to do
- Keep ALL URLs exactly as they appear in the original content - DO NOT modify any links

Please provide:
- translated_title: The translated title value (extracted from original front matter)
- translated_meta_title: The translated meta_title value (extracted from original front matter)
- translated_meta_description: The translated meta_description value (extracted from original front matter)
- translated_meta_keywords: The translated meta_keywords value (extracted from original front matter)
- translated_content: The translated main content ONLY (no YAML front matter, preserving fixed headings and code blocks)

CONTENT TO TRANSLATE:
"""

    def extract_yaml_front_matter(self, content: str) -> Tuple[Dict[str, str], str]:
        """Extract YAML front matter from markdown content."""
        yaml_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", content, re.DOTALL)

        if not yaml_match:
            return {}, content

        yaml_content = yaml_match.group(1)
        main_content = yaml_match.group(2)

        # Parse YAML manually (simple key-value pairs)
        front_matter = {}
        for line in yaml_content.split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip().strip("\"'")
                front_matter[key] = value

        return front_matter, main_content

    def process_labex_links(self, content: str, target_language: str) -> str:
        """Process LabEx links to add language code for non-English languages."""
        if target_language == "en":
            return content

        # Pattern to match LabEx links
        labex_pattern = r"https://labex\.io/(?!(" + target_language + r")/)"

        # Replace with language-specific links
        processed_content = re.sub(
            labex_pattern, f"https://labex.io/{target_language}/", content
        )

        return processed_content

    def validate_translation_quality(
        self, translation_data: Dict[str, str], original_content: str
    ) -> bool:
        """Validate the quality and completeness of translated content."""

        # 1. Check meta fields are not empty or too short
        meta_fields = [
            "translated_title",
            "translated_meta_title",
            "translated_meta_description",
            "translated_meta_keywords",
        ]

        for field in meta_fields:
            value = translation_data.get(field, "").strip()
            if not value:
                console.print(f"[yellow]Warning: {field} is empty[/yellow]")
                return False

        translated_content = translation_data.get("translated_content", "")

        # 2. Check that fixed headings are preserved
        for heading in FIXED_HEADINGS:
            if heading not in translated_content:
                console.print(
                    f"[yellow]Warning: Missing required heading: {heading}[/yellow]"
                )
                return False

        # 3. Check code blocks preservation (count should match)
        original_code_blocks = len(re.findall(r"```[\s\S]*?```", original_content))
        translated_code_blocks = len(re.findall(r"```[\s\S]*?```", translated_content))

        if original_code_blocks != translated_code_blocks:
            console.print(
                f"[yellow]Warning: Code block count mismatch. Original: {original_code_blocks}, Translated: {translated_code_blocks}[/yellow]"
            )
            return False

        # 4. Check inline code preservation (approximate count)
        original_inline_code = len(re.findall(r"`[^`\n]+`", original_content))
        translated_inline_code = len(re.findall(r"`[^`\n]+`", translated_content))

        # Allow some variance in inline code count (±20%) due to formatting differences
        if abs(original_inline_code - translated_inline_code) > max(
            1, original_inline_code * 0.2
        ):
            console.print(
                f"[yellow]Warning: Inline code count significantly different. Original: {original_inline_code}, Translated: {translated_inline_code}[/yellow]"
            )
            return False

        # 5. Check Quiz Answer section preservation (if exists)
        quiz_answer_match = re.search(
            r"## Quiz Answer\s*\n(.*?)(?=##|$)", original_content, re.DOTALL
        )
        if quiz_answer_match:
            original_quiz_answer = quiz_answer_match.group(1).strip()

            # If original Quiz Answer is empty, skip validation for missing Quiz Answer section
            if not original_quiz_answer:
                return True

            translated_quiz_match = re.search(
                r"## Quiz Answer\s*\n(.*?)(?=##|$)", translated_content, re.DOTALL
            )

            if not translated_quiz_match:
                console.print(
                    "[yellow]Warning: Quiz Answer section missing in translation[/yellow]"
                )
                return False

            translated_quiz_answer = translated_quiz_match.group(1).strip()

            # Quiz Answer content should be identical (allowing for minor whitespace differences)
            if original_quiz_answer.replace(" ", "").replace(
                "\n", ""
            ) != translated_quiz_answer.replace(" ", "").replace("\n", ""):
                console.print(
                    "[yellow]Warning: Quiz Answer content was modified during translation[/yellow]"
                )
                return False

        return True

    def translate_document(
        self, content: str, target_language: str, file_path: Path = None
    ) -> Optional[Dict[str, str]]:
        """Translate a markdown document using AI with structured output."""
        prompt = self.get_translation_prompt(LANGUAGE_NAMES[target_language])
        schema = self.get_translation_schema()

        # Extract front matter
        front_matter, main_content = self.extract_yaml_front_matter(content)

        for attempt in range(self.max_retries):
            try:
                if attempt > 0:
                    time.sleep(self.retry_delay * attempt)

                # Prepare the full message with front matter info for context
                front_matter_info = f"""
Original front matter for reference:
title: "{front_matter.get('title', '')}"
meta_title: "{front_matter.get('meta_title', '')}"
meta_description: "{front_matter.get('meta_description', '')}"
meta_keywords: "{front_matter.get('meta_keywords', '')}"

Main content to translate:
"""

                completion = self.client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": self.site_url,
                        "X-Title": self.site_name,
                    },
                    model=OPENROUTER_MODEL,
                    messages=[
                        {
                            "role": "user",
                            "content": f"{prompt}\n\n{front_matter_info}{main_content}",
                        }
                    ],
                    temperature=0.1,
                    max_tokens=8000,
                    response_format={
                        "type": "json_schema",
                        "json_schema": {"name": "translation", "schema": schema},
                    },
                )

                response_content = completion.choices[0].message.content
                if response_content:
                    try:
                        translation_data = json.loads(response_content)
                        required_fields = [
                            "translated_title",
                            "translated_meta_title",
                            "translated_meta_description",
                            "translated_meta_keywords",
                            "translated_content",
                        ]

                        if all(key in translation_data for key in required_fields):
                            # Validate translation quality and completeness
                            if self.validate_translation_quality(
                                translation_data, main_content
                            ):
                                return translation_data
                            else:
                                self.stats["validation_failed"] += 1

                    except json.JSONDecodeError:
                        pass

                if attempt == self.max_retries - 1:
                    return None

            except Exception:
                if attempt == self.max_retries - 1:
                    return None

        return None

    def create_translated_document(
        self,
        original_content: str,
        translation_data: Dict[str, str],
        target_language: str,
    ) -> str:
        """Create the final translated document with proper formatting."""
        front_matter, _ = self.extract_yaml_front_matter(original_content)

        # Helper function to escape quotes in YAML values
        def escape_yaml_value(value: str) -> str:
            """Replace double quotes with single quotes to avoid YAML conflicts."""
            return value.replace('"', "'")

        # Process LabEx links in the translated content
        processed_content = self.process_labex_links(
            translation_data["translated_content"], target_language
        )

        # Create new front matter with translated values
        translated_front_matter = "---\n"

        # Preserve index if it exists
        if "index" in front_matter:
            translated_front_matter += f'index: {front_matter["index"]}\n'

        # Update language code
        translated_front_matter += f'lang: "{target_language}"\n'

        # Add translated fields with escaped quotes
        translated_front_matter += (
            f'title: "{escape_yaml_value(translation_data["translated_title"])}"\n'
        )
        translated_front_matter += f'meta_title: "{escape_yaml_value(translation_data["translated_meta_title"])}"\n'
        translated_front_matter += f'meta_description: "{escape_yaml_value(translation_data["translated_meta_description"])}"\n'
        translated_front_matter += f'meta_keywords: "{escape_yaml_value(translation_data["translated_meta_keywords"])}"\n'
        translated_front_matter += "---\n\n"

        return translated_front_matter + processed_content

    def process_single_file_language(
        self,
        file_path: Path,
        target_language: str,
        skip_existing: bool = True,
    ) -> bool:
        """Process a single file for a single language."""
        try:
            # Determine output path
            lessons_en_dir = file_path.parents[1]
            lessons_dir = lessons_en_dir.parent
            relative_path = file_path.relative_to(lessons_en_dir)
            output_path = lessons_dir / target_language / relative_path

            # Check if file already exists
            if skip_existing and output_path.exists():
                self.stats["skipped"] += 1
                return True

            # Read original content
            with open(file_path, "r", encoding="utf-8") as f:
                original_content = f.read()

            # Generate translation
            translation_data = self.translate_document(
                original_content, target_language, file_path
            )

            if translation_data is None:
                self.stats["errors"] += 1
                self.failed_files.append(f"{file_path} ({target_language})")
                return False

            # Create translated document
            translated_content = self.create_translated_document(
                original_content, translation_data, target_language
            )

            # Create output directory if needed
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Write translated file
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(translated_content)

            # Add delay between translations
            time.sleep(1)
            return True

        except Exception:
            self.stats["errors"] += 1
            self.failed_files.append(f"{file_path} ({target_language})")
            return False

    def process_file(
        self,
        file_path: Path,
        target_languages: List[str],
        skip_existing: bool = True,
    ) -> Dict[str, bool]:
        """Process a single markdown file for all target languages."""
        results = {}

        try:
            # Read the original content once
            original_content = None

            for target_lang in target_languages:
                try:
                    # Determine output path
                    lessons_en_dir = file_path.parents[1]
                    lessons_dir = lessons_en_dir.parent
                    relative_path = file_path.relative_to(lessons_en_dir)
                    output_path = lessons_dir / target_lang / relative_path

                    # Check if file already exists
                    if skip_existing and output_path.exists():
                        results[target_lang] = True
                        self.stats["skipped"] += 1
                        continue

                    # Read original content only when needed
                    if original_content is None:
                        with open(file_path, "r", encoding="utf-8") as f:
                            original_content = f.read()

                    # Generate translation
                    translation_data = self.translate_document(
                        original_content, target_lang, file_path
                    )

                    if translation_data is None:
                        self.stats["errors"] += 1
                        self.failed_files.append(f"{file_path} ({target_lang})")
                        results[target_lang] = False
                        continue

                    # Create translated document
                    translated_content = self.create_translated_document(
                        original_content, translation_data, target_lang
                    )

                    # Create output directory if needed
                    output_path.parent.mkdir(parents=True, exist_ok=True)

                    # Write translated file
                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write(translated_content)

                    results[target_lang] = True

                    # Add delay between language translations
                    time.sleep(1)

                except Exception:
                    self.stats["errors"] += 1
                    self.failed_files.append(f"{file_path} ({target_lang})")
                    results[target_lang] = False

            self.stats["processed"] += 1
            return results

        except Exception:
            self.stats["errors"] += 1
            for lang in target_languages:
                self.failed_files.append(f"{file_path} ({lang})")
                results[lang] = False
            return results

    def find_markdown_files(self, directory: Path) -> List[Path]:
        """Find all markdown files in the directory and subdirectories."""
        markdown_files = [
            file_path for file_path in directory.rglob("*.md") if file_path.is_file()
        ]
        return sorted(markdown_files)

    def save_failed_files(self) -> None:
        """Save the list of failed files to a JSON file."""
        if not self.failed_files:
            return

        failed_files_path = Path("failed_localization_files.json")
        failed_data = {
            "timestamp": datetime.now().isoformat(),
            "total_failed": len(self.failed_files),
            "failed_files": self.failed_files,
        }

        try:
            with open(failed_files_path, "w", encoding="utf-8") as f:
                json.dump(failed_data, f, indent=2, ensure_ascii=False)
        except Exception:
            pass

    def process_files_with_progress(
        self,
        file_list: List[Path],
        target_languages: List[str],
        skip_existing: bool = True,
    ) -> None:
        """Process a list of markdown files with rich progress display."""

        # Calculate total tasks (files × languages)
        total_tasks = len(file_list) * len(target_languages)

        # Display summary
        console.print(
            f"[blue]Processing {len(file_list)} files for {len(target_languages)} languages ({total_tasks} total tasks)[/blue]"
        )

        # Progress tracking
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TextColumn("({task.completed}/{task.total})"),
            console=console,
        ) as progress:

            # Create main progress task based on total language-file combinations
            main_task = progress.add_task("Processing translations", total=total_tasks)

            for file_path in file_list:
                # Process each language for this file
                for lang in target_languages:
                    progress.update(
                        main_task, description=f"Processing {file_path.name} ({lang})"
                    )

                    # Process single file-language combination
                    success = self.process_single_file_language(
                        file_path, lang, skip_existing
                    )

                    # Count processed files (only increment once per file, not per language)
                    if lang == target_languages[0]:  # First language for this file
                        self.stats["processed"] += 1

                    # Advance progress after each language completion
                    progress.advance(main_task)

        # Display final results
        self._display_final_results()

    def _display_final_results(self) -> None:
        """Display final translation results."""
        console.print(
            f"[green]Completed: {self.stats['processed']} files, {self.stats['skipped']} skipped, {self.stats['errors']} errors, {self.stats['validation_failed']} validation failures[/green]"
        )

        if self.failed_files:
            self.save_failed_files()
            console.print(
                "[yellow]Some translations failed, check failed_localization_files.json[/yellow]"
            )


@click.command()
@click.option(
    "--lang",
    multiple=True,
    type=click.Choice(list(LANGUAGE_NAMES.keys())),
    default=list(LANGUAGE_NAMES.keys()),
    help=f"Target languages. Default: all languages ({', '.join(LANGUAGE_NAMES.keys())})",
)
@click.option(
    "--force",
    is_flag=True,
    help="Overwrite existing translated files (default: skip existing files)",
)
@click.option(
    "--git-changes", is_flag=True, help="Only translate files with unstaged changes"
)
@click.option(
    "--path",
    type=click.Path(exists=True, path_type=Path),
    help="Specific markdown file or directory to translate",
)
def main(lang: tuple, force: bool, git_changes: bool, path: Path):
    """
    Linux Journey AI Localization Script

    Translate markdown files to multiple languages using AI while preserving
    code blocks, technical terms, and specific formatting requirements.

    Options:
    - Default: Translate all files in lessons/en directory
    - --git-changes: Only translate files with unstaged changes
    - --path: Translate specific markdown file or directory
    - --lang: Specify target languages (default: all supported languages)
    - --force: Overwrite existing translated files

    Examples:
    python localize_docs.py --path lessons/en/getting-started/linux-history.md
    python localize_docs.py --path lessons/en/getting-started --lang zh es
    """

    console.print("[bold blue]Linux Journey AI Localization[/bold blue]")

    # Check for API key
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        console.print(
            "[red]Error: OPENROUTER_API_KEY environment variable not found[/red]"
        )
        sys.exit(1)

    # Convert tuple to list for easier handling
    target_languages = list(lang) if lang else list(LANGUAGE_NAMES.keys())

    # Create localizer
    localizer = DocumentLocalizer(api_key)

    try:
        script_dir = Path(__file__).parent
        en_directory = script_dir / "lessons" / "en"

        if not en_directory.exists():
            console.print(f"[red]Error: Directory not found: {en_directory}[/red]")
            sys.exit(1)

        # Check for conflicting options
        option_count = sum([bool(git_changes), bool(path)])
        if option_count > 1:
            console.print(
                "[red]Error: Cannot use --git-changes and --path options together[/red]"
            )
            sys.exit(1)

        # Determine which files to process
        if path:
            # Convert to absolute path if relative
            target_path = path if path.is_absolute() else script_dir / path

            if target_path.is_file():
                # Process single file
                valid_files = GitChangeDetector.validate_and_filter_files(
                    [target_path], script_dir
                )

                if not valid_files:
                    console.print(
                        "[red]Error: The specified file is not a valid English markdown file[/red]"
                    )
                    sys.exit(1)

                console.print(f"[blue]Processing 1 specified file[/blue]")
                console.print(f"  • {valid_files[0].relative_to(script_dir)}")

            elif target_path.is_dir():
                # Process directory
                markdown_files = localizer.find_markdown_files(target_path)
                valid_files = GitChangeDetector.validate_and_filter_files(
                    markdown_files, script_dir
                )

                if not valid_files:
                    console.print(
                        "[red]Error: No valid English markdown files found in the specified directory[/red]"
                    )
                    sys.exit(1)

                console.print(
                    f"[blue]Processing {len(valid_files)} files from directory[/blue]"
                )
                for file_path in valid_files[:5]:  # Show first 5 files
                    console.print(f"  • {file_path.relative_to(script_dir)}")
                if len(valid_files) > 5:
                    console.print(f"  ... and {len(valid_files) - 5} more files")
            else:
                console.print("[red]Error: The specified path does not exist[/red]")
                sys.exit(1)

            localizer.process_files_with_progress(
                valid_files, target_languages, skip_existing=not force
            )

        elif git_changes:
            # Process files with unstaged changes
            git_detector = GitChangeDetector(script_dir)
            try:
                changed_files = git_detector.get_unstaged_files()
                english_files = git_detector.filter_english_markdown_files(
                    changed_files
                )

                if not english_files:
                    console.print("[yellow]No unstaged files to translate[/yellow]")
                    return

                localizer.process_files_with_progress(
                    english_files, target_languages, skip_existing=not force
                )

            except subprocess.CalledProcessError:
                markdown_files = localizer.find_markdown_files(en_directory)
                localizer.process_files_with_progress(
                    markdown_files, target_languages, skip_existing=not force
                )
        else:
            # Process all files
            markdown_files = localizer.find_markdown_files(en_directory)
            localizer.process_files_with_progress(
                markdown_files, target_languages, skip_existing=not force
            )

    except KeyboardInterrupt:
        console.print("[yellow]Interrupted[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
