---
index: 11
lang: "en"
title: "mv (Move)"
meta_title: "mv (Move) - Command Line"
meta_description: "Learn how to use the Linux mv command to move and rename files/directories. Understand its options and prevent overwrites. Start your Linux journey!"
meta_keywords: "mv command, Linux mv, move files Linux, rename files Linux, Linux tutorial, beginner, Linux guide"
---

## Lesson Content

Used for moving files and also renaming them. Quite similar to the `cp` command in terms of flags and functionality.

You can rename files like this:

```bash
mv oldfile newfile
```

Or you can actually move a file to a different directory:

```bash
mv file2 /home/pete/Documents
```

And move more than one file:

```bash
mv file_1 file_2 /somedirectory
```

You can rename directories as well:

```bash
mv directory1 directory2
```

Like `cp`, if you `mv` a file or directory, it will overwrite anything in the same directory. So you can use the `-i` flag to prompt you before overwriting anything.

```bash
mv -i directory1 directory2
```

Let’s say you did want to `mv` a file to overwrite the previous one. You can also make a backup of that file, and it will just rename the old version with a `~`.

```bash
mv -b directory1 directory2
```

## Exercise

Practice makes perfect! Hands-on experience is crucial for mastering Linux commands like `mv`. These labs will help you solidify your understanding of moving and renaming files and directories in a real environment:

1. **[Linux mv Command: File Moving and Renaming](https://labex.io/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Practice using the `mv` command to move and rename files and directories, including understanding its various options and behaviors.
2. **[Organizing Files and Directories](https://labex.io/labs/linux-organizing-files-and-directories-387877)** - Apply your knowledge of `mv` (along with `cp` and `rm`) in a practical challenge to organize a project structure, move files, and clean up directories.

These labs will help you apply the concepts in real scenarios and build confidence with file and directory management using the `mv` command.

## Quiz Question

How do you rename a file called `cat` to `dog`?

## Quiz Answer

mv cat dog
