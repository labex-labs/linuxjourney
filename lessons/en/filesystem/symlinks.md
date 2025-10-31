---
index: 12
lang: "en"
title: "symlinks"
meta_title: "symlinks - The Filesystem"
meta_description: "Explore Linux symlinks (symbolic links) and hard links. Learn how to create them with the ln command, check the link count in linux with ls, and understand the difference when you ls symlink and hard link outputs."
meta_keywords: "Linux symlinks, hard links, ln command, symbolic links, ls symlink, link count in linux, ls symlinks, ls links, Linux file system, Linux tutorial"
---

## Lesson Content

When you list files in detail, you see a lot of information. Let's look at a previous example of inode information from the `ls -li` command:

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

We've previously glossed over the third field in this output. This field is the link count.

### The Link Count in Linux

The **link count in linux** is the total number of hard links a file has. To understand what this means, we first need to discuss what links are. In Linux, there are two types of links: symbolic links (symlinks) and hard links.

### Understanding Symlinks

In the Windows operating system, you have shortcuts, which are essentially aliases that point to other files. In Linux, the equivalent is a symbolic link, also known as a soft link or **symlink**. A symlink is a special type of file that points to another file or directory by its name.

Let's see this in practice. We'll create a few files and then a symlink.

```bash
pete@icebox:~/Desktop$ echo 'myfile' > myfile
pete@icebox:~/Desktop$ echo 'myfile2' > myfile2
pete@icebox:~/Desktop$ echo 'myfile3' > myfile3

pete@icebox:~/Desktop$ ln -s myfile myfilelink
pete@icebox:~/Desktop$ ls -li
total 12
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
```

Here, we've created a symbolic link named `myfilelink` that points to `myfile`. When you use `ls` to view an `ls symlink`, it's clearly identified by the `l` at the beginning of the permissions string and the `->` symbol pointing to the target. Notice that the symlink has its own unique inode number (93403). Because symlinks point to filenames rather than inodes, they can span across different filesystems.

### Understanding Hard Links

The other type of link is a hard link. A hard link creates another file entry that points directly to the same inode as the original file.

Let's create a hard link for `myfile2`:

```bash
pete@icebox:~/Desktop$ ln myfile2 myhardlink
pete@icebox:~/Desktop$ ls -li
total 16
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myhardlink
```

Notice that `myhardlink` shares the exact same inode number (93401) as `myfile2`. The link count for both files has also increased to 2. This is because two file entries now point to the same inode. If you modify the contents of `myfile2`, the changes will be reflected in `myhardlink`, and vice versa. If you delete `myfile2`, the file's data will still be accessible through `myhardlink`. The inode and its data are only removed from the disk when the link count drops to zero. Because hard links point to inodes, which are unique within a single filesystem, they cannot span across different filesystems.

### Creating Symlinks and Hard Links

You can create both types of links using the `ln` command. The syntax is straightforward.

To create a symbolic link, use the `-s` flag:

```bash
ln -s /path/to/original /path/to/link
```

To create a hard link, omit the `-s` flag:

```bash
ln /path/to/original /path/to/link
```

Using `ls symlinks` or general `ls links` commands with the `-l` option is essential for managing and identifying these different file types.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of file management, links, and inodes:

1. **[Manage Files and Directories in Linux](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835)** - Practice creating, copying, moving, and removing files and directories, and specifically learn about symbolic and hard links, and how to analyze inodes.
2. **[Navigate the Filesystem in Linux](https://labex.io/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Master essential commands like `pwd`, `cd`, and `ls` to efficiently move through the Linux filesystem, a foundational skill for understanding where files and their inodes reside.

These labs will help you apply the concepts of file management and links in real scenarios and build confidence with the Linux filesystem.

## Quiz Question

What is the command and its primary option used to create a symlink? Your answer must be in English and is case-sensitive. Please include the space between the command and the option.

## Quiz Answer

ln -s
