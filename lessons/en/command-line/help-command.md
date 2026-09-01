---
lesson_id: "help-command"
course_id: "command-line"
lang: "en"
order_index: 15
title: "help"
description: "Learn how to choose built-in help, program usage output, or manual pages for a command."
meta_title: "help - Command Line"
meta_description: "Learn how to get Linux command line help with Bash help, --help output, man pages, and type for shell built-ins and external commands."
meta_keywords: "linux help command, bash help, command line help, --help, shell built-in, man command, type command"
---

You do not need to memorize every command option. Bash and many installed programs can explain their syntax directly in the terminal, but the right help source depends on what kind of command you are using.

## Getting Help for Bash Builtins

Bash provides the `help` builtin for commands implemented by the shell itself. Examples include `cd`, `history`, and `type`.

Pass the builtin name as an argument:

```bash
$ help echo
```

The output describes the builtin's syntax and behavior. Running `help` without an argument lists the builtins for which Bash has help.

:::single-choice{#help-for-bash-cd} Which command displays Bash's help entry for its `cd` builtin?

::option[`cd --help`]{#cd-help-option explanation="Some builtins may recognize options, but Bash's dedicated documentation interface is `help` followed by the builtin name."}
::option[`help cd`]{#help-cd .correct explanation="Bash's `help` builtin looks up the documentation for the named builtin, which is `cd` here."}
::option[`type cd`]{#type-cd explanation="`type` explains how Bash resolves the name `cd`. It identifies the command but does not show the full help entry."}
:::

## Requesting a Program's Usage Summary

Many external programs follow the convention of accepting `--help` and printing a usage summary:

```bash
$ ls --help
```

This convention is common but not universal. Read the output and exit status rather than assuming every program supports the same option.

:::single-choice{#quick-ls-usage} Which command commonly prints a quick usage summary provided by the external `ls` program?

::option[`help ls`]{#bash-help-ls explanation="Bash `help` documents shell builtins. On a typical system, it does not provide the external `ls` program's usage page."}
::option[`ls --help`]{#ls-help .correct explanation="GNU `ls` follows the common `--help` convention and prints its usage and options."}
::option[`type --help ls`]{#type-help-ls explanation="This asks the `type` builtin about its own option handling, not `ls` to explain its usage."}
:::

## Finding How Bash Resolves a Name

Use `type` to see whether Bash resolves a name as a builtin, alias, function, keyword, or executable file:

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

The exact result can vary with aliases, functions, installed programs, and `PATH`. Use `type -a NAME` when you want Bash to show all known resolutions rather than only the one it would use first.

:::single-choice{#identify-command-resolution} You do not know whether `deploy` is an alias, function, builtin, or executable. Which Bash command checks how the name resolves?

::option[`type deploy`]{#type-deploy .correct explanation="The `type` builtin reports how Bash interprets the command name in the current shell environment."}
::option[`help deploy`]{#help-deploy explanation="`help` looks for Bash builtin documentation. It does not generally identify aliases, functions, and external files."}
::option[`deploy --help`]{#deploy-help explanation="This attempts to run the command and depends on its own option support. It does not first explain how Bash resolved the name."}
:::

## Choosing the Level of Detail

- Use `help COMMAND` for a Bash builtin.
- Use `COMMAND --help` for a quick summary from many external commands.
- Use `man COMMAND` for an installed manual page with more detailed documentation.
- Use `whatis COMMAND` for a one-line description.

The next lessons examine manual pages and one-line descriptions in more detail.

:::single-choice{#choose-detailed-manual} You need detailed documentation for the external command `ls`, not only a short usage summary. Which command should you try?

::option[`man ls`]{#man-ls .correct explanation="`man ls` opens the installed manual page, which normally provides a fuller description of syntax, options, and behavior."}
::option[`whatis ls`]{#whatis-ls explanation="`whatis` is designed to show concise manual-page descriptions. It is not the detailed documentation requested."}
::option[`type ls`]{#type-ls explanation="`type` reports how Bash resolves `ls`. It does not display the program's detailed manual."}
:::

## Summary

You can now choose a help source based on how Bash resolves a command.

1. Use `help` for Bash builtins.
2. Try `--help` for a program's quick usage output.
3. Inspect name resolution with `type`.
4. Open detailed documentation with `man`.
