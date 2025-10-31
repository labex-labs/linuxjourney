---
index: 4
lang: "en"
title: "ls (List Directories)"
meta_title: "ls (List Directories) - Command Line"
meta_description: "Learn how to use the powerful command ls in Linux. This guide covers how to list directory contents, view hidden files with ls -a, get detailed listings with ls -l, and use the ls -r command to reverse sort. A perfect lesson for mastering the cmd ls."
meta_keywords: "ls command, list directories, cmd ls, ls -r command, command ls, linux ls -r, command linux ls, hidden files, Linux commands, beginner Linux"
---

## Lesson Content

Now that we know how to move around the file system, how do we figure out what is available to us? Without the right tool, it's like moving around in the dark. Fortunately, the wonderful `command linux ls` is here to help by listing directory contents.

### Basic Usage of the ls Command

By default, the `ls` command will list the directories and files in your current directory. However, you can also specify a path to list the contents of a different directory.

```bash
ls
ls /home/pete
```

The `command ls` is a versatile tool that can show you detailed information about the files and directories you are viewing.

### Viewing Hidden Files

Note that not all files in a directory are visible by default. In Linux, filenames that start with a dot (`.`) are hidden. You can view them by using the `cmd ls` with the `-a` flag, which stands for "all".

```bash
ls -a
```

### Getting Detailed Information

Another essential `ls` flag is `-l` for "long". This option provides a detailed list of files in a long format. This will show you detailed information, starting from the left: file permissions, number of links, owner name, owner group, file size, timestamp of last modification, and the file or directory name.

```bash
ls -l
```

Here is an example of the output:

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

### Sorting in Reverse Order

Sometimes you may want to change the sort order. The `ls -r command` lists files and directories in reverse alphabetical order. The `linux ls -r` option is particularly handy when you want to see the last items in a long list first.

```bash
ls -r
```

### Combining Command Flags

Commands have flags (also called arguments or options) to add more functionality. As we saw with `-a` and `-l`, you can combine them into a single command like `ls -la`. The order of the flags usually doesn't matter, so `ls -al` would work identically. You can also add the reverse flag: `ls -lar`.

```bash
ls -la
```

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of the `ls` command:

- **[Linux ls Command: Content Listing](https://labex.io/labs/linux-linux-ls-command-content-listing-219205)** - Practice using the `ls` command to efficiently list and analyze file and directory contents. You'll learn various options for detailed listings, hidden file display, human-readable sizes, and sorting techniques to enhance your command-line skills.

This lab will help you apply the concepts in a real scenario and build confidence with directory listing in Linux.

## Quiz Question

What command would you use to see hidden files? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

ls -a
