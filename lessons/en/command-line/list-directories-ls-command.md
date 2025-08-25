---
index: 4
lang: "en"
title: "ls (List Directories)"
meta_title: "ls (List Directories) - Command Line"
meta_description: "Learn how to use the 'ls' command in Linux to list directory contents, view hidden files, and understand file details. Improve your Linux command line skills!"
meta_keywords: "ls command, list directories, Linux tutorial, hidden files, Linux commands, beginner Linux, Linux guide"
---

## Lesson Content

Now that we know how to move around the system, how do we figure out what is available to us? Right now, it's like we are moving around in the dark. Well, we can use the wonderful `ls` command to list directory contents. The `ls` command will list directories and files in the current directory by default; however, you can specify which path you want to list the directories of.

```bash
ls
ls /home/pete
```

`ls` is a quite useful tool; it also shows you detailed information about the files and directories you are looking at.

Also, note that not all files in a directory will be visible. Filenames that start with `.` are hidden. You can view them, however, with the `ls` command and pass the `-a` flag to it (`a` for all).

```bash
ls -a
```

There is also one more useful `ls` flag, `-l` for long. This shows a detailed list of files in a long format. This will show you detailed information, starting from the left: file permissions, number of links, owner name, owner group, file size, timestamp of last modification, and file/directory name.

```bash
ls -l
```

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

Commands have things called flags (or arguments or options, whatever you want to call them) to add more functionality. See how we added `-a` and `-l`; well, you can add them both together with `-la`. The order of the flags determines which order it goes in. Most of the time, this doesn't really matter, so you can also do `ls -al` and it would still work.

```bash
ls -la
```

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of the `ls` command:

- **[Linux ls Command: Content Listing](https://labex.io/labs/linux-linux-ls-command-content-listing-219205)** - Practice using the `ls` command to efficiently list and analyze file and directory contents. You'll learn various options for detailed listings, hidden file display, human-readable sizes, and sorting techniques to enhance your command-line skills.

This lab will help you apply the concepts in a real scenario and build confidence with directory listing in Linux.

## Quiz Question

What command would you use to see hidden files?

## Quiz Answer

ls -a
