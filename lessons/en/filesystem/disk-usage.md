---
index: 9
lang: "en"
title: "Disk Usage"
meta_title: "Disk Usage - The Filesystem"
meta_description: "Learn to check Linux disk usage and free space with the df and du commands. This guide covers how to analyze disk space, including inode usage with df -i linux, and find which files are taking up space."
meta_keywords: "df command, du command, Linux disk usage, check free space, df -i linux, disk management, Linux tutorial, disk utilization, filesystem usage"
---

## Lesson Content

Managing disk space is a fundamental task for any Linux user or administrator. Two essential commands for this purpose are `df` and `du`. Let's explore how to use them to monitor your disk utilization effectively.

### Checking Filesystem Space with df

The `df` (disk free) command reports the amount of disk space used and available on your currently mounted filesystems. It provides a high-level overview of your storage.

To get a report in a human-readable format (e.g., GB, MB, KB), use the `-h` flag:

```bash
pete@icebox:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

This output shows the filesystem device, total size, used space, available space, the percentage of use, and where it is mounted.

### Analyzing Inode Usage

Besides block space, filesystems also use inodes to store metadata about files (like permissions, ownership, and location). On rare occasions, you can run out of inodes even if you have free disk space. To check inode usage, you can use the `df -i` command. Running `df -i` in Linux gives you a clear picture of inode allocation.

```bash
pete@icebox:~$ df -i
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      4128768 128768 4000000    4% /
```

### Summarizing Directory Usage with du

When you notice a disk is getting full, you'll want to identify which files or directories are consuming the most space. For this task, the `du` (disk usage) command is the perfect tool.

Running `du` without arguments shows the disk usage for each subdirectory in your current location. Using the `-h` flag provides a human-readable summary:

```bash
du -h
```

You can also specify a path, like `du -h /home/pete`, to analyze a specific directory. Running it on the root directory (`du -h /`) can produce a lot of output, so it's often better to check specific directories you suspect are large.

### df vs du A Quick Summary

The syntax for `df` and `du` is so similar that it can be easy to mix them up. Here’s a simple way to remember the difference:

- Use `df` to check how much **d**isk is **f**ree on your filesystems.
- Use `du` to check the **d**isk **u**sage of specific files and directories.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of disk space management and utilization in Linux:

1. **[Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practice creating, formatting, and mounting filesystems, which are the underlying structures reported by `df` and `du`.
2. **[Create and Activate a Swap File in Linux](https://labex.io/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Learn to manage virtual memory on disk, a critical aspect of system resource management that impacts disk space.

These labs will help you apply the concepts in real scenarios and build confidence with managing disk resources.

## Quiz Question

What command is used to show how much space is free on your disk? Please answer in lowercase English letters.

## Quiz Answer

df
