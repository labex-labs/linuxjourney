---
index: 11
lang: "en"
title: "join and split"
meta_title: "join and split - Text-Fu"
meta_description: "Learn to use Linux 'join' and 'split' commands for file manipulation. Understand how to combine files by common fields and split large files efficiently. Get practical examples and tips."
meta_keywords: "Linux join command, Linux split command, file manipulation, Linux tutorial, command line, beginner Linux, Linux guide"
---

## Lesson Content

The `join` command allows you to join multiple files together by a common field:

Let's say I had two files that I wanted to join together:

```plaintext
file1.txt
1 John
2 Jane
3 Mary

file2.txt
1 Doe
2 Doe
3 Sue
```

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

See how it joined together my files? They are joined together by the first field by default, and the fields have to be identical. If they are not, you can sort them. In this case, the files are joined via 1, 2, 3.

How would we join the following files?

```plaintext
file1.txt
John 1
Jane 2
Mary 3

file2.txt
1 Doe
2 Doe
3 Sue
```

To join this file, you need to specify which fields you are joining. In this case, we want field 2 on `file1.txt` and field 1 on `file2.txt`, so the command would look like this:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1` refers to `file1.txt` and `-2` refers to `file2.txt`. Pretty neat. You can also split a file up into different files with the `split` command:

```bash
split somefile
```

This will split it into different files. By default, it will split them once they reach a 1000-line limit. The files are named `x**` by default.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of joining and manipulating text files:

1. **[Linux join Command: File Joining](https://labex.io/labs/linux-linux-join-command-file-joining-219193)** - This lab provides a direct, hands-on introduction to the `join` command, allowing you to practice merging lines from two sorted text files based on a common field, just as discussed in the lesson.
2. **[Processing Employees Data](https://labex.io/labs/linux-processing-employees-data-388132)** - Apply your knowledge of `join` and other powerful Linux command-line utilities like `awk` to combine and process data from multiple sources, simulating a real-world data analysis scenario.
3. **[Sequence Control and Pipeline](https://labex.io/labs/linux-sequence-control-and-pipeline-17994)** - Enhance your command-line efficiency and data manipulation skills by learning to control command execution sequences, utilize pipelines, and leverage powerful text processing tools, which complements the data combining capabilities of `join`.

These labs will help you apply the concepts of text file manipulation and data combining in real scenarios and build confidence with Linux command-line tools.

## Quiz Question

What command would you use to join files named `cat`, `dog`, `cow`?

## Quiz Answer

join cat dog cow
