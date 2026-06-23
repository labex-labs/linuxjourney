---
index: 6
lang: "en"
title: "file"
meta_title: "file - Command Line"
meta_description: "Learn the Linux file command with examples for identifying text files, images, scripts, compressed archives, binaries, and MIME types."
meta_keywords: "linux file command, file command, identify file type linux, mime type linux, text file, binary file, archive file"
---

## Lesson Content

In the previous lesson, we learned about `touch`. Let's revisit that for a bit. Did you notice that the filename didn't conform to standard naming conventions, like you've probably seen with other operating systems such as Windows? Normally, you would expect a file called `banana.jpeg` to be a JPEG picture file.

In Linux, filenames aren't required to represent the contents of the file. You can create a file called `funny.gif` that isn't actually a GIF.

To find out what kind of file a file is, you can use the `file` command. It will show you a description of the file's contents.

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

### Why File Extensions Are Not Enough

Linux tools usually do not require a file extension to decide what a file is. A shell script can be named `backup`, a text file can be named `README`, and an image can have the wrong extension. The `file` command inspects the file's contents and metadata to make a better guess.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

### Checking Multiple Files

You can check several files at once:

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

Wildcards also work:

```bash
$ file *
```

### Showing MIME Types

The `-i` option prints MIME-style information, which is useful when working with web files or scripts.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

### Common file Options

- `-i`: Show MIME type information.
- `-b`: Brief mode, omit the filename in output.
- `-L`: Follow symbolic links.
- `-z`: Try to inspect compressed files.

For example:

```bash
$ file -b notes.txt
ASCII text
```

### Common Questions

**Does file rely only on extensions?** No. It primarily inspects file contents and known signatures.

**Can file be wrong?** Yes. It makes an educated guess, especially for unusual or damaged files.

**Why does file say "data"?** The file does not match a more specific known type, or it may be binary data without a recognizable signature.

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
