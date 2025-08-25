---
index: 15
lang: "en"
title: "wc and nl"
meta_title: "wc and nl - Text-Fu"
meta_description: "Learn wc and nl Linux commands. Understand word count, line numbering, and file analysis. Improve your Linux command-line skills today!"
meta_keywords: "wc command, nl command, Linux word count, Linux line numbers, file analysis, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

The `wc` (word count) command shows the total count of words in a file.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

It displays the number of lines, number of words, and number of bytes, respectively.

To see just the count of a certain field, use the `-l`, `-w`, or `-c` options, respectively.

```bash
$ wc -l /etc/passwd
96
```

Another command you can use to check the count of lines in a file is the `nl` (number lines) command.

```plaintext
file1.txt
i
like
turtles
```

```bash
$ nl file1.txt
1. i
2. like
3. turtles
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of text counting and line numbering in Linux:

1. **[Linux wc Command: Text Counting](https://labex.io/labs/linux-linux-wc-command-text-counting-219200)** - Practice counting words, lines, and characters in text files using the `wc` command.
2. **[Linux nl Command: Line Numbering](https://labex.io/labs/linux-linux-nl-command-line-numbering-210988)** - Learn to number lines in text files with the `nl` command.
3. **[Word Count and Sorting](https://labex.io/labs/linux-word-count-and-sorting-388125)** - Apply your knowledge of `wc` to count lines, words, and characters, and combine it with sorting for practical text analysis tasks.

These labs will help you apply the concepts in real scenarios and build confidence with text processing in Linux.

## Quiz Question

What command would you use to get the total number of words in a file and just the words?

## Quiz Answer

wc -w
