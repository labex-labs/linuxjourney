---
index: 8
lang: "en"
title: "The Sticky Bit"
meta_title: "The Sticky Bit - Permissions"
meta_description: "Learn about the Linux sticky bit, its purpose in shared directories like /tmp, and how to set it using chmod. Understand this key file permission!"
meta_keywords: "Linux sticky bit, chmod +t, /tmp directory, Linux permissions, file security, Linux tutorial, beginner Linux"
---

## Lesson Content

One last special permission bit I want to talk about is the sticky bit.

This permission bit "sticks a file/directory," meaning that only the owner or the root user can delete or modify the file. This is very useful for shared directories. Take a look at the example below:

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

You'll see a special permission bit at the end here **t**. This means everyone can add files, write files, and modify files in the `/tmp` directory, but only root can delete the `/tmp` directory.

### Modify sticky bit

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

The numerical representation for the sticky bit is **1**.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux file permissions and their impact on file and directory management:

1. **[Linux User Group and File Permissions](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002)** - Practice creating and managing users and groups, understanding file permissions, and manipulating file ownership. This lab provides the foundational knowledge for understanding how special permissions like the sticky bit function.
2. **[Delete and Move Files](https://labex.io/labs/linux-delete-and-move-files-7777)** - Learn how to delete and move files in Linux systems. This lab will help you understand the practical implications of permissions, including how they can restrict these actions.
3. **[Find a File](https://labex.io/labs/linux-find-a-file-17993)** - Practice locating files and setting access authority. This lab reinforces the importance of file permissions and how they control access and modification.

These labs will help you apply the concepts of file permissions in real scenarios and build confidence with managing file access in Linux.

## Quiz Question

What symbol represents the sticky bit?

## Quiz Answer

t
