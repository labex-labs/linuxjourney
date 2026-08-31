---
lesson_id: "cat-command"
course_id: "command-line"
lang: "en"
order_index: 7
title: "cat"
description: "Learn how to display, concatenate, and redirect file content safely with the cat command."
meta_title: "cat - Command Line"
meta_description: "Learn the Linux cat command with examples for viewing files, concatenating files, numbering lines, creating files, and using redirection safely."
meta_keywords: "linux cat command, cat command, view file linux, concatenate files, cat -n, cat -b, cat redirection, linux cat"
---

After learning to identify files, the next step is to read their contents. The `cat` command displays files and joins their contents; its name is short for "concatenate."

## Viewing File Contents

The simplest use of `cat` displays a file directly in the terminal:

```bash
$ cat myfile.txt
```

The command writes the entire file to standard output. This works well for short text, but a long file may scroll past too quickly.

:::single-choice{#display-short-file}
Which command displays all of `myfile.txt` in the terminal?

::option[`file myfile.txt`]{#classify-myfile explanation="`file` reports the likely file type. It does not print the complete text stored in the file."}
::option[`touch myfile.txt`]{#update-myfile explanation="`touch` updates timestamps or creates a missing file. It does not display the file's contents."}
::option[`cat myfile.txt`]{#display-myfile .correct explanation="`cat` reads `myfile.txt` and writes its contents to standard output, which is the terminal here."}
:::

## Concatenating Files

When you give `cat` several files, it reads them in operand order and writes their contents one after another:

```bash
$ cat dogfile birdfile
```

This displays `dogfile` first and `birdfile` second. To save the combined output in a new file, redirect standard output with `>`:

```bash
$ cat dogfile birdfile > animals
```

The shell creates `animals` or truncates it before running `cat`, then sends the combined output there. Do not use one of the input files as this destination, because it may be emptied before `cat` reads it.

:::single-choice{#combine-files-in-order}
Which command writes `part1` followed by `part2` into a new or replaced file named `whole`?

::option[`cat whole > part1 part2`]{#reverse-redirection explanation="Redirection has one destination, while the other words become operands to `cat`. This does not express the requested input and output order."}
::option[`cat part1 part2 > whole`]{#ordered-inputs .correct explanation="`cat` emits the two files in the order listed, and `>` redirects that combined output to `whole`."}
::option[`cat part2 part1 > whole`]{#reverse-inputs explanation="This writes the same two inputs to `whole`, but it reads `part2` before `part1`. Operand order controls output order."}
:::

## Reading Terminal Input into a File

When no input file is given, `cat` reads standard input. You can combine that behavior with `>` to enter text from the terminal and write it to a file:

```bash
$ cat > newfile.txt
```

After running the command, type the desired text. Press `Ctrl+D` to send an end-of-file signal and return to the shell. Be careful: if `newfile.txt` already exists, `>` truncates its previous contents.

Use `>>` to append new input instead of replacing existing contents:

```bash
$ cat >> notes.txt
```

:::single-choice{#append-terminal-input}
You want to type more text at the end of an existing `notes.txt`. Which command starts that operation without truncating the file?

::option[`cat > notes.txt`]{#overwrite-notes explanation="A single `>` redirects input after truncating the destination. Existing text in `notes.txt` would be lost."}
::option[`cat >> notes.txt`]{#append-notes .correct explanation="The `>>` operator opens the destination for appending, so text read by `cat` is added after the existing contents."}
::option[`cat notes.txt > notes.txt`]{#same-input-output explanation="Using the same file as input and a `>` destination can truncate it before `cat` reads it. It is not a safe append operation."}
:::

## Formatting the Output

Several options make output easier to inspect:

- `-n`: Number all output lines, starting from 1.
- `-b`: Number only non-empty output lines.
- `-s`: Squeeze multiple blank lines into one blank line.
- `-A`: Show nonprinting characters, tabs, and line endings.

Examples:

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

:::single-choice{#number-nonempty-lines}
Which command numbers only the nonempty output lines from `notes.txt`?

::option[`cat -b notes.txt`]{#number-nonblank .correct explanation="The `-b` option numbers nonempty output lines while leaving empty lines unnumbered."}
::option[`cat -n notes.txt`]{#number-all-lines explanation="The `-n` option numbers every output line, including empty ones. It does not meet the nonempty-only condition."}
::option[`cat -s notes.txt`]{#squeeze-blank-lines explanation="The `-s` option reduces repeated blank lines to one. It does not add line numbers."}
:::

## Choosing a Viewer for Long Files

Use `cat` when you want the entire output at once. For a long file, `less` is usually more convenient because it lets you scroll, search, and quit without flooding the terminal:

```bash
$ less /var/log/syslog
```

:::single-choice{#choose-viewer-for-long-file}
Which command is better suited to interactively reading a long log file?

::option[`less /var/log/syslog`]{#page-through-log .correct explanation="`less` provides scrolling, searching, and a controlled exit, making it suitable for interactive reading of long files."}
::option[`cat /var/log/syslog`]{#print-entire-log explanation="`cat` writes the entire log to the terminal at once. A long file may scroll past before you can inspect it."}
::option[`touch /var/log/syslog`]{#update-log-time explanation="`touch` changes timestamps and may require permissions. It is not a command for reading the log."}
:::

To practice displaying and combining file content, try these hands-on labs:

1. **[Linux cat Command: File Concatenating](https://labex.io/labs/linux-linux-cat-command-file-concatenating-210986)** - Learn the `cat` command for viewing, concatenating, and manipulating text files, enhancing your command-line skills for efficient text file handling.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice using commands like `cat` to efficiently view and navigate text files, including system logs and configuration files, to extract critical information.

## Summary

You can now use `cat` to display and combine file content while choosing safe redirection.

1. Display the complete contents of a short file.
2. Concatenate files in a chosen order.
3. Replace or append to a destination deliberately.
4. Number or simplify output lines.
5. Choose `less` when interactive reading is more suitable.
