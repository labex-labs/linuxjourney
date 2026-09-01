---
lesson_id: "anatomy-of-a-disk"
course_id: "filesystem"
lang: "en"
order_index: 3
title: "Anatomy of a Disk"
description: "Learn how block devices, partition tables, partitions, and filesystems form distinct storage layers."
meta_title: "Anatomy of a Disk - The Filesystem"
meta_description: "Explore the anatomy of a disk in Linux. This guide explains what component of a disk tells the OS how the disk is partitioned, covering MBR and GPT partition tables, different types of Linux partitions, and how they are organized."
meta_keywords: "disk in linux, linux partitions, types of linux partitions, what component of a disk tells the os how the disk is partitioned, what contains information on how hard drive partitions are organized, MBR, GPT, partition table, filesystem"
---

A storage device is exposed as a block device, such as `/dev/sda` or `/dev/nvme0n1`. It can contain a partition table, whose entries describe regions exposed as child block devices. A partition can then hold a filesystem, swap signature, RAID member, encryption container, logical-volume physical volume, or another data format.

These layers are independent: not every disk has a partition table, not every partition contains a filesystem, and a filesystem can reside on a logical volume or whole device.

## Partition Tables and Boundaries

A partition table records start positions, lengths, type identifiers, and scheme-specific attributes. The kernel reads it to create partition block devices such as `/dev/sda1` or `/dev/nvme0n1p1`.

Partition boundaries must not overlap in ordinary layouts. Space outside all entries is unallocated from the partition table's perspective, though it can still contain old signatures or data. Changing a table does not automatically move filesystem contents to match new boundaries.

:::single-choice{#anatomy-disk-partition-table-role} What tells the operating system where disk partitions begin and end?

::option[The current shell's working directory.]{#anatomy-disk-shell-directory explanation="A shell pathname has no role in on-disk partition boundaries."}
::option[The disk's partition table.]{#anatomy-disk-table-boundaries .correct explanation="Partition entries describe regions that the kernel can expose as child block devices."}
::option[The user account's primary group.]{#anatomy-disk-user-group explanation="Account credentials do not define disk geometry or partition layout."}
:::

## MBR Partitioning

The legacy DOS/MBR scheme stores its primary table in the first logical sector. It has four primary table entries. One entry can describe an extended partition that acts as a container for a linked series of logical partitions, providing more than four usable regions.

With 32-bit sector addresses and 512-byte logical sectors, MBR reaches a commonly cited limit of about 2 TiB. Exact addressability depends on sector size and tool support. MBR also lacks GPT's redundant header and table copies and per-partition GUIDs.

:::single-choice{#anatomy-disk-mbr-more-than-four} Which MBR construct allows more than four usable partitions?

::option[A journal partition containing more primary entries.]{#anatomy-disk-mbr-journal explanation="Filesystem journaling is unrelated to the four-entry MBR table."}
::option[An extended partition containing logical partitions.]{#anatomy-disk-mbr-extended .correct explanation="One primary entry can define an extended container, within which logical partitions are linked."}
::option[A filesystem superblock that renumbers the entries.]{#anatomy-disk-mbr-superblock explanation="A filesystem's metadata does not expand the disk partition table."}
:::

## GPT Partitioning

The GUID Partition Table, or GPT, uses 64-bit logical block addresses and normally stores a primary header and entry array near the start plus backup copies near the end of the disk. A protective MBR helps older MBR-only software avoid treating the disk as empty.

Each GPT entry includes a partition type GUID and a unique partition GUID; GPT therefore does not have only one partition type. The number of available entries is determined by the allocated table and tools, commonly far more than four, without extended or logical partitions.

GPT is normally used for UEFI boot disks, but partitioning and firmware boot mode are distinct concepts. A UEFI system also needs appropriate boot files and an EFI System Partition; GPT alone does not make a disk bootable.

:::single-choice{#anatomy-disk-gpt-identifiers} Which identifiers does a GPT partition entry include?

::option[A type GUID and a unique partition GUID.]{#anatomy-disk-gpt-guids .correct explanation="The type describes intended use, while the unique GUID identifies that particular partition entry."}
::option[Only one universal type shared by every GPT partition.]{#anatomy-disk-gpt-one-type explanation="GPT defines many type GUIDs for different partition purposes."}
::option[The login UID and GID of the user who created it.]{#anatomy-disk-gpt-user-ids explanation="Filesystem account identifiers are not GPT partition identity fields."}
:::

## Filesystem Structures Are Format-Specific

After partitioning, a filesystem creation tool writes the structures defined by that filesystem. Many formats have concepts such as superblocks, allocation metadata, directory records, and data extents or blocks, but their layout, redundancy, and terminology differ.

For example, ext filesystems use inodes and block groups, while other filesystems organize metadata through different trees or allocation structures. Do not apply one simplified “boot block, one superblock, inode table, data blocks” diagram to every filesystem.

:::single-choice{#anatomy-disk-filesystem-layer} Does creating a partition automatically create a filesystem inside it?

::option[No; formatting or another explicit use is a separate step.]{#anatomy-disk-partition-not-filesystem .correct explanation="The partition table only defines a block region; its contents remain independent."}
::option[Yes; every partition is automatically formatted as ext4.]{#anatomy-disk-auto-ext4 explanation="Partitioning tools do not universally create an ext4 filesystem."}
::option[Yes; GPT entries are themselves mounted directories.]{#anatomy-disk-gpt-mounted explanation="A partition entry describes storage and is not a filesystem mount point."}
:::

## Inspecting the Current Layout

Use read-only views before any modification:

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,PTTYPE,PARTTYPE,FSTYPE,MOUNTPOINTS
$ sudo parted --list
```

`PTTYPE` describes a detected partition-table scheme, `PARTTYPE` a partition type identifier, and `FSTYPE` a detected content signature. Detection is evidence, not a guarantee that content is healthy or safe to mount.

Device names can change, and stale signatures can confuse detection. Confirm model, serial, size, transport, persistent links, active mounts, swap, RAID, LVM, encryption, and backups before opening any partitioning tool in write mode.

:::single-choice{#anatomy-disk-lsblk-fields} Which `lsblk` field distinguishes detected filesystem content from the partition-table scheme?

::option[`FSTYPE`]{#anatomy-disk-fstype .correct explanation="`FSTYPE` reports a detected filesystem or other recognized content signature, while `PTTYPE` reports the table scheme."}
::option[`NAME`]{#anatomy-disk-name-field explanation="`NAME` labels the kernel block-device entry and does not specifically identify content format."}
::option[`SIZE`]{#anatomy-disk-size-field explanation="Size reports capacity rather than filesystem type."}
:::

Use [Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) only on disposable storage to practice these layers.

## Summary

You can now separate disk layout metadata from the data formats stored within it.

1. Identify whole devices and their partition child devices.
2. Relate MBR extended partitions to legacy four-entry limits.
3. Relate GPT to redundant tables and per-partition GUIDs.
4. Treat filesystem creation as separate from partition creation.
5. Inspect every storage layer and active consumer before changes.
