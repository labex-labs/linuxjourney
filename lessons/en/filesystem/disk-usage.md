---
lesson_id: "disk-usage"
course_id: "filesystem"
lang: "en"
order_index: 9
title: "Disk Usage"
description: "Learn how `df` and `du` measure different views of filesystem block and inode consumption."
meta_title: "Disk Usage - The Filesystem"
meta_description: "Learn to check Linux disk usage and free space with the df and du commands. This guide covers how to analyze disk space, including inode usage with df -i linux, and find which files are taking up space."
meta_keywords: "df command, du command, Linux disk usage, check free space, df -i linux, disk management, Linux tutorial, disk utilization, filesystem usage"
---

Filesystem capacity has at least two limits: data blocks and metadata objects such as inodes. `df` reports allocation from the filesystem's perspective, while `du` walks reachable pathnames and sums usage attributed to them. The values answer different questions and need not match.

## Filesystem Capacity with `df`

Show mounted filesystem type and human-readable block figures with:

```bash
$ df -hT
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda1      ext4  6.2G  2.3G  3.6G  40% /
```

`Size`, `Used`, and `Avail` come from filesystem accounting. Available space can be less than total minus used because of reserved blocks, metadata, allocation policy, quotas, or rounding. Run `df` on a path to report the filesystem containing that path:

```bash
$ df -hT /var/log
```

:::single-choice{#disk-usage-df-scope} What does `df` primarily report?

::option[The byte content of each file in one directory.]{#disk-usage-df-file-content explanation="Directory-tree accounting is the role of tools such as `du`."}
::option[Filesystem-level capacity, use, and available space.]{#disk-usage-df-filesystem .correct explanation="Df queries mounted filesystem allocation statistics rather than walking every pathname."}
::option[Only the physical size printed on a disk label.]{#disk-usage-df-physical-label explanation="Its figures describe filesystem accounting, not merely hardware-marketed capacity."}
:::

## Inode Capacity

Filesystems that allocate inode-like objects can exhaust them even while blocks remain:

```bash
$ df -i /var
```

Large numbers of tiny files can consume available inodes. Deleting one large file frees many blocks but generally only one inode; deleting many unnecessary small files can relieve inode pressure. Some filesystems allocate metadata dynamically and report these concepts differently.

:::single-choice{#disk-usage-inode-exhaustion} What can happen when a filesystem has free blocks but no free inodes?

::option[Every existing file automatically doubles in size.]{#disk-usage-inode-double explanation="Inode exhaustion prevents new metadata allocation and does not expand existing content."}
::option[Creating another file can fail.]{#disk-usage-inode-create-fail .correct explanation="A new filesystem object needs metadata even when space remains for file data."}
::option[The filesystem is converted into swap.]{#disk-usage-inode-swap explanation="Resource exhaustion does not change the filesystem's type."}
:::

## Path Usage with `du`

Summarize allocated space reachable below one directory:

```bash
$ du -sh /var/log
```

Compare immediate children while staying on one filesystem:

```bash
$ sudo du -xhd1 /var | sort -h
```

GNU options shown here mean human-readable output, maximum depth one, and one filesystem. Permissions can hide subtrees and produce an incomplete total. `du` can also count hard-linked files only once by default, distinguish apparent size from allocated blocks, and treat sparse files differently depending on options.

:::single-choice{#disk-usage-du-purpose} Which command summarizes allocated usage under `/var/log`?

::option[`df -i /var/log`]{#disk-usage-df-inodes explanation="This reports inode statistics for the containing filesystem."}
::option[`du -sh /var/log`]{#disk-usage-du-summary .correct explanation="Du walks the named tree and `-s` emits one summary in human-readable units."}
::option[`mount -a /var/log`]{#disk-usage-mount-a explanation="Mounting is unrelated to a read-only directory-usage summary."}
:::

## Why `df` and `du` Differ

Common causes include:

- a process keeps a deleted file open, so its blocks remain allocated but no pathname exists for `du`
- filesystem metadata, reserved space, journals, reflinks, snapshots, or compression affect accounting
- another filesystem is mounted within the walked tree
- permissions prevent `du` from reading some directories
- sparse files have different apparent and allocated sizes

For deleted-but-open files, inspect authorized processes with a tool such as `lsof +L1`; restart or signal the responsible service through its normal procedure rather than truncating unknown descriptors.

:::single-choice{#disk-usage-deleted-open-file} Why can `df` show space in use that pathname-based `du` cannot find?

::option[`df` always multiplies every file size by two.]{#disk-usage-df-doubles explanation="There is no universal doubling rule."}
::option[A deleted file can remain open and allocated to a running process.]{#disk-usage-open-deleted .correct explanation="The directory entry is gone, but the filesystem keeps blocks until the final open reference closes."}
::option[`du` automatically deletes files after counting them.]{#disk-usage-du-deletes explanation="Du is an accounting tool and does not remove the walked files."}
:::

## Investigating Without Making the Incident Worse

Start at the full filesystem reported by `df`, identify its mount target with `findmnt`, then narrow `du` searches on that same filesystem. Account for snapshots, container layers, logs, package caches, and application retention policy. Do not delete files solely because they are large; determine ownership, backup, compliance, and service behavior first.

:::single-choice{#disk-usage-safe-investigation} What is the safest response to finding a large file?

::option[Delete it immediately while the service is writing.]{#disk-usage-delete-immediately explanation="This can lose required data and may not free space if the file remains open."}
::option[Run `mkfs` on the containing device.]{#disk-usage-mkfs-device explanation="Formatting would destroy the filesystem rather than resolve one file's growth."}
::option[Identify its owner and retention role before changing it.]{#disk-usage-review-large-file .correct explanation="Size alone does not establish that the file is disposable or safe to truncate."}
:::

## Summary

You can now reconcile filesystem and pathname-based space reports.

1. Use `df` for mounted filesystem block capacity.
2. Use `df -i` for inode pressure where supported.
3. Use scoped `du` walks to attribute reachable path usage.
4. Investigate deleted-open files and filesystem-specific accounting differences.
5. Apply ownership and retention policy before deleting data.
