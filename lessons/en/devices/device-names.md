---
index: 3
lang: "en"
title: "Device Names"
meta_title: "Device Names - Devices"
meta_description: "Learn Linux device names like SCSI (sd), pseudo, and PATA (hd) devices. Understand /dev/sda, /dev/null, and more in this beginner-friendly guide."
meta_keywords: "Linux device names, /dev, SCSI devices, pseudo devices, PATA devices, Linux tutorial, beginner Linux, device files"
---

## Lesson Content

Here are the most common device names that you will encounter:

### SCSI Devices

If you have any sort of mass storage on your machine, chances are it is using the SCSI (pronounced "scuzzy") protocol. SCSI stands for Small Computer System Interface; it is a protocol used to allow communication between disks, printers, scanners, and other peripherals and your system. You may have heard of SCSI devices, which aren't actually in use in modern systems; however, our Linux systems correspond SCSI disks with hard disk drives in `/dev`. They are represented by a prefix of `sd` (SCSI disk):

Common SCSI device files:

- `/dev/sda` - First hard disk
- `/dev/sdb` - Second hard disk
- `/dev/sda3` - Third partition on the first hard disk

### Pseudo Devices

As we discussed earlier, pseudo devices aren't really physically connected to your system. Most common pseudo devices are character devices:

- `/dev/zero` - accepts and discards all input, produces a continuous stream of NULL (zero value) bytes
- `/dev/null` - accepts and discards all input, produces no output
- `/dev/random` - produces random numbers

### PATA Devices

Sometimes in older systems, you may see hard drives being referred to with an `hd` prefix:

- `/dev/hda` - First hard disk
- `/dev/hdd2` - Second partition on 4th hard disk

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux device names and storage management:

1. **[Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practice creating, formatting, and mounting partitions, which directly involves working with device names.
2. **[Explore Hardware Devices in Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)** - Learn to identify and inspect various hardware devices and their associated names within a Linux environment.

These labs will help you apply the concepts in real scenarios and build confidence with managing storage and understanding hardware in Linux.

## Quiz Question

What would commonly be the device name for the first partition on the second SCSI disk?

## Quiz Answer

sdb1
