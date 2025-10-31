---
index: 2
lang: "en"
title: "pwd (Print Working Directory)"
meta_title: "pwd (Print Working Directory) - Command Line"
meta_description: "Master the linux pwd command to display your current directory in Linux. This lesson explains the full form of pwd in linux and how to navigate the directory tree in linux."
meta_keywords: "linux pwd, current directory linux, directory tree in linux, full form of pwd in linux, print working directory, linux path, linux navigation, command line basics"
---

## Lesson Content

In Linux, a core concept is that everything is treated as a file. These files are organized within a hierarchical structure known as the filesystem. Understanding this structure is key to navigating your system effectively.

### The Directory Tree in Linux

The entire filesystem starts from a single top-level directory called the root directory, represented by a forward slash (`/`). From the root, the **directory tree in linux** branches out into various subdirectories, which can contain files and further subdirectories.

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

The location of any file or directory is described by its path. A path is a sequence of directories that leads from a starting point to a specific destination. For example, if you have a folder named `pete` inside the `/home` directory, and a `Movies` folder inside `pete`, the full path would be `/home/pete/Movies`.

### What is the Full Form of PWD in Linux?

When navigating the filesystem, it's essential to know your current location. The command for this is `pwd`. The **full form of pwd in linux** is "print working directory." Its sole purpose is to display the full path of the directory you are currently in, starting from the root (`/`).

### Using the linux pwd Command

To find your **current directory linux**, simply type the **linux pwd** command and press Enter. It prints the absolute path to your present location on the command line.

```bash
pwd
```

Where are you? Where am I? Give it a try to see your own current working directory.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux file system navigation and identifying your current location:

1.  **[Linux pwd Command: Directory Displaying](https://labex.io/labs/linux-linux-pwd-command-directory-displaying-209734)** - This lab provides a focused overview and practical usage of the `pwd` command, directly aligning with the lesson's introduction to finding your current directory.
2.  **[Linux Directory Navigation](https://labex.io/labs/linux-directory-navigation-387844)** - Put your basic Linux command-line skills to the test by navigating through various directories, solidifying your understanding of paths and the file system structure.
3.  **[Linux cd Command: Directory Changing](https://labex.io/labs/linux-linux-cd-command-directory-changing-209733)** - Learn to efficiently navigate your file system using the `cd` command, understanding different techniques for changing directories and exploring the file structure.

These labs will help you apply the concepts of file system hierarchy and navigation in real scenarios and build confidence with essential Linux commands.

## Quiz Question

Which command is used to find the directory you are currently in? (Please answer in English, using only the command name in lowercase.)

## Quiz Answer

pwd
