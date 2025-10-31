---
index: 14
lang: "en"
title: "uniq (Unique)"
meta_title: "uniq (Unique) - Text-Fu"
meta_description: "Explore the uniq command in Linux to filter and remove duplicate adjacent lines from text. Learn how to use the uniq linux tool with options like -c, -u, -d, and combine it with sort for powerful text processing."
meta_keywords: "uniq command, Linux uniq, uniq linux, remove duplicates, sort uniq, text processing, data cleaning, Linux tutorial"
---

## Lesson Content

The `uniq` (unique) command is an essential tool for text processing in Linux. It helps you filter and manage duplicate lines within a text file, but it's important to understand how it works to use it effectively.

### Basic Duplicate Removal

The primary function of the `uniq` command is to remove duplicate adjacent lines. Imagine you have a file named `reading.txt` with the following content:

```plaintext
book
book
paper
paper
article
article
magazine
```

To remove the repeated lines, you can run the `uniq` command:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

As you can see, `uniq` outputs a version of the file with the duplicate adjacent lines removed.

### Advanced Filtering Options

The `uniq` command also provides several options for more detailed analysis.

To count the occurrences of each line, use the `-c` (count) flag:

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

To display only the lines that are not repeated (i.e., are unique), use the `-u` (unique) flag:

```bash
$ uniq -u reading.txt
magazine
```

Conversely, to display only the lines that are repeated, use the `-d` (duplicated) flag:

```bash
$ uniq -d reading.txt
book
paper
article
```

### The Importance of Sorting

A critical detail about the **uniq linux** command is that it only detects duplicate lines if they are directly adjacent to each other. If the duplicates are scattered throughout the file, `uniq` will not identify them.

Consider this version of `reading.txt` where duplicates are not adjacent:

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

No lines were removed because no two identical lines were next to each other. To solve this, you must first sort the file's contents. By piping the output of `sort` into `uniq`, you ensure that all identical lines become adjacent, allowing `uniq` to work correctly. This combination is a powerful and common pattern in shell scripting.

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

This command first sorts the lines alphabetically, then `uniq` filters out the duplicates, giving you a clean list of unique entries.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of text processing with `uniq` and `sort`:

1. **[Linux uniq Command: Duplicate Filtering](https://labex.io/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Learn how to use the Linux `uniq` command in combination with `sort` to identify, filter, and analyze duplicate lines in text files.
2. **[Linux sort Command: Text Sorting](https://labex.io/labs/linux-linux-sort-command-text-sorting-219196)** - Practice using the `sort` command to organize lines of text files, a crucial step before using `uniq` effectively.
3. **[Word Count and Sorting](https://labex.io/labs/linux-word-count-and-sorting-388125)** - Learn the essential Linux text processing tools `wc` (word count) and `sort` in this hands-on challenge. Learn to count lines, words, and characters, find frequent patterns, and sort data efficiently for various text analysis tasks.

These labs will help you apply the concepts in real scenarios and build confidence with text processing and data manipulation in Linux.

## Quiz Question

What command would you use to remove adjacent duplicate lines in a file? Please answer using only the command name in lowercase English letters.

## Quiz Answer

uniq
