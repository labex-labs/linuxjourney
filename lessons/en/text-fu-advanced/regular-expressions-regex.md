---
title: "regex (Regular Expressions)"
description: "Learn regular expressions (regex) for Linux pattern matching. Understand regex syntax like ^, $, ., and [] for text manipulation. Improve your grep skills!"
keywords: "regular expressions, regex, Linux regex, grep regex, pattern matching, regex tutorial, Linux commands, beginner"
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

Try to combine regular expressions with `grep` and search through some files.

```bash
grep [regular expression here] [file]
```

## Quiz Question

What regular expression would you use to match a single character?

## Quiz Answer

.
