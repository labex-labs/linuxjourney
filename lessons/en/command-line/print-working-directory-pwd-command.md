---
lesson_id: "print-working-directory-pwd-command"
course_id: "command-line"
lang: "en"
order_index: 2
title: "pwd (Print Working Directory)"
description: "Learn how to use pwd to identify your current location in the Linux filesystem."
meta_title: "pwd (Print Working Directory) - Command Line"
meta_description: "Learn the Linux pwd command, what print working directory means, and how absolute paths show your current location in the filesystem."
meta_keywords: "pwd command, linux pwd, print working directory, current directory linux, absolute path, linux filesystem, directory tree"
---

In Linux, files and directories are organized in a hierarchy called the filesystem. Before you can move around confidently, you need to know where you are. The `pwd` command answers that question by printing your current working directory.

## The Directory Tree in Linux

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

:::single-choice{#identify-root-subdirectories}
In the directory tree above, how are `home` and `etc` related to `/`?

::option[They are subdirectories that branch from `/`.]{#root-subdirectories .correct explanation="Both directories appear directly below `/` in the tree. The filesystem branches into subdirectories from its root."}
::option[They are files stored inside the `bin` directory.]{#files-inside-bin explanation="The tree places `home` and `etc` alongside `bin`, not inside it. They are directories rather than files in this example."}
::option[They are alternate names for the root directory.]{#alternate-root-names explanation="Linux has one filesystem root represented by `/`. `home` and `etc` are directories beneath it."}
:::

## Understanding File Paths

The location of any file or directory is described by its path. A path is a sequence of directories that leads from a starting point to a specific destination.

For example, if you have a folder named `pete` inside `/home`, and a `Movies` folder inside `pete`, the full path is:

```plaintext
/home/pete/Movies
```

A path that starts with `/` is an absolute path because it starts at the root directory. A path such as `Movies` is relative because it depends on your current location.

:::single-choice{#recognize-absolute-path}
What makes `/home/pete/Movies` an absolute path?

::option[It contains several directory names separated by `/`.]{#contains-directories explanation="Both absolute and relative paths can contain several directory names. The starting point, not the number of names, determines the path type."}
::option[It ends at a directory named `Movies`.]{#ends-with-movies explanation="The destination name does not determine whether a path is absolute. An absolute path is identified by its root starting point."}
::option[It starts at root with a leading `/`.]{#starts-at-root .correct explanation="An absolute path starts from the root directory. The leading `/` shows that starting point."}
:::

## What is the Full Form of PWD in Linux?

The full form of `pwd` is "print working directory." Your working directory is the directory where your shell is currently located. Commands that use relative paths start from this location.

:::single-choice{#expand-pwd-name}
What does `pwd` stand for?

::option[Print working directory]{#print-working-directory .correct explanation="The name describes exactly what the command does: it prints the shell's current working directory."}
::option[Present working directory]{#present-working-directory explanation="The current location can be called the present directory in ordinary speech, but that is not the expansion of `pwd`."}
::option[Print whole directory]{#print-whole-directory explanation="`pwd` reports the current directory's path. It does not print the directory's entire contents."}
:::

## Using the pwd Command

To find your current directory, type `pwd` and press Enter.

```bash
$ pwd
/home/pete
```

The output is an absolute path. In this example, the shell is currently in the `pete` user's home directory.

The exact output may be different on your system because your username, home directory, and current location may differ. The `pwd` command only prints information; it does not change your working directory. By contrast, `cd` changes the directory where your shell is located.

:::single-choice{#check-location-without-changing-it}
Which action checks your current directory without changing it?

::option[Run `cd` and read the directory it moves to.]{#run-cd explanation="The `cd` command changes the working directory. It does not meet the requirement to check your location without changing it."}
::option[Enter `/home/pete` and use the path as a command.]{#run-path explanation="An absolute path identifies a location, but the path by itself is not the command that reports your current directory."}
::option[Run `pwd` and read the absolute path it prints.]{#run-pwd .correct explanation="`pwd` reports the shell's current location without moving it. This makes it safe to use whenever you need to confirm where you are."}
:::

## Why pwd is Useful

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

To reinforce your understanding of Linux filesystem navigation and identifying your current location, try these hands-on labs:

1. **[Linux pwd Command: Directory Displaying](https://labex.io/labs/linux-linux-pwd-command-directory-displaying-209734)** - This lab provides a focused overview and practical usage of the `pwd` command, directly aligning with the lesson's introduction to finding your current directory.
2. **[Linux Directory Navigation](https://labex.io/labs/linux-directory-navigation-387844)** - Put your basic Linux command-line skills to the test by navigating through various directories, solidifying your understanding of paths and the file system structure.
3. **[Linux cd Command: Directory Changing](https://labex.io/labs/linux-linux-cd-command-directory-changing-209733)** - Learn to efficiently navigate your file system using the `cd` command, understanding different techniques for changing directories and exploring the file structure.

## Summary

You can now use `pwd` to identify your current location in the Linux filesystem.

1. Recognize the root of the directory tree.
2. Distinguish an absolute path from a relative path.
3. Explain what `pwd` means and what it reports.
4. Check your working directory without changing it.
