---
index: 5
lang: "en"
title: "touch"
meta_title: "touch - Command Line"
meta_description: "Learn the Linux touch command with examples for creating empty files, updating timestamps, setting dates, using reference files, and avoiding overwrites."
meta_keywords: "linux touch command, touch command, create file linux, update timestamp linux, touch -d, touch -r, touch -c"
---

## Lesson Content

The `touch` command is a standard utility on Unix-like operating systems. While its primary purpose is to change file timestamps, it is also commonly used to create new, empty files.

The basic syntax is:

```bash
touch [OPTIONS] FILE...
```

### Creating New Files

The simplest way to create an empty file is to use `touch` followed by a filename. If the file does not exist, `touch` creates it.

```bash
$ touch mysuperduperfile
```

After running this command, a new empty file named `mysuperduperfile` will appear in your current directory. You can create multiple files at once by listing their names.

```bash
$ touch file1.txt file2.txt file3.log
```

This is useful when setting up a project structure or creating placeholder files before adding content.

### Updating File Timestamps

The original function of `touch` is to update the access and modification timestamps of a file or directory. If you use `touch` on an existing file, it updates its timestamps to the current time.

You can verify this by using `ls -l` to check a file's timestamp, running `touch` on it, and then checking again.

```bash
# Check the original timestamp
$ ls -l mysuperduperfile

# Update the timestamp
$ touch mysuperduperfile

# Check the new timestamp
$ ls -l mysuperduperfile
```

### Advanced Timestamp Control

The `touch` command also provides options for more precise timestamp manipulation.

Use a reference file with `-r` to copy timestamps from one file to another.

```bash
$ touch -r file1.txt file2.txt
```

Set a specific date and time with `-d`:

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

Use `-c` when you want to update a file only if it already exists. With `-c`, `touch` will not create a missing file.

```bash
$ touch -c existing-file.txt
```

### Common touch Options

- `-a`: Change only the access time.
- `-m`: Change only the modification time.
- `-c`: Do not create the file if it does not exist.
- `-d "DATE"`: Use a specific date string.
- `-r FILE`: Use another file's timestamp as a reference.
- `-t STAMP`: Use a timestamp in a compact numeric format.

For example, this changes only the modification time:

```bash
$ touch -m notes.txt
```

### Common Questions

**Does touch add text to a file?** No. `touch` creates an empty file or updates timestamps. Use an editor, `echo`, or `cat` to add text.

**Will touch overwrite an existing file?** No. It updates timestamps but does not replace file contents.

**Why use touch in scripts?** It is a quick way to ensure a file exists or to mark that a task happened at a certain time.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of creating and managing file system objects:

1. **[Linux mkdir Command: Directory Creating](https://labex.io/labs/linux-linux-mkdir-command-directory-creating-209739)** - Learn how to use the `mkdir` command in Linux to create directories, set permissions, and organize your file system. This will help you understand the broader concept of creating new items in the file system.
2. **[Setting Up a New Project Structure](https://labex.io/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts of file system creation and organization in real scenarios and build confidence with Linux commands.

## Quiz Question

How do you create a file called `myfile`? Please answer using only the English command, paying attention to case sensitivity.

## Quiz Answer

touch myfile
