---
lang: "en"
title: "tr (Translate)"
meta_description: "Learn how to use the Linux 'tr' command to translate and delete characters. Understand character translation with examples and exercises. Start your Linux journey!"
meta_keywords: "tr command, Linux tr, translate characters, delete characters, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

The `tr` (translate) command allows you to translate one set of characters into another set of characters. Let's try an example of translating all lowercase characters to uppercase characters.

```bash
$ tr a-z A-Z
hello
HELLO
```

As you can see, we made the ranges of `a-z` into `A-Z`, and all text we type that is lowercase gets uppercased.

## Exercise

Try the following command. What happens?

```bash
$ tr -d ello
hello
```

## Quiz Question

What command is used to translate characters?

## Quiz Answer

tr
