---
index: 14
lang: "en"
title: "uniq (Unique)"
meta_title: "uniq (Unique) - Text-Fu"
meta_description: "Learn how to use the Linux `uniq` command to remove duplicate lines from text files. Discover options like -c, -u, -d, and combine with `sort` for effective data cleaning."
meta_keywords: "uniq command, Linux uniq, remove duplicates, sort uniq, Linux tutorial, text processing, beginner Linux, Linux guide"
---

## Lesson Content

The `uniq` (unique) command is another useful tool for parsing text.

Let's say you had a file with lots of duplicates:

```plaintext
reading.txt
book
book
paper
paper
article
article
magazine
```

And you wanted to remove the duplicates; well, you can use the `uniq` command:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Let's get the count of how many occurrences of a line:

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

Let's just get unique values:

```bash
$ uniq -u reading.txt
magazine
```

Let's just get duplicate values:

```bash
$ uniq -d reading.txt
book
paper
article
```

**Note**: `uniq` does not detect duplicate lines unless they are adjacent. For example:

Let's say you had a file with duplicates that are not adjacent:

```plaintext
reading.txt
book
paper
book
paper
article
magazine
article
```

```bash
$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article
```

The result returned by `uniq` will contain all the entries, unlike the very first example.

To overcome this limitation of `uniq`, we can use `sort` in combination with `uniq`:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of text processing with `uniq` and `sort`:

1. **[Linux uniq Command: Duplicate Filtering](https://labex.io/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Learn how to use the Linux `uniq` command in combination with `sort` to identify, filter, and analyze duplicate lines in text files.
2. **[Linux sort Command: Text Sorting](https://labex.io/labs/linux-linux-sort-command-text-sorting-219196)** - Practice using the `sort` command to organize lines of text files, a crucial step before using `uniq` effectively.
3. **[Word Count and Sorting](https://labex.io/labs/linux-word-count-and-sorting-388125)** - Learn the essential Linux text processing tools `wc` (word count) and `sort` in this hands-on challenge. Learn to count lines, words, and characters, find frequent patterns, and sort data efficiently for various text analysis tasks.

These labs will help you apply the concepts in real scenarios and build confidence with text processing and data manipulation in Linux.

## Quiz Question

What command would you use to remove duplicates in a file?

## Quiz Answer

uniq
