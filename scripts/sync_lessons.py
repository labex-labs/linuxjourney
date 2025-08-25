#!/usr/bin/env python3
"""
Linux Journey Lessons Update Script for Cloudflare D1 Database

This script parses markdown lesson files and updates existing lessons in a Cloudflare D1 database.
It extracts frontmatter, content, exercise, quiz questions and answers from markdown files.
Only existing lessons are updated - no new records are inserted.

Usage:
    python sync_lessons.py --path FILE_OR_DIRECTORY [--no-preview] [--lang LANGUAGE]

Examples:
    # Process a single file and all its language variants (with preview)
    python sync_lessons.py --path lessons/en/filesystem/anatomy-of-a-disk.md

    # Process all markdown files in a directory and all their language variants (with preview)
    python sync_lessons.py --path lessons/en/filesystem/
    python sync_lessons.py --path lessons/

    # Process only specific language files
    python sync_lessons.py --path lessons/en/filesystem/anatomy-of-a-disk.md --lang zh
    python sync_lessons.py --path lessons/ --lang en

    # Skip preview and sync directly
    python sync_lessons.py --path lessons/en/filesystem/anatomy-of-a-disk.md --no-preview
    python sync_lessons.py --path lessons/zh/command-line/ --no-preview --lang zh

Environment Variables Required:
    CLOUDFLARE_API_TOKEN: Your Cloudflare API token
    CLOUDFLARE_ACCOUNT_ID: Your Cloudflare account ID
    CLOUDFLARE_DATABASE_ID: Your D1 database ID (linuxjourney)
    CLOUDFLARE_KV_NAMESPACE_ID: Your KV namespace ID (optional, for cache clearing)
"""

import os
import re
import yaml
import logging
import requests
import click
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Confirm

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Initialize rich console
console = Console()

# Supported languages
SUPPORTED_LANGUAGES = ["en", "zh", "es", "fr", "de", "ja", "ru", "ko", "pt"]


