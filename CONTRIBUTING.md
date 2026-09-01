# Contributing to Linux Journey

Thank you for helping improve Linux Journey. This repository contains the course metadata, lesson content, and course images used by the Linux Journey learning experience.

## Quick Start Rules

- **Keep pull requests small:** Change no more than 3 files in one pull request and keep the changes focused on one topic.
- **Write new content in English:** Add new lessons under `lessons/en/`. LabEx handles the initial translations; native speakers are welcome to improve existing translations.
- **Match the repository schema:** Paths, identifiers, and ordering metadata must agree.
- **Use the current lesson format:** Lessons use topic sections, inline `single-choice` checks, and a final summary. Do not use the legacy four-section lesson template.
- **Verify examples:** Run commands and check expected output whenever it is safe and practical to do so.

## Repository Structure

```text
courses/
  <course-id>.yml
images/
  courses/<course-id>.png
lessons/
  <language-code>/<course-id>/<lesson-id>.md
```

- `courses/` contains one YAML metadata file per course.
- `lessons/` contains localized Markdown lessons. The currently maintained language directories are `de`, `en`, `es`, `fr`, `ja`, `ko`, `pt`, `ru`, and `zh`.
- `images/courses/` contains course artwork.
- A lesson's path, `lesson_id`, `course_id`, and `lang` values must match one another.

For example, `lessons/en/command-line/the-shell.md` must use:

```yaml
lesson_id: "the-shell"
course_id: "command-line"
lang: "en"
```

Use lowercase kebab-case for course IDs, lesson IDs, directory names, and Markdown filenames.

## Ways to Contribute

### Improve Existing Content

- Fix spelling, grammar, and broken links.
- Correct outdated or inaccurate technical information.
- Make explanations clearer for beginners.
- Improve command examples and expected output.
- Improve an existing translation without changing its meaning.

### Add a Lesson

- Write the lesson in English under `lessons/en/<course-id>/`.
- Use the lesson schema and body structure below.
- Choose an `order_index` that is unique within the course and language.
- Keep the topic focused and beginner-friendly.
- Include 3–5 meaningful comprehension checks distributed through the lesson.

### Change Course Metadata

Course metadata lives in `courses/<course-id>.yml` and uses this shape:

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
    meta_description: "A search-friendly description of the course."
    meta_keywords: "Linux command line, shell basics, Linux commands"
```

The filename and top-level `id` must match. Use one of the existing category IDs: `grasshopper`, `journeyman`, or `networking-nomad`. Keep each `order_index` unique within its category. When changing shared course facts, update affected translations consistently; do not add machine-generated or placeholder translations.

## Lesson Front Matter

Every lesson begins with YAML front matter in this field order:

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

Apply these rules:

- `lesson_id` is the Markdown filename without `.md`.
- `course_id` is the lesson's parent course directory and must match a file in `courses/`.
- `lang` is the lesson's language directory, using an ISO 639-1 language code.
- `order_index` is an unquoted number and must be unique within the course and language.
- `description` is one concise sentence describing the lesson's main topic or outcome.
- `meta_title` normally follows `Lesson Title - Course Title`.
- `meta_description` should be useful, specific, and concise.
- `meta_keywords` is a comma-separated string of relevant search terms.
- Wrap string values in double quotation marks. Do not quote numbers or booleans.

## Lesson Body

Use level-two headings for the lesson's top-level topics. Do not add a level-one heading: the application renders the front matter `title` as the page title.

Explain an idea before testing it, and place each check directly after the supporting explanation:

```markdown
## Interacting with the Shell

A shell prompt ending in `$` normally indicates that the shell is ready for input from a regular user.

