---
index: 13
lang: "en"
title: "tr (Translate)"
meta_title: "tr (Translate) - Text-Fu"
meta_description: "Learn the Linux tr command with examples for translating characters, deleting characters, squeezing repeats, using character classes, and cleaning text."
meta_keywords: "linux tr command, tr command, tr -d, tr -s, translate characters, delete characters, character classes, text processing linux"
---

## Lesson Content

The `tr` command, short for translate, is a command-line utility that translates, deletes, or squeezes characters from standard input. It is useful for simple text manipulation and is often used with pipes to process the output of other commands.

The basic syntax is:

```bash
tr [OPTIONS] SET1 [SET2]
```

Unlike tools such as `sed` or `awk`, `tr` works character by character. It does not understand words, columns, or regular expressions in the same way. That makes it fast and simple for tasks such as changing case, removing digits, and normalizing repeated spaces.

### Basic Character Translation

The most common use of `tr` is to substitute one set of characters for another. For example, you can easily translate all lowercase characters to uppercase.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

In this example, we piped the output of `echo` to the `tr` command. The `tr` command then translated the character range `a-z` into the corresponding characters in the range `A-Z`.

You can also translate one character to another:

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

Each character in `SET1` maps to the character in the same position in `SET2`.

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

Here, `a` becomes `A`, `b` becomes `B`, and `c` becomes `C`.

### Deleting Characters with -d

Another powerful feature is the ability to delete specific characters using the `-d` option. This is particularly useful for cleaning up text. For instance, if you want to remove all digits from a string, you can use:

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Here, `tr -d` deleted every character in the specified set, from `0` through `9`.

You can remove punctuation from a string by using a character class:

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

You can also remove newline characters to join lines together:

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

### Squeezing Repeated Characters

The `tr` command can also "squeeze" repeated characters into a single instance using the `-s` option. This is great for normalizing text with extra whitespace.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

In this case, `tr -s ' '` replaced sequences of multiple spaces with a single space, making the output much cleaner.

You can squeeze repeated newlines too:

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

### Using Character Classes

Character classes make `tr` commands easier to read and more portable. Common classes include:

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

Delete everything except letters and digits by using `-c` with `-d`. The `-c` option means complement, or "everything not in this set."

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

### Combining Delete and Squeeze

You can combine options when cleaning text. This example deletes punctuation, then squeezes repeated spaces:

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

For tab-separated input, you can translate tabs into commas:

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

### Common tr Options

Here are the options you will use most often:

- `-d`: Delete characters in `SET1`.
- `-s`: Squeeze repeated characters in `SET1`.
- `-c`: Use the complement of `SET1`.
- `-t`: Truncate `SET1` to the length of `SET2` before translating.

### Common Questions

**Why does tr read from a pipe?** `tr` reads from standard input, so it is commonly used after commands such as `echo`, `cat`, `printf`, or other text-producing commands.

**Does tr replace words?** No. `tr` translates characters, not words. Use `sed` when you need to replace whole words or patterns.

**Why did my tr command change characters one by one?** That is how `tr` works. It maps each character in `SET1` to the corresponding character in `SET2`.

**Why should I quote sets like 'a-z'?** Quoting prevents the shell from interpreting special characters before `tr` receives them.

## Exercise

To put your knowledge into practice, try the following hands-on lab. It will help you reinforce your understanding of character translation and text processing.

1. **[Linux tr Command: Character Translating](https://labex.io/labs/linux-linux-tr-command-character-translating-219198)** - Learn the Linux `tr` command for character-level transformations in text streams. You'll practice translating characters, deleting specific characters, working with character classes, and squeezing repeated characters.

This lab will help you apply the concepts of text manipulation in real scenarios and build confidence with the `tr` command.

## Quiz Question

What command is used to translate characters? (Please answer in lowercase English letters only)

## Quiz Answer

tr
