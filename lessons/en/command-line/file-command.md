---
index: 6
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

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of inspecting file content and properties:

1. **[Linux ls Command: Content Listing](https://labex.io/labs/linux-linux-ls-command-content-listing-219205)** - Learn the Linux `ls` command to efficiently list and analyze file and directory contents, which often precedes or follows using the `file` command to understand what's in your directories.
2. **[Linux cat Command: File Concatenating](https://labex.io/labs/linux-linux-cat-command-file-concatenating-210986)** - Practice viewing and manipulating text files, a common task after identifying a file's type.
3. **[Linux more Command: File Scrolling](https://labex.io/labs/linux-linux-more-command-file-scrolling-214299)** - Enhance your command-line skills for navigating and exploring large text files, building on the ability to identify file types and then inspect their content.

These labs will help you apply the concepts of file inspection and content viewing in real scenarios and build confidence with managing files in Linux.

## Quiz Question

What command can you use to find the file type of a file?

## Quiz Answer

file
