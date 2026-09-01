---
lesson_id: "cut-command"
course_id: "text-fu"
lang: "en"
order_index: 6
title: "cut"
description: "Learn how to select character positions or delimited fields from each line with cut."
meta_title: "cut - Text-Fu"
meta_description: "Learn how to use the Linux `cut` command to extract specific sections of text from files. This guide covers cutting by character and field (`cut f`), including how to cut f with custom delimiters. Perfect for mastering Linux text processing."
meta_keywords: "cut command, Linux text processing, extract text, cut f, how to cut f, Linux tutorial, cut examples, Linux guide, field cutting"
---

The `cut` command selects specified character positions or fields from each input line. It works best with consistently structured text whose delimiters and field positions are known.

Create a small tab-separated file for the examples. `printf` interprets `\t` as a literal tab and `\n` as a newline:

```bash
$ printf 'name\trole\nalice\tadmin\nbob\tviewer\n' > team.tsv
```

## Selecting Character Positions

Use `-c LIST` to select positions from each line. Positions start at 1:

```bash
$ cut -c 1 team.tsv
n
a
b
```

The list can contain individual positions and ranges:

```bash
$ cut -c 1-4 team.tsv
name
alic
bob
$ cut -c 1,3 team.tsv
nm
ai
bb
```

Spaces, tabs, and punctuation occupy positions too. `cut` processes each line independently.

:::single-choice{#cut-first-character} Which command prints the first character from every line of `names.txt`?

::option[`cut -c 1 names.txt`]{#cut-character-one .correct explanation="The `-c` option selects character positions, and position 1 is the first character of each line."}
::option[`cut -f 1 names.txt`]{#cut-field-one explanation="The `-f` option selects the first tab-delimited field, which can contain more than one character."}
::option[`cut -d 1 names.txt`]{#cut-delimiter-one explanation="The `-d` option specifies a field delimiter and must be paired with field selection. It does not select a character position."}
:::

## Selecting Tab-Delimited Fields

Use `-f LIST` to select fields. The default delimiter is a tab:

```bash
$ cut -f 2 team.tsv
role
admin
viewer
```

As with character selection, a list can include values such as `1`, `1,3`, `2-4`, `-3`, or `2-`.

:::single-choice{#cut-second-tab-field} Which command prints the second tab-delimited field from every line of `team.tsv`?

::option[`cut -c 2 team.tsv`]{#cut-second-character explanation="This selects the second character position from each line, not the second tab-separated field."}
::option[`cut -f 2 team.tsv`]{#cut-second-field .correct explanation="Without `-d`, field mode uses a tab delimiter, and `-f 2` selects the second field."}
::option[`cut -d 2 team.tsv`]{#cut-delimiter-two explanation="This tries to use `2` as a delimiter but supplies no field list. It does not select field 2."}
:::

## Choosing a Custom Delimiter

Use `-d CHARACTER` with `-f` when fields use a delimiter other than a tab. This example creates semicolon-separated data:

```bash
$ printf 'alice;admin\nbob;viewer\n' > team.txt
$ cut -d ';' -f 1 team.txt
alice
bob
```

The delimiter for this form is one character. Quote `;` because an unquoted semicolon has control meaning in the shell.

:::single-choice{#cut-semicolon-role-field} Which command prints the second semicolon-delimited field from `team.txt`?

::option[`cut -d ':' -f 2 team.txt`]{#cut-colon-second explanation="This selects fields separated by colons, but the file uses semicolons."}
::option[`cut -d ';' -f 2 team.txt`]{#cut-semicolon-second .correct explanation="The quoted semicolon sets the delimiter, and `-f 2` selects the second field from each line."}
::option[`cut -c 2 -f ';' team.txt`]{#cut-mixed-options explanation="This mixes character selection with an invalid field argument. The delimiter belongs after `-d`, and the field number after `-f`."}
:::

## Handling Lines without the Delimiter

In field mode, `cut` normally prints a line unchanged when it contains no delimiter. Add `-s` to suppress those lines:

```bash
$ printf 'alice;admin\nheader\nbob;viewer\n' | cut -s -d ';' -f 2
admin
viewer
```

This does not validate a general CSV file. CSV can contain quoted delimiters, embedded newlines, and escaping rules that a single-character split does not understand; use a CSV-aware tool for such data.

:::single-choice{#cut-suppress-undelimited} What does `-s` do with `cut -d ':' -f 1`?

::option[It sorts the selected fields before printing them.]{#cut-s-sort explanation="`cut` does not sort input, and `-s` is unrelated to ordering."}
::option[It treats consecutive delimiters as one separator.]{#cut-s-squeeze explanation="`cut` does not use `-s` to collapse delimiters. Empty fields remain meaningful positions."}
::option[It suppresses lines that contain no selected delimiter.]{#cut-s-suppress .correct explanation="In field mode, `-s` prevents undelimited lines from being passed through unchanged."}
:::

## Reading from stdin

When no file is named, or when `-` is used as an input operand, `cut` reads stdin. That makes it a natural pipeline stage:

```bash
$ printf 'red:1\nblue:2\n' | cut -d ':' -f 1
red
blue
```

:::single-choice{#cut-pipeline-input} In `generate-data | cut -d ':' -f 1`, where does `cut` read its input?

::option[From the stdout of `generate-data` through the pipe.]{#cut-pipe-stdin .correct explanation="The pipe connects the producer's stdout to `cut`'s stdin, and no separate input file is named."}
::option[From a file whose literal name is `generate-data`.]{#cut-pipe-file explanation="`generate-data` is executed as the left pipeline command. It is not passed to `cut` as a filename."}
::option[From `cut`'s standard error stream.]{#cut-pipe-stderr explanation="A normal pipe feeds standard input from the previous command's stdout, not from `cut`'s stderr."}
:::

To practice positional and field selection, try these hands-on labs:

1. **[Linux cut Command: Text Cutting](https://labex.io/labs/linux-linux-cut-command-text-cutting-219187)** - This lab provides a direct, hands-on introduction to the `cut` command, allowing you to practice extracting specific columns or fields from text files, just as discussed in the lesson.
2. **[Sequence Control and Pipeline](https://labex.io/labs/linux-sequence-control-and-pipeline-17994)** - Enhance your command-line efficiency by learning to control command execution sequences, utilize pipelines, and leverage powerful text processing tools like `cut`, `grep`, `wc`, `sort`, and `uniq`.

## Summary

You can now select predictable positions from line-oriented text with `cut`.

1. Select individual character positions or ranges.
2. Extract tab-delimited fields with `-f`.
3. Supply a one-character delimiter with `-d`.
4. Suppress undelimited lines when appropriate.
5. Read structured text from files or stdin.
