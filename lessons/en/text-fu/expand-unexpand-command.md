---
lesson_id: "expand-unexpand-command"
course_id: "text-fu"
lang: "en"
order_index: 10
title: "expand and unexpand"
description: "Learn how tab stops control conversion between tabs and spaces with expand and unexpand."
meta_title: "expand and unexpand - Text-Fu"
meta_description: "Master text formatting in Linux with our guide on the expand and unexpand commands. Learn how to convert tabs to spaces and spaces back to tabs for consistent file layouts."
meta_keywords: "expand command, unexpand command, Linux tabs, Linux spaces, text formatting, Linux tutorial, beginner Linux, Linux guide"
---

Tabs store movement to a tab stop rather than a fixed number of visible spaces. Their displayed width depends on the current column and the tab-stop settings. The `expand` and `unexpand` commands convert between tab characters and spaces while accounting for those positions.

## Converting Tabs to Spaces

`expand` reads input, replaces tabs with the spaces needed to reach the appropriate tab stops, and writes the result to stdout:

```bash
$ expand sample.txt
```

By default, tab stops occur every 8 columns. A tab at column 1 therefore expands differently from a tab at column 6; it is not always replaced by eight spaces.

:::single-choice{#expand-default-tab-stops}
With default settings, how does `expand` replace a tab character?

::option[It inserts enough spaces to reach the next default tab stop.]{#expand-next-stop .correct explanation="`expand` preserves tab-stop alignment by calculating the spaces needed from the current column."}
::option[It always inserts exactly eight spaces.]{#expand-eight-spaces explanation="Default stops are eight columns apart, but the number of spaces depends on the current column."}
::option[It removes the tab without adding any characters.]{#expand-remove-tab explanation="The command replaces the tab with spaces so later text remains aligned at the selected tab stop."}
:::

## Choosing Tab Stops

Use `-t NUMBER` to place tab stops every specified number of columns. For four-column stops:

```bash
$ expand -t 4 sample.txt
```

GNU `expand` also accepts a comma-separated list of explicit tab positions. Use `-i` when only tabs before the first nonblank character on each line should be converted.

:::single-choice{#expand-four-column-stops}
Which command converts tabs using tab stops every four columns?

::option[`expand -i 4 sample.txt`]{#expand-initial-four explanation="The `-i` option limits conversion to initial tabs and does not take `4` as the tab-stop interval."}
::option[`unexpand -t 4 sample.txt`]{#unexpand-tabs-four explanation="`unexpand` converts suitable spaces to tabs, the reverse direction from the requested operation."}
::option[`expand -t 4 sample.txt`]{#expand-tabs-four .correct explanation="The `-t` option sets the tab-stop interval, and `4` requests stops every four columns."}
:::

## Saving Converted Output Safely

`expand` does not edit its input file. Redirect stdout to a different pathname when you want to save the converted text:

```bash
$ expand sample.txt > result.txt
```

Do not use `expand sample.txt > sample.txt`. The shell truncates the destination before `expand` can read it, so the source data can be lost. After verifying a separately written result, you can deliberately replace the original using an appropriate file-management step.

:::single-choice{#expand-safe-output-file}
Which command saves expanded text without truncating `sample.txt` before it is read?

::option[`expand sample.txt > sample.txt`]{#expand-same-file explanation="The shell opens and truncates `sample.txt` for output before starting `expand`, which can erase the input."}
::option[`expand sample.txt > result.txt`]{#expand-separate-result .correct explanation="The input and output pathnames differ, so the shell can create `result.txt` without destroying the source."}
::option[`> sample.txt expand result.txt`]{#expand-leading-redirection explanation="This still truncates `sample.txt` and does not express a safe conversion from the original file."}
:::

## Converting Spaces to Tabs

`unexpand` replaces eligible spaces with tabs while preserving alignment at the selected tab stops. By default, GNU `unexpand` converts only initial blanks before the first nonblank character on a line:

```bash
$ unexpand result.txt
```

Use `-a` to consider suitable blanks throughout each line:

```bash
$ unexpand -a result.txt
```

This does not simply replace every run of eight spaces. Conversion depends on column positions and tab stops, just as it does for `expand`. Use `-t 4` or another tab-stop specification when the file follows a different convention.

:::single-choice{#unexpand-default-scope}
Without `-a`, which spaces does GNU `unexpand` normally consider for conversion?

::option[Every group of spaces anywhere in the file.]{#unexpand-every-group explanation="Considering blanks throughout the line requires `-a`, and conversion still depends on tab-stop positions."}
::option[Only spaces that appear after the final word.]{#unexpand-trailing-blanks explanation="The default scope concerns initial blanks, not specifically trailing whitespace."}
::option[Only initial blanks before the first nonblank character.]{#unexpand-initial-blanks .correct explanation="Default GNU `unexpand` behavior is limited to leading blank space on each line."}
:::

:::single-choice{#unexpand-all-blanks}
Which option tells GNU `unexpand` to consider blanks after the first nonblank character too?

::option[`-i`]{#unexpand-initial-option explanation="For `expand`, `-i` limits work to initial tabs. It is not the all-blanks option for `unexpand`."}
::option[`-a`]{#unexpand-all-option .correct explanation="The `-a` option enables conversion of suitable blanks throughout each input line."}
::option[`-t`]{#unexpand-tab-list-option explanation="The `-t` option sets tab stops. Although GNU behavior can imply broader conversion with it, `-a` explicitly requests all blanks."}
:::

Both commands read stdin when no file is named, so they can be used in pipelines. Remember that converting to spaces and back may not reconstruct the original choice of tabs and spaces even when the displayed alignment is unchanged.

## Summary

You can now convert tabs and spaces while preserving tab-stop alignment.

1. Expand tabs to the next configured stop.
2. Set custom tab stops with `-t`.
3. Save output to a different file before replacing an input.
4. Convert leading blanks with `unexpand` by default.
5. Use `-a` when blanks throughout each line should be considered.
