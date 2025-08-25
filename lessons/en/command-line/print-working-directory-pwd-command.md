---
index: 2
lang: "en"
title: "pwd (Print Working Directory)"
meta_title: "pwd (Print Working Directory) - Command Line"
meta_description: "Learn how to use the 'pwd' command in Linux to print your current working directory. Understand Linux filesystem paths and navigation for beginners."
meta_keywords: "pwd command, Linux directory, current directory, Linux path, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Everything in Linux is a file. As you journey deeper into Linux, you'll understand this, but for now, just keep that in mind. Every file is organized in a hierarchical directory tree. The first directory in the filesystem is aptly named the root directory. The root directory has many folders and files, which can store more folders and files, etc. Here is an example of what the directory tree looks like:

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

The location of these files and directories are referred to as paths. If you had a folder named `home` with a folder inside of it named `pete` and another folder in that folder called `Movies`, that path would look like this: `/home/pete/Movies`. Pretty simple, huh?

Navigation of the filesystem, much like real life, is helpful if you know where you are and where you are going. To see where you are, you can use the `pwd` command. This command means "print working directory" and it just shows you which directory you are in. Note that the path stems from the root directory.

```bash
pwd
```

Where are you? Where am I? Give it a try.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux file system navigation and identifying your current location:

1. **[Linux pwd Command: Directory Displaying](https://labex.io/labs/linux-linux-pwd-command-directory-displaying-209734)** - This lab provides a focused overview and practical usage of the `pwd` command, directly aligning with the lesson's introduction to finding your current directory.
2. **[Linux Directory Navigation](https://labex.io/labs/linux-directory-navigation-387844)** - Put your basic Linux command-line skills to the test by navigating through various directories, solidifying your understanding of paths and the file system structure.
3. **[Linux cd Command: Directory Changing](https://labex.io/labs/linux-linux-cd-command-directory-changing-209733)** - Learn to efficiently navigate your file system using the `cd` command, understanding different techniques for changing directories and exploring the file structure.

These labs will help you apply the concepts of file system hierarchy and navigation in real scenarios and build confidence with essential Linux commands.

## Quiz Question

How do I find what directory you are currently in?

## Quiz Answer

pwd
