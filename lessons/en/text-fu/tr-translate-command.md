---
index: 13
lang: "en"
title: "tr (Translate)"
meta_title: "tr (Translate) - Text-Fu"
meta_description: "Master the Linux tr command for character translation and deletion. This guide covers how to trtranslate characters, use options like linux tr -d to remove characters, and provides practical examples for text manipulation."
meta_keywords: "tr, tr command, trtranslate, linux tr -d, tr -d linux, translate characters, delete characters, text processing, Linux command"
---

## Lesson Content

The `tr` command, short for translate, is a command-line utility in Linux that translates or deletes characters from standard input. It is a useful tool for simple text manipulation and is often used with pipes to process the output of other commands. The `trtranslate` functionality is a core part of text processing.

### Basic Character Translation

The most common use of `tr` is to substitute one set of characters for another. For example, you can easily translate all lowercase characters to uppercase.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

In this example, we piped the output of `echo` to the `tr` command. The `tr` command then translated the character range `a-z` into the corresponding characters in the range `A-Z`.

### Deleting Characters with -d

Another powerful feature is the ability to delete specific characters using the `-d` (delete) option. This is particularly useful for cleaning up text. For instance, if you want to remove all digits from a string, you can use `linux tr -d`.

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Here, the `tr -d` command deleted every character in the specified set ('0' through '9') from the input stream. This is a common pattern for `tr -d linux` users.

### Squeezing Repeated Characters

The `tr` command can also "squeeze" repeated characters into a single instance using the `-s` (squeeze) option. This is great for normalizing text with extra whitespace.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

In this case, `tr -s ' '` replaced sequences of multiple spaces with a single space, making the output much cleaner.

## Exercise

To put your knowledge into practice, try the following hands-on lab. It will help you reinforce your understanding of character translation and text processing.

1.  **[Linux tr Command: Character Translating](https://labex.io/labs/linux-linux-tr-command-character-translating-219198)** - Learn the Linux `tr` command for character-level transformations in text streams. You'll practice translating characters, deleting specific characters, working with character classes, and squeezing repeated characters.

This lab will help you apply the concepts of text manipulation in real scenarios and build confidence with the `tr` command.

## Quiz Question

What command is used to translate characters? (Please answer in lowercase English letters only)

## Quiz Answer

tr
