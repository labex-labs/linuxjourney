---
lesson_id: "filesystem-repair"
course_id: "filesystem"
lang: "en"
order_index: 10
title: "Filesystem Repair"
description: "Learn how to diagnose filesystem damage and choose a type-specific, offline repair workflow with backups."
meta_title: "Filesystem Repair - The Filesystem"
meta_description: "Learn to use fsck for Linux filesystem repair and data recovery. Understand how to check and fix disk errors with this essential command. Start your Linux journey!"
meta_keywords: "fsck, filesystem repair, Linux commands, disk errors, data recovery, Linux tutorial, beginner guide"
---

Filesystem repair rewrites metadata to restore internal consistency. It can discard damaged references or data and can worsen loss when storage hardware is failing. Treat repair as a recovery operation: preserve evidence and recoverable data first, then use the tool documented for the exact filesystem.

## Diagnose Before Repairing

Symptoms such as I/O errors, read-only remounts, missing files, or mount failures do not all prove filesystem corruption. First gather read-only evidence:

```bash
$ findmnt --target /affected/path
$ lsblk -f
$ journalctl -k -b
```

Check the storage stack, device health, cables or network path, RAID state, encryption, and recent events. If the device is failing, repeated scans can consume its remaining life. Capture an image or clone with a recovery-oriented tool and work on the copy when feasible.

:::single-choice{#filesystem-repair-first-response}
What should precede a write-capable filesystem repair when hardware failure is possible?

::option[Repeatedly run every repair tool until one exits zero.]{#filesystem-repair-repeat-tools explanation="Using mismatched tools and repeated writes can compound damage."}
::option[Create a new partition table over the device immediately.]{#filesystem-repair-new-table explanation="Overwriting layout metadata destroys evidence and can make recovery harder."}
::option[Preserve recoverable data or an image and investigate device health.]{#filesystem-repair-preserve-first .correct explanation="Repair mutates metadata, while failing media can deteriorate during repeated access."}
:::

## Identify the Exact Filesystem and Device

Determine whether the filesystem lives on a partition, logical volume, RAID device, encrypted mapping, or whole disk. Do not run a checker against `/dev/sda` merely because a child partition such as `/dev/sda1` is affected.

Use `lsblk -f`, `blkid`, `findmnt`, and storage-layer tools to map the target. Detection signatures can be stale, so reconcile them with known configuration and backups.

:::single-choice{#filesystem-repair-target-layer}
If ext4 is stored on `/dev/sda1`, which layer should its ext4 checker normally receive?

::option[`/dev/sda` regardless of its partition table.]{#filesystem-repair-whole-disk explanation="The whole disk contains the partition table and possibly several child regions, not the ext4 instance directly."}
::option[`/dev/sda1` after it is safely offline.]{#filesystem-repair-partition-target .correct explanation="The checker operates on the block device that directly contains that filesystem."}
::option[`/mnt/data` while applications continue writing there.]{#filesystem-repair-live-mount explanation="A pathname mount point is not the offline block-device target expected by the checker."}
:::

## Make the Filesystem Offline

Most traditional consistency checkers require the filesystem to be unmounted. A mounted filesystem changes while the checker reads it, and repair writes can conflict with the kernel's cached state, causing corruption.

Stop dependent services, unmount nested filesystems, move process working directories, and deactivate higher layers as required. For the root filesystem, boot a rescue environment or use the distribution's documented offline check mechanism. Confirm with `findmnt` that the target is not mounted in the relevant namespace.

:::single-choice{#filesystem-repair-mounted-risk}
Why should a filesystem normally be unmounted before a repair checker writes to it?

::option[Concurrent kernel and checker updates can conflict and corrupt metadata.]{#filesystem-repair-concurrent-writes .correct explanation="An offline view prevents the filesystem from changing underneath the repair operation."}
::option[Unmounting automatically restores every damaged file from backup.]{#filesystem-repair-unmount-restores explanation="Detachment provides consistency for checking but is not data restoration."}
::option[Filesystem tools can read only directories, never block devices.]{#filesystem-repair-tools-directories explanation="Repair tools normally operate directly on offline block devices."}
:::

## Use the Filesystem-Specific Tool

`fsck` is a front end that can invoke filesystem-specific helpers. It is not one universal repair engine. Examples of distinct workflows include `e2fsck` for ext filesystems, `xfs_repair` for XFS, and filesystem-specific Btrfs diagnostic and recovery tools.

Options with similar names can have different semantics. In particular, do not apply `--repair` or force flags copied from another filesystem's guide. Read the installed manual and current project or distribution recovery documentation. Begin with a no-modification or diagnostic mode if that implementation provides a reliable one, capture output, and understand the proposed fixes.

:::single-choice{#filesystem-repair-fsck-role}
What is `fsck` on Linux commonly responsible for?

::option[Dispatching checks to a helper appropriate for the filesystem type.]{#filesystem-repair-fsck-dispatch .correct explanation="Actual validation and repair logic belongs to format-specific tools and workflows."}
::option[Converting every filesystem into ext4 before checking it.]{#filesystem-repair-fsck-convert explanation="A checker must preserve and understand the existing format."}
::option[Repairing failed hardware sectors with no data loss guarantee.]{#filesystem-repair-fsck-hardware explanation="Filesystem consistency tools cannot repair physical hardware or guarantee data recovery."}
:::

## Verify and Restore Service

Record the repair tool, version, options, output, and exit status. After repair, repeat device-health checks, mount read-only first where appropriate, inspect critical data, and compare with known backups. Then restore normal mounts and services gradually while monitoring kernel and application logs.

A filesystem becoming mountable does not prove every file is correct. Restore lost or damaged application data from backups and validate at the application layer.

:::single-choice{#filesystem-repair-mountable-proof}
Does a successful mount after repair prove that all application data is correct?

::option[No; consistency repair and application-level data validation are different.]{#filesystem-repair-not-data-proof .correct explanation="The filesystem can be structurally mountable while files or transactions remain missing or damaged."}
::option[Yes; mounting cryptographically verifies every file against a backup.]{#filesystem-repair-mount-verifies explanation="Ordinary mount does not perform a full backup comparison."}
::option[Yes; repair tools recreate all unknown contents automatically.]{#filesystem-repair-recreates-data explanation="Metadata repair cannot infer arbitrary lost user data."}
:::

## Summary

You can now plan filesystem repair as a staged recovery procedure.

1. Diagnose hardware and preserve recoverable data before writes.
2. Map the exact filesystem-containing block layer.
3. Make the filesystem offline in the relevant namespace.
4. Use the documented filesystem-specific diagnostic and repair tool.
5. Validate device health, filesystem state, and application data separately.
