---
index: 15
lang: "en"
title: "help"
meta_title: "help - Command Line"
meta_description: "Learn how to use the 'help' command in Bash for quick command-line assistance. Understand built-in commands and find options for Linux programs."
meta_keywords: "Linux help command, Bash help, command line help, Linux commands, beginner Linux, Linux tutorial, Bash tutorial"
---

## Lesson Content

Linux has some great built-in tools to help you understand how to use a command or check what flags are available for a command. One tool, `help`, is a built-in Bash command that provides help for other Bash commands (e.g., `echo`, `logout`, `pwd`).

```bash
help echo
```

This will give you a description and the options you can use when you want to run `echo`. For other executable programs, it’s convention to have an option called `--help` or something similar.

```bash
echo --help
```

Not all developers who ship executables will conform to this standard, but it’s probably your best shot to find some help on a program.

## Exercise

Run `help` on the `echo` command, `logout` command, and `pwd` command.

For additional hands-on practice with basic Linux commands, explore these interactive labs:

- [Linux pwd Command: Directory Displaying](https://labex.io/labs/linux-linux-pwd-command-directory-displaying-209734)
- [Linux cd Command: Directory Changing](https://labex.io/labs/linux-linux-cd-command-directory-changing-209733)

## Quiz Question

How do you get quick command-line help for built-in Bash commands?

## Quiz Answer

help
