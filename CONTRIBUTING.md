# Contributing to Linux Journey

Thank you for helping improve Linux Journey. This repository contains course metadata, lesson content, and course images.

## Contribution Rules

- Keep each pull request focused on one topic and change no more than 3 files.
- Write new lessons in English under `lessons/en/`. LabEx handles initial translations.
- Preserve accurate content and metadata unless your contribution needs to change them.
- Use the schemas and lesson structure documented below.
- Test commands and expected output whenever it is safe and practical.

## Repository Structure

```text
courses/<course-id>.yml
images/courses/<course-id>.png
lessons/<language-code>/<course-id>/<lesson-id>.md
```

Course and lesson IDs, directory names, and Markdown filenames use lowercase kebab-case. A lesson's path must agree with its `lesson_id`, `course_id`, and `lang` values. For example, `lessons/en/command-line/the-shell.md` belongs to the `command-line` course and uses the lesson ID `the-shell` and language `en`.

The maintained language directories are `de`, `en`, `es`, `fr`, `ja`, `ko`, `pt`, `ru`, and `zh`. Contributions may correct or improve lesson content, translations, course metadata, or artwork. Keep revisions as small as possible while leaving the affected content accurate and coherent.

## Course Metadata

Each course is defined in `courses/<course-id>.yml`:

```yaml
id: command-line
category:
  id: grasshopper
image_url: https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/courses/command-line.png
order_index: 1
translations:
  en:
    title: "Command Line"
    description: "A concise course description."
    faqs:
      - question: "A common learner question?"
        answer: "A clear, self-contained answer."
    meta_title: "Linux Command Line Course"
    meta_description: "A specific, search-friendly course description."
    meta_keywords: "Linux command line, shell basics, Linux commands"
```

The filename and `id` must match. Use the category ID `grasshopper`, `journeyman`, or `networking-nomad`, and keep `order_index` unique within that category. When shared course facts change, update the affected translations consistently; do not add placeholder or machine-generated translations.

## Lesson Format

### Front Matter

Every lesson starts with these fields in this order:

```yaml
---
lesson_id: "the-shell"
course_id: "command-line"
lang: "en"
order_index: 1
title: "The Shell"
description: "Learn what the Linux shell is and how commands are executed."
meta_title: "The Shell - Command Line"
meta_description: "Learn what the Linux shell is, how the Bash prompt works, and how to run your first command."
meta_keywords: "linux shell, bash shell, command line, linux terminal"
---
```

- `lesson_id` matches the filename without `.md`.
- `course_id` matches the parent course directory and a file in `courses/`.
- `lang` matches the language directory and uses an ISO 639-1 code.
- `order_index` is an unquoted number unique within the course and language.
- `description` is one concise sentence describing the lesson's topic or outcome.
- `meta_title` normally follows `Lesson Title - Course Title`.
- `meta_description` is specific and concise; `meta_keywords` is a comma-separated string.
- String values use double quotes. Numbers and booleans are not quoted.

### Body Structure

- Do not add a level-one heading; the application renders `title` as the page title.
- Use level-two headings for top-level topics and lower levels only for real hierarchy.
- Explain each idea before asking a question about it.
- Integrate practice, resources, and explanations into the relevant topic instead of creating standalone exercise, quiz, answer, common-questions, or FAQ sections.
- Include 3–5 meaningful `single-choice` checks throughout the lesson.
- Make `## Summary` the final section.

### Single-choice Checks

Place each check immediately after the content it assesses:

```markdown
:::single-choice{#identify-regular-user-prompt} Which symbol normally ends a regular user's shell prompt?

::option[`#`]{#root-prompt-symbol explanation="This normally identifies a root prompt, which has elevated privileges."}
::option[`$`]{#regular-prompt-symbol .correct explanation="A regular user's shell prompt normally ends in `$`."}
::option[`/`]{#path-separator-symbol explanation="A slash separates parts of a filesystem path; it does not identify a regular-user prompt."}
:::
```

Each check must:

- put the question on the same line as `:::single-choice{#component-id}`;
- contain exactly three plausible options and exactly one `.correct` marker;
- give every option a specific, non-empty `explanation`;
- use stable lowercase kebab-case component and option IDs;
- use IDs unique across the English lesson collection, while translations reuse the corresponding English IDs;
- be answerable from content that appears before it; and
- close with `:::` on its own line.

Explain why the correct option fits and why each distractor does not, using concepts already taught. Keep feedback neutral, self-contained, and brief. Vary correct-answer positions.

Options should use parallel grammar and comparable detail. The correct answer must not stand out because it is longer, more specific, or more qualified. Distractors should represent plausible beginner misunderstandings, and exactly one answer must be unambiguously correct.

### Summary

End with one short sentence followed by no more than five concise learning outcomes:

```markdown
## Summary

You can now explain the role of a shell and interact with a basic shell prompt.

1. Distinguish between a terminal and a shell.
2. Identify a command prompt.
3. Run a simple command with `echo`.
```

## Writing Guidelines

- Use clear, direct language and define technical terms when introduced.
- Prefer concrete explanations and realistic examples over jargon.
- Teach prerequisites before relying on them.
- Use correct product capitalization in learner-facing text.
- Use fenced code blocks with a suitable language such as `bash` or `plaintext`.
- In terminal sessions, use `$` for regular users and `#` for root, and make clear that prompts are not typed.
- Show expected output when it helps learners verify a result.
- Warn readers before commands that require root access or can modify or remove data.

## Translation Guidelines

Do not create translations for a new lesson or start a new full-language translation. Native speakers are welcome to improve files in an existing language directory by correcting grammar, phrasing, and technical terminology.

Keep the translation aligned with the English source. Preserve commands, code, links, file paths, directive syntax, and all IDs. Translate learner-facing titles, headings, questions, options, explanations, and prose naturally. Note substantially outdated source alignment in the pull request.

## Course Map

- **Grasshopper:** `getting-started`, `command-line`, `text-fu`, `advanced-text-fu`, `user-management`, `permissions`, `processes`, `packages`
- **Journeyman:** `devices`, `filesystem`, `boot-system`, `kernel`, `init`, `process-utilization`, `logging`
- **Networking Nomad:** `network-sharing`, `network-basics`, `subnetting`, `routing`, `network-config`, `troubleshooting`, `dns`

## Submit a Pull Request

This is a content repository, so ordinary lesson changes do not require an application build.

1. Fork the repository and create a focused branch:

   ```bash
   git checkout -b feature/lesson-name
   ```

2. Make and review your changes against the requirements above.
3. Verify affected commands, output, links, paths, IDs, ordering, and directive syntax.
4. Check the final diff:

   ```bash
   git diff --check
   git diff -- lessons/en/<course-id>/<lesson-id>.md
   ```

5. Submit a pull request explaining what changed and why.

Use direct commit messages, for example:

```text
Add lesson: Process monitoring with top
Fix filesystem lesson terminology
Improve German translation of the network interfaces lesson
```

## Getting Help

Search existing issues before opening a new one. Open an issue if a content change needs discussion or its course placement is unclear, and keep discussions respectful and learner-focused.

Thank you for helping make Linux education accessible to everyone!
