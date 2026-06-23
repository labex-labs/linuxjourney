---
index: 4
lang: "en"
title: "ls (List Directories)"
meta_title: "ls (List Directories) - Command Line"
meta_description: "Learn the Linux ls command with examples for listing files, hidden files, long format output, human-readable sizes, sorting, and combining options."
meta_keywords: "ls command, linux ls, list files linux, list directories, ls -a, ls -l, ls -lh, ls -r, hidden files"
---

## Lesson Content

Now that we know how to move around the filesystem, how do we figure out what is available to us? The `ls` command lists files and directories so you can inspect your current location or another path.

### Basic Usage of the ls Command

By default, the `ls` command will list the directories and files in your current directory. However, you can also specify a path to list the contents of a different directory.

```bash
$ ls
$ ls /home/pete
```

You can list a specific file too:

```bash
$ ls /etc/hosts
/etc/hosts
```

### Viewing Hidden Files

Not all files in a directory are visible by default. In Linux, filenames that start with a dot (`.`) are hidden. You can view them with the `-a` option, which stands for all.

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

### Getting Detailed Information

Another essential `ls` option is `-l` for long format. It shows file permissions, number of links, owner, group, size, modification time, and name.

```bash
$ ls -l
```

Here is an example of the output:

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

For easier file sizes, add `-h` for human-readable output:

```bash
$ ls -lh
```

### Sorting in Reverse Order

Sometimes you may want to change the sort order. The `-r` option lists files and directories in reverse order.

```bash
$ ls -r
```

You can sort by modification time with `-t`, then reverse it with `-r`:

```bash
$ ls -lt
$ ls -ltr
```

### Combining Command Flags

Commands have flags, also called options, to add more functionality. As we saw with `-a` and `-l`, you can combine them into a single command like `ls -la`. The order of the flags often does not matter, so `ls -al` works the same way.

```bash
$ ls -la
```

Useful combinations include:

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

### Common ls Options

- `-a`: Show all files, including hidden files.
- `-l`: Use long format.
- `-h`: Show human-readable sizes with `-l`.
- `-r`: Reverse the sort order.
- `-t`: Sort by modification time.
- `-S`: Sort by file size.
- `-d`: List the directory itself instead of its contents.

### Common Questions

**Why do some filenames start with a dot?** Dotfiles are hidden by default and often store configuration, such as `.bashrc`.

**How do I list only a directory itself?** Use `ls -d directory/`.

**How do I see the newest files last?** Use `ls -ltr`.

**Why does ls show colors?** Many systems configure `ls` to color file types through an alias or environment setting.

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of the `ls` command:

- **[Linux ls Command: Content Listing](https://labex.io/labs/linux-linux-ls-command-content-listing-219205)** - Practice using the `ls` command to efficiently list and analyze file and directory contents. You'll learn various options for detailed listings, hidden file display, human-readable sizes, and sorting techniques to enhance your command-line skills.

This lab will help you apply the concepts in a real scenario and build confidence with directory listing in Linux.

## Quiz Question

What command would you use to see hidden files? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

ls -a
