---
index: 4
lang: "en"
title: "Disk Partitioning"
meta_title: "Disk Partitioning - The Filesystem"
meta_description: "Learn disk partitioning in Linux using parted. Understand how to partition, select, view, and resize disks. Get started with this beginner-friendly guide!"
meta_keywords: "Linux disk partitioning, parted command, fdisk, gparted, Linux tutorial, beginner Linux, disk management, Linux guide"
---

## Lesson Content

Let's do some practical stuff with filesystems by working through the process on a USB drive. If you don't have one, no worries, you can still follow along these next couple of lessons.

First, we'll need to partition our disk. There are many tools available to do this:

- fdisk - basic command-line partitioning tool; it does not support GPT
- parted - this is a command-line tool that supports both MBR and GPT partitioning
- gparted - this is the GUI version of parted
- gdisk - fdisk, but it does not support MBR, only GPT

Let's use parted to do our partitioning. Let's say I connect the USB device and we see the device name is /dev/sdb2.

### Launch parted

```bash
sudo parted
```

You'll be entered into the parted tool; here you can run commands to partition your device.

### Select the device

```bash
select /dev/sdb2
```

To select the device you'll be working with, select it by its device name.

### View current partition table

```plaintext
(parted) print
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

Here you will see the available partitions on the device. The **start** and **end** points are where the partitions take up space on the hard drive; you'll want to find a good start and end location for your partitions.

### Partition the device

```bash
mkpart primary 123 4567
```

Now just choose a start and end point and make the partition; you'll need to specify the type of partition depending on what table you used.

### Resize a partition

You can also resize a partition if you don't have any space.

```bash
resize 2 1245 3456
```

Select the partition number and then the start and end points of where you want to resize it to.

Parted is a very powerful tool, and you should be careful when partitioning your disks.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux disk partitioning and filesystem management:

1.  [Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) - In this lab, you will learn to manage disk partitions and filesystems in Linux. You'll use fdisk to create a new partition, format it with ext4, mount it, configure persistent mounting in /etc/fstab, and create a swap partition, all on a safe secondary virtual disk.

This lab will help you apply the concepts of disk partitioning and filesystem management in a real scenario and build confidence with these essential Linux administration skills.

## Quiz Question

What is the parted command to make a partition?

## Quiz Answer

mkpart
