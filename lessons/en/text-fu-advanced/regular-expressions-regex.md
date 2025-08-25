---
index: 1
lang: "en"
title: "regex (Regular Expressions)"
meta_title: "regex (Regular Expressions) - Advanced Text-Fu"
meta_description: "Learn regular expressions (regex) for Linux pattern matching. Understand regex syntax like ^, $, ., and [] for text manipulation. Improve your grep skills!"
meta_keywords: "regular expressions, regex, Linux regex, grep regex, pattern matching, regex tutorial, Linux commands, beginner"
---

## Lesson Content

Regular expressions are a powerful tool for pattern-based selection. They use special notations similar to those we've encountered already, such as the `*` wildcard.

We'll go through a couple of the most common regular expressions; these are almost universal with any programming language.

We'll use this phrase as our test string:

```plaintext
sally sells seashells
by the seashore
```

### 1. Beginning of a line with ^

```plaintext
^by
would match the line "by the seashore"
```

### 2. End of a line with $

```plaintext
seashore$
would match the line "by the seashore"
```

### 3. Matching any single character with

```plaintext
b.
would match by
```

### 4. Bracket notation with [] and ()

This can be a little tricky. Brackets allow us to specify characters found within the bracket.

```plaintext
d[iou]g
would match: dig, dog, dug
```

The previous anchor tag `^` when used in a bracket means anything except the characters within the bracket.

```plaintext
d[^i]g
would match: dog and dug but not dig
```

Brackets can also use ranges to increase the amount of characters you want to use.

```plaintext
d[a-c]g
will match patterns like dag, dbg, and dcg
```

Be careful, though, as brackets are case-sensitive:

```plaintext
d[A-C]g
will match dAg, dBg and dCg but not dag, dbg and dcg
```

And those are some basic regular expressions.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of regular expressions and pattern matching:

1.  **[Search Text with grep in Linux](https://labex.io/labs/comptia-search-text-with-grep-in-linux-590841)** - In this lab, you will learn to search for text in files on a Linux system using the `grep` command. You will perform basic searches, display line numbers, use anchors like `^` and `$` to match line positions, and harness both basic and extended regular expressions for complex pattern matching.
2.  **[Text Processing and Regular Expressions](https://labex.io/labs/linux-text-processing-and-regular-expressions-18003)** - Learn the powerful text processing tools grep, sed, and awk. Learn to use regular expressions for efficient text manipulation and pattern matching in Linux.
3.  **[Extracting Mails and Numbers](https://labex.io/labs/linux-extracting-mails-and-numbers-17991)** - In this challenge, you will learn how to use grep and regular expressions to extract email addresses and numbers from a file, demonstrating essential Linux text processing skills.

These labs will help you apply the concepts in real scenarios and build confidence with regular expressions and text processing.

## Quiz Question

What regular expression would you use to match a single character?

## Quiz Answer

.
