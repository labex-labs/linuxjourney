---
lesson_id: "regular-expressions-regex"
course_id: "advanced-text-fu"
lang: "en"
order_index: 1
title: "regex (Regular Expressions)"
description: "Learn how anchors, character sets, repetition, and regex flavors control text pattern matching."
meta_title: "regex (Regular Expressions) - Advanced Text-Fu"
meta_description: "Master the basics of Linux with our guide to regular expressions (regex). Learn pattern matching with grep, using syntax like ^, $, and []. This is one of the best ways to learn Linux text manipulation and advance your skills."
meta_keywords: "regular expression linux, regex, basics of linux, pattern matching, grep, text processing, learn linux, linux tutorial, quickest way to linux advanced"
---

Regular expressions, often shortened to **regex**, describe text patterns. Tools such as `grep`, `sed`, and `awk` use regex, but their supported syntax can differ, so always identify the tool and regex flavor.

GNU `grep` uses basic regular expressions (BRE) by default and extended regular expressions (ERE) with `-E`. This lesson introduces constructs shared by both, then notes common ERE additions.

Use this input in the examples:

```text
sally sells seashells
by the seashore
```

## Matching Literal Text

Most ordinary characters match themselves. The pattern `seashells` selects a line containing that exact sequence anywhere:

```bash
$ grep 'seashells' sample.txt
sally sells seashells
```

Quote regex patterns so the shell does not expand or split them before the matching tool receives them. Regex is also different from shell pathname expansion: in a regex, `*` repeats the preceding atom; in a shell glob, `*` is itself a wildcard for a string of pathname characters.

