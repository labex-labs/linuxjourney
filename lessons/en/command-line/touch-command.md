---
index: 5
lang: "en"
title: "touch"
meta_title: "touch - Command Line"
meta_description: "Learn how to use the linux touch command to create files and manage timestamps. This guide covers the touch command in linux, including options like linux touch -r and touch -d."
meta_keywords: "linux touch, touch command in linux, bash touch, touch -d linux, linux touch -r, create files, update timestamps, file management, linux commands"
---

## Lesson Content

The `touch` command is a standard utility on Unix-like operating systems. While its primary purpose is to change file timestamps, it is also commonly used to create new, empty files. Let's explore how the `linux touch` command works.

### Creating New Files

The simplest way to create an empty file is by using the `touch` command followed by a filename. If the file does not exist, `touch` will create it for you. This is a fundamental `bash touch` operation for scripting and daily tasks.

```bash
touch mysuperduperfile
```

After running this command, a new empty file named `mysuperduperfile` will appear in your current directory. You can create multiple files at once by listing their names.

```bash
touch file1.txt file2.txt file3.log
```

### Updating File Timestamps

The original function of the `touch command in linux` is to update the access and modification timestamps of a file or directory. If you use `touch` on an existing file, it will update its timestamps to the current time.

You can verify this by using `ls -l` to check a file's timestamp, running `touch` on it, and then checking again.

```bash
# Check the original timestamp
ls -l mysuperduperfile

# Update the timestamp
touch mysuperduperfile

# Check the new timestamp
ls -l mysuperduperfile
```

### Advanced Timestamp Control

The `linux touch` command also provides options for more precise timestamp manipulation.

#### Using a Reference File

The `linux touch -r` option allows you to set a file's timestamp to match that of another file (a reference file). This is useful for synchronizing timestamps across related files.

```bash
# Set file2.txt's timestamp to match file1.txt's timestamp
touch -r file1.txt file2.txt
```

#### Setting a Specific Date

With the `touch -d` option, you can set a file's timestamp to a specific date and time. The `touch -d linux` functionality accepts various string formats for the date.

```bash
# Set the timestamp to a specific date and time
touch -d "2023-01-01 12:30:00" mysuperduperfile
```

Mastering `touch` is a great step in learning to manage your file system efficiently from the command line.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of creating and managing file system objects:

1. **[Linux mkdir Command: Directory Creating](https://labex.io/labs/linux-linux-mkdir-command-directory-creating-209739)** - Learn how to use the `mkdir` command in Linux to create directories, set permissions, and organize your file system. This will help you understand the broader concept of creating new items in the file system.
2. **[Setting Up a New Project Structure](https://labex.io/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts of file system creation and organization in real scenarios and build confidence with Linux commands.

## Quiz Question

How do you create a file called `myfile`? Please answer using only the English command, paying attention to case sensitivity.

## Quiz Answer

touch myfile
