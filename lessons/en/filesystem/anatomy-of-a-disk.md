---
index: 3
lang: "en"
title: "Anatomy of a Disk"
meta_title: "Anatomy of a Disk - The Filesystem"
meta_description: "Explore the anatomy of a disk in Linux. This guide explains what component of a disk tells the OS how the disk is partitioned, covering MBR and GPT partition tables, different types of Linux partitions, and how they are organized."
meta_keywords: "disk in linux, linux partitions, types of linux partitions, what component of a disk tells the os how the disk is partitioned, what contains information on how hard drive partitions are organized, MBR, GPT, partition table, filesystem"
---

## Lesson Content

A hard disk in Linux can be subdivided into partitions, which function as individual block devices. You may recall examples like `/dev/sda1` and `/dev/sda2`. Here, `/dev/sda` represents the entire disk, while `/dev/sda1` is the first partition on that disk. Partitions are incredibly useful for separating data. If you need a specific filesystem for a portion of your storage, you can create a new partition for it instead of formatting the entire disk.

### The Partition Table

So, what component of a disk tells the OS how the disk is partitioned? The answer is the **partition table**. This crucial component contains information on how hard drive partitions are organized. The partition table specifies where each partition begins and ends, which partitions are bootable, and what sectors of the disk are allocated to each partition. There are two primary partition table schemes: Master Boot Record (MBR) and GUID Partition Table (GPT).

### Understanding Linux Partitions

Disks are composed of partitions that help us organize our data. You can have multiple partitions on a single disk, but they cannot overlap. Any space on the disk not allocated to a partition is known as free space. The types of Linux partitions available depend on the partition table scheme you use. Inside a partition, you can create a filesystem or dedicate it to other purposes, such as swap space.

### MBR Partitions

The Master Boot Record (MBR) is the traditional partition table standard.

- It supports primary, extended, and logical partitions.
- MBR has a limit of four primary partitions.
- To create more partitions, one primary partition must be designated as an extended partition (only one is allowed per disk). Within this extended partition, you can create multiple logical partitions, which function like any other partition.
- It supports disks up to 2 terabytes in size.

### GPT Partitions

The GUID Partition Table (GPT) is the modern standard for disk partitioning.

- It has only one type of partition, and you can create a large number of them.
- Each partition is assigned a Globally Unique Identifier (GUID).
- GPT is commonly used with UEFI-based booting systems.

### Filesystem Structure

As we learned previously, a filesystem is an organized collection of files and directories. At its core, it consists of a database to manage files and the files themselves. Let's explore its structure in more detail.

- **Boot block**: Located in the first few sectors of a filesystem, this block is not used by the filesystem itself. Instead, it contains information used to boot the operating system. Only one boot block is needed per OS. While other partitions may have boot blocks, they often go unused.
- **Superblock**: This is a single block following the boot block that contains metadata about the filesystem, such as the size of the inode table, the size of logical blocks, and the total size of the filesystem.
- **Inode table**: This is the database that manages files and directories. Each file or directory has a unique entry in the inode table, which stores various attributes about it. We will cover inodes in a dedicated lesson.
- **Data blocks**: This is where the actual content of your files and directories is stored.

Below is an example of a disk using the MBR partition table (labeled as `msdos`). You can see the primary, extended, and logical partitions.

```plaintext
pete@icebox:~$ sudo parted -l
Model: Seagate (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Number  Start   End     Size    Type      File system     Flags
 1      1049kB  6860MB  6859MB  primary   ext4            boot
 2      6861MB  21.5GB  14.6GB  extended
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
 6      7381MB  21.5GB  14.1GB  logical   xfs
```

This second example shows a GPT partition table, which uses unique IDs for its partitions.

```plaintext
Model: Thumb Drive (scsi)
Disk /dev/sdb: 4041MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt

Number  Start   End     Size     File system  Name        Flags
 1      17.4kB  1000MB  1000MB                first
 2      1000MB  4040MB  3040MB                second
```

## Exercise

To reinforce your understanding of disk partitioning and filesystems, we recommend this hands-on lab:

1. **[Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practice creating new partitions, formatting them with filesystems like ext4, mounting them, and configuring persistent mounting in `/etc/fstab`.

This lab will help you apply disk management concepts in real-world scenarios and build confidence with Linux storage.

## Quiz Question

What partition type is used to create more than 4 partitions in the MBR partitioning scheme? (Please answer in a single lowercase English word.)

## Quiz Answer

extended
