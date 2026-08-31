---
lesson_id: "uniq-unique-command"
course_id: "text-fu"
lang: "en"
order_index: 14
title: "uniq (Unique)"
description: "Learn how to collapse, count, or filter adjacent groups of equal lines with uniq."
meta_title: "uniq (Unique) - Text-Fu"
meta_description: "Explore the uniq command in Linux to filter and remove duplicate adjacent lines from text. Learn how to use the uniq linux tool with options like -c, -u, -d, and combine it with sort for powerful text processing."
meta_keywords: "uniq command, Linux uniq, uniq linux, remove duplicates, sort uniq, text processing, data cleaning, Linux tutorial"
---

The `uniq` command compares each input line with the preceding line. It can collapse, count, or select groups of adjacent equal lines, but it does not search the entire file for separated duplicates.

## Collapsing Adjacent Duplicate Lines

Suppose `reading.txt` contains grouped values:

```plaintext
book
book
paper
paper
article
article
magazine
```

Run `uniq` with no filtering option to print one representative line from each adjacent group:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

The input file remains unchanged because the result goes to stdout.

:::single-choice{#uniq-collapse-adjacent}
What does `uniq reading.txt` do by default?

::option[Sorts the complete file and then removes every repeated value.]{#uniq-auto-sort explanation="`uniq` preserves input order and does not sort. Separated copies remain separate groups."}
::option[Prints one line from each adjacent group of equal lines.]{#uniq-one-per-group .correct explanation="Default `uniq` collapses consecutive equal lines into one output line."}
::option[Deletes duplicate lines directly from `reading.txt`.]{#uniq-edit-file explanation="The command writes filtered text to stdout by default and does not edit the input file."}
:::

## Counting Adjacent Groups

Use `-c` to prefix each output group with its number of consecutive input lines:

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

These are run lengths, not global totals unless all equal lines have first been made adjacent.

:::single-choice{#uniq-count-groups}
What does the count from `uniq -c` represent?

::option[The number of characters in each input line.]{#uniq-character-count explanation="Character counting is not the purpose of `uniq -c`; tools such as `wc` handle character and byte totals."}
::option[The number of consecutive equal lines in each group.]{#uniq-consecutive-count .correct explanation="`-c` prefixes each collapsed adjacent group with the number of lines it contained."}
::option[The total number of matching lines anywhere in the file.]{#uniq-global-count explanation="Separated equal lines form separate groups unless the data is sorted or otherwise grouped first."}
:::

## Selecting Unique or Repeated Groups

Use `-u` to print only groups containing exactly one line:

```bash
$ uniq -u reading.txt
magazine
```

Use `-d` to print one representative line from each adjacent group containing more than one line:

```bash
$ uniq -d reading.txt
book
paper
article
```

GNU `uniq -D` prints every line from repeated groups, whereas lowercase `-d` prints each repeated group's value once.

:::single-choice{#uniq-only-singletons}
Which command prints only adjacent groups that occur exactly once?

::option[`uniq -c reading.txt`]{#uniq-count-reading explanation="This prints every group with a count, including repeated and singleton groups."}
::option[`uniq -d reading.txt`]{#uniq-duplicate-reading explanation="Lowercase `-d` prints one line for each repeated group, the opposite selection."}
::option[`uniq -u reading.txt`]{#uniq-single-reading .correct explanation="The `-u` option selects groups whose adjacent run length is exactly one."}
:::

:::single-choice{#uniq-one-per-duplicate-group}
Which command prints one line for each adjacent group that appears more than once?

::option[`uniq -d reading.txt`]{#uniq-duplicate-groups .correct explanation="The `-d` option selects repeated adjacent groups and emits one representative line per group."}
::option[`uniq -D reading.txt`]{#uniq-all-duplicate-lines explanation="GNU uppercase `-D` prints all lines belonging to repeated groups, not only one representative."}
::option[`uniq -u reading.txt`]{#uniq-unique-groups explanation="The `-u` option selects singleton groups rather than repeated ones."}
:::

## Grouping Separated Duplicates

If equal lines are separated, they form different groups:

```plaintext
book
paper
book
paper
article
magazine
article
```

Running `uniq` on this file will produce a surprising result:

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

No lines are collapsed because neighboring values differ. Sort first when changing the order is acceptable and you want equal complete lines grouped together:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

Use a consistent locale and comparison policy across both steps. `sort -u reading.txt` can also sort and retain one line per equal sort key in a single command.

:::single-choice{#uniq-separated-duplicates}
Equal lines are scattered through `reading.txt`, and output order may change. Which pipeline produces one sorted copy of each distinct complete line?

::option[`sort reading.txt | uniq`]{#sort-then-uniq .correct explanation="Sorting groups equal complete lines, then `uniq` collapses each adjacent group to one line."}
::option[`uniq reading.txt | sort`]{#uniq-before-sort explanation="`uniq` runs before equal separated lines become adjacent, so later sorting can leave duplicate output lines."}
::option[`uniq -c reading.txt | head`]{#uniq-count-head explanation="This counts existing adjacent groups and then limits output. It does not globally group separated duplicates."}
:::

`uniq` reads stdin when no input file is named, which is why it fits naturally after `sort`. GNU options such as `-i` can ignore case, while `-f`, `-s`, and `-w` can skip or limit comparison regions; use them only when equality should be defined by part of each line.

To practice grouping, counting, and filtering duplicates, try these hands-on labs:

1. **[Linux uniq Command: Duplicate Filtering](https://labex.io/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Learn how to use the Linux `uniq` command in combination with `sort` to identify, filter, and analyze duplicate lines in text files.
2. **[Linux sort Command: Text Sorting](https://labex.io/labs/linux-linux-sort-command-text-sorting-219196)** - Practice using the `sort` command to organize lines of text files, a crucial step before using `uniq` effectively.
3. **[Word Count and Sorting](https://labex.io/labs/linux-word-count-and-sorting-388125)** - Learn the essential Linux text processing tools `wc` (word count) and `sort` in this hands-on challenge. Learn to count lines, words, and characters, find frequent patterns, and sort data efficiently for various text analysis tasks.

## Summary

You can now analyze adjacent groups of equal lines with `uniq`.

1. Collapse each adjacent duplicate group to one line.
2. Count consecutive occurrences with `-c`.
3. Select singleton groups with `-u`.
4. Select repeated groups with `-d` or GNU `-D`.
5. Sort first when separated duplicates must be grouped.
