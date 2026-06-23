---
index: 16
lang: "en"
title: "man"
meta_title: "man - Command Line"
meta_description: "Learn the Linux man command with examples for reading manual pages, searching inside man pages, understanding sections, and finding command options."
meta_keywords: "man command, linux man pages, command manual, man ls, man sections, search man page, command line help"
---

## Lesson Content

In Linux, nearly every command comes with its own instruction manual. These are called "man pages" (short for manual pages), and they are an essential resource for learning how to use the system effectively.

### Understanding Man Pages

Man pages are the built-in documentation for Linux commands, utilities, and system calls. They provide a detailed description of what a command does, its available options (or flags), and how to use it. They are your first and best source for command-line help.

### Accessing a Manual with man

To view the manual for any command, use `man` followed by the command name. For example, to read the manual for `ls`, type:

```bash
$ man ls
```

This opens the `ls` man page. You can scroll with arrow keys, search with `/`, and press `q` to quit.

### Finding Details on Command Options

Man pages are particularly useful for understanding command options. For instance, if you have seen `ls -l` and want to know what `-l` means, open `man ls` and search for `-l`.

Inside a man page:

- Press `/` and type a search term to search forward.
- Press `n` to jump to the next match.
- Press `N` to jump to the previous match.
- Press `q` to quit.

### Understanding Man Page Sections

Manual pages are organized into numbered sections. Common sections include:

- `1`: User commands.
- `2`: System calls.
- `3`: Library functions.
- `5`: File formats.
- `8`: System administration commands.

Sometimes the same name exists in more than one section. You can specify the section number:

```bash
$ man 5 passwd
$ man 1 passwd
```

### Common Questions

**Why is man output so long?** Man pages are reference documentation. Use search inside `man` to jump to the part you need.

**How do I quit man?** Press `q`.

**What if no man page exists?** Try `COMMAND --help`, `help COMMAND`, or install the documentation package for your distribution.

## Exercise

Practice is key to mastering the command line. These hands-on labs will help you reinforce your skills with fundamental commands. After completing them, use the `man` command to explore each tool's full potential.

1. **[Linux ls Command: Content Listing](https://labex.io/labs/linux-linux-ls-command-content-listing-219205)** - Practice listing and analyzing file and directory contents, and then use `man ls` to discover more options.
2. **[Linux pwd Command: Directory Displaying](https://labex.io/labs/linux-linux-pwd-command-directory-displaying-209734)** - Learn the `pwd` command to display your current directory, and explore its man page for details.
3. **[Linux cd Command: Directory Changing](https://labex.io/labs/linux-linux-cd-command-directory-changing-209733)** - Master navigating your file system with `cd`, and use `man cd` to understand its various techniques.

These labs will help you apply core concepts in real scenarios and build confidence with essential Linux commands, preparing you to effectively use `man` to deepen your knowledge.

## Quiz Question

How do you see the manual for a command? (Please answer using only the command name in lowercase English letters).

## Quiz Answer

man
