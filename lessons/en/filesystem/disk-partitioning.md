---
index: 4
lang: "en"
title: "Disk Partitioning"
meta_title: "Disk Partitioning - The Filesystem"
meta_description: "Learn Linux disk partitioning with the parted command. This guide covers how to view partitions with `sudo parted -l`, create, and resize them. Also introduces gparted, a popular graphical alternative."
meta_keywords: "Linux disk partitioning, parted command, sudo parted -l, gparted, gparted windows alternative, fdisk, disk management, create partition, resize partition, Linux guide"
---

## Lesson Content

This lesson provides a practical guide to managing filesystems by partitioning a disk, such as a USB drive. If you don't have a spare drive, you can still follow along to understand the concepts.

First, we'll need to partition our disk. There are many tools available for this task:

- **fdisk**: A basic command-line partitioning tool; it does not support GPT.
- **parted**: A powerful command-line tool that supports both MBR and GPT partitioning.
- **gparted**: The graphical version of `parted`. For users who prefer a visual interface, `gparted` is an intuitive tool, often considered a great `gparted windows alternative`.
- **gdisk**: Similar to `fdisk`, but it only supports GPT.

We will use `parted` for our examples.

### Listing Existing Partitions

Before making changes, it's crucial to identify your disk and its current layout. A quick way to do this is with the `sudo parted -l` command, which lists the partition tables for all connected block devices.

```bash
sudo parted -l
```

This command helps you find the correct device name, such as `/dev/sdb`, before you begin modifying it.

### Launching Interactive Mode

To start making changes, launch `parted` in interactive mode. Let's assume your target device is `/dev/sdb`.

```bash
sudo parted
```

You will enter the `parted` tool's shell, where you can run commands to manage your device's partitions.

### Selecting a Device

Once inside the `parted` shell, you must select the disk you want to modify. Be very careful to choose the correct one to avoid data loss.

```bash
select /dev/sdb
```

### Viewing the Partition Table

Use the `print` command to display the partition table of the selected disk.

```plaintext
(parted) print
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sdb: 10.7GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type      File system  Flags
 1      1049kB  10.7GB  10.7GB  primary   ext4         boot
```

This output shows available partitions on the device. The **Start** and **End** columns indicate where each partition is located on the disk.

### Creating a Partition

The `mkpart` command creates a new partition. You need to specify the partition type (e.g., `primary`), an optional filesystem type, and the start and end points.

```bash
mkpart primary ext4 1MB 5000MB
```

This command creates a primary partition formatted with ext4, starting at 1MB and ending at 5000MB.

### Resizing a Partition

You can also resize an existing partition with the `resizepart` command. You'll need the partition number and the new end point.

```bash
resizepart 1 8000MB
```

This command resizes partition number 1 to end at the 8000MB mark. Note that this only changes the partition size; you may still need to resize the filesystem itself using other tools (like `resize2fs`).

`parted` is a very powerful tool. Always double-check your commands before executing them to prevent accidental data loss.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux disk partitioning and filesystem management:

1. [Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) - In this lab, you will learn to manage disk partitions and filesystems in Linux. You'll use fdisk to create a new partition, format it with ext4, mount it, configure persistent mounting in /etc/fstab, and create a swap partition, all on a safe secondary virtual disk.

This lab will help you apply the concepts of disk partitioning and filesystem management in a real scenario and build confidence with these essential Linux administration skills.

## Quiz Question

What is the `parted` command to make a partition? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

mkpart
