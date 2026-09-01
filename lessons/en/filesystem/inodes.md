---
lesson_id: "inodes"
course_id: "filesystem"
lang: "en"
order_index: 11
title: "Inodes"
description: "Learn how inode numbers connect directory names to filesystem object metadata and data."
meta_title: "Inodes - The Filesystem"
meta_description: "Explore the concept of the Linux inode. Learn what an i-node is, how inodes in Linux manage file metadata, and how to check inode usage with `df -i` and `ls -li`."
meta_keywords: "linux inode, inode in linux, i node, inode, inode linux, inode number, filesystem, df -i, ls -li, stat"
---

In inode-based Unix filesystems, a directory maps each entry name to an inode number. The inode represents the filesystem object and records metadata needed to find and interpret its data. The pathname is therefore not stored as the object's own primary identity.

## Metadata Stored with an Inode

Common inode-associated metadata includes:

- object type and permission mode
- user and group ownership
- logical size and allocated-block accounting
- hard-link count
- access, modification, and status-change timestamps
- references to file data or filesystem-specific extent structures

The inode does not normally store the directory-entry name. A filesystem may also store extended attributes, access control lists, birth time, inline data, or other information through format-specific structures.

`ctime` is the inode status-change time, not necessarily file creation time. A separate birth or creation timestamp is optional and may be unavailable.

:::single-choice{#inodes-name-location} Where is a regular file's pathname component normally associated with its inode number?

::option[In the process scheduler.]{#inodes-scheduler-name explanation="CPU scheduling state does not implement filesystem pathname lookup."}
::option[In a directory entry.]{#inodes-directory-entry .correct explanation="A directory maps a name to an inode number within that filesystem."}
::option[In the disk's partition table.]{#inodes-partition-name explanation="A partition table maps storage regions, not individual filenames."}
:::

## Inode Numbers and Filesystem Scope

Display inode numbers with:

```bash
$ ls -li
```

The first field is the inode number. Inspect one object in more detail with:

```bash
$ stat path
```

An inode number is unique only within one filesystem at a given time. The same number can exist on another filesystem, and a number can be reused after an inode is freed. Identify an object robustly with both filesystem identity and inode number rather than inode number alone.

:::single-choice{#inodes-number-scope} Within what scope is an inode number an object identifier?

::option[Every Linux system in the world forever.]{#inodes-global-forever explanation="Inode allocation is local to a filesystem and identifiers are reusable."}
::option[One filesystem, at a particular time.]{#inodes-one-filesystem .correct explanation="Other filesystems can use the same number, and freed inode numbers can later be reused."}
::option[Only the shell process that created the file.]{#inodes-shell-scope explanation="The filesystem, not one shell, maintains inode identity."}
:::

## Hard Links and Open References

Several directory entries can refer to the same inode; these are hard links. Creating another hard link increments the object's link count. Removing one name decrements the count without deleting the data while another link remains.

Even after the final directory entry is removed, an open file remains allocated until the last process reference closes. Its link count can be zero while a file descriptor still accesses it. This explains why deleting a large open log might not immediately reduce `df` usage.

:::single-choice{#inodes-unlinked-open-file} When are an unlinked file's resources normally released?

::option[Immediately after any one hard-link name is removed.]{#inodes-one-link-removed explanation="Other hard links or open references can keep the object alive."}
::option[Only when the entire filesystem is reformatted.]{#inodes-reformat-only explanation="Normal unlink and close operations reclaim unused inodes and blocks."}
::option[After its link count is zero and its final open reference closes.]{#inodes-zero-links-no-opens .correct explanation="Directory names and process file descriptors are independent references to the inode."}
:::

## Inode Capacity

On filesystems with a finite or reported inode pool, millions of small files can exhaust metadata capacity before data blocks fill. Inspect mounted filesystem inode accounting with:

```bash
$ df -i
```

If no free inodes remain, creating another file can fail even when `df -h` reports available blocks. Allocation strategies differ: some filesystems preallocate inode structures at creation, while others manage metadata dynamically and may report inode capacity differently.

:::single-choice{#inodes-df-i-purpose} What does `df -i` report where the filesystem provides inode accounting?

::option[The contents of every file in inode order.]{#inodes-df-i-content explanation="Df reports aggregate filesystem statistics and does not read file contents."}
::option[Used and available inode capacity.]{#inodes-df-i-capacity .correct explanation="The inode view helps diagnose metadata-object exhaustion independently of data blocks."}
::option[The disk's firmware revision.]{#inodes-df-i-firmware explanation="Firmware inventory is unrelated to inode usage."}
:::

## Filesystem-Specific Data Mapping

Do not assume every inode has exactly 12 direct pointers plus three indirect pointers. That is a useful description of some classic filesystem layouts, but modern ext4 can use extents, and XFS, Btrfs, and other filesystems use different structures. Inline data and compressed or copy-on-write extents further change the relationship.

Use filesystem-specific diagnostic tools only in read-only or documented modes when internal mapping matters. For ordinary administration, `stat`, `find -inum`, `df -i`, and link-aware tools provide safer abstractions.

:::single-choice{#inodes-layout-portability} Why should you not assume one fixed pointer layout for every inode?

::option[Inodes never refer to file data in any way.]{#inodes-no-data-reference explanation="The filesystem must associate the object with its content, though the mechanism varies."}
::option[Filesystem implementations use different extent, tree, and inline-data structures.]{#inodes-format-specific-layout .correct explanation="The on-disk mapping from inode to content is part of each filesystem's format."}
::option[Every inode layout is chosen separately by the file owner.]{#inodes-owner-layout explanation="The filesystem implementation and format determine the metadata structure."}
:::

Use [Manage Files and Directories in Linux](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835) to compare inode numbers and link counts on disposable files.

## Summary

You can now relate pathnames, inodes, links, and filesystem capacity.

1. Treat directory entries as mappings from names to inode numbers.
2. Read metadata and timestamps without confusing ctime with creation.
3. Scope inode numbers to one filesystem and moment.
4. Account for both hard links and open file descriptors.
5. Use filesystem-specific models rather than one universal pointer layout.
