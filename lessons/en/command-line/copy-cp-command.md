---
index: 10
lang: "en"
title: "cp (Copy)"
meta_title: "cp (Copy) - Command Line"
meta_description: "Learn how to use the Linux cp command for copying files and directories. Understand options like -r and wildcards. Start your Linux journey today!"
meta_keywords: "cp command, copy files Linux, Linux tutorial, beginner Linux, cp -r, Linux wildcards, Linux guide"
---

## Lesson Content

Let’s start making some copies of these files. Much like copying and pasting files in other operating systems, the shell gives us an even simpler way of doing that.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile` is the file you want to copy, and `/home/pete/Documents/cooldocs` is where you are copying the file to.

You can copy multiple files and directories, as well as use wildcards. A wildcard is a character that can be substituted for a pattern-based selection, giving you more flexibility with searches. You can use wildcards in every command for more flexibility.

- `*` the wildcard of wildcards, it's used to represent all single characters or any string.
- `?` used to represent one character
- `[]` used to represent any character within the brackets

```bash
cp *.jpg /home/pete/Pictures
```

This will copy all files with the `.jpg` extension in your current directory to the `Pictures` directory.

A useful command is to use the `-r` flag; this will recursively copy the files and directories within a directory.

Try to do a `cp` on a directory that contains a couple of files to your `Documents` directory. Didn’t work, did it? Well, that’s because you’ll need to copy over the files and directories inside as well with the `-r` command.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

One thing to note, if you copy a file over to a directory that has the same filename, the file will be overwritten with whatever you are copying over. This is no bueno if you have a file that you don’t want to get accidentally overwritten. You can use the `-i` flag (interactive) to prompt you before overwriting a file.

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

Copy over a couple of files; be careful not to overwrite anything important.

For hands-on practice with the `cp` command, try this interactive lab:

- [Linux cp Command: File Copying](https://labex.io/labs/linux-linux-cp-command-file-copying-209744)

## Quiz Question

What flag do you need to specify to copy over a directory?

## Quiz Answer

-r
