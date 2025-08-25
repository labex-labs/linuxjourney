---
index: 12
lang: "en"
title: "sort"
meta_title: "sort - Text-Fu"
meta_description: "Learn how to use the Linux sort command for sorting text files. Discover options like reverse and numerical sorting. Improve your Linux command line skills!"
meta_keywords: "Linux sort command, sort -r, sort -n, Linux tutorial, command line, beginner Linux, sort guide"
---

## Lesson Content

The `sort` command is useful for sorting lines.

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

You can also do a reverse sort:

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

And also sort by numerical value:

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of the `sort` command and text processing:

1. **[Linux sort Command: Text Sorting](https://labex.io/labs/linux-linux-sort-command-text-sorting-219196)** - This lab provides a direct introduction to the `sort` command, allowing you to practice sorting lines of text files in various ways, including ascending and descending order.
2. **[Word Count and Sorting](https://labex.io/labs/linux-word-count-and-sorting-388125)** - In this challenge, you'll apply your knowledge of sorting along with word counting to analyze text data, helping you find frequent patterns and sort data efficiently.

These labs will help you apply the concepts in real scenarios and build confidence with text manipulation and sorting in Linux.

## Quiz Question

What flag do you use to perform a reverse sort?

## Quiz Answer

-r
