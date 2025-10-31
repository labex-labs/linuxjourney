---
index: 10
lang: "en"
title: "expand and unexpand"
meta_title: "expand and unexpand - Text-Fu"
meta_description: "Master text formatting in Linux with our guide on the expand and unexpand commands. Learn how to convert tabs to spaces and spaces back to tabs for consistent file layouts."
meta_keywords: "expand command, unexpand command, Linux tabs, Linux spaces, text formatting, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Inconsistent spacing can make text files difficult to read. While tabs are meant to create uniform indentation, their display width can vary across different editors and systems. This can disrupt text formatting and alignment. Fortunately, Linux provides simple tools to manage this by converting between tabs and spaces. This beginner Linux guide will walk you through the process.

### Converting Tabs to Spaces with the expand Command

When you need to ensure consistent spacing, you can convert tabs into a standard number of spaces using the `expand` command. This command reads a file and replaces each tab character with a set of space characters, printing the result to standard output.

```bash
expand sample.txt
```

By default, the `expand command` converts each tab into 8 spaces. This simple utility is a powerful tool for improving text formatting.

### Saving the Converted Output

The `expand` command only prints the converted text to your terminal. To save the changes, you must redirect the output to a new file.

```bash
expand sample.txt > result.txt
```

This command takes the output of `expand sample.txt` and writes it into `result.txt`, giving you a new file with spaces instead of tabs.

### Converting Spaces to Tabs with the unexpand Command

The reverse operation, converting spaces back into tabs, is handled by the `unexpand` command. This can be useful for reducing file size or adhering to coding standards that require tabs.

```bash
unexpand -a result.txt
```

By default, `unexpand` only converts leading spaces on each line. The `-a` option tells the `unexpand command` to convert all instances of 8 spaces into a tab, not just those at the beginning of a line, providing more comprehensive control over your Linux spaces and tabs.

## Exercise

To master text manipulation and redirection in Linux, practice is key. The following hands-on labs will help reinforce your understanding:

1.  **[Redirecting Input and Output in Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practice controlling data flow from commands by manipulating standard output (stdout), standard error (stderr), and standard input (stdin) using operators like `>` and `>>`.
2.  **[Simple Text Processing](https://labex.io/labs/linux-simple-text-processing-18004)** - Learn to use powerful commands like `tr`, `col`, `join`, and `paste` to manipulate and analyze text data efficiently, enhancing your command-line skills for data processing.
3.  **[Text Processing and Regular Expressions](https://labex.io/labs/linux-text-processing-and-regular-expressions-18003)** - Learn the powerful text processing tools `grep`, `sed`, and `awk`, and use regular expressions for efficient text manipulation and pattern matching in Linux.

Completing these labs will help you apply the concepts of text transformation and file manipulation in real-world scenarios, building your confidence with essential Linux command-line tools.

## Quiz Question

What command is used to convert tabs to spaces? (Please answer using the lowercase English command name.)

## Quiz Answer

expand
