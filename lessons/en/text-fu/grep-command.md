---
lesson_id: "grep-command"
course_id: "text-fu"
lang: "en"
order_index: 16
title: "grep"
description: "Learn how to select lines with fixed strings or regular expressions and interpret grep results."
meta_title: "grep - Text-Fu"
meta_description: "Learn to use the powerful grep command in Linux to search for text patterns. This guide covers basic usage, the grep -e command, grep -c for counting, and other essential options for effective text processing."
meta_keywords: "grep command, grep -e command, grep -c, grep -f, grep -o, grep -e example, linux grep, search text, pattern matching, text processing, linux tutorial"
---

The `grep` command selects input lines that match a pattern. It can search named files or stdin, print matching context, count selected lines, and communicate whether a match was found through its exit status.

## Matching Lines in a File

Pass a pattern followed by one or more input files:

```bash
$ grep 'fox' sample.txt
```

By default, GNU `grep` interprets the pattern as a basic regular expression and prints every selected line. Quote patterns to keep spaces and shell metacharacters from being interpreted by the shell first.

Use `-F` when the pattern should be treated as a fixed string rather than a regular expression:

```bash
$ grep -F 'price: $5.00' products.txt
```

:::single-choice{#grep-fixed-string} Which command searches `products.txt` for the literal text `price: $5.00` without treating pattern characters as regular-expression syntax?

::option[`grep -F 'price: $5.00' products.txt`]{#grep-fixed-price .correct explanation="`-F` selects fixed-string matching, and single quotes protect the dollar sign from shell expansion."}
::option[`grep -E 'price: $5.00' products.txt`]{#grep-extended-price explanation="`-E` enables extended regular expressions, where `$` and `.` have special meanings rather than being literal."}
::option[`grep -v 'price: $5.00' products.txt`]{#grep-invert-price explanation="`-v` selects nonmatching lines and still uses regular-expression interpretation by default."}
:::

## Selecting Pattern Syntax

GNU `grep` offers three commonly used pattern modes:

- Default: Basic regular expressions.
- `-E`: Extended regular expressions, including operators such as `|`, `+`, and `?` without backslashes.
- `-F`: Fixed strings with no regular-expression operators.

Anchors such as `^` and `$` match the beginning and end of a line. To match filenames ending in the literal suffix `.txt` within a text list:

```bash
$ grep -E '\.txt$' filenames.txt
```

The backslash makes the dot literal; an unescaped `.` in a regular expression matches any single character.

:::single-choice{#grep-literal-txt-suffix} Which extended regular expression matches lines ending with the literal suffix `.txt`?

::option[`'.txt$'`]{#grep-anychar-txt explanation="The dot is unescaped, so it matches any one character before `txt`, not specifically a literal period."}
::option[`'\.txt$'`]{#grep-dot-txt-end .correct explanation="`\.` matches a literal period and `$` anchors the match at the end of the line."}
::option[`'^.txt'`]{#grep-start-anychar-txt explanation="This anchors at the beginning and still uses an unescaped dot, so it expresses a different match."}
:::

## Supplying Patterns Safely

Use `-e PATTERN` to supply a pattern explicitly. This is particularly useful when the pattern begins with `-`, because quoting alone does not stop option parsing:

```bash
$ grep -e '-v' settings.conf
```

You can repeat `-e` to select lines matching any supplied pattern. Use `-f patterns.txt` to read one pattern per line from a file.

:::single-choice{#grep-hyphen-pattern} Which command searches `settings.conf` for the pattern `-v` rather than interpreting it as an option?

::option[`grep '-v' settings.conf`]{#grep-quoted-v explanation="Quotes protect characters from shell expansion, but `grep` can still interpret the resulting `-v` argument as its invert-match option."}
::option[`grep -v settings.conf`]{#grep-invert-settings explanation="This enables inverted matching and does not supply `settings.conf` as both a pattern and an input in the requested way."}
::option[`grep -e '-v' settings.conf`]{#grep-explicit-v .correct explanation="The `-e` option declares that the following argument is a pattern even though it starts with a hyphen."}
:::

## Controlling Selected Output

- `-i`: Ignore case distinctions.
- `-n`: Prefix selected lines with line numbers.
- `-v`: Select lines that do not match.
- `-c`: Print the count of selected lines for each input file.
- `-o`: Print only each nonempty matching part rather than the full selected line.

For example, count lines containing `fox`, ignoring case:

```bash
$ grep -ic 'fox' sample.txt
```

`-c` counts selected lines, not the total number of matches within those lines. A line containing `fox fox` contributes one to the count. When you specifically need nonoverlapping match occurrences with GNU `grep`, `grep -o PATTERN | wc -l` is one possible pipeline.

:::single-choice{#grep-count-lines} `data.txt` has one line containing `error error` and two lines with no match. What does `grep -c 'error' data.txt` report?

::option[`2`, because the word occurs twice on one line.]{#grep-count-occurrences explanation="`-c` counts selected lines, not individual matches within a line."}
::option[`1`, because exactly one line matches.]{#grep-count-one-line .correct explanation="The single line is selected once even though the pattern appears twice within it."}
::option[`3`, because the file contains three lines total.]{#grep-count-total-lines explanation="Only selected lines contribute to `grep -c`; nonmatching lines are excluded."}
:::

## Filtering stdin and Searching Directories

When no input file is named, `grep` reads stdin and fits naturally in a pipeline:

```bash
$ env | grep '^USER='
```

Use `-r` to search readable files recursively below a directory:

```bash
$ grep -r 'listen_port' config/
```

Diagnostics such as permission errors go to stderr and are not matching input. Narrow the search path and understand permissions rather than immediately elevating access.

:::single-choice{#grep-pipeline-input} In `generate-report | grep 'failed'`, what input does `grep` search?

::option[A file named `generate-report` in the current directory.]{#grep-report-file explanation="The left-hand word is executed as a command and is not passed to `grep` as a file operand."}
::option[The stdout stream produced by `generate-report`.]{#grep-report-stdout .correct explanation="The pipe connects the producer's stdout to `grep`'s stdin."}
::option[The stderr stream produced by `generate-report`.]{#grep-report-stderr explanation="A plain pipe carries stdout. Stderr remains separate unless it is explicitly redirected."}
:::

## Interpreting the Exit Status

For ordinary searches, GNU `grep` returns status `0` when at least one line is selected, `1` when no line is selected, and `2` for an error. This lets scripts test for a match without treating “no match” as the same condition as an unreadable file or invalid pattern.

Options such as `-q` suppress normal output and stop after a match is found, which is useful for condition checks. Do not infer success from empty display alone: `-q`, redirection, no match, and an error can all produce little or no stdout, while their statuses differ.

To practice fixed-string and regular-expression searches, try these hands-on labs:

1. **[Search Text with grep in Linux](https://labex.io/labs/comptia-search-text-with-grep-in-linux-590841)** - Practice basic searches, display line numbers, use anchors, and harness both basic and extended regular expressions for complex pattern matching with `grep`.
2. **[Linux grep Command: Pattern Searching](https://labex.io/labs/linux-linux-grep-command-pattern-searching-219192)** - Learn to use `grep` for searching and matching patterns within text files, and explore regular expressions to define complex search patterns.
3. **[Needle in the Haystack](https://labex.io/labs/linux-needle-in-the-haystack-388109)** - Learn the power of the `grep` command to search for specific patterns, count occurrences, extract unique values, and combine multiple search criteria across various log files.

## Summary

You can now search line-oriented text and distinguish matches from errors.

1. Choose basic, extended, or fixed-string matching.
2. Quote patterns and use `-e` for a leading hyphen.
3. Count selected lines without confusing them with occurrences.
4. Filter stdin or recursively search a focused directory.
5. Interpret exit statuses for match, no match, and error.
