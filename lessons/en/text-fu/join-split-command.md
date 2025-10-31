---
index: 11
lang: "en"
title: "join and split"
meta_title: "join and split - Text-Fu"
meta_description: "Master how to use the Linux join and split commands. Learn to efficiently join files based on common fields and split large files into smaller parts. This guide covers what command you would use to join files named cat, dog, cow and other practical examples."
meta_keywords: "linux join files, what command would you use to join files, linux join command, linux split command, file manipulation, command line, text processing"
---

## Lesson Content

In Linux, managing and manipulating text files is a common task. Two powerful utilities for this are `join` and `split`. The `join` command merges lines from two files based on a common field, while `split` breaks a large file into smaller, more manageable pieces.

### Joining Files by a Common Field

The `join` command is a fundamental tool when you need to **linux join files**. By default, it combines lines from two sorted files based on an identical first field.

For example, imagine you have two files you want to merge:

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

Using the `join` command, you can combine them easily:

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

As you can see, the files were joined using the common first field (1, 2, 3). For `join` to work correctly, the join fields in both files must be sorted.

### Specifying Different Join Fields

What if the common field is not the first column? You can tell `join` which fields to use. Consider these files:

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

Here, we need to join on the second field of `file1.txt` and the first field of `file2.txt`. The command would be:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

The `-1 2` flag specifies field 2 of the first file, and `-2 1` specifies field 1 of the second file.

### Splitting Large Files

The `split` command does the opposite of joining; it divides a large file into smaller ones.

```bash
split somefile
```

By default, this command splits `somefile` into new files once a 1000-line limit is reached. The output files are named `xaa`, `xab`, and so on. You can customize this behavior, for example, by specifying a different line count with the `-l` flag or splitting by file size with the `-b` flag.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of joining and manipulating text files:

1. **[Linux join Command: File Joining](https://labex.io/labs/linux-linux-join-command-file-joining-219193)** - This lab provides a direct, hands-on introduction to the `join` command, allowing you to practice merging lines from two sorted text files based on a common field, just as discussed in the lesson.
2. **[Processing Employees Data](https://labex.io/labs/linux-processing-employees-data-388132)** - Apply your knowledge of `join` and other powerful Linux command-line utilities like `awk` to combine and process data from multiple sources, simulating a real-world data analysis scenario.
3. **[Sequence Control and Pipeline](https://labex.io/labs/linux-sequence-control-and-pipeline-17994)** - Enhance your command-line efficiency and data manipulation skills by learning to control command execution sequences, utilize pipelines, and leverage powerful text processing tools, which complements the data combining capabilities of `join`.

These labs will help you apply the concepts of text file manipulation and data combining in real scenarios and build confidence with Linux command-line tools.

## Quiz Question

What command would you use to join files named `cat`, `dog`, `cow`? Please provide the full command in English. The command and filenames should be in lowercase.

## Quiz Answer

join cat dog cow
