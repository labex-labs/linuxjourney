---
index: 1
lang: "en"
title: "File Permissions"
meta_title: "File Permissions - Permissions"
meta_description: "A key part of our complete linux tutorial. Learn about Linux file permissions, including the rwx bits for user, group, and other. Master the `ls -l` output and understand file modes."
meta_keywords: "file permissions, linux file permissions, best way to learn linux, complete linux tutorial, rwx permissions, ls -l command, file modes, linux guide"
---

## Lesson Content

In Linux, everything is a file, and managing access to these files is a critical skill. Understanding **file permissions** is fundamental for system security and administration. Let's explore how to read and interpret these permissions.

### Introduction to File Permissions

When we list files in a detailed format, we see a string of characters that define their permissions. Let's look at an example using the `ls -l` command:

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
```

This output provides a wealth of information, but we will focus on the first column, `drwxr-xr-x`, which represents the file type and its permissions.

### Decoding the Permission String

The permission string has four main parts. The first character indicates the file type. In our example, the **d** signifies that `Desktop` is a directory. For a regular file, you would see a hyphen (`-`).

The next nine characters represent the actual **file permissions**. These are divided into three sets of three characters each. To make it clearer, we can visualize them like this:

```plaintext
d | rwx | r-x | r-x
```

Each character in these sets corresponds to a specific permission:

- **r**: Read permission.
- **w**: Write permission.
- **x**: Execute permission.
- **-**: No permission granted.

The meaning of these permissions can change slightly depending on whether it's a file or a directory. For example, execute (`x`) permission on a directory allows you to enter it, while on a file, it allows you to run it as a program.

### User, Group, and Other Permissions

The three sets of permissions apply to different levels of access:

1. **User (Owner)**: The first set (`rwx`) applies to the owner of the file, which is `pete` in our example. The owner has read, write, and execute permissions.
2. **Group**: The second set (`r-x`) applies to the group associated with the file, which is `penguins`. Members of this group have read and execute permissions but cannot write to the file.
3. **Other**: The final set (`r-x`) applies to all other users on the system. They have read and execute permissions.

Mastering **file permissions** is a core concept, and this foundation is essential as you continue through this **complete linux tutorial**.

## Exercise

The **best way to learn linux** is through hands-on practice. These exercises will help you master Linux **file permissions**, users, and groups:

1. **[Linux User Group and File Permissions](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002)** - Learn essential Linux user and group management concepts, including creating users, exploring group memberships, understanding file permissions, and manipulating file ownership.
2. **[Add New User and Group](https://labex.io/labs/linux-add-new-user-and-group-17987)** - Practice creating new user accounts, setting up custom groups, and managing group memberships, simulating real-world system administration tasks.
3. **[Find a File](https://labex.io/labs/linux-find-a-file-17993)** - Apply your knowledge of file permissions by finding a specific file and setting its access authority, ensuring you're the only authorized user.

These labs will help you apply the concepts in real scenarios and build confidence with managing permissions and users in Linux.

## Quiz Question

What permission bit is used for executable? Please answer in English, paying close attention to case sensitivity.

## Quiz Answer

x
