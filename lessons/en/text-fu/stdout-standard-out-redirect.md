---
lesson_id: "stdout-standard-out-redirect"
course_id: "text-fu"
lang: "en"
order_index: 1
title: "stdout (Standard Out)"
description: "Learn how standard output flows to the terminal and how Bash redirects it to files."
meta_title: "stdout (Standard Out) - Text-Fu"
meta_description: "Start your journey to learn Linux by mastering standard output (stdout) and I/O redirection. This lesson covers how to redirect command output to files using the > and >> operators, a fundamental skill for any Linux user."
meta_keywords: "Linux, learn linux, stdout, I/O redirection, standard output, redirect output, bash, shell scripting, Linux commands, Linux tutorial"
---

Programs communicate through input/output streams. Standard output, abbreviated **stdout**, is the stream a program normally uses for its regular results. In a terminal, the shell initially connects that stream to the terminal display.

## Writing to Standard Output

The `echo` command writes its arguments to stdout:

```bash
$ echo Hello World
Hello World
```

Stdout is file descriptor `1`, a number that becomes useful when you redirect more than one stream. Programs can also have standard input, or stdin, and standard error, or stderr; the next lessons examine those streams.

:::single-choice{#stdout-default-destination}
Without redirection, where does `echo Hello World` normally send its regular output in an interactive terminal?

::option[To a file named `stdout` in the current directory.]{#stdout-file explanation="Standard output is a stream, not an automatically created file named `stdout`. A file is used only when you redirect to one."}
::option[To the terminal through standard output.]{#stdout-terminal .correct explanation="The shell normally connects a command's stdout to the terminal, so `echo` is displayed there."}
::option[To the command's standard input stream.]{#stdout-to-stdin explanation="Standard input carries data into a program. `echo` sends its regular result out through stdout."}
:::

## Replacing a File with >

Bash interprets `>` as an output-redirection operator. It opens the destination file and connects the command's stdout to it:

```bash
$ echo Hello World > peanuts.txt
```

The text no longer appears on the terminal because stdout goes to `peanuts.txt`. If the file is missing, the shell creates it. If it exists, the shell truncates it before the command writes, so the previous contents are lost.

Use `cat` to inspect the result:

```bash
$ cat peanuts.txt
Hello World
```

:::single-choice{#stdout-replace-file}
`notes.txt` already contains text. What does `echo new > notes.txt` do?

::option[It replaces the file's contents with `new`.]{#stdout-replace-existing .correct explanation="The shell truncates the existing destination for `>` and directs `echo` output into the now-empty file."}
::option[It adds `new` after the existing text.]{#stdout-add-existing explanation="Appending requires `>>`. A single `>` does not preserve the destination's previous contents."}
::option[It displays `new` without changing the file.]{#stdout-display-only explanation="The redirection sends stdout to `notes.txt`, so the normal output does not remain on the terminal."}
:::

Because the shell opens the destination before the command runs, verify the pathname before pressing Enter. A misspelled or unintended existing file can be truncated even if the command later fails.

## Appending to a File with >>

Use `>>` when new stdout should be added after a file's existing contents:

```bash
$ echo Another line >> peanuts.txt
$ cat peanuts.txt
Hello World
Another line
```

Like `>`, `>>` creates a missing destination. The difference is how an existing file is opened: `>>` appends instead of truncating.

:::single-choice{#stdout-append-file}
Which command adds `Finished` to the end of `status.log` without erasing existing content?

::option[`echo Finished > status.log`]{#stdout-truncate-status explanation="A single `>` truncates an existing destination before writing. It would erase the earlier log content."}
::option[`echo Finished >> status.log`]{#stdout-append-status .correct explanation="`echo` produces the text, and `>>` appends that stdout to the destination file."}
::option[`cat Finished >> status.log`]{#stdout-cat-filename explanation="This asks `cat` to read a file named `Finished`. It does not produce the requested text as stdout."}
:::

## Redirection Belongs to the Shell

The shell recognizes `>` and `>>`, removes those operators from the arguments passed to the program, opens the file, and arranges the stream connection. The command itself simply writes to stdout as usual.

This means the same redirection syntax works with many commands:

```bash
$ pwd > current-directory.txt
$ ls -la >> directory-list.txt
```

:::single-choice{#stdout-shell-role}
Who normally interprets `>` in `pwd > current-directory.txt`?

::option[The `pwd` command after receiving `>` as an argument.]{#stdout-pwd-redirection explanation="The shell consumes the redirection syntax, so `pwd` normally does not receive `>` or the destination as ordinary arguments."}
::option[The Bash shell before it starts `pwd`.]{#stdout-bash-redirection .correct explanation="Bash opens the destination and connects file descriptor 1 before executing the command."}
::option[The terminal after `pwd` has printed the path on screen.]{#stdout-terminal-redirection explanation="The stream is redirected before output is written, so the terminal never receives that stdout in the first place."}
:::

To practice standard-stream redirection, try this hands-on lab:

1. **[Redirecting Input and Output in Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practice controlling data flow from commands by manipulating standard output (stdout), standard error (stderr), and standard input (stdin) using operators like `>`, `>>`, `2>`, and the `tee` command.

## Summary

You can now redirect a command's standard output without confusing replacement and append behavior.

1. Recognize stdout as the stream for regular command results.
2. Replace a file's contents with `>`.
3. Preserve existing contents and append with `>>`.
4. Verify a destination before the shell opens it.
