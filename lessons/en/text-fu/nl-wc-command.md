---
index: 15
lang: "en"
title: "wc and nl"
meta_title: "wc and nl - Text-Fu"
meta_description: "Master the wc and nl commands in this Linux tutorial. Learn how to perform a Linux word count, add line numbers to files, and conduct basic file analysis. A perfect guide for beginners to enhance their command-line skills."
meta_keywords: "wc command, nl command, Linux word count, count words in file Linux, Linux line numbers, nl command Linux, file analysis, text processing Linux, Linux command line, Linux tutorial for beginners"
---

## Lesson Content

In Linux, analyzing text files is a common task. Two fundamental utilities for this are `wc` and `nl`, which help you count content and number lines, respectively.

### Counting with the wc Command

The `wc` (word count) command is a powerful tool for basic file analysis. When run on a file, it provides a summary of its contents.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

The output displays three numbers followed by the filename. From left to right, these numbers represent:

1. The number of lines.
2. The number of words (the Linux word count).
3. The number of bytes.

### Getting Specific Counts

Often, you only need one piece of information. You can use options to display a specific count instead of all three.

- `-l`: Shows only the line count.
- `-w`: Shows only the word count.
- `-c`: Shows only the byte count.

For example, to see just the number of lines in the `/etc/passwd` file, you would use:

```bash
$ wc -l /etc/passwd
96
```

### Numbering Lines with the nl Command

Another useful command for inspecting files is `nl` (number lines). As its name suggests, it reads a file and outputs its content with line numbers added to the beginning of each line. This is especially helpful for reviewing scripts or configuration files.

Consider a file named `file1.txt` with the following content:

```plaintext
i
like
turtles
```

Using the `nl` command, you can easily add Linux line numbers:

```bash
$ nl file1.txt
     1 i
     2 like
     3 turtles
```

Both `wc` and `nl` are essential commands for everyday text processing on the Linux command line.

## Exercise

To master these commands, hands-on practice is key. Try these exercises to solidify your skills in text counting and line numbering on Linux:

1. **[Linux wc Command: Text Counting](https://labex.io/labs/linux-linux-wc-command-text-counting-219200)** - Practice counting words, lines, and characters in text files using the `wc` command.
2. **[Linux nl Command: Line Numbering](https://labex.io/labs/linux-linux-nl-command-line-numbering-210988)** - Learn to number lines in text files with the `nl` command.
3. **[Word Count and Sorting](https://labex.io/labs/linux-word-count-and-sorting-388125)** - Apply your knowledge of `wc` to count lines, words, and characters, and combine it with sorting for practical text analysis tasks.

These labs will help you apply the concepts in real-world scenarios and build confidence with text processing in Linux.

## Quiz Question

Which command and option would you use to display only the total word count of a file? Please answer using only the command and its option in English. The answer is case-sensitive.

## Quiz Answer

wc -w
