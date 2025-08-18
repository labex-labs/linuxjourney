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

1. Create a new file.
2. Note the timestamp.
3. Touch the file and check the timestamp once again.

## Quiz Question

How do you create a file called `myfile`?

## Quiz Answer

touch myfile
