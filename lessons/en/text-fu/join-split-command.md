---
lesson_id: "join-split-command"
course_id: "text-fu"
lang: "en"
order_index: 11
title: "join and split"
description: "Learn how to join two sorted text files by a key and split one file into named pieces."
meta_title: "join and split - Text-Fu"
meta_description: "Master how to use the Linux join and split commands. Learn to efficiently join files based on common fields and split large files into smaller parts. This guide covers what command you would use to join files named cat, dog, cow and other practical examples."
meta_keywords: "linux join files, what command would you use to join files, linux join command, linux split command, file manipulation, command line, text processing"
---

The `join` and `split` commands solve different file-processing problems. `join` combines related records from two sorted text inputs, while `split` divides one input into a sequence of smaller files.

## Joining Two Files by Their First Field

By default, `join` compares the first blank-separated field in exactly two input files. Consider these already sorted files:

`people.txt`:

```text
1 John
2 Jane
3 Mary
```

`surnames.txt`:

```text
1 Doe
2 Doe
3 Sue
```

Join records whose key fields are equal:

```bash
$ join people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

The output contains the shared key once, then the remaining fields from the first and second files. `join` processes two files at a time; it does not accept three ordinary file operands as a three-way relational join.

:::single-choice{#join-default-key} With no field options, which records does `join first.txt second.txt` combine?

::option[Lines whose first blank-separated fields are equal.]{#join-first-fields .correct explanation="Default `join` behavior compares field 1 from each of the two sorted inputs."}
::option[Lines that occupy the same physical line number.]{#join-line-numbers explanation="Matching is based on key-field values, not simply on record positions."}
::option[Every line from the first file with every line from the second.]{#join-all-pairs explanation="`join` emits records for matching keys rather than an unrestricted Cartesian product of all lines."}
:::

## Sorting the Join Keys

Each input must be ordered by its join field using compatible comparison rules. For default field 1, prepare copies with `sort -k 1,1`:

```bash
$ LC_ALL=C sort -k 1,1 people-raw.txt > people.txt
$ LC_ALL=C sort -k 1,1 surnames-raw.txt > surnames.txt
$ LC_ALL=C join people.txt surnames.txt
```

Using the same locale for sorting and joining keeps collation rules consistent. Do not redirect a sort back to its own input pathname, because the shell would truncate that file first.

:::single-choice{#join-sort-requirement} What preparation does `join` normally require for reliable matching?

::option[Both files must contain exactly the same number of physical lines.]{#join-equal-line-count explanation="Input lengths can differ. Key matches, not equal line counts, determine joined output."}
::option[Both files must use filenames that sort next to each other alphabetically.]{#join-filename-order explanation="The content keys need sorting; the lexical relationship between the two filenames is irrelevant."}
::option[Both files must be sorted by their respective join fields with compatible ordering.]{#join-sorted-keys .correct explanation="`join` advances through ordered keys, so each input must use an ordering consistent with the comparison it performs."}
:::

## Selecting Different Join Fields

Use `-1 FIELD` for the first file's key and `-2 FIELD` for the second file's key. Suppose the first input contains:

```text
John 1
Jane 2
Mary 3
```

The second contains:

```text
1 Doe
2 Doe
3 Sue
```

After sorting the first file by field 2 and the second by field 1, run:

```bash
$ join -1 2 -2 1 people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Use `-t CHARACTER` when a single nonblank character, such as `:`, separates fields. Options such as `-a 1` or `-a 2` can include unpaired lines from one input; the default output contains matched keys only.

:::single-choice{#join-different-fields} Which options join field 2 of the first file to field 1 of the second?

::option[`-1 1 -2 2`]{#join-fields-reversed explanation="This selects field 1 from the first input and field 2 from the second, the reverse of the requested mapping."}
::option[`-1 2 -2 1`]{#join-fields-two-one .correct explanation="`-1 2` chooses field 2 from file one, and `-2 1` chooses field 1 from file two."}
::option[`-f 2 -d 1`]{#join-cut-style-options explanation="Those resemble field and delimiter options from other text tools. They are not the `join` field selectors."}
:::

## Splitting by Line Count

`split` writes consecutive portions of one input to separate output files. It is not the inverse of a key-based `join` operation.

```bash
$ split large.txt
```

The default GNU behavior writes up to 1000 lines per output file and uses the prefix `x`, producing names such as `xaa`, `xab`, and `xac`.

Use `-l NUMBER` to choose a line count and add a final operand to choose the output prefix:

```bash
$ split -l 500 large.txt part-
```

This produces `part-aa`, `part-ab`, and so on, with at most 500 lines in each piece.

:::single-choice{#split-lines-with-prefix} Which command splits `large.txt` into pieces of at most 500 lines named with the prefix `part-`?

::option[`split -b 500 large.txt part-`]{#split-five-hundred-bytes explanation="The `-b` option selects bytes, so these pieces would be far smaller than 500 lines in ordinary text."}
::option[`split -l 500 large.txt part-`]{#split-five-hundred-lines .correct explanation="`-l 500` sets the maximum line count, and the final operand supplies the output filename prefix."}
::option[`join -l 500 large.txt part-`]{#join-split-lines explanation="`join` combines keyed records from two files. It does not divide one input into pieces."}
:::

## Splitting by Size

Use `-b SIZE` to divide input by byte size. GNU suffixes such as `K`, `M`, and `G` represent powers of 1024 in this context:

```bash
$ split -b 10M archive.bin chunk-
```

This requests pieces of 10 mebibytes except for a potentially smaller final piece. `split` does not create an archive manifest or reassembly metadata; preserve the ordering of suffixes and concatenate the pieces in order when reconstruction is appropriate.

:::single-choice{#split-ten-mebibytes} Which command splits `archive.bin` into pieces of 10 MiB using the prefix `chunk-`?

::option[`split -l 10M archive.bin chunk-`]{#split-lines-ten-m explanation="The `-l` option expects a line count, not a byte-size suffix for binary chunks."}
::option[`join -b 10M archive.bin chunk-`]{#join-bytes explanation="`join` does not split binary input or accept this piece-size operation."}
::option[`split -b 10M archive.bin chunk-`]{#split-ten-mib .correct explanation="The `-b` option selects piece size, `10M` requests 10×1024×1024 bytes, and `chunk-` is the output prefix."}
:::

To practice keyed joins and structured data processing, try these hands-on labs:

1. **[Linux join Command: File Joining](https://labex.io/labs/linux-linux-join-command-file-joining-219193)** - This lab provides a direct, hands-on introduction to the `join` command, allowing you to practice merging lines from two sorted text files based on a common field, just as discussed in the lesson.
2. **[Processing Employees Data](https://labex.io/labs/linux-processing-employees-data-388132)** - Apply your knowledge of `join` and other powerful Linux command-line utilities like `awk` to combine and process data from multiple sources, simulating a real-world data analysis scenario.
## Summary

You can now combine sorted records or divide one input into ordered pieces.

1. Join exactly two files by equal key fields.
2. Sort both inputs consistently by their join keys.
3. Select nondefault key fields with `-1` and `-2`.
4. Split by line count with `-l`.
5. Split by byte size with `-b` and a clear prefix.
