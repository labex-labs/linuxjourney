---
index: 7
lang: "en"
title: "cat"
meta_title: "cat - Command Line"
meta_description: "Master the linux cat command to view, create, and concatenate files. This guide covers basic usage, common options, and how to use cat linux with redirection like linux cat >."
meta_keywords: "linux cat command, cat linux, cat manual linux, linux cat >, view file contents, concatenate files, linux commands, command line"
---

## Lesson Content

After learning to navigate the filesystem, the next step is to view the contents of files. A fundamental and versatile tool for this is the `linux cat command`. The name `cat` is short for "concatenate," which hints at its ability to link files together.

### Viewing File Contents

The most basic use of the `cat` command is to display the content of a single file directly in your terminal.

```bash
cat myfile.txt
```

This command will print the entire content of `myfile.txt` to the screen. While this is perfect for short configuration files or text snippets, it's not ideal for viewing large files, as the text will scroll by very quickly. We will cover tools better suited for large files in a later lesson.

### Concatenating Files

True to its name, `cat` can combine, or concatenate, multiple files and display their combined output. The `cat linux` utility reads the files in the order they are provided and prints them sequentially.

```bash
cat dogfile birdfile
```

This command will first display the contents of `dogfile`, immediately followed by the contents of `birdfile`.

### Creating Files with Redirection

You can also use `cat` with the output redirection operator (`>`) to create new files. The `linux cat >` combination is a quick way to write text into a file directly from your terminal.

```bash
cat > newfile.txt
```

After running this command, you can type your text. Press `Ctrl+D` on a new line to save and exit. This will create `newfile.txt` with the text you entered. Be careful, as using `>` on an existing file will overwrite it completely.

### Common cat Command Options

The `cat` command has several options to modify its behavior. Here are a couple of common ones:

- `-n`: This option numbers all output lines, starting from 1.
- `-b`: This option numbers only the non-empty output lines.

For a complete list of functionalities, you can always refer to the `cat manual linux` page by typing `man cat` in your terminal.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of viewing file contents:

1. **[Linux cat Command: File Concatenating](https://labex.io/labs/linux-linux-cat-command-file-concatenating-210986)** - Learn the `cat` command for viewing, concatenating, and manipulating text files, enhancing your command-line skills for efficient text file handling.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice using commands like `cat` to efficiently view and navigate text files, including system logs and configuration files, to extract critical information.

These labs will help you apply the concepts in real scenarios and build confidence with file content viewing in Linux.

## Quiz Question

What command is used to display the contents of a file on the command line? (Note: Your answer should be a single, lowercase English word.)

## Quiz Answer

cat
