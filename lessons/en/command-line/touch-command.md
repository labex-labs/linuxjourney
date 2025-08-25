---
index: 5
lang: "en"
title: "touch"
meta_title: "touch - Command Line"
meta_description: "Learn how to use the Linux touch command to create new files and update timestamps. This beginner-friendly guide helps you understand file management."
meta_keywords: "touch command, create files, Linux tutorial, file timestamps, Linux for beginners, Linux guide, basic commands"
---

## Lesson Content

Let's learn how to make some files. A very simple way is to use the `touch` command. `touch` allows you to create new empty files.

```bash
touch mysuperduperfile
```

And boom, new file!

`touch` is also used to change timestamps on existing files and directories. Give it a try: do an `ls -l` on a file and note the timestamp, then `touch` that file, and it will update the timestamp.

There are many other ways to create files that involve other things like redirection and text editors, but we'll get to that in the Text Manipulation course.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of creating and managing file system objects:

1. **[Linux mkdir Command: Directory Creating](https://labex.io/labs/linux-linux-mkdir-command-directory-creating-209739)** - Learn how to use the `mkdir` command in Linux to create directories, set permissions, and organize your file system. This will help you understand the broader concept of creating new items in the file system.
2. **[Setting Up a New Project Structure](https://labex.io/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts of file system creation and organization in real scenarios and build confidence with Linux commands.

## Quiz Question

How do you create a file called `myfile`?

## Quiz Answer

touch myfile
