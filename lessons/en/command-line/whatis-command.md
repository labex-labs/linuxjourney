---
lesson_id: "whatis-command"
course_id: "command-line"
lang: "en"
order_index: 17
title: "whatis"
description: "Learn how to retrieve concise manual-page descriptions and interpret their section numbers."
meta_title: "whatis - Command Line"
meta_description: "Learn the Linux whatis command with examples for getting one-line command descriptions from man pages and understanding multiple manual sections."
meta_keywords: "whatis command, linux whatis, command description linux, man page summary, command line help, apropos"
---

When you recognize a command name but forget its purpose, `whatis` can provide a short reminder from the manual-page database.

## Looking Up an Exact Name

Pass one or more exact topic names to `whatis`. Each result is derived from the `NAME` section recorded for an installed manual page:

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

The output is a description, not a list of command options or examples. Use `man cat` or `cat --help` when you need more detail.

:::single-choice{#describe-known-command} You know the name `cat` and want its one-line manual-page description. Which command should you run?

::option[`man cat`]{#manual-cat explanation="`man cat` opens the full manual page. It provides more than the requested one-line reminder."}
::option[`apropos cat`]{#apropos-cat explanation="`apropos` searches descriptions for a keyword and can return many related topics. It is broader than an exact-name lookup."}
::option[`whatis cat`]{#whatis-cat .correct explanation="`whatis` looks up the exact topic name and prints its concise description from the manual database."}
:::

## Reading Section Numbers

If the same topic has manual pages in several sections, `whatis` can display more than one result:

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

The number in parentheses is the manual section. Here, `passwd(1)` describes the user command and `passwd(5)` describes a file format. You can open one explicitly with `man 1 passwd` or `man 5 passwd`.

:::single-choice{#interpret-whatis-section} In the output `passwd (5) - the password file`, what does `(5)` identify?

::option[The fifth option accepted by the `passwd` command.]{#fifth-option explanation="The number is not an option position. Options are documented inside a selected manual page."}
::option[The manual section containing the file-format page.]{#section-five .correct explanation="Section 5 is used for file formats and conventions, so `passwd(5)` refers to that manual section."}
::option[Five manual pages that share the name `passwd`.]{#five-pages explanation="Multiple results may exist, but the parenthesized value identifies one section rather than a page count."}
:::

## Choosing between whatis, man, and apropos

- `whatis NAME`: Show concise descriptions for an exact manual topic name.
- `man NAME`: Open a full manual page.
- `apropos KEYWORD`: Search manual-page names and descriptions for a keyword.

For example:

```bash
$ apropos password
```

Use `apropos` when you know the task but not the command name. Use `whatis` when you already know the name.

:::single-choice{#search-by-purpose} You do not know a command's name, but you want to search manual descriptions for the keyword `password`. Which command fits that task?

::option[`apropos password`]{#apropos-password .correct explanation="`apropos` searches manual-page names and descriptions for the keyword, helping discover relevant topics."}
::option[`whatis password`]{#exact-password explanation="`whatis` looks for an exact manual topic named `password`. It is not the general keyword-search interface."}
::option[`man password`]{#manual-password explanation="`man` attempts to open a page with that topic name. It does not perform the requested description search."}
:::

## When No Description Appears

If `whatis` reports that nothing is appropriate, the topic may not have an installed manual page or the manual database may be out of date. This result does not prove that no executable, alias, function, or builtin with that name exists. Use `type NAME` to see how Bash resolves a command name, then choose an appropriate help source.

:::single-choice{#whatis-versus-type} `whatis deploy` finds no manual description. Which command checks whether Bash resolves `deploy` as an alias, function, builtin, or executable?

::option[`whatis -r deploy`]{#whatis-regex-deploy explanation="Changing the manual-database query does not show all of Bash's aliases, functions, builtins, and path resolution."}
::option[`man 5 deploy`]{#manual-five-deploy explanation="This attempts to open a section 5 page. It does not determine how Bash resolves the command name."}
::option[`type deploy`]{#resolve-deploy .correct explanation="Bash `type` reports how the current shell resolves a command name, independently of whether a manual description is installed."}
:::

## Summary

You can now retrieve and interpret concise descriptions from the manual database.

1. Look up an exact topic with `whatis`.
2. Read the manual section shown in parentheses.
3. Use `man` when you need the full page.
4. Use `apropos` when you know a keyword rather than a name.
