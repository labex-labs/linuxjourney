# Contributing to Linux Journey

Thank you for your interest in contributing! This guide covers the essential information you need to get started.

## Quick Start Rules

- **PR File Limit**: Maximum 3 files per pull request
- **English First**: All new lessons must be written in English (translations handled by LabEx team)
- **Template Required**: Follow our 4-section lesson template exactly
- **Small Changes**: Keep changes focused on a single topic

## How to Contribute

**Content Improvements**

- Fix typos and grammar errors  
- Update outdated information
- Improve explanations with practical examples

**New Lessons**

- Write in English only
- Follow the lesson template structure
- Make content beginner-friendly
- Include hands-on exercises and quiz questions

**Translation Reviews**

- Review AI-generated translations for accuracy
- Improve natural language flow and terminology
- Don't start translations from scratch

## Lesson Template (Required Structure)

Every lesson must have exactly these 4 sections:

```markdown
---
lang: "en"
title: "Lesson Title"
meta_description: "Brief description (under 160 characters)"
meta_keywords: "relevant, keywords"
---

## Lesson Content

Use ### headers to organize content:

### Introduction
### Basic Concepts  
### Practical Examples

Keep content clear, practical, and beginner-friendly.

## Exercise

Provide hands-on tasks with expected outputs.

## Quiz Question

Ask a specific question to test understanding.

## Quiz Answer

Provide the correct answer with brief explanation.
```

**Template Rules:**

- The 4 main sections (##) cannot be changed
- Use only ### headers within "Lesson Content"
- Keep structure consistent across all lessons

## Course Structure

**Grasshopper (Beginner):** getting-started, command-line, text-fu, user-management, access, processes, packages

**Journeyman (Intermediate):** devices, filesystem, booting, kernel, init, process-utilization, logging  

**Networking Nomad (Advanced):** network-fundamentals, subnetting, routing, network-configuration, troubleshooting, sharing, dns

## Development Process

1. **Fork** the repository
2. **Create branch**: `git checkout -b feature/lesson-name`
3. **Make changes** following the template
4. **Test** any code examples
5. **Submit PR** with clear description

**Good Commit Messages:**

```
Add new lesson: Process monitoring with top
Fix typo in filesystem lesson  
Update German translation for network module
```

## Content Guidelines

**Writing Style:**

- Use clear, simple language
- Explain technical terms when introduced
- Include practical, working examples
- Structure with ### headers only in lesson content

**Code Examples:**

- Use realistic examples that work
- Include prompts (`$` for user, `#` for root)
- Show expected output when helpful

## Translation Guidelines

**LabEx handles initial translations** using AI for all new English lessons.

**Native speakers can:**

- Review existing translations in `lessons/{language_code}/`
- Fix grammar and improve clarity
- Correct technical terminology
- Update `i18n/{language_code}.yml` when needed

**Avoid:**

- Starting new translations from scratch
- Large manual translation projects

## Getting Help

- Open an issue for questions
- Check existing issues first
- Be respectful in discussions

Thank you for helping make Linux education accessible to everyone!
