---
lesson_id: "stderr-standard-error-redirect"
course_id: "text-fu"
lang: "en"
order_index: 3
title: "stderr (Standard Error)"
description: "Learn how to redirect standard error separately or combine it with standard output in Bash."
meta_title: "stderr (Standard Error) - Text-Fu"
meta_description: "Learn how to manage standard error in Linux. This guide covers stderr redirection, the stderr file descriptor (2), and how to redirect stderr to a file or /dev/null using 2>, 2>&1, and &>."
meta_keywords: "stderr, standard error linux, stderr file descriptor, stderr file, linux standard error, redirect stderr, 2>, 2>&1, &>, /dev/null, bash error handling"
---

Programs normally write regular results to standard output and diagnostics to a separate stream called standard error, or **stderr**. Keeping the streams separate lets you save useful data without mixing error messages into it.

## Separating Regular Output from Errors

Consider a command whose pathname does not exist:

```bash
$ ls /fake/directory > peanuts.txt
ls: cannot access '/fake/directory': No such file or directory
```

The `>` operator redirects stdout only. The diagnostic is written to stderr, which is still connected to the terminal. Meanwhile, the shell creates or truncates `peanuts.txt` for stdout even though `ls` produces no regular result.

The standard streams conventionally use these file descriptors:

- `0`: stdin (standard input)
- `1`: stdout (standard output)
- `2`: stderr (standard error)

:::single-choice{#stderr-not-in-stdout-file} Why does the error from `ls /missing > results.txt` normally remain on the terminal?

::option[`>` redirects stdout, while the diagnostic is written to stderr.]{#stderr-separate-stream .correct explanation="A plain `>` changes file descriptor 1 only. File descriptor 2 keeps its existing terminal destination."}
::option[`ls` waits until the file closes before printing any error.]{#stderr-waits-for-close explanation="The issue is not timing. The regular and diagnostic messages use different output streams."}
::option[`results.txt` can store regular text but cannot store diagnostics.]{#stderr-file-capability explanation="An ordinary file can store either stream. The command line simply did not redirect stderr to it."}
:::

## Redirecting stderr with 2>

Put file descriptor `2` before `>` to redirect stderr:

```bash
$ ls /fake/directory 2> errors.txt
```

The shell creates or truncates `errors.txt` and connects it to descriptor 2. Stdout keeps its previous destination. Use `2>> errors.txt` instead when error output should be appended.

:::single-choice{#stderr-to-error-file} Which command replaces `errors.log` with diagnostics from `find /restricted` while leaving stdout on its existing destination?

::option[`find /restricted > errors.log`]{#stdout-errors-log explanation="A plain `>` redirects descriptor 1, so it captures regular results rather than specifically redirecting diagnostics."}
::option[`find /restricted < errors.log`]{#stdin-errors-log explanation="The less-than operator supplies the file as stdin. It does not capture either output stream."}
::option[`find /restricted 2> errors.log`]{#stderr-errors-log .correct explanation="The leading `2` selects stderr, and `>` creates or truncates the destination for that stream."}
:::

## Combining stdout and stderr

To place both output streams in one file, first redirect stdout, then duplicate stderr to stdout's current destination:

```bash
$ ls /fake/directory /etc/passwd > combined.txt 2>&1
```

Redirections are processed from left to right:

1. `> combined.txt` connects stdout to the file.
2. `2>&1` connects stderr to wherever stdout points at that moment.

Reversing the order changes the result:

```bash
$ ls /fake/directory /etc/passwd 2>&1 > regular.txt
```

Here, stderr first duplicates stdout's original terminal destination. Stdout then moves to `regular.txt`, so the two streams end in different places.

:::single-choice{#stderr-combine-order} Which Bash redirection sends both stdout and stderr from `command` to `all.log`?

::option[`command 2>&1 > all.log`]{#stderr-before-stdout explanation="This first connects stderr to stdout's old destination, then redirects only stdout to the file. The streams end up separated."}
::option[`command 2> all.log > /dev/null`]{#stderr-file-stdout-null explanation="This sends stderr to `all.log` but discards stdout. It does not combine both streams in the file."}
::option[`command > all.log 2>&1`]{#stdout-then-stderr .correct explanation="Stdout goes to the file first, and stderr then duplicates that current stdout destination."}
:::

Bash also provides `&>` as a shorter syntax for replacing a file with both streams:

```bash
$ ls /fake/directory /etc/passwd &> combined.txt
```

Use `&>>` to append both streams in Bash. The explicit `> file 2>&1` form is useful to recognize because it also appears in shell scripts and documentation.

:::single-choice{#stderr-bash-short-form} Which Bash command appends both stdout and stderr from `build` to `build.log`?

::option[`build &> build.log`]{#replace-both-build explanation="Bash `&>` redirects both streams but replaces an existing file instead of appending to it."}
::option[`build 2>> build.log`]{#append-errors-build explanation="This appends stderr only. Stdout retains its previous destination."}
::option[`build &>> build.log`]{#append-both-build .correct explanation="In Bash, `&>>` appends file descriptors 1 and 2 to the same destination."}
:::

## Discarding a Stream Deliberately

`/dev/null` is a special device that discards data written to it. Redirect stderr there only when you have determined that those diagnostics are expected and unnecessary:

```bash
$ ls /fake/directory 2> /dev/null
```

This does not make the command succeed or change its exit status; it only hides the diagnostic stream. During troubleshooting, preserve or display stderr instead of discarding the information you need.

:::single-choice{#stderr-dev-null-effect} What does `check-data 2> /dev/null` change?

::option[It discards stdout and converts every error into success.]{#discard-stdout-success explanation="Descriptor 2 is stderr, not stdout, and redirection does not rewrite the program's exit status."}
::option[It discards stderr but does not force a successful exit status.]{#discard-stderr-only .correct explanation="The redirection changes where diagnostics go. The program still determines its own success or failure status."}
::option[It saves stderr in a hidden file named `/dev/null`.]{#save-dev-null explanation="`/dev/null` discards written data; it is not a storage file for later recovery."}
:::

To practice managing all three standard streams, try this hands-on lab:

1. **[Redirecting Input and Output in Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** - In this lab, you will learn to redirect input and output in the Linux shell. You will practice controlling data flow from commands by manipulating standard output (stdout), standard error (stderr), and standard input (stdin) using operators like >, >>, 2>, and the tee command.

## Summary

You can now keep diagnostics separate or combine them with regular command output.

1. Recognize stderr as file descriptor 2.
2. Replace or append an error log with `2>` or `2>>`.
3. Apply multiple redirections from left to right.
4. Combine both output streams with deliberate syntax.
5. Discard diagnostics only when their loss is acceptable.
