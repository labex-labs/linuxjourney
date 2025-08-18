---
lang: "en"
title: "file"
meta_title: "file - Command Line"
meta_description: "Learn how to use the Linux 'file' command to identify file types and contents. Understand Linux file naming conventions with this beginner-friendly guide."
meta_keywords: "Linux file command, identify file type, Linux tutorial, file naming, beginner Linux, Linux guide"
---

## Lesson Content

In the previous lesson, we learned about `touch`. Let's revisit that for a bit. Did you notice that the filename didn't conform to standard naming conventions, like you've probably seen with other operating systems such as Windows? Normally, you would expect a file called `banana.jpeg` to be a JPEG picture file.

In Linux, filenames aren't required to represent the contents of the file. You can create a file called `funny.gif` that isn't actually a GIF.

To find out what kind of file a file is, you can use the `file` command. It will show you a description of the file's contents.

```bash
file banana.jpg
```

## Exercise

Run the `file` command on a few different directories and files and note the output.

## Quiz Question

What command can you use to find the file type of a file?

## Quiz Answer

file
