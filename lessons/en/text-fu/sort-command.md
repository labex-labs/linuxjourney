---
lesson_id: "sort-command"
course_id: "text-fu"
lang: "en"
order_index: 12
title: "sort"
description: "Learn how to order text lines by lexical, numeric, or selected field values with sort."
meta_title: "sort - Text-Fu"
meta_description: "Learn how to use the Linux sort command for sorting text files. Discover options like reverse and numerical sorting. Improve your Linux command line skills!"
meta_keywords: "Linux sort command, sort -r, sort -n, Linux tutorial, command line, beginner Linux, sort guide"
---

The `sort` command reads complete lines, orders them according to selected comparison rules, and writes the result to stdout. It does not change an input file unless you explicitly choose an output operation.

## Sorting Complete Lines

Consider `animals.txt`:

```text
dog
cow
cat
elephant
bird
```

Sort the lines in ascending order:

```bash
$ sort animals.txt
bird
cat
cow
dog
elephant
```

Text ordering follows the current locale, which can affect case, accents, and punctuation. Use a consistent locale such as `LC_ALL=C` when a script requires reproducible byte-oriented collation:

```bash
$ LC_ALL=C sort animals.txt
```

:::single-choice{#sort-lines-ascending}
What does `sort animals.txt` do with no key or numeric option?

::option[Orders complete input lines according to the current locale.]{#sort-locale-lines .correct explanation="Default `sort` compares whole lines using the active locale's collation rules."}
::option[Orders words within each line but keeps the line order fixed.]{#sort-words-within-lines explanation="`sort` treats each line as a record. It does not rearrange words inside individual lines."}
::option[Rewrites `animals.txt` in place automatically.]{#sort-auto-rewrite explanation="The sorted result goes to stdout by default, and the input file remains unchanged."}
:::

## Reversing the Result

Add `-r` to reverse the comparison result:

```bash
$ sort -r animals.txt
elephant
dog
cow
cat
bird
```

:::single-choice{#sort-reverse-order}
Which command sorts `animals.txt` in reverse order?

::option[`sort -n animals.txt`]{#sort-numeric-animals explanation="The `-n` option requests numeric comparison. It does not mean reverse order."}
::option[`sort -u animals.txt`]{#sort-unique-animals explanation="The `-u` option suppresses duplicate keys. It does not reverse the output."}
::option[`sort -r animals.txt`]{#sort-reverse-animals .correct explanation="The `-r` option reverses the ordering chosen by the other comparison rules."}
:::

## Comparing Numbers

Lexical order compares characters, so `10` normally comes before `2`. Use `-n` for ordinary numeric comparison:

```bash
$ printf '10\n2\n30\n' | sort -n
2
10
30
```

Combine options when needed. `sort -nr scores.txt` compares numerically and places larger values first.

:::single-choice{#sort-numbers-descending}
Which command sorts numeric lines in `scores.txt` from largest to smallest?

::option[`sort -n scores.txt`]{#sort-numeric-ascending explanation="Numeric comparison is selected, but the default direction places smaller values first."}
::option[`sort -nr scores.txt`]{#sort-numeric-reverse .correct explanation="`-n` selects numeric comparison and `-r` reverses it, producing descending numeric order."}
::option[`sort -r scores.txt`]{#sort-lexical-reverse explanation="This reverses text collation but does not request numeric comparison, so values such as `10` and `2` can order unexpectedly."}
:::

## Sorting by a Field

Use `-k START[,END]` to choose a key. Fields are separated by runs of blanks by default. For colon-separated records, use `-t ':'`:

```bash
$ printf 'alice:30\nbob:8\ncarol:20\n' | sort -t ':' -k 2,2n
bob:8
carol:20
alice:30
```

Here, `-t ':'` selects the delimiter, `-k 2,2` limits the key to field 2, and the attached `n` compares that key numerically. Without the ending `,2`, a key starting at field 2 normally continues through the rest of the line.

:::single-choice{#sort-second-colon-field}
Which command sorts `users.txt` numerically by only its second colon-separated field?

::option[`sort -n -k 1,1 users.txt`]{#sort-first-blank-field explanation="This uses default blank-separated fields and selects field 1, not the second colon-separated field."}
::option[`cut -d ':' -f 2 users.txt`]{#cut-second-user-field explanation="`cut` extracts field 2 but does not sort the original records by that key."}
::option[`sort -t ':' -k 2,2n users.txt`]{#sort-colon-field-two .correct explanation="The colon sets field boundaries, `2,2` confines the key to field 2, and `n` gives that key numeric comparison."}
:::

## Removing Duplicates and Saving Output

Use `-u` to output one line for each equal comparison key:

```bash
$ sort -u names.txt
```

This both sorts and removes duplicates under the selected comparison rules. If you only want to remove adjacent duplicates from already sorted data, the `uniq` command covered later can do that.

To write the result to a file, ordinary redirection is fine when the destination differs from the input:

```bash
$ sort names.txt > names-sorted.txt
```

Do not run `sort names.txt > names.txt`; the shell truncates the input before `sort` reads it. GNU `sort -o names.txt names.txt` safely arranges its own output when you intentionally want the same pathname:

```bash
$ sort -o names.txt names.txt
```

Keep a backup or write and verify a separate result when the original data matters.

:::single-choice{#sort-safe-same-file}
On GNU/Linux, which command asks `sort` to safely write the sorted result back to `names.txt` without shell redirection truncating it first?

::option[`sort -o names.txt names.txt`]{#sort-output-same-file .correct explanation="GNU `sort` manages `-o` output after reading as needed, so the shell does not pre-truncate the input through `>`."}
::option[`sort names.txt > names.txt`]{#sort-redirection-same-file explanation="The shell truncates `names.txt` before starting `sort`, so the command can lose the input."}
::option[`sort -u names.txt`]{#sort-unique-stdout explanation="This writes unique sorted lines to stdout and leaves the input file unchanged."}
:::

To practice ordering and analyzing line-oriented data, try these hands-on labs:

1. **[Linux sort Command: Text Sorting](https://labex.io/labs/linux-linux-sort-command-text-sorting-219196)** - This lab provides a direct introduction to the `sort` command, allowing you to practice sorting lines of text files in various ways, including ascending and descending order.
2. **[Word Count and Sorting](https://labex.io/labs/linux-word-count-and-sorting-388125)** - In this challenge, you'll apply your knowledge of sorting along with word counting to analyze text data, helping you find frequent patterns and sort data efficiently.

## Summary

You can now choose comparison rules and destinations for sorted text.

1. Sort complete lines under an explicit locale when reproducibility matters.
2. Reverse results with `-r`.
3. Compare numeric values with `-n`.
4. Select a bounded field key with `-t` and `-k`.
5. Remove duplicates or save output without truncating the input.
