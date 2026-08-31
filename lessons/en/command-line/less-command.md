---
lesson_id: "less-command"
course_id: "command-line"
lang: "en"
order_index: 8
title: "less"
description: "Learn how to navigate, search, and follow long text files interactively with less."
meta_title: "less - Command Line"
meta_description: "Learn the Linux less command with examples for viewing large files, scrolling, searching, jumping to lines, following logs, and quitting less."
meta_keywords: "less command, linux less, view large file linux, search in less, quit less, less -N, less +F, text viewer linux"
---

When a text file is too long for one screen, `less` lets you read it without sending the entire file scrolling through the terminal. Its name inspired the old Unix joke, "less is more," because `more` is another pager.

## Opening a File

Start the pager by passing it a filename:

```bash
$ less /home/pete/Documents/text1
```

While `less` is active, keystrokes control the pager rather than starting ordinary shell commands. You return to the shell when you quit the pager.

:::single-choice{#open-long-file}
Which command opens `/var/log/syslog` in an interactive pager?

::option[`less /var/log/syslog`]{#page-log .correct explanation="`less` opens the file in a pager so you can move through it, search it, and quit back to the shell."}
::option[`cat /var/log/syslog`]{#print-log explanation="`cat` sends the whole file to standard output at once. It does not provide interactive paging controls."}
::option[`file /var/log/syslog`]{#classify-log explanation="`file` reports a likely content type. It does not open the log for interactive reading."}
:::

## Navigating in less

Use these keys while the pager is open:

- Use `Up`, `Down`, `Page Up`, and `Page Down` to move by lines or screens.
- Press `g` to jump to the beginning.
- Press `G` to jump to the end.
- Press `u` to move up half a screen or `d` to move down half a screen.
- Press `h` to open the built-in help.

:::single-choice{#jump-to-file-end}
Which key jumps directly to the end of a file in `less`?

::option[`g`]{#lowercase-g explanation="Lowercase `g` jumps to the beginning of the file. The uppercase form goes in the opposite direction."}
::option[`G`]{#uppercase-g .correct explanation="Uppercase `G` jumps to the end of the input. The command is case-sensitive."}
::option[`h`]{#help-key explanation="The `h` key opens the pager's help screen. It does not jump to the end of the file."}
:::

## Searching in less

Type `/` followed by a pattern and press Enter to search forward. Begin with `?` to search backward.

- `/search_term`: Search forward for `search_term`.
- `?search_term`: Search backward for `search_term`.
- `n`: Repeat the search in the same direction.
- `N`: Repeat the search in the opposite direction.

:::single-choice{#repeat-search-direction}
After a forward search for `error`, which key repeats the search in the same direction?

::option[`n`]{#same-search .correct explanation="Lowercase `n` repeats the most recent search in its original direction. Here, that direction is forward."}
::option[`N`]{#opposite-search explanation="Uppercase `N` repeats the most recent search in the opposite direction. After a forward search, it moves backward through matches."}
::option[`g`]{#search-to-start explanation="The `g` key jumps to the beginning of the input. It does not repeat a search."}
:::

## Leaving less

Press `q` to quit `less` and return to the shell prompt.

:::single-choice{#quit-less}
Which key exits `less` and returns to the shell?

::option[`q`]{#less-quit .correct explanation="The `q` command quits the pager and restores the shell prompt."}
::option[`h`]{#less-help explanation="The `h` key opens help inside `less`. It does not return directly to the shell."}
::option[`G`]{#less-end explanation="Uppercase `G` moves to the end of the input. The pager remains open."}
:::

## Starting less with Options

Options and initial commands can change how the pager starts:

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`: Show line numbers.
- `+G`: Open at the end of the file.
- `+F`: Follow new content as it is added, similar to `tail -f`.

While following a file with `+F`, press `Ctrl+C` to stop following and return to normal navigation, then press `q` to quit. Use `-i` for searches that ignore case unless the pattern contains an uppercase letter, or `-I` to ignore case regardless of the pattern.

Commands can also send output through a pipe to `less`:

```bash
$ dmesg | less
```

:::single-choice{#follow-growing-log}
Which command opens `/var/log/syslog` and follows new content as it arrives?

::option[`less +F /var/log/syslog`]{#follow-log .correct explanation="The `+F` initial command enters follow mode, so `less` displays new content appended to the log."}
::option[`less +G /var/log/syslog`]{#open-at-log-end explanation="The `+G` initial command opens at the end, but it does not keep following content that arrives later."}
::option[`less -N /var/log/syslog`]{#number-log-lines explanation="The `-N` option displays line numbers. It does not enable continuous following."}
:::

To practice paging, searching, and reading system text, try these hands-on labs:

1. **[Linux less Command: File Paging](https://labex.io/labs/linux-linux-less-command-file-paging-214301)** - Learn the Linux 'less' command for efficient text file viewing and navigation, including search, line numbers, and pattern matching.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Learn essential Linux command-line skills for efficiently viewing and navigating text files, including system logs and configuration files, using commands like `cat`, `more`, and `less`.

## Summary

You can now use `less` to inspect long files without flooding the terminal.

1. Open a file or piped command output in the pager.
2. Navigate to specific parts of the input.
3. Search forward or backward and repeat a search.
4. Show line numbers or follow growing content.
5. Quit safely and return to the shell.
