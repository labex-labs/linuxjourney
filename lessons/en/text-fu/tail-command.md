---
lesson_id: "tail-command"
course_id: "text-fu"
lang: "en"
order_index: 9
title: "tail"
description: "Learn how to view the end of input and follow files as new content is appended."
meta_title: "tail - Text-Fu"
meta_description: "A beginner Linux guide to the tail command. Learn how to use Linux tail to view the end of files and monitor logs in real-time with the powerful tail -f option."
meta_keywords: "tail command, Linux tail, tail -f, view logs, monitor logs, Linux tutorial, beginner Linux, Linux guide, file monitoring"
---

The `tail` command displays the end of a file or input stream. It can also remain active and show data appended to a file, which is useful when observing logs.

## Displaying the Last Ten Lines

With no count option, `tail` prints the last 10 lines of each named file:

```bash
$ tail application.log
```

If the file contains fewer than 10 lines, all available lines are printed. The file itself is not changed.

:::single-choice{#tail-default-lines}
What does `tail application.log` display by default?

::option[Up to the initial 10 lines of the file.]{#tail-first-ten explanation="The beginning of a file is selected by `head`. `tail` works from the end."}
::option[Every line added after the command starts.]{#tail-follow-only explanation="Continuous following requires `-f` or a related option. Plain `tail` prints a snapshot and exits."}
::option[Up to the final 10 lines of the file.]{#tail-last-ten .correct explanation="Without a count option, `tail` selects the final ten lines, or every line when fewer are available."}
:::

## Choosing a Line or Byte Count

Use `-n NUMBER` to select a different number of final lines:

```bash
$ tail -n 20 application.log
```

Use `-c NUMBER` when you need the final bytes instead:

```bash
$ tail -c 100 payload.bin
```

Byte mode can begin in the middle of a text line or encoded character, so line mode is usually clearer for text.

:::single-choice{#tail-twenty-lines}
Which command displays the final 20 lines of `application.log`?

::option[`tail -n 20 application.log`]{#tail-twenty-end .correct explanation="The `-n` option selects a line count, and `tail` takes those lines from the end."}
::option[`head -n 20 application.log`]{#head-twenty-start explanation="This selects 20 lines from the beginning rather than from the end."}
::option[`tail -c 20 application.log`]{#tail-twenty-bytes explanation="The `-c` option selects the final 20 bytes, which is not the same as 20 lines."}
:::

## Starting at a Particular Line

A count prefixed with `+` changes the meaning: `tail -n +N` starts with line N and prints through the end.

```bash
$ tail -n +5 report.txt
```

This skips the first four lines and begins at line 5. It is useful for removing a known number of header lines from a stream.

:::single-choice{#tail-start-line-five}
Which command prints `report.txt` starting with line 5?

::option[`tail -n +5 report.txt`]{#tail-from-five .correct explanation="The `+5` count tells `tail` to begin at line 5 and continue through the end."}
::option[`tail -n 5 report.txt`]{#tail-final-five explanation="Without a plus sign, this selects the final five lines, regardless of their absolute line numbers."}
::option[`head -n +5 report.txt`]{#head-plus-five explanation="This is not the `tail` start-at-line form. Use `tail -n +5` for the requested range."}
:::

## Following Appended Data

With `-f`, `tail` prints the initial ending and remains active, showing data as it is appended:

```bash
$ tail -f application.log
```

Press `Ctrl+C` to interrupt `tail` and return to the shell. Following a file only displays new content; it does not guarantee that the application producing the log is healthy or that every relevant event uses that file.

:::single-choice{#tail-follow-file}
Which command shows the current end of `application.log` and keeps waiting for appended content?

::option[`tail -f application.log`]{#tail-follow-app .correct explanation="The `-f` option keeps `tail` active and displays data appended to the file."}
::option[`tail -n 0 application.log`]{#tail-zero-lines explanation="This initially prints no lines and exits because no follow option is present."}
::option[`less application.log`]{#less-log explanation="`less` provides interactive paging, but this form does not remain in `tail`-style follow mode."}
:::

## Following a Rotated Log by Name

Log rotation can rename an old file and create a new file at the original pathname. GNU `tail -F` is equivalent to following by name while retrying, so it can reopen a file that is replaced or temporarily missing:

```bash
$ tail -F application.log
```

Use `-f` when following the currently opened file is the desired behavior, and `-F` when a named log is expected to rotate. These are GNU behaviors; other implementations can differ.

:::single-choice{#tail-follow-rotated-name}
On GNU/Linux, which option is better suited to following `application.log` across common rename-and-recreate log rotation?

::option[`-n`]{#tail-rotation-lines explanation="The `-n` option changes the number of lines displayed. It does not retry a replaced pathname."}
::option[`-c`]{#tail-rotation-bytes explanation="The `-c` option changes the selection unit to bytes. It does not provide rotation-aware following."}
::option[`-F`]{#tail-follow-name .correct explanation="GNU `-F` follows by name and retries, allowing `tail` to reopen a log that is replaced or temporarily absent."}
:::

When no file is named, `tail` reads stdin, so it can select the end of command output. Multiple named files receive identifying headers by default, as with `head`.

To practice viewing and following file endings, try these hands-on labs:

1. **[Linux tail Command: File End Display](https://labex.io/labs/linux-linux-tail-command-file-end-display-214303)** - Learn the Linux `tail` command for viewing and monitoring the end of text files, including the `-f` option for real-time updates.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice using `tail` (along with `cat` and `more`) to efficiently view and navigate log and configuration files, which is crucial for system monitoring.
3. **[Rapid Threat Detection](https://labex.io/labs/linux-rapid-threat-detection-387930)** - Apply your knowledge of `tail` to quickly extract and analyze recent log entries, simulating rapid threat detection in a cybersecurity context.

## Summary

You can now inspect file endings and observe newly appended content with `tail`.

1. Display the final ten lines by default.
2. Select a line or byte count explicitly.
3. Start output at a numbered line with `-n +N`.
4. Follow appended content with `-f` and stop with `Ctrl+C`.
5. Use GNU `-F` when a named log may be rotated.
