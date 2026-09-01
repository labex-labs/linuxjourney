#!/usr/bin/env python3
"""Normalize single-choice directives to the LabEx sync format.

The learning sync API expects the question text on the same line as the
single-choice directive header:

    :::single-choice{#question-id} Question text

This script converts the older two-line form in Markdown lesson files while
leaving already-normalized directives unchanged.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


HEADER_PATTERN = re.compile(
    r"^(?P<indent>[ \t]*):::single-choice\{#(?P<id>[A-Za-z0-9_-]+)\}[ \t]*$"
)


def markdown_files(paths: list[Path]) -> list[Path]:
    files: set[Path] = set()
    for path in paths:
        if path.is_dir():
            files.update(candidate for candidate in path.rglob("*.md") if candidate.is_file())
        elif path.is_file() and path.suffix.lower() == ".md":
            files.add(path)
        else:
            raise ValueError(f"path is not a Markdown file or directory: {path}")
    return sorted(files)


def normalize(content: str, source: Path) -> tuple[str, int]:
    lines = content.splitlines(keepends=True)
    output: list[str] = []
    changes = 0
    index = 0

    while index < len(lines):
        line = lines[index]
        header_text = line.rstrip("\r\n")
        header = HEADER_PATTERN.fullmatch(header_text)
        if header is None:
            output.append(line)
            index += 1
            continue

        if index + 1 >= len(lines):
            raise ValueError(f"{source}:{index + 1}: single-choice header has no question")

        question_line = lines[index + 1]
        question = question_line.rstrip("\r\n").strip()
        if not question or question.startswith("::") or question.startswith("```") or question.startswith("~~~"):
            raise ValueError(
                f"{source}:{index + 1}: single-choice header is not followed by a valid question"
            )

        newline = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
        output.append(f"{header.group('indent')}:::single-choice{{#{header.group('id')}}} {question}{newline}")
        changes += 1
        index += 2

    return "".join(output), changes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path("lessons")],
        help="Markdown files or directories to process (default: lessons)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="report files requiring normalization without modifying them",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        files = markdown_files(args.paths)
        changed_files = 0
        changed_directives = 0
        for path in files:
            with path.open("r", encoding="utf-8", newline="") as source:
                content = source.read()
            normalized, changes = normalize(content, path)
            if changes == 0:
                continue
            changed_files += 1
            changed_directives += changes
            if args.check:
                print(f"would normalize {changes:>2} directive(s): {path}")
            else:
                with path.open("w", encoding="utf-8", newline="") as destination:
                    destination.write(normalized)
                print(f"normalized {changes:>2} directive(s): {path}")
    except (OSError, UnicodeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    action = "require normalization" if args.check else "normalized"
    print(f"{changed_directives} directive(s) in {changed_files} file(s) {action}")
    return 1 if args.check and changed_files else 0


if __name__ == "__main__":
    raise SystemExit(main())
