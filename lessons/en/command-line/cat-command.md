---
index: 7
lang: "en"
title: "cat"
meta_title: "cat - Command Line"
meta_description: "Learn the Linux cat command with examples for viewing files, concatenating files, numbering lines, creating files, and using redirection safely."
meta_keywords: "linux cat command, cat command, view file linux, concatenate files, cat -n, cat -b, cat redirection, linux cat"
---

## Lesson Content

After learning to navigate the filesystem, the next step is to view the contents of files. A fundamental and versatile tool for this is the `cat` command. The name `cat` is short for "concatenate," which hints at its ability to link files together.

### Viewing File Contents

The most basic use of the `cat` command is to display the content of a single file directly in your terminal.

```bash
$ cat myfile.txt
```

This command will print the entire content of `myfile.txt` to the screen. While this is perfect for short configuration files or text snippets, it's not ideal for viewing large files, as the text will scroll by very quickly. We will cover tools better suited for large files in a later lesson.

### Concatenating Files

True to its name, `cat` can combine, or concatenate, multiple files and display their combined output. It reads the files in the order they are provided and prints them sequentially.

```bash
$ cat dogfile birdfile
```

This command will first display the contents of `dogfile`, immediately followed by the contents of `birdfile`.

To save the combined output into a new file, use redirection:

```bash
$ cat dogfile birdfile > animals
```

### Creating Files with Redirection

You can also use `cat` with the output redirection operator (`>`) to create new files. This is a quick way to write text into a file directly from your terminal.

```bash
$ cat > newfile.txt
```

After running this command, you can type your text. Press `Ctrl+D` on a new line to save and exit. This will create `newfile.txt` with the text you entered. Be careful, as using `>` on an existing file will overwrite it completely.

To append to a file instead of overwriting it, use `>>`.

```bash
$ cat >> notes.txt
```

### Common cat Command Options

The `cat` command has several options to modify its behavior.

- `-n`: Number all output lines, starting from 1.
- `-b`: Number only non-empty output lines.
- `-s`: Squeeze multiple blank lines into one blank line.
- `-A`: Show non-printing characters, tabs, and line endings.

Examples:

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

### When Not to Use cat

Use `cat` for short files. For long files, use `less` so you can scroll, search, and quit without flooding your terminal.

```bash
$ less /var/log/syslog
```

### Common Questions

**What does cat stand for?** It stands for concatenate.

**Can cat edit a file?** Not interactively. It can create or overwrite files with redirection, but a text editor is better for editing.

**What is the difference between > and >>?** `>` overwrites a file. `>>` appends to the end of a file.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of viewing file contents:

1. **[Linux cat Command: File Concatenating](https://labex.io/labs/linux-linux-cat-command-file-concatenating-210986)** - Learn the `cat` command for viewing, concatenating, and manipulating text files, enhancing your command-line skills for efficient text file handling.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice using commands like `cat` to efficiently view and navigate text files, including system logs and configuration files, to extract critical information.

These labs will help you apply the concepts in real scenarios and build confidence with file content viewing in Linux.

## Quiz Question

What command is used to display the contents of a file on the command line? (Note: Your answer should be a single, lowercase English word.)

## Quiz Answer

cat
