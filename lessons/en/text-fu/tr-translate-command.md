---
lesson_id: "tr-translate-command"
course_id: "text-fu"
lang: "en"
order_index: 13
title: "tr (Translate)"
description: "Learn how to translate, delete, and squeeze character sets in a standard input stream."
meta_title: "tr (Translate) - Text-Fu"
meta_description: "Learn the Linux tr command with examples for translating characters, deleting characters, squeezing repeats, using character classes, and cleaning text."
meta_keywords: "linux tr command, tr command, tr -d, tr -s, translate characters, delete characters, character classes, text processing linux"
---

The `tr` command, short for translate, translates, deletes, or squeezes characters read from stdin. It does not accept ordinary input-file operands, so use a pipe or input redirection to provide data.

The basic syntax is:

```bash
tr [OPTIONS] SET1 [SET2]
```

`tr` works with character sets rather than words or general regular expressions. Use another tool when a transformation depends on a complete word, line structure, or surrounding context.

## Translating Characters

With two sets, characters from `SET1` map by position to characters in `SET2`:

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

Here, lowercase range positions map to corresponding uppercase positions. Quote set expressions so the shell passes them unchanged.

You can also translate one character to another:

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

Characters not in `SET1` pass through unchanged.

:::single-choice{#tr-map-characters}
What does `printf '%s\n' 'abc123' | tr 'abc' 'ABC'` print?

::option[`ABCABC`]{#tr-uppercase-digits explanation="Digits are not members of the source set, so `tr` does not replace them with letters."}
::option[`ABC123`]{#tr-uppercase-abc .correct explanation="Each of `a`, `b`, and `c` maps to the character at the same position in `ABC`; the digits are unchanged."}
::option[`abc123ABC`]{#tr-append-set explanation="`tr` translates matching input characters. It does not append the destination set to the stream."}
:::

## Deleting Characters

Use `-d` with one set to remove every matching character:

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Every digit is removed independently; `tr` is not identifying a complete number token.

Character classes can describe groups defined by the current locale:

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

Deleting newlines joins input lines without inserting a replacement separator:

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

:::single-choice{#tr-delete-digits}
Which command removes every digit from stdin while leaving other characters unchanged?

::option[`tr -d '[:digit:]'`]{#tr-delete-digit-class .correct explanation="The `-d` option deletes all characters in the digit class from the input stream."}
::option[`tr -s '[:digit:]'`]{#tr-squeeze-digits explanation="The `-s` option collapses repeated digits but leaves one character from each run."}
::option[`tr '[:digit:]'`]{#tr-one-set-no-delete explanation="Translation normally needs a second set. A set alone does not request deletion."}
:::

## Squeezing Repeated Characters

Use `-s SET` to replace each run of a listed character with one instance of that character:

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

This set contains an ordinary space, so tabs and newlines are not squeezed by that command.

You can squeeze repeated newlines too:

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

:::single-choice{#tr-squeeze-spaces}
Which command reduces every run of ordinary spaces in stdin to one space?

::option[`tr -s ' '`]{#tr-squeeze-space .correct explanation="The `-s` option squeezes repeated members of the supplied set, which contains one ordinary space."}
::option[`tr -d ' '`]{#tr-delete-space explanation="The `-d` option removes all ordinary spaces rather than preserving one per run."}
::option[`tr ' ' ''`]{#tr-empty-destination explanation="An empty translation set is not the clear, portable way to request squeezing. Use `-s` for repeated characters."}
:::

## Using Character Classes and Complements

Character classes make intent clearer than hand-written ranges in many locales. Common classes include:

- `[:lower:]`: Lowercase letters.
- `[:upper:]`: Uppercase letters.
- `[:digit:]`: Digits.
- `[:alpha:]`: Letters.
- `[:alnum:]`: Letters and digits.
- `[:space:]`: Whitespace characters.
- `[:punct:]`: Punctuation characters.

For example, convert lowercase text to uppercase with character classes:

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

The `-c` option complements `SET1`, meaning every character not in the set. Combine it with `-d` to retain only selected kinds of characters:

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

This also removes the newline because a newline is not alphanumeric. Add or preserve separators deliberately when record boundaries matter.

:::single-choice{#tr-keep-alphanumeric}
What does `tr -cd '[:alnum:]'` do to stdin?

::option[Deletes alphanumeric characters and keeps everything else.]{#tr-delete-alnum explanation="The complement changes which characters `-d` targets. The alphanumeric set itself is retained."}
::option[Deletes every character that is not alphanumeric.]{#tr-delete-nonalnum .correct explanation="`-c` complements the alphanumeric set, and `-d` deletes the resulting non-alphanumeric set."}
::option[Converts every letter and digit to uppercase.]{#tr-uppercase-alnum explanation="No destination translation set is present, so this command does not perform case conversion."}
:::

## Building Stream Transformations

Several `tr` processes can be connected when transformations are clearer as separate stages:

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

For simple tab-separated input, translate tab characters into commas:

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

Because `tr` reads stdin, a file can be provided with `<`:

```bash
$ tr '[:lower:]' '[:upper:]' < names.txt
```

Redirect stdout to a different file if you need to save the result. Do not redirect back to the input pathname, because the shell would truncate it before `tr` reads.

:::single-choice{#tr-read-file-input}
Which command makes `tr` read `names.txt` as stdin and convert lowercase characters to uppercase?

::option[`tr names.txt '[:lower:]' '[:upper:]'`]{#tr-file-operand explanation="`tr` does not take an ordinary input filename this way; the extra operand makes the syntax invalid."}
::option[`tr -d '[:lower:]' < names.txt`]{#tr-delete-lowercase explanation="This reads the file correctly but deletes lowercase letters rather than translating them."}
::option[`tr '[:lower:]' '[:upper:]' < names.txt`]{#tr-input-redirection .correct explanation="The shell opens `names.txt` on stdin, and `tr` maps the lowercase class to the uppercase class."}
:::

To practice character-level stream transformations, try this hands-on lab:

1. **[Linux tr Command: Character Translating](https://labex.io/labs/linux-linux-tr-command-character-translating-219198)** - Learn the Linux `tr` command for character-level transformations in text streams. You'll practice translating characters, deleting specific characters, working with character classes, and squeezing repeated characters.

## Summary

You can now transform character streams with focused `tr` operations.

1. Map characters between corresponding sets.
2. Delete selected characters with `-d`.
3. Squeeze repeated characters with `-s`.
4. Use locale-aware classes and complements deliberately.
5. Supply input through stdin rather than a filename operand.
