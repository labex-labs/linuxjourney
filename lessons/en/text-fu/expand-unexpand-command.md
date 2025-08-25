---
index: 10
lang: "en"
title: "expand and unexpand"
meta_title: "expand and unexpand - Text-Fu"
meta_description: "Learn to convert tabs to spaces with the `expand` command and spaces to tabs with `unexpand`. Improve text file formatting with this Linux tutorial."
meta_keywords: "expand command, unexpand command, Linux tabs, Linux spaces, text formatting, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

In our lesson on the `cut` command, we had our `sample.txt` file that contained a tab. Normally, tabs would usually show a noticeable difference, but some text files don't show that well enough. Having tabs in a text file may not provide the desired spacing. To change your tabs to spaces, use the `expand` command.

```bash
expand sample.txt
```

The command above will print output with each tab converted into a group of spaces. To save this output in a file, use output redirection as shown below.

```bash
expand sample.txt > result.txt
```

Opposite to `expand`, we can convert back each group of spaces to a tab with the `unexpand` command:

```bash
unexpand -a result.txt
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of text manipulation and redirection in Linux:

1. **[Redirecting Input and Output in Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practice controlling data flow from commands by manipulating standard output (stdout), standard error (stderr), and standard input (stdin) using operators like `>` and `>>`.
2. **[Simple Text Processing](https://labex.io/labs/linux-simple-text-processing-18004)** - Learn to use powerful commands like `tr`, `col`, `join`, and `paste` to manipulate and analyze text data efficiently, enhancing your command-line skills for data processing.
3. **[Text Processing and Regular Expressions](https://labex.io/labs/linux-text-processing-and-regular-expressions-18003)** - Learn the powerful text processing tools `grep`, `sed`, and `awk`, and use regular expressions for efficient text manipulation and pattern matching in Linux.

These labs will help you apply the concepts of text transformation and file manipulation in real scenarios and build confidence with Linux command-line tools.

## Quiz Question

What command is used to convert tabs to spaces?

## Quiz Answer

expand
