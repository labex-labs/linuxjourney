---
lang: "en"
title: "Creating Filesystems"
meta_title: "Creating Filesystems - The Filesystem"
meta_description: "Learn how to create filesystems on Linux using mkfs. This beginner-friendly guide covers ext4 and disk partitioning. Start your Linux journey!"
meta_keywords: "mkfs, create filesystem, ext4, Linux partitioning, Linux tutorial, beginner Linux, disk management, Linux guide"
---

## Lesson Content

Now that you've actually partitioned a disk, let's create a filesystem!

```bash
sudo mkfs -t ext4 /dev/sdb2
```

Simple as that! The **mkfs** (make filesystem) tool allows us to specify the type of filesystem we want and where we want it. You'll only want to create a filesystem on a newly partitioned disk or if you are repartitioning an old one. You'll most likely leave your filesystem in a corrupted state if you try to create one on top of an existing one.

## Exercise

Make an ext4 filesystem on the USB drive.

## Quiz Question

What command is used to create a filesystem?

## Quiz Answer

mkfs
