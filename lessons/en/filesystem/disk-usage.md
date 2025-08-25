---
index: 9
lang: "en"
title: "Disk Usage"
meta_title: "Disk Usage - The Filesystem"
meta_description: "Learn how to check disk usage and free space in Linux using the df and du commands. Understand their differences and when to use each. Linux disk management tutorial."
meta_keywords: "df command, du command, Linux disk usage, check free space, Linux tutorial, beginner Linux, disk management, Linux guide"
---

## Lesson Content

There are a few tools you can use to see the utilization of your disks:

```bash
pete@icebox:~$ df -h
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

The `df` command shows you the utilization of your currently mounted filesystems. The `-h` flag gives you a human-readable format. You can see what the device is and how much capacity is used and available.

Let's say your disk is getting full and you want to know what files or directories are taking up that space; for that, you can use the **du** command.

```bash
du -h
```

This shows you the disk usage of the current directory you are in. You can take a peek at the root directory with `du -h /`, but that can get a little cluttered.

Both of these commands are so similar in syntax it can be hard to remember which one to use. To check how much of your **disk** is **free**, use `df`. To check **disk usage**, use `du`.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of disk space management and utilization in Linux:

1. **[Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practice creating, formatting, and mounting filesystems, which are the underlying structures reported by `df` and `du`.
2. **[Create and Activate a Swap File in Linux](https://labex.io/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Learn to manage virtual memory on disk, a critical aspect of system resource management that impacts disk space.

These labs will help you apply the concepts in real scenarios and build confidence with managing disk resources.

## Quiz Question

What command is used to show how much space is free on your disk?

## Quiz Answer

df
