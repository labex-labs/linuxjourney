---
index: 12
lang: "en"
title: "mkdir (Make Directory)"
meta_title: "mkdir (Make Directory) - Command Line"
meta_description: "Learn the Linux mkdir command with examples for creating one directory, multiple directories, nested parent directories, and setting permissions."
meta_keywords: "mkdir command, linux mkdir, create directory linux, make directory linux, mkdir -p, mkdir -m, create folder linux"
---

## Lesson Content

As you work with files, you will need to organize them into directories. The primary tool for this task is the `mkdir` command, which stands for make directory.

The basic syntax is:

```bash
mkdir [OPTIONS] DIRECTORY...
```

### Creating a Single Directory

The most basic use of `mkdir` is to create a single new directory. If the directory does not already exist, this command creates it in your current location.

```bash
$ mkdir documents
```

### Creating Multiple Directories

You can also create several directories at once by listing their names, separated by spaces. This is an efficient way to set up multiple folders quickly.

```bash
$ mkdir books paintings
```

### Creating Nested Directories

Sometimes you need to create a directory and its parent directories simultaneously. The `-p` option is perfect for this. It prevents errors if parent directories do not exist.

```bash
$ mkdir -p books/hemingway/favorites
```

This single command creates `books`, `hemingway`, and `favorites` if they do not already exist.

### Setting Directory Permissions

Use `-m` to set permissions while creating a directory.

```bash
$ mkdir -m 755 public
```

You will learn more about permissions later, but this example creates a directory that the owner can write to and others can read and enter.

### Common mkdir Options

- `-p`: Create parent directories as needed.
- `-m MODE`: Set permissions for the new directory.
- `-v`: Print a message for each created directory.

Example:

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

### Common Questions

**Why does mkdir say "File exists"?** A file or directory with that name already exists. Use `ls` to inspect it.

**How do I create nested directories?** Use `mkdir -p parent/child/grandchild`.

**Can mkdir create files?** No. Use `touch` to create empty files.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of directory creation and management:

1. **[Linux mkdir Command: Directory Creating](https://labex.io/labs/linux-linux-mkdir-command-directory-creating-209739)** - Learn how to use the `mkdir` command in Linux to create directories, set permissions, and organize your file system. This lab covers basic and advanced usage, including creating nested directories.
2. **[Setting Up a New Project Structure](https://labex.io/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts in real scenarios and build confidence with creating and organizing directories in Linux.

## Quiz Question

What command is used to make a directory? Please answer using only the lowercase English command.

## Quiz Answer

mkdir