class CloudflareD1Client:
    """Client for interacting with Cloudflare D1 database and KV store"""

    def __init__(
        self,
        api_token: str,
        account_id: str,
        database_id: str,
        kv_namespace_id: Optional[str] = None,
    ):
        self.api_token = api_token
        self.account_id = account_id
        self.database_id = database_id
        self.kv_namespace_id = kv_namespace_id
        self.base_url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/d1/database/{database_id}"
        self.kv_base_url = (
            f"https://api.cloudflare.com/client/v4/accounts/{account_id}/storage/kv/namespaces/{kv_namespace_id}"
            if kv_namespace_id
            else None
        )
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }

    def execute_query(self, sql: str, params: Optional[List] = None) -> Dict:
        """Execute a SQL query against the D1 database"""
        payload = {"sql": sql}
        if params:
            payload["params"] = params

        response = requests.post(
            f"{self.base_url}/query", headers=self.headers, json=payload
        )

        if response.status_code != 200:
            logger.error(
                f"ERROR: Query failed with status {response.status_code}: {response.text}"
            )
            response.raise_for_status()

        return response.json()

    def get_existing_lesson(self, lesson_id: str, lang: str) -> Optional[Dict]:
        """Get existing lesson data from the database"""
        query_sql = """
        SELECT title, content, exercise_content, quiz_question, quiz_answer,
               meta_title, meta_description, meta_keywords
        FROM lessons 
        WHERE lesson_id = ? AND lang = ?
        """

        try:
            result = self.execute_query(query_sql, [lesson_id, lang])
            logger.debug(f"Query result for {lesson_id} ({lang}): {result}")

            # Check if result structure is as expected
            if not isinstance(result, dict) or "result" not in result:
                logger.error(
                    f"ERROR: Unexpected result structure: {type(result)} - {result}"
                )
                return None

            if not isinstance(result["result"], list) or len(result["result"]) == 0:
                logger.error(
                    f"ERROR: Result array is empty or not a list: {result['result']}"
                )
                return None

            first_result = result["result"][0]
            if not isinstance(first_result, dict) or "results" not in first_result:
                logger.error(
                    f"ERROR: First result doesn't have 'results' key: {first_result}"
                )
                return None

            if first_result["results"]:
                row = first_result["results"][0]

                # Helper function to normalize NULL values to empty strings
                def normalize_value(value):
                    if value is None:
                        return ""
                    return str(value) if value else ""

                return {
                    "title": normalize_value(row.get("title")),
                    "content": normalize_value(row.get("content")),
                    "exercise_content": normalize_value(row.get("exercise_content")),
                    "quiz_question": normalize_value(row.get("quiz_question")),
                    "quiz_answer": normalize_value(row.get("quiz_answer")),
                    "meta_title": normalize_value(row.get("meta_title")),
                    "meta_description": normalize_value(row.get("meta_description")),
                    "meta_keywords": normalize_value(row.get("meta_keywords")),
                }
            return None

        except Exception as e:
            logger.error(
                f"ERROR: Failed to query existing lesson {lesson_id} ({lang}): {type(e).__name__}: {str(e)}"
            )
            logger.error(
                f"Query result structure: {result if 'result' in locals() else 'No result available'}"
            )
            return None

    def update_lesson(self, lesson_data: Dict) -> bool:
        """Update an existing lesson in the database"""
        # Check if lesson exists
        check_sql = """
        SELECT id FROM lessons 
        WHERE lesson_id = ? AND lang = ?
        """

        try:
            result = self.execute_query(
                check_sql,
                [
                    lesson_data["lesson_id"],
                    lesson_data["lang"],
                ],
            )

            exists = len(result["result"][0]["results"]) > 0

            if exists:
                # Update existing lesson (保持 id, lesson_id, course_id, order_index, lang, created_at 不变)
                update_sql = """
                UPDATE lessons SET
                    title = ?,
                    content = ?,
                    exercise_content = ?,
                    quiz_question = ?,
                    quiz_answer = ?,
                    meta_title = ?,
                    meta_description = ?,
                    meta_keywords = ?,
                    updated_at = CURRENT_TIMESTAMP
                WHERE lesson_id = ? AND lang = ?
                """

                params = [
                    lesson_data["title"],
                    lesson_data["content"],
                    lesson_data["exercise_content"],
                    lesson_data["quiz_question"],
                    lesson_data["quiz_answer"],
                    lesson_data["meta_title"],
                    lesson_data["meta_description"],
                    lesson_data["meta_keywords"],
                    lesson_data["lesson_id"],
                    lesson_data["lang"],
                ]

                self.execute_query(update_sql, params)
                logger.info(
                    f"SUCCESS: Updated lesson: {lesson_data['lesson_id']} ({lesson_data['lang']})"
                )

                # Clear KV cache for this lesson
                cache_cleared = self.clear_lesson_cache(
                    lesson_data["lesson_id"], lesson_data["lang"]
                )
                if cache_cleared:
                    logger.info(
                        f"INFO: Cache cleared for lesson: {lesson_data['lesson_id']} ({lesson_data['lang']})"
                    )
                else:
                    logger.warning(
                        f"WARNING: Failed to clear cache for lesson: {lesson_data['lesson_id']} ({lesson_data['lang']})"
                    )

                return True

            else:
                logger.warning(
                    f"WARNING: Lesson not found in database: {lesson_data['lesson_id']} ({lesson_data['lang']}). Skipping."
                )
                return False

        except Exception as e:
            logger.error(
                f"ERROR: Failed to update lesson {lesson_data['lesson_id']}: {str(e)}"
            )
            return False

    def clear_lesson_cache(self, lesson_id: str, lang: str) -> bool:
        """Clear KV cache for a specific lesson"""
        if not self.kv_namespace_id or not self.kv_base_url:
            logger.warning(
                "WARNING: KV namespace not configured, skipping cache clearing"
            )
            return True

        cache_key = f"cache:v1:lessons/{lesson_id}:{lang}"

        try:
            response = requests.delete(
                f"{self.kv_base_url}/values/{cache_key}", headers=self.headers
            )

            # KV DELETE returns 200 even if the key doesn't exist
            if response.status_code == 200:
                logger.info(f"INFO: Cleared cache for key: {cache_key}")
                return True
            else:
                logger.warning(
                    f"WARNING: Failed to clear cache for {cache_key}: {response.status_code} - {response.text}"
                )
                return False

        except Exception as e:
            logger.error(
                f"ERROR: Failed to clear cache for {cache_key}: {type(e).__name__}: {str(e)}"
            )
            return False


