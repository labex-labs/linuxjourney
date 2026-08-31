---
lesson_id: "head-command"
course_id: "text-fu"
lang: "en"
order_index: 8
title: "head"
description: "Learn how to display a controlled number of lines or bytes from the beginning of input."
meta_title: "head - Text-Fu"
meta_description: "A beginner Linux guide on using the head command to view the beginning of a file. Learn how to use the head -n option to control line count, an essential skill for any Linux tutorial."
meta_keywords: "head command, Linux head, view file beginning, Linux tutorial, Linux commands, beginner Linux, head -n, Linux guide, text files, command line"
---

The `head` command displays the beginning of a file or input stream. It is useful for checking headers, previewing structured data, or sampling output without printing everything.

## Displaying the First Ten Lines

With no count option, `head` prints the first 10 lines of each named file:

```bash
$ head events.log
```

The file is not modified. If it contains fewer than 10 lines, all available lines are printed.

:::single-choice{#head-default-lines}
What does `head events.log` print by default?

::option[The last 10 lines, or all lines if the file is shorter.]{#head-last-ten explanation="Displaying the end of input is the role of `tail`. `head` selects from the beginning."}
::option[The first 10 lines, or all lines if the file is shorter.]{#head-first-ten .correct explanation="Without a count option, `head` selects up to the first ten lines of the input."}
::option[Only the first line, regardless of the file length.]{#head-first-one explanation="One line requires an explicit count such as `-n 1`; the default count is ten."}
:::

## Choosing a Line Count

Use `-n NUMBER` to choose how many lines to print:

```bash
$ head -n 15 events.log
```

GNU `head` also accepts the compact form `-15`, but `-n 15` states the option's meaning more clearly.

:::single-choice{#head-five-lines}
Which command displays the first five lines of `report.txt`?

::option[`head -c 5 report.txt`]{#head-five-bytes explanation="The `-c` option counts bytes rather than lines, so it may stop within the first line."}
::option[`head -n 5 report.txt`]{#head-report-five .correct explanation="The `-n` option selects a line count, and `5` requests the first five lines."}
::option[`tail -n 5 report.txt`]{#tail-five-lines explanation="This displays the final five lines of the file, not the beginning."}
:::

## Choosing a Byte Count

Use `-c NUMBER` when you need bytes rather than complete lines:

```bash
$ head -c 20 archive.bin
```

This prints the first 20 bytes. The output may end in the middle of a text line or, for multibyte text, in the middle of an encoded character. Use line mode for ordinary text previews.

:::single-choice{#head-first-bytes}
Which command writes the first 100 bytes of `payload.bin` to stdout?

::option[`head -c 100 payload.bin`]{#head-hundred-bytes .correct explanation="The `-c` option selects a byte count, so exactly the available first 100 bytes are requested."}
::option[`head -n 100 payload.bin`]{#head-hundred-lines explanation="The `-n` option counts lines, not bytes. It can produce far more or less than 100 bytes."}
::option[`cut -c 100 payload.bin`]{#cut-hundredth-character explanation="This selects position 100 from each line rather than the first 100 bytes of the entire input."}
:::

## Reading stdin and Multiple Files

When no file operand is supplied, `head` reads stdin:

```bash
$ generate-report | head -n 5
```

When several files are named, `head` normally adds a header identifying each file's output:

```bash
$ head -n 2 january.txt february.txt
==> january.txt <==
...

==> february.txt <==
...
```

Use `-q` to suppress these headers or `-v` to show a header even for one file.

:::single-choice{#head-pipeline-preview}
In `generate-report | head -n 5`, what does `head` read?

::option[The stdout of `generate-report` through stdin.]{#head-pipe-input .correct explanation="The pipe connects the producer's stdout to `head`'s stdin, from which the first five lines are selected."}
::option[The first five filenames in the current directory.]{#head-directory-names explanation="No directory-listing command is involved. `head` receives a stream through the pipeline."}
::option[Five bytes from a file named `generate-report`.]{#head-producer-file explanation="The left side is executed as a command, and `-n` counts lines rather than bytes."}
:::

:::single-choice{#head-suppress-filename-headers}
Which option suppresses filename headers when `head` reads several files?

::option[`-v`]{#head-verbose explanation="The `-v` option requests headers even when only one file is supplied, the opposite of suppression."}
::option[`-c`]{#head-byte-option explanation="The `-c` option changes the selection unit to bytes. It does not control filename headers."}
::option[`-q`]{#head-quiet .correct explanation="The `-q` or quiet option prevents `head` from printing per-file header labels."}
:::

To practice previewing file beginnings, try these hands-on labs:

1. **[Linux head Command: File Beginning Display](https://labex.io/labs/linux-linux-head-command-file-beginning-display-214302)** - This lab will guide you through using the `head` command to display the initial lines of text files, including modifying the line count.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice essential Linux command-line skills for efficiently viewing and navigating text files, including system logs and configuration files, which often require commands like `head`.
3. **[Rapid Threat Detection](https://labex.io/labs/linux-rapid-threat-detection-387930)** - Apply your knowledge of `head` (and `tail`) to quickly extract and analyze recent log entries, simulating real-world cybersecurity analysis.

## Summary

You can now preview the beginning of files and command output with `head`.

1. Use the default first-ten-line view.
2. Select a line count with `-n`.
3. Select a byte count with `-c` when appropriate.
4. Read from stdin in a pipeline.
5. Control headers when several files are shown.
