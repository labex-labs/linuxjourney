---
index: 15
lang: "en"
title: "help"
meta_title: "help - Command Line"
meta_description: "Learn how to get Linux command line help with Bash help, --help output, man pages, and type for shell built-ins and external commands."
meta_keywords: "linux help command, bash help, command line help, --help, shell built-in, man command, type command"
---

## Lesson Content

When working on the Linux command line, you will often need a quick reminder of how a command works or what options it accepts. Linux provides several help tools directly in the terminal.

### The 'help' Command for Bash Built-ins

One of the most direct tools is `help`, a command that is built directly into the Bash shell. It is specifically designed to provide information about other Bash built-in commands. A built-in command is part of the shell itself, not a separate program. Examples include `echo`, `cd`, and `pwd`.

To use `help`, type it followed by the name of the built-in command.

```bash
$ help echo
```

This will display a summary of the `echo` command, its syntax, and a list of available options. This is the fastest way to get assistance for shell-specific functions.

### The --help Flag for Executable Programs

For most other executable programs that are not built into the shell, the `help` command won't work. Instead, a common convention is to provide a `--help` flag. This option signals the program to print a usage summary and then exit.

```bash
$ ls --help
```

While most developers follow this standard, it is not universal. Trying `--help` is usually a good first step for an unfamiliar program.

### Finding Command Type

If you are not sure whether a command is a Bash built-in or an external program, use `type`.

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

This helps you choose between `help cd`, `ls --help`, or `man ls`.

### Choosing the Right Help Tool

- Use `help COMMAND` for Bash built-ins such as `cd`, `echo`, and `history`.
- Use `COMMAND --help` for a quick summary from many external commands.
- Use `man COMMAND` for detailed manual pages.
- Use `whatis COMMAND` for a one-line description.

### Common Questions

**Why does help ls not work?** `ls` is usually an external program, not a Bash built-in. Try `ls --help` or `man ls`.

**Why does --help not work for every command?** It is a convention, not a strict rule.

**What is the fastest way to check a command?** Try `COMMAND --help` for external commands and `help COMMAND` for Bash built-ins.

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

How do you get quick command-line help for built-in Bash commands? (Please provide the single command name in English and in lowercase.)

## Quiz Answer

help
