---
index: 11
lang: "en"
title: "Inodes"
meta_title: "Inodes - The Filesystem"
meta_description: "Explore the concept of the Linux inode. Learn what an i-node is, how inodes in Linux manage file metadata, and how to check inode usage with `df -i` and `ls -li`."
meta_keywords: "linux inode, inode in linux, i node, inode, inode linux, inode number, filesystem, df -i, ls -li, stat"
---

## Lesson Content

Remember how our filesystem is comprised of all our actual files and a database that manages them? This database is known as the inode table, a fundamental part of how `inode in linux` works.

### What is a Linux Inode

An inode (short for index node) is an entry in this table. Every file and directory has its own `inode`. It describes everything about the file, such as:

- File type (e.g., regular file, directory, character device)
- Owner
- Group
- Access permissions
- Timestamps: mtime (last modification), ctime (last attribute change), atime (last access)
- Number of hard links to the file
- Size of the file
- Number of blocks allocated to the file
- Pointers to the file's data blocks (most important!)

Essentially, an `i node` stores all metadata about the file, except for its name and the actual content.

### Inode Creation and Allocation

When a filesystem is created, space for inodes is also allocated. Algorithms determine how much `inode` space you need based on the disk's volume and other factors. You've probably seen out-of-disk-space errors before. The same can happen with inodes, although it's less common. If you run out of inodes, you cannot create new files. Data storage depends on both the data blocks and the database (the `inode` table).

To see how many inodes are left on your system, use the `df -i` command. This is a crucial check for system administrators managing a large number of small files.

### Viewing Inode Information

Each `linux inode` is identified by a unique number. When a file is created, it's assigned an inode number, often sequentially. However, you might notice a new file getting a lower inode number than older ones. This happens because deleted inode numbers can be reused for new files. To view inode numbers, run `ls -li`:

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

The first field in this command's output is the inode number. You can also see detailed information about a file's `i node` with the `stat` command:

```bash
pete@icebox:~$ stat ~/Desktop/
  File: ‘/home/pete/Desktop/’
  Size: 6               Blocks: 0          IO Block: 4096   directory
Device: 806h/2054d      Inode: 140         Links: 2
Access: (0755/drwxr-xr-x)  Uid: ( 1000/   pete)   Gid: ( 1000/   pete)
Access: 2016-01-20 20:13:50.647435982 -0800
Modify: 2016-01-20 20:13:06.191675843 -0800
Change: 2016-01-20 20:13:06.191675843 -0800
 Birth: -
```

### How an I-Node Points to Data

We know our data is stored on the disk, but it's likely not in one continuous block. This is where the `inode linux` structure becomes essential. Inodes point to the actual data blocks of your files. In a typical filesystem (though implementations vary), each inode contains 15 pointers. The first 12 pointers point directly to data blocks. The 13th pointer points to a block that contains more pointers. The 14th and 15th pointers point to further nested blocks of pointers. This might seem confusing, but this structure allows the `i node` to remain a fixed size while being able to reference files of varying sizes. Small files can be accessed quickly using the direct pointers, while larger files are located through the nested pointers.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of the Linux filesystem and file management:

1. **[Manage Files and Directories in Linux](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835)** - Practice creating, removing, copying, and moving files and directories, and explore creating symbolic and hard links while analyzing inodes.
2. **[Navigate the Filesystem in Linux](https://labex.io/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Learn the fundamental skills to navigate the Linux filesystem using essential shell commands like `pwd`, `cd`, and `ls`.
3. **[Find Files and Commands in Linux](https://labex.io/labs/comptia-find-files-and-commands-in-linux-590834)** - Master essential techniques for locating files and commands in Linux using `find`, `locate`, `whereis`, `which`, and `type`.

These labs will help you apply the concepts in real scenarios and build confidence with Linux filesystem management.

## Quiz Question

How do you see how many inodes are left on your system? (Please answer in English, paying attention to case sensitivity.)

## Quiz Answer

df -i
