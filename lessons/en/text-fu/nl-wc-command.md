---
lang: "en"
title: "wc and nl"
description: "Learn wc and nl Linux commands. Understand word count, line numbering, and file analysis. Improve your Linux command-line skills today!"
keywords: "wc command, nl command, Linux word count, Linux line numbers, file analysis, Linux tutorial, beginner Linux, Linux guide"
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

How would you get the total count of lines using the `nl` command without searching through the entire output? Hint: Use some of the other commands you learned in this course.

## Quiz Question

What command would you use to get the total number of words in a file and just the words?

## Quiz Answer

wc -w
