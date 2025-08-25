---
index: 13
lang: "en"
title: "rm (Remove)"
meta_title: "rm (Remove) - Command Line"
meta_description: "Learn how to use the `rm` command in Linux to safely delete files and directories. Understand options like -f, -i, -r, and rmdir. Start your Linux journey!"
meta_keywords: "rm command, delete files Linux, remove directories, Linux tutorial, beginner Linux, rmdir, Linux guide"
---

## Lesson Content

Now, I think we have too many files; let's remove some. To remove files, you can use the `rm` command. The `rm` (remove) command is used to delete files and directories.

```bash
rm file1
```

Take caution when using `rm`; there is no magical trash can from which you can retrieve removed files. Once they are gone, they are gone for good, so be careful.

Fortunately, there are some safety measures in place, so the average user can't just remove a bunch of important files. Write-protected files will prompt you for confirmation before deleting them. If a directory is write-protected, it will also not be easily removed.

Now, if you don't care about any of that, you can absolutely remove a bunch of files.

```bash
rm -f file1
```

The `-f` or force option tells `rm` to remove all files, whether they are write-protected or not, without prompting the user (as long as you have the appropriate permissions).

```bash
rm -i file
```

Adding the `-i` flag, like many of the other commands, will give you a prompt on whether you want to actually remove the files or directories.

```bash
rm -r directory
```

You can't just `rm` a directory by default; you'll need to add the `-r` flag (recursive) to remove all the files and any subdirectories it may have.

You can remove a directory with the `rmdir` command.

```bash
rmdir directory
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of file and directory removal in Linux:

1. **[Linux rm Command: File Removing](https://labex.io/labs/linux-linux-rm-command-file-removing-209741)** - Learn how to use the `rm` command for removing files and directories, including various options like `-r` and `-i`, and practice safe and effective file deletion.
2. **[Organizing Files and Directories](https://labex.io/labs/linux-organizing-files-and-directories-387877)** - Practice essential Linux file management skills, including using `rm` to clean up unnecessary directories, in a practical challenge.

These labs will help you apply the concepts in real scenarios and build confidence with managing files and directories in Linux.

## Quiz Question

How do you remove a file called `myfile`?

## Quiz Answer

rm myfile
