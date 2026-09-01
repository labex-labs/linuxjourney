---
lesson_id: "paste-command"
course_id: "text-fu"
lang: "en"
order_index: 7
title: "paste"
description: "Learn how to merge corresponding lines or serialize lines with configurable delimiters using paste."
meta_title: "paste - Text-Fu"
meta_description: "Learn how to use the Linux paste command to merge file lines. Discover delimiters and combine files with this essential Linux command tutorial."
meta_keywords: "Linux paste command, paste command tutorial, merge file lines, Linux commands, beginner Linux, Linux guide"
---

The `paste` command combines lines as columns. By default, it takes one line from each input file, joins those lines with a tab, and repeats until all inputs reach end-of-file.

## Merging Files Side by Side

Create two small files:

```bash
$ printf 'alice\nbob\n' > names.txt
$ printf 'admin\nviewer\n' > roles.txt
```

Pass both files to `paste`:

```bash
$ paste names.txt roles.txt
alice	admin
bob	viewer
```

The visible spacing between columns is a tab. Unlike `cat`, which writes one complete file after another, `paste` combines corresponding input lines.

:::single-choice{#paste-corresponding-lines} `first.txt` contains `A` then `B`, and `second.txt` contains `1` then `2`. What does `paste first.txt second.txt` produce by default?

::option[`A`, `B`, `1`, and `2` on four consecutive lines.]{#paste-concatenated-files explanation="That resembles writing the files one after another. `paste` instead combines corresponding lines."}
::option[`A`, `B`, `1`, and `2` on one line with no separators.]{#paste-one-line-no-separator explanation="One-line serialization requires `-s`, and the default separator is a tab rather than nothing."}
::option[`A` with `1`, then `B` with `2`, separated by tabs.]{#paste-parallel-result .correct explanation="Default parallel mode takes one line from each file for every output line and separates the fields with a tab."}
:::

## Choosing a Delimiter

Use `-d LIST` to replace the default tab separator. For a colon:

```bash
$ paste -d ':' names.txt roles.txt
alice:admin
bob:viewer
```

Quote delimiters that have shell meaning. `paste` can cycle through multiple delimiter characters when the list contains more than one, but a single character is easiest when building two columns.

:::single-choice{#paste-colon-delimiter} Which command joins corresponding lines from `names.txt` and `roles.txt` with a colon?

::option[`paste -d ':' names.txt roles.txt`]{#paste-colon-files .correct explanation="The `-d` option replaces the default tab with the supplied colon for each pair of fields."}
::option[`paste -s ':' names.txt roles.txt`]{#paste-serial-colon-operand explanation="The `-s` option selects serial mode, and `:` would be treated as another input pathname rather than a delimiter."}
::option[`paste names.txt ':' roles.txt`]{#paste-colon-file-operand explanation="Without `-d`, every operand is treated as an input file. This would try to open a file named `:`."}
:::

## Serializing Lines from One File

The `-s` option processes each input file serially, joining its lines into one output line. Create a file with one word per line:

```bash
$ printf 'The\nquick\nbrown\nfox\n' > words.txt
$ paste -s words.txt
The	quick	brown	fox
```

Combine `-s` with `-d` to choose the separator:

```bash
$ paste -s -d ' ' words.txt
The quick brown fox
```

If several files are supplied with `-s`, each file becomes its own output line.

:::single-choice{#paste-serialize-with-spaces} Which command joins every line of `words.txt` into one space-separated output line?

::option[`paste -d ' ' words.txt`]{#paste-parallel-one-file explanation="In default parallel mode, a single input file still produces one output line per input line. The delimiter has nothing to join across files."}
::option[`paste -s words.txt roles.txt`]{#paste-two-serial-files explanation="This serializes two files separately with the default tab, producing two output lines rather than the requested one-file space-separated result."}
::option[`paste -s -d ' ' words.txt`]{#paste-serial-spaces .correct explanation="`-s` serializes the file's lines, and `-d ' '` uses a space between them."}
:::

## Handling Unequal Input Lengths

When parallel input files have different numbers of lines, `paste` continues until the longest file ends. Missing values from a shorter file become empty fields:

```bash
$ printf 'A\nB\nC\n' > letters.txt
$ printf '1\n2\n' > numbers.txt
$ paste -d ':' letters.txt numbers.txt
A:1
B:2
C:
```

:::single-choice{#paste-unequal-files} What happens when one file passed to parallel `paste` ends before another?

::option[`paste` uses empty fields for that file until the longest input ends.]{#paste-empty-fields .correct explanation="Parallel mode continues until all files are exhausted, representing missing lines from shorter inputs as empty fields."}
::option[`paste` stops immediately and discards remaining lines.]{#paste-stop-shortest explanation="`paste` continues through the longest input, so remaining lines are not discarded merely because another file ended."}
::option[`paste` repeats the shorter file from its beginning.]{#paste-repeat-shorter explanation="The command does not cycle input records. An exhausted input contributes empty fields."}
:::

## Reading One Input from stdin

Use `-` as a file operand to read that position from stdin:

```bash
$ printf 'admin\nviewer\n' | paste -d ':' names.txt -
alice:admin
bob:viewer
```

:::single-choice{#paste-stdin-operand} In `producer | paste names.txt -`, what does the `-` operand mean?

::option[Write the merged result to stderr.]{#paste-write-stderr explanation="A hyphen here identifies an input source. It does not redirect an output stream."}
::option[Remove delimiters between the two columns.]{#paste-remove-delimiter explanation="Delimiter selection is controlled with `-d`. The hyphen does not change the separator."}
::option[Read that input column from stdin.]{#paste-read-stdin .correct explanation="The hyphen tells `paste` to use its standard input at that operand position."}
:::

To practice merging line-oriented data, try this hands-on lab:

1. **[Simple Text Processing](https://labex.io/labs/linux-simple-text-processing-18004)** - Learn to use powerful commands like `tr`, `col`, `join`, and `paste` to manipulate and analyze text data efficiently.
## Summary

You can now combine line-oriented inputs with predictable alignment and delimiters.

1. Merge corresponding lines from several files.
2. Replace the default tab separator with `-d`.
3. Serialize one file's lines with `-s`.
4. Interpret empty fields from shorter inputs.
5. Use `-` when one input comes from stdin.
