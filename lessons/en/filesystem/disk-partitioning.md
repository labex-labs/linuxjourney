---
lesson_id: "disk-partitioning"
course_id: "filesystem"
lang: "en"
order_index: 4
title: "Disk Partitioning"
description: "Learn a verification-first workflow for inspecting, creating, and resizing partition boundaries with `parted`."
meta_title: "Disk Partitioning - The Filesystem"
meta_description: "Learn Linux disk partitioning with the parted command. This guide covers how to view partitions with `sudo parted -l`, create, and resize them. Also introduces gparted, a popular graphical alternative."
meta_keywords: "Linux disk partitioning, parted command, sudo parted -l, gparted, gparted windows alternative, fdisk, disk management, create partition, resize partition, Linux guide"
---

Partition editing changes the map that defines storage boundaries. A wrong device, start, or end can make existing data inaccessible or overwrite critical metadata. Practice only on a disposable virtual disk and maintain a separately tested backup before modifying valuable storage.

## Choosing a Tool

Common tools include:

- `fdisk`, a terminal partition editor from util-linux that supports MBR and GPT
- `parted`, a terminal and scriptable editor for GPT, MBR, and other table formats
- `gdisk`, an interactive GPT-focused editor
- GParted, a graphical partition and filesystem front end

Tool support evolves, so use the local manual and distribution documentation. A graphical interface does not make destructive operations safe; it still changes the same disk metadata.

:::single-choice{#disk-partitioning-fdisk-gpt} Which statement about current Linux `fdisk` is accurate?

::option[It supports both MBR and GPT partition tables.]{#disk-partitioning-fdisk-supports-gpt .correct explanation="Current util-linux fdisk can edit DOS/MBR and GPT layouts, among others."}
::option[It can edit only GPT and never MBR.]{#disk-partitioning-fdisk-only-gpt explanation="GPT-focused `gdisk` is closer to that description; fdisk supports multiple label types."}
::option[It creates filesystems but cannot edit partition entries.]{#disk-partitioning-fdisk-filesystem-only explanation="Its central purpose is viewing and editing partition tables."}
:::

## Identify and Quiesce the Target

Start with read-only inventory:

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,TRAN,PTTYPE,FSTYPE,MOUNTPOINTS
$ findmnt --real
$ sudo parted --list
```

Confirm the whole device by persistent identity, model, serial, size, transport, and topology—not merely `/dev/sdX`. Then identify every consumer: mounted filesystems, swap, LVM, RAID, encryption, containers, virtual machines, databases, and open file descriptors.

Unmount or deactivate all relevant layers using their documented procedures. Do not edit the partition table of the running system disk merely because the tool opens successfully. Record the existing table in a restorable form and confirm that your backup resides on a different failure domain.

:::single-choice{#disk-partitioning-target-identity} Why is a device name such as `/dev/sdb` insufficient as the only target check?

::option[Linux never exposes whole disks under `/dev`.]{#disk-partitioning-no-whole-disks explanation="Whole disks commonly do have block nodes under `/dev`."}
::option[Enumeration names can change when devices or topology change.]{#disk-partitioning-enumeration-changes .correct explanation="A letter is assigned by discovery order and can refer to another disk in a later session."}
::option[Partition tools accept only filesystem UUIDs as operands.]{#disk-partitioning-only-uuid explanation="Editors normally operate on a whole block-device path, after identity verification."}
:::

## Inspecting One Device in `parted`

Open the explicitly verified whole device:

```bash
$ sudo parted /dev/VERIFIED-DISK
```

Then select consistent display units and print the table:

```text
(parted) unit MiB
(parted) print free
```

`print free` shows current entries and unallocated regions. Parted commands can update disk metadata immediately rather than waiting for a final “save” operation, so treat the interactive prompt as live write access.

:::single-choice{#disk-partitioning-print-free} What does `print free` help display in `parted`?

::option[Files that can be deleted to shrink any filesystem safely.]{#disk-partitioning-free-files explanation="Parted reads partition layout, not filesystem-level file allocation."}
::option[Every backup stored on remote systems.]{#disk-partitioning-remote-backups explanation="Remote backup inventory is outside a partition editor's scope."}
::option[Existing partition entries and unallocated regions.]{#disk-partitioning-free-regions .correct explanation="The view helps choose boundaries based on the current table and remaining gaps."}
:::

## Creating a Partition Entry

The exact `mkpart` syntax depends on the table type. A GPT example in MiB units resembles:

```text
(parted) mkpart data ext4 1MiB 5000MiB
```

This creates a partition entry with a name, suggested content type, start, and end. It does **not** create an ext4 filesystem. Formatting is a separate, destructive step performed only after the kernel recognizes the intended new partition and its identity is verified.

Use tool-recommended alignment and understand whether endpoints are inclusive and how they are rounded. Inspect the result with `print` and `lsblk`; do not assume a requested decimal boundary was recorded exactly.

:::single-choice{#disk-partitioning-mkpart-effect} What does `parted` `mkpart` create?

::option[A mounted ext4 filesystem containing a home directory.]{#disk-partitioning-mounted-filesystem explanation="Formatting and mounting are separate operations after partition creation."}
::option[A complete backup of the previous partition contents.]{#disk-partitioning-automatic-backup explanation="Partition editors do not create a recovery backup automatically."}
::option[A partition-table entry, without formatting a filesystem.]{#disk-partitioning-entry-only .correct explanation="The filesystem-type argument influences partition metadata but does not run `mkfs`."}
:::

## Resizing Boundaries and Contents

`resizepart NUMBER END` moves only a partition's end boundary. It does not resize the filesystem or other structure stored inside.

Order is critical:

- To grow, enlarge the containing partition or logical device first, then grow the filesystem with its own supported tool.
- To shrink, verify that the filesystem supports shrinking, shrink it first while observing its offline/online requirements, then reduce the containing boundary without crossing the new end.

Some filesystems cannot shrink. Encryption, LVM, RAID, and nested layouts add more ordered layers. A kernel can also refuse to reread a changed table while devices are busy, requiring a controlled reboot before the new layout is usable.

:::single-choice{#disk-partitioning-shrink-order} When a filesystem supports shrinking, which order avoids cutting off live filesystem data?

::option[Reduce the partition first, then discover whether the filesystem fits.]{#disk-partitioning-shrink-partition-first explanation="Shortening the container first can truncate filesystem structures and data."}
::option[Shrink the filesystem first, then reduce its containing partition boundary.]{#disk-partitioning-shrink-filesystem-first .correct explanation="The content must fit inside the smaller range before the outer block device is shortened."}
::option[Delete the partition table and let the filesystem recreate it.]{#disk-partitioning-delete-table explanation="A filesystem does not reconstruct a safe partition table as part of normal shrinking."}
:::

Use [Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) on its designated secondary virtual disk; do not substitute a host disk.

## Summary

You can now describe partition editing as a layered, destructive storage operation.

1. Select a tool that supports the actual table and workflow.
2. Verify persistent disk identity and deactivate every consumer.
3. Inspect units, entries, and free regions before writing.
4. Remember that `mkpart` does not create a filesystem.
5. Resize inner content and outer boundaries in the safe order.
