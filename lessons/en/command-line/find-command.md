---
lesson_id: "find-command"
course_id: "command-line"
lang: "en"
order_index: 14
title: "find"
description: "Learn how to search directory trees by name, type, size, and time, then act on verified matches."
meta_title: "find - Command Line"
meta_description: "Learn the Linux find command with examples for searching by name, type, size, modification time, and running actions on matching files."
meta_keywords: "linux find command, find command, find files linux, find by name, find by type, find by size, find mtime, find exec"
---

The `find` command walks a directory tree and tests each entry against criteria such as its name, type, size, or modification time.

## Choosing Where to Search

The basic syntax is:

```bash
find [PATH] [EXPRESSION]
```

The path chooses the starting point, and the expression selects or acts on entries below it.

This command searches `/home` and its descendants for entries named `puppies.jpg`:

```bash
$ find /home -name puppies.jpg
```

Recursion is the default. Use `.` as the starting path when you want to search the current directory tree.

:::single-choice{#search-current-tree}
Which command searches the current directory and its descendants for entries named `notes.txt`?

::option[`find . -name notes.txt`]{#find-current-notes .correct explanation="The dot selects the current directory as the starting path, and `-name` tests each entry's basename."}
::option[`find / -name notes.txt`]{#find-root-notes explanation="A starting path of `/` searches from the filesystem root, which is much broader than the current directory tree."}
::option[`find notes.txt .`]{#find-operands-reversed explanation="`find` expects starting paths before the expression. This order does not express the requested search."}
:::

## Matching Names and Types

The `-name` test accepts an exact basename or a shell-style pattern. Quote wildcard patterns so the current shell passes them unchanged to `find`:

```bash
$ find . -name "*.txt"
```

Without the quotes, the shell may expand `*.txt` against the current directory before `find` begins. Use `-iname` instead of `-name` when the name match should ignore letter case.

Add `-type d` to select directories or `-type f` to select regular files:

```bash
$ find /home -type d -name MyFolder
```

Both tests must be true here: the entry must be a directory and its basename must be `MyFolder`.

:::single-choice{#find-text-regular-files}
Which command finds regular files whose names end in `.txt` below the current directory?

::option[`find . -type f -name "*.txt"`]{#text-files .correct explanation="`-type f` selects regular files, while the quoted `-name` pattern is evaluated by `find` for every entry."}
::option[`find . -type d -name "*.txt"`]{#text-directories explanation="The pattern is quoted correctly, but `-type d` selects directories rather than regular files."}
::option[`find . -type f -name *.txt`]{#unquoted-text-files explanation="The unquoted wildcard can be expanded by the current shell before `find` runs, changing the intended expression."}
:::

## Matching Size and Modification Time

Use `-size` with `+` for greater than the specified unit or `-` for less than it:

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

Here, uppercase `M` represents 1,048,576-byte units, while lowercase `k` represents 1,024-byte units. `find` rounds sizes up to the selected unit before applying the numeric comparison, so boundary behavior is based on those units.

Use `-mtime` to test the number of complete 24-hour periods since the file was modified:

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7` matches a value less than 7, while `-mtime +30` matches a value greater than 30. Because complete 24-hour periods are used, these tests are not based on calendar-midnight boundaries.

:::single-choice{#find-recent-regular-files}
Which command finds regular files below `.` whose modification age is less than seven complete 24-hour periods?

::option[`find . -type f -mtime -7`]{#recent-files .correct explanation="`-type f` selects regular files, and `-mtime -7` selects modification ages below seven complete 24-hour periods."}
::option[`find . -type f -mtime +7`]{#older-than-seven explanation="The plus sign selects ages greater than seven units. It looks for older rather than recent files."}
::option[`find . -type d -mtime -7`]{#recent-directories explanation="The time test is recent, but `-type d` restricts the results to directories instead of regular files."}
:::

## Printing and Acting on Matches

If no action is supplied, GNU `find` prints matching paths. You can write `-print` explicitly when you want the expression's action to be clear:

Print matches explicitly:

```bash
$ find . -name "*.log" -print
```

Use `-exec` to run another command for matches:

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

For the `\;` form, `{}` is replaced by one matching pathname for each command invocation. The semicolon terminates the `-exec` action and is escaped so the shell passes it to `find`.

Before using a destructive action such as `-delete` or an `-exec` command that changes files, run the same tests with `-print` and inspect every result. A narrower starting path and `-maxdepth N` can also limit the search.

:::single-choice{#verify-before-delete}
You are developing a `find` command that may later delete old `.log` files. What should you do first?

::option[Add `-delete` immediately and check which files disappear.]{#delete-first explanation="Deletion is not a safe preview and has no built-in undo. Verify the complete match set before adding it."}
::option[Run the same tests with `-print` and inspect every match.]{#print-first .correct explanation="A read-only listing verifies the starting path and tests before a destructive action is introduced."}
::option[Search from `/` so the command cannot miss any log files.]{#root-first explanation="Starting at `/` broadens the scope and can include unrelated or protected paths. Use the narrowest appropriate starting point."}
:::

:::single-choice{#run-ls-for-each-match}
In `find . -name "*.log" -exec ls -l {} \;`, what does `{}` represent?

::option[The current matching pathname supplied to `ls -l`.]{#match-placeholder .correct explanation="For this `-exec` form, `find` substitutes the current match for `{}` before invoking `ls -l`."}
::option[The directory where the `find` command was started.]{#starting-placeholder explanation="The starting directory is the dot near the beginning of the command. The braces have a different role inside `-exec`."}
::option[The semicolon that ends the `-exec` expression.]{#terminator-placeholder explanation="The escaped semicolon terminates the `-exec` action. The braces are the pathname placeholder."}
:::

Permission-denied messages usually mean the current account cannot search part of the tree. Prefer a narrower, relevant starting path; do not add elevated privileges until you understand and intend the expanded access.

To practice building search expressions, try these hands-on labs:

1. **[Linux find Command: File Searching](https://labex.io/labs/linux-linux-find-command-file-searching-219191)** - This lab provides an introduction to the `find` command, a versatile utility for searching and locating files and directories based on various criteria. You'll practice using `find` to locate specific files.
2. **[Discover Critical System Resources](https://labex.io/labs/linux-discover-critical-system-resources-388032)** - Learn essential Linux commands for locating files and executables, including `find`. You'll practice efficiently navigating the file system and discovering critical system resources.

## Summary

You can now build focused `find` expressions and verify results before taking action.

1. Choose the narrowest useful starting path.
2. Quote name patterns and combine them with type tests.
3. Filter by size or complete 24-hour modification periods.
4. Limit recursion depth when appropriate.
5. Print and inspect matches before destructive actions.
