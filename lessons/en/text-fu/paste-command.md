---
index: 7
lang: "en"
title: "paste"
meta_title: "paste - Text-Fu"
meta_description: "Learn how to use the Linux paste command to merge file lines. Discover delimiters and combine files with this essential Linux command tutorial."
meta_keywords: "Linux paste command, paste command tutorial, merge file lines, Linux commands, beginner Linux, Linux guide"
---

## Lesson Content

The `paste` command is similar to the `cat` command; it merges lines together in a file. Let's create a new file with the following contents:

```
sample2.txt
The
quick
brown
fox
```

Let's combine all these lines into one line:

```bash
paste -s sample2.txt
```

The default delimiter for `paste` is TAB, so now there is one line with TABs separating each word.

Let's change this delimiter (`-d`) to something a little more readable:

```bash
paste -d ' ' -s sample2.txt
```

Now everything should be on one line delimited by spaces.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of text processing and data manipulation in Linux:

1. **[Simple Text Processing](https://labex.io/labs/linux-simple-text-processing-18004)** - Learn to use powerful commands like `tr`, `col`, `join`, and `paste` to manipulate and analyze text data efficiently.
2. **[Data Stream Redirection](https://labex.io/labs/linux-data-stream-redirection-17995)** - Learn the art of Linux stream redirection and how to manipulate standard input, output, and error streams, which is fundamental to understanding how commands like `paste` operate.
3. **[Sequence Control and Pipeline](https://labex.io/labs/linux-sequence-control-and-pipeline-17994)** - Learn to control command execution sequences and utilize pipelines, enhancing your ability to combine `paste` with other commands for complex data tasks.

These labs will help you apply the concepts in real scenarios and build confidence with text processing and data handling in Linux.

## Quiz Question

What flag do you use with `paste` to make everything go on one line?

## Quiz Answer

-s
