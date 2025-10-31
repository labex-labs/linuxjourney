---
index: 15
lang: "en"
title: "help"
meta_title: "help - Command Line"
meta_description: "Discover how to use the Linux help command for quick assistance in your terminal. This Bash tutorial explains how to get help for built-in shell commands and use the --help flag for other Linux programs."
meta_keywords: "Linux help command, Bash help, command line help, Linux commands, beginner Linux, Linux tutorial, Bash tutorial, shell built-in, command line assistance"
---

## Lesson Content

When working on the Linux command line, you'll often need a quick reminder of how a command works or what options it accepts. Fortunately, Linux provides excellent tools for command line help right in the terminal.

### The 'help' Command for Bash Built-ins

One of the most direct tools is `help`, a command that is built directly into the Bash shell. It is specifically designed to provide information about other Bash built-in commands. A built-in command is part of the shell itself, not a separate program. Examples include `echo`, `cd`, and `pwd`.

To use the **Linux help command**, simply type `help` followed by the name of the built-in command.

```bash
help echo
```

This will display a summary of the `echo` command, its syntax, and a list of available options. This is the fastest way to get assistance for shell-specific functions.

### The --help Flag for Executable Programs

For most other executable programs that are not built into the shell, the `help` command won't work. Instead, a common convention is to provide a `--help` flag. This option signals the program to print a usage summary and then exit.

```bash
ls --help
```

While most developers adhere to this standard, it's not universal. However, trying the `--help` flag is usually the best first step to find help for an unfamiliar program. It's a fundamental skill for anyone learning about **Linux commands**.

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

How do you get quick command-line help for built-in Bash commands? (Please provide the single command name in English and in lowercase.)

## Quiz Answer

help
