---
index: 2
lang: "en"
title: "pwd (Print Working Directory)"
meta_title: "pwd (Print Working Directory) - Command Line"
meta_description: "Learn the Linux pwd command, what print working directory means, and how absolute paths show your current location in the filesystem."
meta_keywords: "pwd command, linux pwd, print working directory, current directory linux, absolute path, linux filesystem, directory tree"
---

## Lesson Content

In Linux, files and directories are organized in a hierarchy called the filesystem. Before you can move around confidently, you need to know where you are. The `pwd` command answers that question by printing your current working directory.

### The Directory Tree in Linux

The entire filesystem starts from a single top-level directory called the root directory, represented by a forward slash (`/`). From the root, the directory tree branches into subdirectories, which can contain files and more subdirectories.

Here is a simplified example of what this structure looks like:

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

### Understanding File Paths

The location of any file or directory is described by its path. A path is a sequence of directories that leads from a starting point to a specific destination.

For example, if you have a folder named `pete` inside `/home`, and a `Movies` folder inside `pete`, the full path is:

```plaintext
/home/pete/Movies
```

A path that starts with `/` is an absolute path because it starts at the root directory. A path such as `Movies` is relative because it depends on your current location.

### What is the Full Form of PWD in Linux?

The full form of `pwd` is "print working directory." Your working directory is the directory where your shell is currently located. Commands that use relative paths start from this location.

### Using the pwd Command

To find your current directory, type `pwd` and press Enter.

```bash
$ pwd
/home/pete
```

The output is an absolute path. In this example, the shell is currently in the `pete` user's home directory.

### Why pwd is Useful

Use `pwd` when:

- You are following instructions and need to confirm your location.
- A command failed because a file path was wrong.
- You moved through several directories and lost track of where you are.
- You want to copy the current directory path into another command.

For example:

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

This tells you that `app.py` and `README.md` are located in `/home/pete/projects`.

### Common Questions

**Does pwd change anything?** No. `pwd` only prints information.

**Why is the output different on my system?** Your username, home directory, and current location may be different.

**What is the difference between pwd and cd?** `pwd` shows where you are. `cd` changes where you are.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux file system navigation and identifying your current location:

1. **[Linux pwd Command: Directory Displaying](https://labex.io/labs/linux-linux-pwd-command-directory-displaying-209734)** - This lab provides a focused overview and practical usage of the `pwd` command, directly aligning with the lesson's introduction to finding your current directory.
2. **[Linux Directory Navigation](https://labex.io/labs/linux-directory-navigation-387844)** - Put your basic Linux command-line skills to the test by navigating through various directories, solidifying your understanding of paths and the file system structure.
3. **[Linux cd Command: Directory Changing](https://labex.io/labs/linux-linux-cd-command-directory-changing-209733)** - Learn to efficiently navigate your file system using the `cd` command, understanding different techniques for changing directories and exploring the file structure.

These labs will help you apply the concepts of file system hierarchy and navigation in real scenarios and build confidence with essential Linux commands.

## Quiz Question

Which command is used to find the directory you are currently in? (Please answer in English, using only the command name in lowercase.)

## Quiz Answer

pwd
