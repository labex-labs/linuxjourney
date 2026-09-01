---
lesson_id: "pipe-tee-redirect"
course_id: "text-fu"
lang: "en"
order_index: 4
title: "pipe and tee"
description: "Learn how pipelines connect commands and how tee saves a stream while passing it onward."
meta_title: "pipe and tee - Text-Fu"
meta_description: "Explore the powerful pipe and tee command in Linux. Learn how to chain commands with the Linux pipe tee combination and redirect output to both the screen and a file. This guide covers how to pipe to tee for advanced command-line data flow."
meta_keywords: "pipe and tee command in linux, linux pipe tee, pipe to tee, Linux pipe, tee command, stdout, stdin, command line redirection, Linux tutorial"
---

Pipelines connect small commands so data can flow between them without an intermediate file. The `tee` command can copy part of that flow to a file while continuing to send it onward.

## Connecting Commands with |

Suppose a directory listing is too long to read at once:

```bash
$ ls -la /etc
```

Place the pipe operator, `|`, between commands to connect the left command's stdout to the right command's stdin:

```bash
$ ls -la /etc | less
```

The shell starts the pipeline commands and arranges the stream connection. The commands can work concurrently: `less` can begin reading before `ls` has produced its entire listing.

:::single-choice{#pipe-stream-connection} In `ls -la /etc | less`, which streams does `|` connect by default?

::option[`ls` stdin to `less` stdout.]{#pipe-reversed-streams explanation="This reverses both the producer and consumer. Data flows from the left command's output to the right command's input."}
::option[`ls` stderr to both streams of `less`.]{#pipe-stderr-both explanation="A plain pipe does not connect the left command's stderr, and it does not target both streams of the right command."}
::option[`ls` stdout to `less` stdin.]{#pipe-stdout-stdin .correct explanation="A standard pipeline connects file descriptor 1 of the left command to file descriptor 0 of the right command."}
:::

## Keeping stderr Separate

A plain `|` carries stdout only. Stderr from the left command keeps its previous destination, which is often the terminal:

```bash
$ find /etc -name "*.conf" | less
```

Matching pathnames go through the pipe, while permission diagnostics can still appear directly on the terminal. Redirect stderr separately when you need different behavior:

```bash
$ find /etc -name "*.conf" 2> find-errors.log | less
```

:::single-choice{#pipe-left-stderr} In `find /etc -name "*.conf" | less`, where does `find`'s stderr normally go if no other redirection is present?

::option[Into `less` through the same pipe as stdout.]{#pipe-errors-to-less explanation="The ordinary pipe connects stdout only. Stderr is not automatically combined with it."}
::option[Into a file named `stderr` in the current directory.]{#pipe-errors-to-file explanation="No error-file redirection is present, so the shell does not create such a file."}
::option[To its existing destination, usually the terminal.]{#pipe-errors-terminal .correct explanation="Because descriptor 2 is unchanged, diagnostics normally remain connected to the terminal."}
:::

## Copying a Stream with tee

`tee` reads stdin, writes a copy to each named file, and also writes the same data to stdout:

```bash
$ ls | tee listing.txt
```

Here, `listing.txt` receives the listing and `tee`'s stdout remains connected to the terminal. By default, `tee` creates or truncates the named file, just like `>`.

:::single-choice{#tee-display-and-save} Which command displays `generate-report` output and also replaces `report.txt` with the same output?

::option[`generate-report > report.txt`]{#redirect-report-only explanation="A plain output redirection writes the file but does not keep a copy flowing to the terminal."}
::option[`generate-report | tee report.txt`]{#tee-report .correct explanation="`tee` copies stdin to `report.txt` and to its stdout, which remains the terminal in this pipeline."}
::option[`tee generate-report | report.txt`]{#tee-operands-reversed explanation="This treats `generate-report` as a destination filename and attempts to execute `report.txt` as a command. The producer belongs on the left."}
:::

Use `-a` when the file should be appended instead of replaced:

```bash
$ date | tee -a activity.log
```

:::single-choice{#tee-append-log} Which command displays the current date and appends it to `activity.log`?

::option[`date | tee -a activity.log`]{#tee-append-activity .correct explanation="The `-a` option makes `tee` append to the file while it continues copying the input to stdout."}
::option[`date | tee activity.log`]{#tee-replace-activity explanation="Without `-a`, `tee` replaces the existing file rather than preserving its earlier entries."}
::option[`date > activity.log`]{#redirect-replace-activity explanation="This replaces the file and sends no copy to the terminal. It meets neither the append nor display requirement."}
:::

## Saving an Intermediate Result

Put `tee` in the middle of a pipeline to save an intermediate stream and continue processing it:

```bash
$ ls -la /etc | tee etc-listing.txt | grep "conf"
```

This pipeline:

1. Produces the complete long listing.
2. Saves that complete stream in `etc-listing.txt`.
3. Sends the same stream to `grep`, which prints only lines containing `conf`.

The file contains the data before `grep` filters it. If you want only the filtered lines in the file, put `tee` after `grep`.

:::single-choice{#tee-before-filter-result} What does `all.txt` contain after `produce | tee all.txt | grep error` finishes successfully?

::option[Only the lines that `grep` matched.]{#tee-filtered-only explanation="`tee` runs before `grep`, so it writes the unfiltered input rather than the downstream match set."}
::option[Only stderr from `produce`.]{#tee-producer-stderr explanation="A plain pipe carries `produce` stdout. Its stderr is not the input to `tee`."}
::option[All stdout produced before filtering.]{#tee-complete-intermediate .correct explanation="`tee` saves every byte it receives, then passes that same stream to `grep` for filtering."}
:::

To practice pipelines and stream copying, try these hands-on labs:

1. **[Redirecting Input and Output in Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practice controlling data flow from commands by manipulating standard output (stdout), standard error (stderr), and standard input (stdin) using operators like `>`, `>>`, `2>`, and the `tee` command.
2. **[Sequence Control and Pipeline](https://labex.io/labs/linux-sequence-control-and-pipeline-17994)** - Learn to control command execution sequences, utilize pipelines, and leverage powerful text processing tools like `cut`, `grep`, `wc`, `sort`, and `uniq`.
3. **[Data Stream Redirection](https://labex.io/labs/linux-data-stream-redirection-17995)** - Learn the art of Linux stream redirection, including manipulating standard input, output, and error streams, combining outputs, and utilizing `/dev/null`.

## Summary

You can now connect commands and preserve selected points in a data stream.

1. Pipe stdout from one command into another command's stdin.
2. Redirect stderr separately when required.
3. Copy input to both a file and stdout with `tee`.
4. Append with `tee -a` instead of replacing a file.
5. Position `tee` before or after a filter deliberately.