class MarkdownParser:
    """Parser for Linux Journey markdown lesson files"""

    def __init__(self, lessons_dir: str = "lessons"):
        self.lessons_dir = Path(lessons_dir)

    def parse_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """Parse YAML frontmatter from markdown content"""
        if not content.startswith("---"):
            return {}, content

        # Find the end of frontmatter
        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}, content

        try:
            frontmatter = yaml.safe_load(parts[1])
            body = parts[2].strip()
            return frontmatter or {}, body
        except yaml.YAMLError as e:
            logger.warning(f"WARNING: Failed to parse frontmatter: {e}")
            return {}, content

    def extract_sections(self, content: str) -> Dict[str, str]:
        """Extract different sections from markdown content"""
        sections = {
            "content": "",
            "exercise_content": "",
            "quiz_question": "",
            "quiz_answer": "",
        }

        # Split content by headers
        parts = re.split(r"^##\s+(.+)$", content, flags=re.MULTILINE)

        current_section = "content"
        current_content = parts[0] if parts else content

        for i in range(1, len(parts), 2):
            if i + 1 < len(parts):
                header = parts[i].strip().lower()
                section_content = parts[i + 1].strip()

                if "exercise" in header:
                    # Save current content section before switching
                    if current_section == "content":
                        sections["content"] = current_content.strip()
                    current_section = "exercise_content"
                    sections["exercise_content"] = section_content
                elif "quiz question" in header:
                    # Save current content section before switching
                    if current_section == "content":
                        sections["content"] = current_content.strip()
                    current_section = "quiz_question"
                    sections["quiz_question"] = section_content
                elif "quiz answer" in header:
                    # Save current content section before switching
                    if current_section == "content":
                        sections["content"] = current_content.strip()
                    current_section = "quiz_answer"
                    sections["quiz_answer"] = section_content
                else:
                    # This is a content section (including "Lesson Content" or other headers)
                    if current_section == "content":
                        # For "Lesson Content" headers, only include the content, not the header itself
                        if "lesson content" in header:
                            # Replace the current content with just the section content (without header)
                            current_content = section_content
                        else:
                            # For other content headers, include both header and content
                            current_content += f"\n\n## {parts[i]}\n\n{section_content}"

        # Save the final content section
        if current_section == "content":
            sections["content"] = current_content.strip()

        # Clean up content by only removing extra whitespace, preserving markdown formatting
        for key in sections:
            if sections[key]:
                # Remove extra whitespace only
                sections[key] = re.sub(r"\n\s*\n\s*\n", "\n\n", sections[key]).strip()

        return sections

    def parse_lesson_file(self, file_path: Path) -> Optional[Dict]:
        """Parse a single lesson markdown file"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            frontmatter, body = self.parse_frontmatter(content)
            sections = self.extract_sections(body)

            # Extract lesson metadata from file path
            # Path structure: lessons/{lang}/{course}/{lesson_id}.md
            path_parts = file_path.parts
            lang = path_parts[-3]  # lessons/en/getting-started/lesson.md -> 'en'
            course_id = path_parts[-2]  # -> 'getting-started'
            lesson_id = file_path.stem  # lesson.md -> 'lesson'

            lesson_data = {
                "lesson_id": lesson_id,
                "course_id": course_id,  # 用于查询，但更新时不会修改数据库中的 course_id
                "lang": frontmatter.get("lang", lang),
                "title": frontmatter.get("title", ""),
                "content": sections["content"],
                "exercise_content": sections["exercise_content"],
                "quiz_question": sections["quiz_question"],
                "quiz_answer": sections["quiz_answer"],
                "order_index": frontmatter.get(
                    "index", 0
                ),  # 用于新建记录，更新时不会修改
                "meta_title": frontmatter.get("meta_title", ""),
                "meta_description": frontmatter.get("meta_description", ""),
                "meta_keywords": frontmatter.get("meta_keywords", ""),
            }

            return lesson_data

        except Exception as e:
            logger.error(f"ERROR: Failed to parse {file_path}: {str(e)}")
            return None

    def find_markdown_files_in_directory(self, directory_path: str) -> List[Path]:
        """Find all markdown files in a directory and its subdirectories"""
        directory_path = Path(directory_path)

        if not directory_path.exists():
            logger.error(f"ERROR: Directory not found: {directory_path}")
            return []

        if not directory_path.is_dir():
            logger.error(f"ERROR: Path is not a directory: {directory_path}")
            return []

        # Find all .md files recursively
        md_files = []
        try:
            for md_file in directory_path.rglob("*.md"):
                if md_file.is_file():
                    md_files.append(md_file)
                    logger.info(f"INFO: Found markdown file: {md_file}")

            if not md_files:
                logger.warning(
                    f"WARNING: No markdown files found in directory: {directory_path}"
                )
            else:
                logger.info(f"INFO: Found {len(md_files)} markdown files in directory")

            return sorted(md_files)

        except Exception as e:
            logger.error(f"ERROR: Error scanning directory {directory_path}: {str(e)}")
            return []

    def get_all_language_variants_for_directory(
        self, directory_path: str, target_lang: Optional[str] = None
    ) -> List[Path]:
        """Find all markdown files in directory and get language variants for each"""
        directory_files = self.find_markdown_files_in_directory(directory_path)
        all_variants = []
        processed_lessons = set()  # To avoid duplicates

        for file_path in directory_files:
            try:
                # Get the lesson identifier (course + lesson name)
                path_parts = file_path.parts
                lessons_idx = None
                for i, part in enumerate(path_parts):
                    if part == "lessons":
                        lessons_idx = i
                        break

                if lessons_idx is None or len(path_parts) < lessons_idx + 4:
                    logger.warning(
                        f"WARNING: Skipping file with invalid path format: {file_path}"
                    )
                    continue

                course = path_parts[lessons_idx + 2]
                lesson_file = path_parts[lessons_idx + 3]
                lesson_key = f"{course}/{lesson_file}"

                # Skip if we've already processed this lesson
                if lesson_key in processed_lessons:
                    continue

                processed_lessons.add(lesson_key)

                # Get all language variants for this lesson
                variants = self.get_language_variants(str(file_path), target_lang)
                all_variants.extend(variants)

                logger.info(
                    f"INFO: Added {len(variants)} language variants for {lesson_key}"
                )

            except Exception as e:
                logger.warning(f"WARNING: Error processing {file_path}: {str(e)}")
                continue

        # Remove duplicates and sort
        unique_variants = list(set(all_variants))
        unique_variants.sort()

        logger.info(f"INFO: Total unique files to process: {len(unique_variants)}")
        return unique_variants

    def get_language_variants(
        self, file_path: str, target_lang: Optional[str] = None
    ) -> List[Path]:
        """Get all language variants of a specific lesson file"""
        file_path = Path(file_path)

        # Check if the file exists
        if not file_path.exists():
            logger.error(f"ERROR: File not found: {file_path}")
            return []

        # Parse the file path to extract course and lesson info
        # Expected format: lessons/{lang}/{course}/{lesson}.md
        try:
            path_parts = file_path.parts

            # Find the lessons directory index
            lessons_idx = None
            for i, part in enumerate(path_parts):
                if part == "lessons":
                    lessons_idx = i
                    break

            if lessons_idx is None or len(path_parts) < lessons_idx + 4:
                logger.error(f"ERROR: Invalid file path format: {file_path}")
                logger.error(
                    "ERROR: Expected format: lessons/{lang}/{course}/{lesson}.md"
                )
                return []

            original_lang = path_parts[lessons_idx + 1]
            course = path_parts[lessons_idx + 2]
            lesson_file = path_parts[lessons_idx + 3]

            logger.info(
                f"INFO: Looking for language variants of: {course}/{lesson_file}"
            )

            # Find all language variants
            files = []
            lessons_root = Path(
                *path_parts[: lessons_idx + 1]
            )  # Path to lessons directory

            # Get all language directories
            for lang_dir in lessons_root.iterdir():
                if lang_dir.is_dir():
                    lang_code = lang_dir.name

                    # If target_lang is specified, only process that language
                    if target_lang and lang_code != target_lang:
                        continue

                    variant_file = lang_dir / course / lesson_file
                    if variant_file.exists():
                        files.append(variant_file)
                        logger.info(f"INFO: Found variant: {variant_file}")
                    else:
                        if not target_lang or lang_code == target_lang:
                            logger.warning(f"WARNING: Missing variant: {variant_file}")

            return sorted(files)

        except Exception as e:
            logger.error(f"ERROR: Error parsing file path {file_path}: {str(e)}")
            return []

    def filter_files_by_language(
        self, files: List[Path], target_lang: str
    ) -> List[Path]:
        """Filter files to only include those of the specified language"""
        filtered_files = []

        for file_path in files:
            try:
                # Extract language from file path
                # Expected format: lessons/{lang}/{course}/{lesson}.md
                path_parts = file_path.parts

                # Find the lessons directory index
                lessons_idx = None
                for i, part in enumerate(path_parts):
                    if part == "lessons":
                        lessons_idx = i
                        break

                if lessons_idx is None or len(path_parts) < lessons_idx + 2:
                    continue

                file_lang = path_parts[lessons_idx + 1]

                if file_lang == target_lang:
                    filtered_files.append(file_path)

            except Exception as e:
                logger.warning(
                    f"WARNING: Error extracting language from {file_path}: {str(e)}"
                )
                continue

        return filtered_files


def create_comparison_table(lesson_data: Dict, existing_data: Optional[Dict]) -> Table:
    """Create a rich table comparing new data with existing database data"""
    lesson_id = lesson_data["lesson_id"]
    lang = lesson_data["lang"]

    # Language codes for identification
    lang_codes = {
        "en": "EN",
        "zh": "ZH",
        "ru": "RU",
        "pt": "PT",
        "es": "ES",
        "fr": "FR",
        "de": "DE",
        "ja": "JA",
        "ko": "KO",
    }
    lang_code = lang_codes.get(lang, lang.upper())

    if existing_data is None:
        table_title = f"NEW: Lesson not in database: {lesson_id} [{lang_code}] ({lang})"
        table = Table(title=table_title)
        table.add_column("Field", style="cyan", min_width=16)
        table.add_column("New Value", style="green", max_width=60)
        table.add_column("Length", style="yellow", min_width=8, justify="right")
    else:
        table_title = f"COMPARISON: Lesson: {lesson_id} [{lang_code}] ({lang})"
        table = Table(title=table_title)
        table.add_column("Field", style="cyan", min_width=16)
        table.add_column("Current (DB)", style="red", max_width=40)
        table.add_column("New (File)", style="green", max_width=40)
        table.add_column("Status", style="white", min_width=12)

    # Fields that will be updated
    field_names = [
        "title",
        "content",
        "exercise_content",
        "quiz_question",
        "quiz_answer",
        "meta_title",
        "meta_description",
        "meta_keywords",
    ]

    for field in field_names:
        new_value = str(lesson_data.get(field, ""))

        if existing_data is None:
            # New lesson - show only new values
            display_value = new_value.replace("\n", " ").strip()
            if len(display_value) > 60:
                display_value = display_value[:57] + "..."

            if not display_value:
                display_value = "[dim]<empty>[/dim]"
                char_count = "[dim]0[/dim]"
            else:
                char_count = f"{len(new_value):,}"

            table.add_row(field, display_value, char_count)
        else:
            # Comparison mode
            current_value = str(existing_data.get(field, ""))

            # Truncate for display
            current_display = current_value.replace("\n", " ").strip()
            new_display = new_value.replace("\n", " ").strip()

            if len(current_display) > 40:
                current_display = current_display[:37] + "..."
            if len(new_display) > 40:
                new_display = new_display[:37] + "..."

            # Handle empty values
            if not current_display:
                current_display = "[dim]<empty>[/dim]"
            if not new_display:
                new_display = "[dim]<empty>[/dim]"

            # Determine status
            if current_value == new_value:
                status = "[dim]unchanged[/dim]"
            elif not current_value and new_value:
                status = "[green]NEW[/green]"
                new_display = f"[green]{new_display}[/green]"
            elif current_value and not new_value:
                status = "[red]REMOVED[/red]"
                current_display = f"[red]{current_display}[/red]"
            else:
                status = "[yellow]CHANGED[/yellow]"
                current_display = f"[red]{current_display}[/red]"
                new_display = f"[green]{new_display}[/green]"

            table.add_row(field, current_display, new_display, status)

    return table


def show_comparison_preview(
    lesson_files: List[Path], parser_instance, db_client: CloudflareD1Client
) -> List[Dict]:
    """Show comparison preview between database and file data for all language versions"""
    all_lesson_data = []
    processed_languages = []

    console.print("\n")
    console.print(
        Panel.fit("[bold blue]Database Comparison Preview[/bold blue]", style="blue")
    )

    # Parse all files and query database for all language versions
    for file_path in lesson_files:
        lesson_data = parser_instance.parse_lesson_file(file_path)
        if lesson_data:
            all_lesson_data.append(lesson_data)

            # Get existing data from database for all language versions
            existing_data = db_client.get_existing_lesson(
                lesson_data["lesson_id"], lesson_data["lang"]
            )
            lesson_data["_existing_data"] = existing_data
            processed_languages.append(lesson_data["lang"])

            console.print(f"\n[bold green]FILE: {file_path}[/bold green]")

            # Create comparison table
            table = create_comparison_table(lesson_data, existing_data)
            console.print(table)

        else:
            console.print(f"\n[bold red]ERROR: Failed to parse: {file_path}[/bold red]")

    # Show file count summary with language breakdown
    if all_lesson_data:
        total_count = len(all_lesson_data)
        lang_counts = {}
        lang_codes = {
            "en": "EN",
            "zh": "ZH",
            "ru": "RU",
            "pt": "PT",
            "es": "ES",
            "fr": "FR",
            "de": "DE",
            "ja": "JA",
            "ko": "KO",
        }

        # Count files per language
        for lang in processed_languages:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1

        # Create language summary with codes
        lang_summary = []
        for lang in sorted(lang_counts.keys()):
            code = lang_codes.get(lang, lang.upper())
            count = lang_counts[lang]
            lang_summary.append(f"{code}({count})")

        languages_str = ", ".join(lang_summary)
        console.print(
            f"\n[dim]INFO: Preview shown for: {total_count} file(s) - {languages_str}[/dim]"
        )

    return all_lesson_data


@click.command()
@click.option(
    "--path",
    type=click.Path(exists=True),
    required=True,
    help="Path to a specific lesson file or directory containing lesson files",
)
@click.option(
    "--no-preview",
    is_flag=True,
    default=False,
    help="Skip the comparison preview and proceed directly with synchronization",
)
@click.option(
    "--lang",
    type=click.Choice(SUPPORTED_LANGUAGES),
    help="Only synchronize files for the specified language (e.g., en, zh, es)",
)
def main(path: str, no_preview: bool, lang: Optional[str]):
    """Update existing Linux Journey lessons in Cloudflare D1 database.

    Use --path to specify either:
    - A specific lesson file: lessons/en/filesystem/anatomy-of-a-disk.md (syncs all language variants or specific language)
    - A directory: lessons/en/filesystem/ (processes all .md files and their language variants or specific language)

    Use --lang to only synchronize files for a specific language (e.g., en, zh, es).
    Use --no-preview to skip the comparison preview and proceed directly with synchronization.
    """
    console.print("[bold blue]Linux Journey Lesson Sync Tool[/bold blue]")
    console.print(f"Processing: {path}")
    if lang:
        console.print(f"Language filter: {lang}")
    console.print()

    # Check for required environment variables
    api_token = os.getenv("CLOUDFLARE_API_TOKEN")
    account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
    database_id = os.getenv("CLOUDFLARE_DATABASE_ID")
    kv_namespace_id = os.getenv("CLOUDFLARE_KV_NAMESPACE_ID")  # Optional

    if not all([api_token, account_id, database_id]):
        console.print(
            "[bold red]ERROR: Missing required environment variables:[/bold red]"
        )
        console.print("• CLOUDFLARE_API_TOKEN")
        console.print("• CLOUDFLARE_ACCOUNT_ID")
        console.print("• CLOUDFLARE_DATABASE_ID")
        raise click.Abort()

    # Show KV configuration status
    if kv_namespace_id:
        console.print("[green]INFO: KV cache clearing enabled[/green]")
    else:
        console.print(
            "[yellow]WARNING: KV namespace not configured - cache clearing disabled[/yellow]"
        )
        console.print(
            "[dim]Set CLOUDFLARE_KV_NAMESPACE_ID to enable cache clearing[/dim]"
        )

    # Initialize parser and client
    parser_instance = MarkdownParser("lessons")

    # Determine if path is a file or directory and get files to process
    path_obj = Path(path)
    lesson_files = []

    if path_obj.is_file():
        # Single file - get all language variants
        if path_obj.suffix.lower() != ".md":
            console.print(
                "[bold red]ERROR: File must be a markdown (.md) file[/bold red]"
            )
            raise click.Abort()

        if lang:
            console.print(
                f"[blue]INFO: Processing single file for language: {lang}[/blue]"
            )
        else:
            console.print(
                f"[blue]INFO: Processing single file and its language variants[/blue]"
            )
        lesson_files = parser_instance.get_language_variants(str(path_obj), lang)

    elif path_obj.is_dir():
        # Directory - find all markdown files and their language variants
        if lang:
            console.print(
                f"[blue]INFO: Processing all markdown files in directory for language: {lang}[/blue]"
            )
            # If a specific language is requested and the path is a language-specific directory,
            # process files directly. Otherwise, get language variants.
            if str(path_obj).endswith(f"/{lang}") or f"/{lang}/" in str(path_obj):
                # Path is already language-specific
                lesson_files = parser_instance.find_markdown_files_in_directory(
                    str(path_obj)
                )
            else:
                # Get language variants and filter
                lesson_files = parser_instance.get_all_language_variants_for_directory(
                    str(path_obj), lang
                )
        else:
            console.print(
                f"[blue]INFO: Processing all markdown files in directory and their language variants[/blue]"
            )
            lesson_files = parser_instance.get_all_language_variants_for_directory(
                str(path_obj)
            )

    else:
        console.print(
            "[bold red]ERROR: Path must be either a file or directory[/bold red]"
        )
        raise click.Abort()

    if not lesson_files:
        if lang:
            console.print(
                f"[bold red]ERROR: No lesson files found for language '{lang}' matching criteria[/bold red]"
            )
        else:
            console.print(
                "[bold red]ERROR: No lesson files found matching criteria[/bold red]"
            )
        raise click.Abort()

    if lang:
        console.print(
            f"[green]INFO: Found {len(lesson_files)} lesson files to process for language '{lang}'[/green]"
        )
    else:
        console.print(
            f"[green]INFO: Found {len(lesson_files)} lesson files to process[/green]"
        )

    # Initialize database client to show comparison
    db_client = CloudflareD1Client(api_token, account_id, database_id, kv_namespace_id)

    # Test the connection with a simple query
    console.print("[dim]INFO: Testing database connection...[/dim]")
    try:
        test_result = db_client.execute_query("SELECT 1 as test")
        console.print("[dim green]INFO: Database connection successful[/dim green]")
        logger.debug(f"Test query result: {test_result}")
    except Exception as e:
        console.print(
            f"[bold red]ERROR: Database connection failed: {type(e).__name__}: {str(e)}[/bold red]"
        )
        raise click.Abort()

    # Show comparison with database or parse files directly
    if no_preview:
        console.print("[blue]INFO: Skipping preview, parsing files directly...[/blue]")
        all_lesson_data = []

        # Parse all files without showing comparison
        for file_path in lesson_files:
            lesson_data = parser_instance.parse_lesson_file(file_path)
            if lesson_data:
                all_lesson_data.append(lesson_data)
            else:
                console.print(
                    f"[bold red]ERROR: Failed to parse: {file_path}[/bold red]"
                )

        if not all_lesson_data:
            console.print(
                "[bold red]ERROR: No valid lesson data found to update[/bold red]"
            )
            raise click.Abort()

        console.print(
            f"[green]INFO: Parsed {len(all_lesson_data)} lesson files successfully[/green]"
        )
        console.print("[bold green]INFO: Starting database updates...[/bold green]")
    else:
        # Show comparison with database
        all_lesson_data = show_comparison_preview(
            lesson_files, parser_instance, db_client
        )

        if not all_lesson_data:
            console.print(
                "[bold red]ERROR: No valid lesson data found to update[/bold red]"
            )
            raise click.Abort()

        # Confirm before proceeding
        console.print()
        if not Confirm.ask(
            "[bold yellow]WARNING: Do you want to proceed with the update?[/bold yellow]"
        ):
            console.print("[yellow]INFO: Update cancelled by user[/yellow]")
            raise click.Abort()

        console.print("\n[bold green]INFO: Starting database updates...[/bold green]")

    success_count = 0
    error_count = 0

    # Process each lesson
    for lesson_data in all_lesson_data:
        lesson_id = lesson_data["lesson_id"]
        lang = lesson_data["lang"]
        title = lesson_data["title"]

        try:
            if db_client.update_lesson(lesson_data):
                console.print(
                    f"[green]SUCCESS: Updated: {lesson_id} ({lang}) - {title}[/green]"
                )
                success_count += 1
            else:
                console.print(
                    f"[yellow]WARNING: Skipped: {lesson_id} ({lang}) - Not found in database[/yellow]"
                )
                error_count += 1
        except Exception as e:
            console.print(f"[red]ERROR: Failed: {lesson_id} ({lang}) - {str(e)}[/red]")
            error_count += 1

    # Show final summary
    console.print()
    summary_panel = Panel.fit(
        f"[bold green]SUCCESS: {success_count} successful[/bold green]  [bold red]ERROR: {error_count} errors[/bold red]",
        title="[bold blue]Update Summary[/bold blue]",
        style="blue",
    )
    console.print(summary_panel)

    if error_count > 0:
        raise click.Abort()


if __name__ == "__main__":
    exit(main())
