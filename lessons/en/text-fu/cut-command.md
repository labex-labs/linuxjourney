---
index: 6
lang: "en"
title: "cut"
meta_title: "cut - Text-Fu"
meta_description: "Learn how to use the Linux `cut` command to extract text from files. This beginner-friendly tutorial covers character and field cutting. Improve your Linux text processing skills!"
meta_keywords: "cut command, Linux text processing, extract text, Linux tutorial, beginner Linux, cut examples, Linux guide"
---

## Lesson Content

We're going to learn a couple of useful commands that you can use to process text. Before we get started, let's create a file that we'll be working with. Copy and paste the following command; once you do that, add a TAB in between "lazy" and "dog" (hold down Ctrl-v + TAB).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

The first command we'll be learning about is the `cut` command. It extracts portions of text from a file.

To extract contents by a list of characters:

```bash
cut -c 5 sample.txt
```

This outputs the 5th character in each line of the file. In this case, it is "q"; note that the space also counts as a character.

To extract the contents by a field, we'll need to do a little modification:

```bash
cut -f 2 sample.txt
```

The `-f` or field flag cuts text based on fields. By default, it uses TABs as delimiters, so everything separated by a TAB is considered a field. You should see "dog" as your output.

You can combine the field flag with the delimiter flag to extract the contents by a custom delimiter:

```bash
cut -f 1 -d ";" sample.txt
```

This will change the TAB delimiter to a ";" delimiter, and since we are cutting the first field, the result should be "The quick brown".

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of text processing with `cut` and other related commands:

1. **[Linux cut Command: Text Cutting](https://labex.io/labs/linux-linux-cut-command-text-cutting-219187)** - This lab provides a direct, hands-on introduction to the `cut` command, allowing you to practice extracting specific columns or fields from text files, just as discussed in the lesson.
2. **[Simple Text Processing](https://labex.io/labs/linux-simple-text-processing-18004)** - Expand your text manipulation skills by using powerful commands like `tr`, `col`, `join`, and `paste` to efficiently process and analyze text data.
3. **[Sequence Control and Pipeline](https://labex.io/labs/linux-sequence-control-and-pipeline-17994)** - Enhance your command-line efficiency by learning to control command execution sequences, utilize pipelines, and leverage powerful text processing tools like `cut`, `grep`, `wc`, `sort`, and `uniq`.

These labs will help you apply the concepts in real scenarios and build confidence with text processing in Linux.

## Quiz Question

What command would you use to get the first character of every line in a file?

## Quiz Answer

cut -c 1
