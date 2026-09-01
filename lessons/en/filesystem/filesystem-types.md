---
lesson_id: "filesystem-types"
course_id: "filesystem"
lang: "en"
order_index: 2
title: "Filesystem Types"
description: "Learn how Linux VFS presents local, network, and virtual filesystems through one interface."
meta_title: "Filesystem Types - The Filesystem"
meta_description: "Discover the different Linux file system types, including ext4, Btrfs, and XFS. This guide explains key concepts like journaling and the Virtual File System (VFS), helping you understand the various filesystem types available for Linux."
meta_keywords: "linux file system types, filesystem types, ext4, Btrfs, XFS, journaling, VFS, linux tutorial"
---

Linux supports many filesystem implementations with different on-disk formats, network protocols, consistency models, features, and operational tools. The right choice depends on distribution support, workload, recovery requirements, storage topology, and administrator experience.

## The Virtual Filesystem Layer

The kernel's Virtual Filesystem layer, or VFS, provides common operations such as open, read, write, rename, and permission checks. Filesystem implementations connect those operations to their own data structures and backing stores.

This lets one process access ext4, XFS, NFS, tmpfs, and procfs through a shared pathname and file-descriptor model. It does not make every filesystem feature or behavior identical: case sensitivity, locking, permissions, rename guarantees, extended attributes, and error handling can differ.

:::single-choice{#filesystem-types-vfs-role} What is the primary role of Linux VFS?

::option[Convert every mounted filesystem into ext4 on disk.]{#filesystem-types-vfs-convert-ext4 explanation="The abstraction preserves distinct filesystem implementations and formats."}
::option[Back up every file before an application writes it.]{#filesystem-types-vfs-backup explanation="VFS dispatches operations and does not provide automatic backup history."}
::option[Provide common kernel file operations across filesystem implementations.]{#filesystem-types-vfs-common-interface .correct explanation="VFS lets applications use shared system calls while each filesystem implements the underlying behavior."}
:::

## Journaling and Crash Consistency

A journaling filesystem records selected updates in a journal so it can replay or discard incomplete transactions after a crash. Journaling is primarily about restoring filesystem structural consistency more quickly than a full scan.

It does not guarantee that the latest application data survived, that multi-file application transactions are valid, or that storage hardware honored every completed write. Filesystems offer different data modes and ordering guarantees, while applications must use appropriate flush and atomic-update patterns. A journal is not a backup and does not protect against deletion, malware, or device failure.

:::single-choice{#filesystem-types-journal-scope} What does filesystem journaling primarily help recover after a crash?

::option[Consistent filesystem metadata and recorded transactions.]{#filesystem-types-journal-consistency .correct explanation="Journal replay helps bring filesystem structures back to a coherent state."}
::option[Every historical version of every user document.]{#filesystem-types-journal-versions explanation="A journal is not a versioned backup store."}
::option[Data from a physically destroyed storage device.]{#filesystem-types-journal-hardware-loss explanation="Recovery from device loss requires redundancy or backups outside the failed device."}
:::

## Common Local Filesystems

- **ext4** is a mature journaling filesystem widely supported by Linux distributions and recovery tools.
- **XFS** is a scalable journaling filesystem commonly chosen for large filesystems and parallel I/O workloads.
- **Btrfs** is a copy-on-write filesystem with checksums, subvolumes, snapshots, and integrated multi-device features.

Features require operational context. A Btrfs snapshot initially shares storage with its source and is not an independent backup when it remains on the same failing device. XFS and ext4 have different grow, shrink, repair, and tuning capabilities. Confirm support for the installed kernel, boot environment, and recovery tooling before choosing or changing a root filesystem.

:::single-choice{#filesystem-types-btrfs-snapshot} Why is a Btrfs snapshot on the same device not a complete backup?

::option[Snapshots always delete the original subvolume immediately.]{#filesystem-types-snapshot-deletes explanation="A snapshot creates another subvolume view and does not inherently remove its source."}
::option[It shares the same storage failure domain as the original.]{#filesystem-types-snapshot-failure-domain .correct explanation="Device loss or severe filesystem damage can affect both the source and its local snapshot."}
::option[Btrfs cannot represent more than one file.]{#filesystem-types-btrfs-one-file explanation="Btrfs is a general-purpose filesystem for directory trees and many files."}
:::

## Interoperability, Network, and Virtual Filesystems

Linux can mount interoperability formats such as FAT variants, exFAT, and NTFS, but their Unix ownership, permissions, links, and filename semantics differ. Mount options and driver implementation determine how Linux presents missing features.

Network filesystems such as NFS and SMB depend on a server and network protocol, with distinct caching and identity rules. Virtual filesystems such as tmpfs, procfs, and sysfs do not use a normal persistent disk format: tmpfs stores volatile data in memory-backed pages, while procfs and sysfs expose kernel interfaces.

:::single-choice{#filesystem-types-procfs-category} Which description best fits procfs?

::option[A Windows interchange format for removable media.]{#filesystem-types-procfs-windows explanation="FAT or exFAT more closely match that use; procfs is Linux kernel-facing."}
::option[A virtual filesystem exposing process and kernel interfaces.]{#filesystem-types-procfs-virtual .correct explanation="Procfs generates a live kernel view rather than storing ordinary persistent files on disk."}
::option[A journaling disk filesystem designed for database volumes.]{#filesystem-types-procfs-journal explanation="Procfs has no normal on-disk journal or data-volume role."}
:::

## Discovering Active Types

Show mounted filesystem types with:

```bash
$ findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Alternative views include `df -T` for mounted space accounting, `lsblk -f` for block devices and detected filesystem signatures, and `/proc/filesystems` for types supported or known by the running kernel. These answer different questions; an unmounted filesystem will not appear in an ordinary mounted-filesystem listing.

:::single-choice{#filesystem-types-findmnt-output} Which command directly lists mounted targets with source, type, and options in the shown lesson?

::option[`findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS`]{#filesystem-types-findmnt .correct explanation="Findmnt reads the mount table and formats the requested mounted-filesystem fields."}
::option[`lsblk -o NAME,SIZE,MODEL,SERIAL,ROTA`]{#filesystem-types-mkfs-destructive explanation="This lists block-device hardware details rather than effective mounted filesystem types and options."}
::option[`cat /proc/filesystems | sort --unique`]{#filesystem-types-rm-proc explanation="This reports kernel-supported filesystem types rather than effective mount sources and options."}
:::

Use [Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) on disposable storage to compare types, mount options, and discovery views.

## Summary

You can now compare filesystem categories without assuming identical semantics.

1. Relate VFS to common operations across implementations.
2. Treat journaling as crash-consistency support, not backup.
3. Compare ext4, XFS, and Btrfs by supported operations and workload.
4. Distinguish local disk, network, interoperability, and virtual filesystems.
5. Use mount and block-device tools to answer different inventory questions.
