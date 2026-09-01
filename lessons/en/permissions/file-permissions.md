---
lesson_id: "file-permissions"
course_id: "permissions"
lang: "en"
order_index: 1
title: "File Permissions"
description: "Learn how to read Linux file types and owner, group, and other permission bits."
meta_title: "File Permissions - Permissions"
meta_description: "A key part of our complete linux tutorial. Learn about Linux file permissions, including the rwx bits for user, group, and other. Master the `ls -l` output and understand file modes."
meta_keywords: "file permissions, linux file permissions, best way to learn linux, complete linux tutorial, rwx permissions, ls -l command, file modes, linux guide"
---

Linux represents many resources through file-like interfaces, and each filesystem object has metadata that controls access. Reading that metadata is a foundation for working safely with files and directories.

## Reading a Long Listing

Use `ls -l` to display a long listing:

```bash
$ ls -ld Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 Desktop/
```

The first field, `drwxr-xr-x`, combines one file-type character with nine permission characters. The listing also identifies `pete` as the owner and `penguins` as the group associated with the directory.

The initial character describes the object type. Common values include:

- `-` for a regular file
- `d` for a directory
- `l` for a symbolic link

Other special file types also exist. The remaining nine characters are the access permissions:

```text
d | rwx | r-x | r-x
```

:::single-choice{#file-permissions-type-character} In `drwxr-xr-x`, what does the first `d` indicate?

::option[The object is a symbolic link.]{#file-permissions-type-link explanation="A symbolic link is normally shown with `l` in the file-type position."}
::option[The object is a directory.]{#file-permissions-type-directory .correct explanation="The first character is the file type, and `d` identifies a directory."}
::option[The owner has delete permission.]{#file-permissions-type-delete explanation="Linux mode strings do not use `d` as a delete permission; the first position describes the object type."}
:::

## Understanding `r`, `w`, and `x`

Each permission triplet uses these characters:

- `r` grants read permission.
- `w` grants write permission.
- `x` grants execute permission.
- `-` means that permission is absent.

For a regular file, read permits access to its contents, write permits modification of its contents, and execute permits the kernel to attempt to run it as a program. Execution can still fail if the file format, interpreter line, mount options, or another security control does not allow it.

For a directory, the meanings concern directory entries:

- Read permits listing names in the directory.
- Write permits creating or removing entries, normally in combination with execute permission.
- Execute, also called search permission, permits traversing the directory and accessing entries by name.

Deleting a file is governed primarily by permissions on its parent directory, not by the file's own write bit.

:::single-choice{#file-permissions-directory-execute} What does execute permission on a directory primarily allow?

::option[Running every regular file stored in the directory.]{#file-permissions-directory-run-files explanation="A directory's execute bit does not grant execute permission on each file inside it."}
::option[Changing the contents of every file in the directory.]{#file-permissions-directory-edit-files explanation="Writing file contents depends on the files' permissions and other access controls."}
::option[Traversing the directory and accessing entries by name.]{#file-permissions-directory-search .correct explanation="Directory execute, or search, permission allows pathname traversal through that directory."}
:::

## Owner, Group, and Other Classes

The nine mode characters form three triplets in a fixed order:

1. **Owner**: permissions used when the process's effective user ID matches the file owner.
2. **Group**: permissions used when an applicable process group ID matches the file's group.
3. **Other**: permissions used when neither of the preceding classes matches.

The kernel selects one applicable class; it does not combine the three triplets to find the most permissive result. Additional mechanisms such as access control lists, mount options, capabilities, or mandatory access controls can further affect the final decision.

In the example, the owner triplet is `rwx`, while both group and other are `r-x`. The owner can read, write, and search the directory. The group and other classes can read and search it but cannot create or remove entries through the directory's ordinary mode bits.

:::single-choice{#file-permissions-triplet-order} After the file-type character, in what order do the three permission triplets appear?

::option[Group, owner, then other.]{#file-permissions-order-group-first explanation="The group triplet is second, not first."}
::option[Other, group, then owner.]{#file-permissions-order-other-first explanation="The other triplet is last, and the owner triplet is first."}
::option[Owner, group, then other.]{#file-permissions-order-owner-first .correct explanation="The nine permission characters always present owner, group, and other triplets in that order."}
:::

:::single-choice{#file-permissions-example-group} What ordinary permissions does the group class have in `drwxr-xr-x`?

::option[Read and write.]{#file-permissions-group-read-write explanation="The group triplet is `r-x`, so its write position contains `-`."}
::option[Write and execute.]{#file-permissions-group-write-execute explanation="The group triplet contains `r` rather than `w` in its first position."}
::option[Read and execute.]{#file-permissions-group-read-execute .correct explanation="The middle triplet is `r-x`, which grants read and execute but not write."}
:::

To reinforce these concepts in an isolated environment, try the [Linux User Group and File Permissions](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) lab. It provides practice reading modes and changing ownership and permissions.

## Summary

You can now interpret the basic permission field in a Linux long listing.

1. Separate the file-type character from the nine permission bits.
2. Read `r`, `w`, and `x` according to whether the object is a file or directory.
3. Divide the mode into owner, group, and other triplets.
4. Relate the triplets to the owner and group shown by `ls -l`.
