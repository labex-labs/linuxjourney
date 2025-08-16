---
lang: "en"
title: "cut"
description: "Learn how to use the Linux `cut` command to extract text from files. This beginner-friendly tutorial covers character and field cutting. Improve your Linux text processing skills!"
keywords: "cut command, Linux text processing, extract text, Linux tutorial, beginner Linux, cut examples, Linux guide"
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

What does the following command do? Why?

```bash
cut -c 5-10 sample.txt
cut -c 5- sample.txt
cut -c -5 sample.txt
```

## Quiz Question

What command would you use to get the first character of every line in a file?

## Quiz Answer

cut -c 1