:::single-choice{#identify-regular-user-prompt} Which symbol normally ends a regular user's shell prompt?

::option[`#`]{#root-prompt-symbol explanation="This normally identifies a root prompt, which has elevated privileges."}
::option[`$`]{#regular-prompt-symbol .correct explanation="A regular user's shell prompt normally ends in `$`."}
::option[`/`]{#path-separator-symbol explanation="A slash separates parts of a filesystem path; it does not identify a regular-user prompt."}
:::
```

Each lesson must:

- contain 3–5 `single-choice` checks distributed through the lesson;
- put the question on the same line as `:::single-choice{#component-id}`;
- give every component and option a stable, lowercase kebab-case ID that is unique across the English lesson collection;
- include exactly three plausible options per question;
- mark exactly one option with `.correct`;
- give every option a non-empty, specific `explanation`;
- make the answer clear from content that appears before the check; and
- balance option grammar, length, and specificity so the correct answer does not stand out visually.

Close every component with `:::` on its own line. Keep narrative transitions in normal Markdown rather than in option feedback.

Do not add the legacy headings `## Lesson Content`, `## Exercise`, `## Quiz Question`, or `## Quiz Answer`. Integrate useful exercises and resources naturally into the relevant topic instead.

End every lesson with a `## Summary` section containing one short sentence and an ordered list of no more than five learning outcomes:

```markdown
## Summary

You can now explain the role of a shell and interact with a basic shell prompt.

1. Distinguish between a terminal and a shell.
2. Identify a command prompt.
3. Run a simple command with `echo`.
```

The summary must be the final content section.

## Content Guidelines

### Writing Style

- Use clear, direct language and define technical terms when they first appear.
- Prefer concrete explanations and realistic examples over jargon.
- Teach prerequisites before relying on them.
- Preserve accurate existing content when making a focused correction.
- Use real product capitalization in learner-facing text, even when its identifier is lowercase kebab-case.

### Command Examples

- Use fenced code blocks with an appropriate language such as `bash` or `plaintext`.
- Use `$` for regular-user prompts and `#` for root prompts when showing a complete terminal session.
- Do not imply that readers should type the prompt symbol.
- Show expected output when it helps a beginner verify the result.
- Warn readers before commands that require root access or can modify or remove data.

## Translation Guidelines

LabEx handles the initial translation of new English lessons. Please do not start a new full-language translation or add translated versions of a new lesson from scratch.

Native speakers can contribute by reviewing files in `lessons/<language-code>/` and:

- correcting grammar and unnatural phrasing;
- improving technical terminology;
- preserving commands, code, links, directive syntax, and component IDs;
- keeping front matter and lesson structure aligned with the English source; and
- translating learner-facing headings, questions, options, and explanations naturally.

Do not translate `lesson_id`, `course_id`, component IDs, option IDs, commands, or file paths. Translations reuse the corresponding English component and option IDs. If the English source changed substantially and the translation is now stale, note that clearly in the pull request.

## Development Workflow

This is a content repository, so no application build is required for ordinary lesson edits.

1. Fork the repository and create a focused branch:

   ```bash
   git checkout -b feature/lesson-name
   ```

2. Make the smallest complete change that solves the issue.
3. Verify all commands and links you changed.
4. Review the changed files and check for whitespace errors:

   ```bash
   git diff --check
   git diff -- lessons/en/<course-id>/<lesson-id>.md
   ```

5. Confirm that paths and front matter IDs match, `order_index` values do not collide, every question has exactly three options and one correct answer, directive IDs are unique, and the summary is last.
6. Submit a pull request with a clear description of what changed and why.

Good commit messages describe the content change directly:

```text
Add lesson: Process monitoring with top
Fix filesystem lesson terminology
Improve German translation of the network interfaces lesson
```

## Course Map

- **Grasshopper:** `getting-started`, `command-line`, `text-fu`, `advanced-text-fu`, `user-management`, `permissions`, `processes`, `packages`
- **Journeyman:** `devices`, `filesystem`, `boot-system`, `kernel`, `init`, `process-utilization`, `logging`
- **Networking Nomad:** `network-sharing`, `network-basics`, `subnetting`, `routing`, `network-config`, `troubleshooting`, `dns`

## Getting Help

- Search existing issues before opening a new one.
- Open an issue when a content change needs discussion or the correct course placement is unclear.
- Be respectful and keep review discussions focused on helping learners.

Thank you for helping make Linux education accessible to everyone!
