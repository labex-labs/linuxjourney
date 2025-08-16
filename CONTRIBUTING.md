# Contributing to Linux Journey

Thank you for your interest in contributing to Linux Journey! This guide will help you get started.

## Important Guidelines

- **PR File Limit**: Each pull request should modify no more than 3 files
- **Focus**: Keep changes small and focused on a single topic
- **Quality**: Follow our lesson templates and content guidelines

## Ways to Contribute

### 1. Content Improvements

- Fix typos and grammar errors
- Update outdated information
- Improve lesson explanations
- Add practical examples

### 2. New Lessons

- **English only**: All new lessons must be written in English
- Create lessons following our structure
- Ensure content is beginner-friendly
- Include hands-on exercises
- Add quiz questions

### 3. Translation Reviews

- **AI localization**: LabEx team uses latest AI to translate English content to other languages
- **Native speaker reviews**: Review and improve existing translations
- **No manual translation**: Starting translations from scratch is not recommended
- Update language configuration files when needed

## Content Structure

### Course Organization

Lessons are organized into three progressive levels:

**Grasshopper (Beginner)**

- `getting-started/` - Linux basics and distributions
- `command-line/` - Terminal navigation and file operations
- `text-fu/` - Text manipulation basics
- `text-fu-advanced/` - Advanced text editors (Vim, Emacs)
- `user-management/` - User accounts and roles
- `access/` - File permissions and access control
- `processes/` - Process management
- `packages/` - Package management systems

**Journeyman (Intermediate)**

- `devices/` - Device management and kernel interaction
- `filesystem/` - Filesystem concepts and management
- `booting/` - Boot process and initialization
- `kernel/` - Kernel architecture and modules
- `init/` - Init systems (SysV, Upstart, systemd)
- `process-utilization/` - System monitoring and resources
- `logging/` - System logs and troubleshooting

**Networking Nomad (Advanced)**

- `network-fundamentals/` - TCP/IP and networking basics
- `subnetting/` - Subnet design and IP management
- `routing/` - Packet routing and topology
- `network-configuration/` - Interface configuration
- `network-troubleshooting/` - Diagnostic tools
- `network-sharing/` - File sharing protocols
- `dns/` - Domain Name System

### Lesson Template

Each lesson file must follow this exact structure with **4 fixed sections**:

```markdown
---
lang: "en"
title: "Lesson Title"
description: "Brief lesson description for SEO (under 160 characters)"
keywords: "relevant, keywords, for, search, engines"
---

## Lesson Content

Write your main teaching content here using **level 3 headers (###)** to structure content:

### Introduction
Brief overview of the topic.

### Basic Concepts
Explain fundamental concepts clearly.

### Practical Examples
Use code blocks for commands:
```bash
$ command --example
```

### Advanced Usage

Cover more complex scenarios if needed.

Keep content:

- Clear and concise
- Beginner-friendly
- Practical with real examples
- Well-structured with level 3 headers only

## Exercise

Provide hands-on practice:

- Give specific tasks to complete
- Include expected outputs
- Mention common pitfalls
- Link to additional resources if needed

## Quiz Question

Ask a question to test understanding:

- Make it specific and clear
- Avoid trick questions
- Focus on practical knowledge

## Quiz Answer

Provide the correct answer with brief explanation if needed.

```

### Template Rules

- **Fixed sections**: The 4 main sections (## headers) cannot be modified or renamed
- **No new sections**: Cannot add additional level 2 headers (##)
- **Level 3 headers only**: Use ### headers within "Lesson Content" to structure content
- **Consistent structure**: All lessons must follow this exact format

### File Naming

- Use lowercase with hyphens: `process-management.md`
- Be descriptive: `network-interface-configuration.md`
- Keep names concise but clear

## Translation Guidelines

### Translation Process

**LabEx Team Handles Initial Translation**
- New English lessons are automatically translated using latest AI
- AI generates consistent, high-quality translations across all supported languages
- Translations maintain technical accuracy and formatting

### Native Speaker Contributions

**Review and Improve Existing Translations**
- Check AI-generated translations for accuracy
- Improve natural language flow
- Fix cultural references and idioms
- Ensure technical terms are correctly translated

**What Native Speakers Can Do:**
- Review lessons in `lessons/{language_code}/`
- Submit corrections for grammar and clarity
- Improve technical terminology
- Update language-specific examples when appropriate

**What to Avoid:**
- Starting new translations from scratch
- Large-scale manual translation projects
- Inconsistent terminology across lessons

### Language Configuration

When reviewing translations, you may need to update `i18n/{language_code}.yml`:

```yaml
{language_code}:
  menu:
    languages:
      lang: "🏴 Language Name"
  home:
    tagline:
      title: "Translated tagline"
    # ... other translations
```

### Translation Standards

- Maintain the same structure as English lessons
- Preserve all frontmatter fields
- Keep code examples in English (commands are universal)
- Ensure consistency with existing translations
- Follow language-specific style guides

## Development Workflow

### Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/lesson-name`
3. Make your changes
4. Test your changes locally
5. Commit with clear messages
6. Push and create a pull request

### Commit Guidelines

- Use clear, descriptive commit messages
- Reference issues when applicable
- Keep commits focused on single changes

Examples:

```
Add new lesson: Process monitoring with top
Fix typo in filesystem lesson
Update German translation for network module
```

### Pull Request Process

1. **File Limit**: Each PR should modify no more than 3 files to keep reviews manageable
2. Ensure your changes follow the lesson template
3. Check for spelling and grammar errors
4. Test any code examples you include
5. Update related documentation if needed
6. Write a clear PR description explaining changes

### PR Guidelines

- **Small, focused changes**: Keep PRs small and focused on a single topic
- **File limit**: Maximum 3 files per PR (exceptions may be made for translation reviews)
- **Single purpose**: One lesson addition, one bug fix, or one feature at a time
- **Large changes**: Split big updates into multiple smaller PRs
- **New lessons**: Must be in English only - translations handled by LabEx team
- **Translation PRs**: Focus on reviewing and improving existing AI translations

## Content Guidelines

### Writing Style

- Use clear, simple language
- Explain technical terms when first introduced
- Include practical examples
- **Structure content with level 3 headers (###) only within Lesson Content**
- **Never modify the 4 fixed section headers (##)**
- Use bullet points for lists

### Code Examples

- Use realistic, working examples
- Include command prompts (`$` for user, `#` for root)
- Show expected output when helpful
- Explain what each command does

### Best Practices

- Start with basics before advanced concepts
- Build upon previous lessons
- Include troubleshooting tips
- Reference related lessons when appropriate
- Keep lessons focused on single topics

## Getting Help

- Open an issue for questions or discussions
- Join our community discussions
- Check existing issues before creating new ones
- Be respectful and constructive in feedback

## Recognition

Contributors will be acknowledged in:

- Git commit history
- Project documentation
- Community discussions

Thank you for helping make Linux education accessible to everyone!
