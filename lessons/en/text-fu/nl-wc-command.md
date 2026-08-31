---
lesson_id: "nl-wc-command"
course_id: "text-fu"
lang: "en"
order_index: 15
title: "wc and nl"
description: "Learn how to count lines, words, bytes, or characters with wc and number lines with nl."
meta_title: "wc and nl - Text-Fu"
meta_description: "Master the wc and nl commands in this Linux tutorial. Learn how to perform a Linux word count, add line numbers to files, and conduct basic file analysis. A perfect guide for beginners to enhance their command-line skills."
meta_keywords: "wc command, nl command, Linux word count, count words in file Linux, Linux line numbers, nl command Linux, file analysis, text processing Linux, Linux command line, Linux tutorial for beginners"
---

The `wc` command counts properties of text streams, while `nl` writes input with generated line numbers. Both read files or stdin and send their results to stdout.

## Reading the Default wc Output

With no count option, `wc` prints the number of newline characters, words, and bytes, followed by the filename when one was supplied:

```bash
$ printf 'red blue\ngreen\n' > colors.txt
$ wc colors.txt
 2  3 15 colors.txt
```

From left to right:

1. `2` newline characters, reported as lines.
2. `3` whitespace-delimited words.
3. `15` bytes in this ASCII example.

A final text line without a terminating newline is not counted by `wc -l`, because that option counts newline characters rather than visually perceived lines.

:::single-choice{#wc-default-columns}
In the default output from `wc file.txt`, what do the first three numbers represent?

::option[Lines, words, and bytes, in that order.]{#wc-lines-words-bytes .correct explanation="Default `wc` output reports newline count, word count, and byte count before the filename."}
::option[Bytes, words, and lines, in that order.]{#wc-bytes-words-lines explanation="These are the same measurements in the wrong order. The line count appears first."}
::option[Files, characters, and paragraphs, in that order.]{#wc-files-characters-paragraphs explanation="The default columns do not count files or paragraphs, and the third default measurement is bytes."}
:::

## Requesting One Count

Select only the measurement you need:

- `-l`: Count newline characters.
- `-w`: Count words.
- `-c`: Count bytes.
- `-m`: Count characters according to the current locale.

For example:

```bash
$ wc -w colors.txt
3 colors.txt
```

Byte and character counts are equal for ASCII text but can differ for multibyte encodings such as UTF-8. When stdin is used without a filename operand, `wc` normally omits a filename label:

```bash
$ printf 'one two\n' | wc -w
2
```

:::single-choice{#wc-word-count-only}
Which command reports only the word count for `essay.txt`?

::option[`wc -l essay.txt`]{#wc-lines-essay explanation="The `-l` option reports newline characters, not words."}
::option[`wc -w essay.txt`]{#wc-words-essay .correct explanation="The `-w` option selects the word count measurement."}
::option[`wc -c essay.txt`]{#wc-bytes-essay explanation="The `-c` option reports bytes rather than whitespace-delimited words."}
:::

:::single-choice{#wc-characters-not-bytes}
Which option asks `wc` to count characters rather than bytes in the current locale?

::option[`-m`]{#wc-character-option .correct explanation="The `-m` option reports characters, which may differ from bytes for multibyte text."}
::option[`-c`]{#wc-byte-option explanation="The `-c` option reports bytes. One character can occupy several bytes in encodings such as UTF-8."}
::option[`-w`]{#wc-word-option explanation="The `-w` option counts words rather than characters or bytes."}
:::

When multiple files are named, `wc` prints one result per file and a `total` line. GNU `wc -L` reports the maximum display width of an input line.

## Numbering Nonempty Lines with nl

By default, `nl` numbers nonempty lines in the logical body of its input. Suppose `notes.txt` contains a blank second line:

```text
alpha

beta
```

The blank line is preserved but receives no number:

```bash
$ nl notes.txt
	 1	alpha

	 2	beta
```

`nl` writes numbered output; it does not modify `notes.txt`.

:::single-choice{#nl-default-blank-lines}
How does `nl notes.txt` handle blank body lines by default?

::option[It omits each blank line from the output entirely.]{#nl-omit-blank explanation="The blank line remains in the output, but it is not assigned a number by default."}
::option[It preserves them without line numbers.]{#nl-preserve-unnumbered .correct explanation="Default body style numbers nonempty lines and passes blank lines through unnumbered."}
::option[It numbers them in the same sequence as nonempty lines.]{#nl-number-blank-default explanation="Numbering every body line requires a different style such as `-ba`."}
:::

## Numbering Every Line

Use `-ba` to select body numbering style `a`, which numbers all lines:

```bash
$ nl -ba notes.txt
	 1	alpha
	 2
	 3	beta
```

Other options control formatting. For example, `-w 3` sets the number field width and `-s ': '` changes the separator after the number.

:::single-choice{#nl-number-all-lines}
Which command numbers every body line in `notes.txt`, including blank lines?

::option[`nl -w 3 notes.txt`]{#nl-width-three explanation="This changes the number field width but keeps the default nonempty-line numbering rule."}
::option[`nl -ba notes.txt`]{#nl-body-all .correct explanation="The `-b` option chooses the body style, and style `a` numbers all body lines."}
::option[`wc -l notes.txt`]{#wc-lines-notes explanation="This prints a count of newline characters and does not reproduce the file with line numbers."}
:::

To practice counting and numbering text, try these hands-on labs:

1. **[Linux wc Command: Text Counting](https://labex.io/labs/linux-linux-wc-command-text-counting-219200)** - Practice counting words, lines, and characters in text files using the `wc` command.
2. **[Linux nl Command: Line Numbering](https://labex.io/labs/linux-linux-nl-command-line-numbering-210988)** - Learn to number lines in text files with the `nl` command.
3. **[Word Count and Sorting](https://labex.io/labs/linux-word-count-and-sorting-388125)** - Apply your knowledge of `wc` to count lines, words, and characters, and combine it with sorting for practical text analysis tasks.

## Summary

You can now measure text streams and add visible line numbers without editing the source.

1. Interpret the default lines, words, and bytes columns from `wc`.
2. Select one count with `-l`, `-w`, `-c`, or `-m`.
3. Distinguish byte counts from character counts.
4. Number nonempty lines with default `nl` behavior.
5. Number blank lines too with `nl -ba`.