:::single-choice{#regex-versus-shell-star} What does `*` do in a regular expression such as `ab*`?

::option[It matches any filename in the current directory.]{#regex-shell-glob explanation="That describes shell pathname expansion in a command context, not the meaning of `*` inside a regex."}
::option[It repeats the preceding `b` zero or more times.]{#regex-repeat-b .correct explanation="A regex quantifier applies to the atom immediately before it, so `ab*` matches `a`, `ab`, `abb`, and so on."}
::option[It repeats the complete string `ab` exactly two times.]{#regex-repeat-ab-twice explanation="The star applies only to the preceding atom and allows zero or more repetitions, not exactly two complete-string repetitions."}
:::

## Anchoring a Match

Outside a bracket expression, `^` at the beginning of a pattern anchors the match at the beginning of a line:

```plaintext
^by
```

The `$` anchor matches at the end of a line:

```plaintext
seashore$
```

Combine both anchors when the entire line must fit the pattern:

```text
^by the seashore$
```

:::single-choice{#regex-complete-line} Which pattern matches only a line whose complete text is `by the seashore`?

::option[`^by the seashore$`]{#regex-anchored-line .correct explanation="The caret requires the match to start at the beginning, and the dollar sign requires it to end with the line."}
::option[`by the seashore`]{#regex-unanchored-line explanation="Without anchors, this sequence can match inside a longer line with additional text before or after it."}
::option[`$by the seashore^`]{#regex-reversed-anchors explanation="The end anchor cannot precede the text that must match, and the start anchor cannot follow it in this intended pattern."}
:::

## Matching One Character

The dot matches one character in ordinary line-oriented regex mode:

```plaintext
b.
```

This matches `by`, but it could also match `ba` or `b7`. It does not match a lone `b` because one character is required after it. To match a literal period, escape it as `\.` or place it in a suitable bracket expression.

:::single-choice{#regex-dot-character} Which string is not matched by the complete-line pattern `^b.$`?

::option[`by`]{#regex-dot-by explanation="The dot matches `y`, so the two-character line satisfies the pattern."}
::option[`b`]{#regex-dot-b .correct explanation="The dot requires one character after `b`, but this string ends immediately."}
::option[`b7`]{#regex-dot-b7 explanation="The dot matches the digit `7`, so this two-character line satisfies the pattern."}
:::

## Using Bracket Expressions

A bracket expression matches one character from a specified set:

```plaintext
s[ae]lls
```

This matches `sells` or `salls` at that position.

When `^` is the first character after `[`, it negates the set:

```plaintext
s[^e]lls
```

This matches `salls` but not `sells` because the character after the first `s` cannot be `e`.

:::single-choice{#regex-negated-bracket} What does `[^e]` match?

::option[Exactly one character other than `e`.]{#regex-not-e .correct explanation="A leading caret inside brackets complements the listed set, while the bracket expression still consumes one character."}
::option[The beginning of a line followed by `e`.]{#regex-caret-e-anchor explanation="Inside a bracket expression, a leading caret negates the set rather than anchoring a line."}
::option[Zero or more occurrences of the letter `e`.]{#regex-repeat-e explanation="Repetition would require a quantifier such as `*`; this bracket expression matches one non-`e` character."}
:::

Ranges can describe characters between endpoints:

```plaintext
d[a-c]g
```

This can match `dag`, `dbg`, or `dcg`. Range behavior can depend on locale collation. Character classes such as `[[:lower:]]`, `[[:upper:]]`, and `[[:digit:]]` often express intent more clearly.

## Repeating and Combining Patterns

In both BRE and ERE, `*` means zero or more repetitions of the preceding atom:

```text
seashells*
```

This matches `seashell` followed by zero or more additional `s` characters. In ERE mode with `grep -E`, common operators include:

- `+`: One or more repetitions.
- `?`: Zero or one repetition.
- `|`: Either the expression on the left or the right.
- `(...)`: Group expressions.

For example:

```bash
$ grep -E '^(cat|dog)s?$' animals.txt
```

This selects complete lines equal to `cat`, `cats`, `dog`, or `dogs`. In BRE mode, these operators have different escaping rules, so do not copy a pattern between flavors without checking it.

:::single-choice{#regex-extended-alternation} Which command enables extended regex syntax for the pattern `^(cat|dog)s?$`?

::option[`grep -F '^(cat|dog)s?$' animals.txt`]{#regex-fixed-animals explanation="`-F` treats every regex operator as literal text, so grouping, alternation, and optional repetition are disabled."}
::option[`grep -E '^(cat|dog)s?$' animals.txt`]{#regex-extended-animals .correct explanation="`-E` selects extended regular expressions, enabling the shown grouping, alternation, and optional `s`."}
::option[`grep '^(cat|dog)s?$' animals.txt`]{#regex-basic-animals explanation="Default grep uses BRE, where these unescaped grouping and alternation characters do not have the intended ERE meanings."}
:::

To practice regex selection with Linux text tools, try these hands-on labs:

1. **[Search Text with grep in Linux](https://labex.io/labs/comptia-search-text-with-grep-in-linux-590841)** - In this lab, you will learn to search for text in files on a Linux system using the `grep` command. You will perform basic searches, display line numbers, use anchors like `^` and `$` to match line positions, and harness both basic and extended regular expressions for complex pattern matching.
2. **[Text Processing and Regular Expressions](https://labex.io/labs/linux-text-processing-and-regular-expressions-18003)** - Learn the powerful text processing tools grep, sed, and awk. Learn to use regular expressions for efficient text manipulation and pattern matching in Linux.
3. **[Extracting Mails and Numbers](https://labex.io/labs/linux-extracting-mails-and-numbers-17991)** - In this challenge, you will learn how to use grep and regular expressions to extract email addresses and numbers from a file, demonstrating essential Linux text processing skills.

## Summary

You can now read and build foundational line-oriented regular expressions.

1. Distinguish regex operators from shell pathname wildcards.
2. Anchor matches at the beginning or end of a line.
3. Match one character with a dot or bracket expression.
4. Negate sets and use locale-aware character classes.
5. Choose BRE or ERE syntax deliberately.
