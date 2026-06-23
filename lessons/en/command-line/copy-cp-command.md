---
index: 10
lang: "en"
title: "cp (Copy)"
meta_title: "cp (Copy) - Command Line"
meta_description: "Learn the Linux cp command with examples for copying files, directories, multiple files, wildcards, backups, and options like cp -r, cp -i, and cp -p."
meta_keywords: "linux cp command, cp command, copy files linux, cp -r, cp -i, cp -p, cp -a, cp -u, recursive copy, linux wildcards"
---

## Lesson Content

The `cp` command is the standard tool for copying files and directories in Linux. It creates a new copy while leaving the original file in place. Its basic syntax is:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

You can copy one file to another file, one or more files into a directory, or an entire directory tree with the right option.

### Basic File Copying

To copy a file, you specify the source file and the destination directory or path.

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

In this example, `mycoolfile` is the source file, and `/home/pete/Documents/cooldocs` is the destination directory. You can also copy a file and give it a new name in the destination.

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

If the destination is an existing directory, the copied file keeps its original name. If the destination is a filename, `cp` creates a copy with that new name.

### Copy Multiple Files into a Directory

To copy several files into the same directory, list all sources first and put the destination directory last.

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

The final argument must be a directory when you provide more than one source.

### Using Wildcards for Bulk Copying

Wildcards are special characters that help you select multiple files based on patterns, providing great flexibility.

- `*`: Matches any sequence of characters.
- `?`: Matches any single character.
- `[]`: Matches any one of the characters enclosed in the brackets.

For example, to copy all JPEG images from your current location to the `Pictures` directory:

```bash
$ cp *.jpg /home/pete/Pictures
```

You can preview the files that match before copying:

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

### Copying Directories Recursively

If you try to copy a directory using `cp` without any options, you will receive an error. To copy a directory and all of its contents, including subdirectories, you must use the `-r` (recursive) flag.

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

This command copies the `Pumpkin` directory and everything inside it to your `Documents` directory.

You may also see `-R`, which has the same recursive purpose on typical Linux systems:

```bash
$ cp -R website /home/pete/backups/
```

### Handling File Overwrites

By default, `cp` will overwrite a file at the destination if it has the same name. To prevent accidental data loss, use the `-i` (interactive) flag, which prompts for confirmation before overwriting.

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

Conversely, if you want to force an overwrite without prompts, use the `-f` option. This is useful in scripts where user interaction is not possible.

```bash
$ cp -f mycoolfile /home/pete/Pictures
```

Another useful safety option is `-n`, which means "no clobber." It prevents overwriting an existing destination file.

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

### Preserve File Attributes with -p

When you copy a file, its metadata, such as modification time and ownership, is typically updated. To preserve these original attributes, use the `-p` option.

The `cp -p` option is particularly useful for backups or when migrating files where preserving timestamps is important.

```bash
$ cp -p mycoolfile /home/pete/backups/
```

This copies `mycoolfile` while preserving its mode, ownership where permitted, and timestamps.

### Archive Copies with -a

The `-a` option means archive. It is commonly used for backup-style directory copies because it preserves many attributes and copies recursively.

```bash
$ cp -a project/ project-backup/
```

For many everyday backups, `cp -a` is more convenient than combining several options manually.

### Copy Only Newer Files with -u

The `-u` option copies only when the source file is newer than the destination file or when the destination file does not exist.

```bash
$ cp -u *.txt /home/pete/Documents/
```

This is useful when refreshing a folder without rewriting files that are already up to date.

### Common cp Options

Here are the options you will use most often:

- `-r` or `-R`: Copy directories recursively.
- `-i`: Ask before overwriting a file.
- `-f`: Force overwriting by removing the destination first if needed.
- `-n`: Do not overwrite existing files.
- `-p`: Preserve mode, ownership where possible, and timestamps.
- `-a`: Archive mode, useful for preserving directory trees.
- `-u`: Copy only when the source is newer than the destination.
- `-v`: Show each file as it is copied.

### Common Questions

**Why did cp overwrite my file?** By default, `cp` replaces a destination file with the same name. Use `cp -i` to ask first or `cp -n` to avoid overwriting.

**Why can't cp copy a directory?** A directory requires recursive copying. Use `cp -r source-dir destination-dir`.

**What is the difference between cp and mv?** `cp` creates a copy and keeps the original. `mv` moves or renames the original.

**Should I use cp -r or cp -a for backups?** Use `cp -r` for a simple recursive copy. Use `cp -a` when you want a backup-style copy that preserves more file attributes.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of copying files and directories in Linux:

1. **[Linux cp Command: File Copying](https://labex.io/labs/linux-linux-cp-command-file-copying-209744)** - Practice basic usage, advanced options like recursive copying, preserving attributes, and using wildcards to efficiently copy files and directories.
2. **[Organizing Files and Directories](https://labex.io/labs/linux-organizing-files-and-directories-387877)** - Practice essential Linux file management skills by using `cp`, `mv`, and `rm` commands to organize a project structure, move files, and clean up unnecessary directories.

These labs will help you apply the concepts in real scenarios and build confidence with file copying and management in Linux.

## Quiz Question

What flag do you need to specify to copy over a directory?

## Quiz Answer

-r
