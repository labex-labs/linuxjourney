---
index: 12
lang: "en"
title: "mkdir (Make Directory)"
meta_title: "mkdir (Make Directory) - Command Line"
meta_description: "Learn how to use the mkdir command in Linux to create a new directory. This guide covers the create folder Linux command, including how to create multiple directories and parent directories from the command prompt."
meta_keywords: "create directory linux, mkdir command in linux, create directory in linux, create directory command prompt, create folder linux command, mkdir, make directory, linux"
---

## Lesson Content

As you work with files, you'll need to organize them into directories. The primary tool for this task is the `mkdir` command, which stands for "Make Directory". This command allows you to **create a directory in Linux** right from your terminal or **command prompt**.

### Creating a Single Directory

The most basic use of the **mkdir command in Linux** is to create a single new directory. If the directory doesn't already exist, this command will create it in your current location. For example, to create a directory named `documents`:

```bash
mkdir documents
```

### Creating Multiple Directories

You can also create several directories at once by listing their names, separated by spaces. This is an efficient way to set up multiple folders quickly.

```bash
mkdir books paintings
```

### Creating Nested Directories

Sometimes you need to create a directory and its parent directories simultaneously. The `-p` (parent) option is perfect for this. This powerful feature of the **create folder Linux command** prevents errors if parent directories don't exist. For instance, to create the directory `favorites` inside `hemmingway`, which is inside `books`:

```bash
mkdir -p books/hemmingway/favorites
```

This single command creates `books`, `hemmingway`, and `favorites` if they don't already exist, demonstrating a key capability when you need to **create a directory in Linux**.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of directory creation and management:

1. **[Linux mkdir Command: Directory Creating](https://labex.io/labs/linux-linux-mkdir-command-directory-creating-209739)** - Learn how to use the `mkdir` command in Linux to create directories, set permissions, and organize your file system. This lab covers basic and advanced usage, including creating nested directories.
2. **[Setting Up a New Project Structure](https://labex.io/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts in real scenarios and build confidence with creating and organizing directories in Linux.

## Quiz Question

What command is used to make a directory? Please answer using only the lowercase English command.

## Quiz Answer

mkdir
