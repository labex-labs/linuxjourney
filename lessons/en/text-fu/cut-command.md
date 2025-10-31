---
index: 6
lang: "en"
title: "cut"
meta_title: "cut - Text-Fu"
meta_description: "Learn how to use the Linux `cut` command to extract specific sections of text from files. This guide covers cutting by character and field (`cut f`), including how to cut f with custom delimiters. Perfect for mastering Linux text processing."
meta_keywords: "cut command, Linux text processing, extract text, cut f, how to cut f, Linux tutorial, cut examples, Linux guide, field cutting"
---

## Lesson Content

We're going to learn a couple of useful commands for processing text. Before we begin, let's create a file to work with. Copy and paste the following command. After pasting, you will need to add a literal TAB character between "lazy" and "dog" (you can often do this by pressing Ctrl-v then TAB).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

The first command we'll explore is `cut`, which extracts portions of text from a file.

### Cutting by Character

You can extract content based on character position using the `-c` flag.

```bash
cut -c 5 sample.txt
```

This command outputs the 5th character from each line of the file. In our case, the output is "q". Note that spaces also count as characters.

### Cutting by Field with cut f

A more powerful feature is cutting by fields. The `cut f` syntax, using the `-f` flag, allows you to extract text based on field position. By default, `cut` uses the TAB character as a delimiter, meaning everything separated by a TAB is considered a distinct field.

Let's see how to cut f based on fields:

```bash
cut -f 2 sample.txt
```

Since we inserted a TAB between "lazy" and "dog", this command treats "dog" as the second field. Your output should be "dog".

### Using Custom Delimiters

You can also combine the field flag with the delimiter flag (`-d`) to specify a custom delimiter. This is useful when working with files that use characters like commas or semicolons to separate data.

```bash
cut -f 1 -d ";" sample.txt
```

This command changes the delimiter from a TAB to a semicolon (`;`). Since we are cutting the first field (`-f 1`), the result will be "The quick brown".

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
