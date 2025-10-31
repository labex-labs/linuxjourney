---
index: 8
lang: "en"
title: "The Sticky Bit"
meta_title: "The Sticky Bit - Permissions"
meta_description: "Explore the purpose of the sticky bit in Linux and Unix file permissions. Learn how the sticky bit protects files in shared directories like /tmp and how to set it using chmod."
meta_keywords: "sticky bit, sticky bit linux, unix file permissions sticky bit, chmod +t, /tmp directory, file permissions, linux security"
---

## Lesson Content

Beyond the standard read, write, and execute permissions, Linux offers special permissions for advanced access control. The last of these special permissions we will cover is the **sticky bit**.

### What is the Sticky Bit?

The sticky bit is a permission setting that can be applied to a directory. When a directory has the sticky bit set, files within that directory can only be deleted or renamed by the file's owner, the directory's owner, or the root user. This is particularly useful for shared directories where multiple users need to create and manage their own files without interfering with others. This concept is a key part of **Unix file permissions sticky bit** management.

### A Practical Example: The /tmp Directory

A common use case for the **sticky bit in Linux** is the `/tmp` directory, which is a world-writable location for temporary files. Let's examine its permissions:

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

Notice the `t` at the end of the permission string (`rwxrwxrwt`). This `t` indicates that the sticky bit is set. Because of this, while any user can create files in `/tmp`, they cannot delete or move files created by other users. This prevents one user from disrupting another's work in this shared space.

### How to Set the Sticky Bit

You can set the sticky bit using the `chmod` command in two ways: symbolic mode or octal (numeric) mode.

To add the sticky bit using symbolic mode:

```bash
chmod +t my_shared_dir
```

To set permissions using octal mode, you prepend a `1` to the standard three-digit permission code. The numerical representation for the sticky bit is **1**.

```bash
# This sets permissions to rwxr-xr-x with the sticky bit
chmod 1755 my_shared_dir
```

Understanding the sticky bit is essential for managing multi-user environments and securing shared directories effectively.

## Exercise

To solidify your understanding of file permissions, including special permissions like the sticky bit, try these hands-on labs. They will help you see how these concepts apply in real-world scenarios.

1. **[Linux User Group and File Permissions](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002)** - Practice creating users and groups, and manipulating file ownership and permissions. This lab provides a foundation for understanding how special permissions function.
2. **[Delete and Move Files](https://labex.io/labs/linux-delete-and-move-files-7777)** - Learn how to delete and move files, and see how permissions, including the sticky bit on a directory, can restrict these actions.
3. **[Find a File](https://labex.io/labs/linux-find-a-file-17993)** - Practice locating files and setting access controls, reinforcing the importance of file permissions in managing file access and modification.

## Quiz Question

In a long directory listing (ls -l), what single character in the permissions string represents that the sticky bit is set? Please answer with a single lowercase English letter.

## Quiz Answer

t
