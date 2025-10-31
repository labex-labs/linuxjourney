---
index: 10
lang: "en"
title: "cp (Copy)"
meta_title: "cp (Copy) - Command Line"
meta_description: "Master the Linux cp command to copy files and directories. This guide covers essential options like recursive copying (-r), preserving attributes with the cp -p flag, and forcing overwrites with the cp -f flag. Learn how cp -p in Linux helps maintain file metadata."
meta_keywords: "cp command, copy files linux, linux cp -p, cp -p flag, cp -p in linux, cp -f flag, recursive copy, cp -r, linux wildcards, linux command line"
---

## Lesson Content

The `cp` command is the standard tool for copying files and directories in Linux. Its basic syntax is `cp [SOURCE] [DESTINATION]`.

### Basic File Copying

To copy a file, you specify the source file and the destination directory or path.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

In this example, `mycoolfile` is the source file, and `/home/pete/Documents/cooldocs` is the destination directory. You can also copy a file and give it a new name in the destination.

```bash
cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

### Using Wildcards for Bulk Copying

Wildcards are special characters that help you select multiple files based on patterns, providing great flexibility.

- `*`: Matches any sequence of characters.
- `?`: Matches any single character.
- `[]`: Matches any one of the characters enclosed in the brackets.

For example, to copy all JPEG images from your current location to the `Pictures` directory:

```bash
cp *.jpg /home/pete/Pictures
```

### Copying Directories Recursively

If you try to copy a directory using `cp` without any options, you will receive an error. To copy a directory and all of its contents, including subdirectories, you must use the `-r` (recursive) flag.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

This command copies the `Pumpkin` directory and everything inside it to your `Documents` directory.

### Handling File Overwrites

By default, `cp` will overwrite a file at the destination if it has the same name. To prevent accidental data loss, use the `-i` (interactive) flag, which prompts for confirmation before overwriting.

```bash
cp -i mycoolfile /home/pete/Pictures
```

Conversely, if you want to force an overwrite without any prompts, you can use the `cp -f flag`. This is useful in scripts where user interaction is not possible.

```bash
cp -f mycoolfile /home/pete/Pictures
```

### Preserving File Attributes with cp -p

When you copy a file, its metadata, such as modification time and ownership, is typically updated. To preserve these original attributes, the `cp -p` flag is essential. Using `cp -p in linux` ensures that the copy is an exact replica, not just in content but also in its metadata.

The `cp -p flag` is particularly useful for backups or when migrating files where preserving timestamps is critical.

```bash
cp -p mycoolfile /home/pete/backups/
```

This command demonstrates how to use `linux cp -p` to copy `mycoolfile` while preserving its mode, ownership, and timestamps.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of copying files and directories in Linux:

1. **[Linux cp Command: File Copying](https://labex.io/labs/linux-linux-cp-command-file-copying-209744)** - Practice basic usage, advanced options like recursive copying, preserving attributes, and using wildcards to efficiently copy files and directories.
2. **[Organizing Files and Directories](https://labex.io/labs/linux-organizing-files-and-directories-387877)** - Practice essential Linux file management skills by using `cp`, `mv`, and `rm` commands to organize a project structure, move files, and clean up unnecessary directories.

These labs will help you apply the concepts in real scenarios and build confidence with file copying and management in Linux.

## Quiz Question

What flag do you need to specify to copy over a directory?

## Quiz Answer

-r
