---
index: 6
lang: "en"
title: "Setgid"
meta_title: "Setgid - Permissions"
meta_description: "Learn about Linux SGID (Set Group ID) permissions, how they work, and how to modify them. Understand this crucial Linux security concept."
meta_keywords: "Linux SGID, Set Group ID, Linux permissions, chmod g+s, Linux security, beginner Linux, Linux tutorial"
---

## Lesson Content

Similar to the set user ID permission bit, there is a set group ID (SGID) permission bit. This bit allows a program to run as if it were a member of that group.

Let's look at one example:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

We can now see that the permission bit is in the group permission set.

### Modifying SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

The numerical representation for SGID is 2.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux user, group, and file permissions:

1. **[Linux User Group and File Permissions](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002)** - Learn essential Linux user and group management concepts, including creating and managing users, exploring group memberships, understanding file permissions, and manipulating file ownership.
2. **[Add New User and Group](https://labex.io/labs/linux-add-new-user-and-group-17987)** - Practice creating new user accounts, setting up custom groups, and managing group memberships, simulating real-world system administration tasks.

These labs will help you apply the concepts in real scenarios and build confidence with Linux permissions and user management.

## Quiz Question

What number represents the SGID?

## Quiz Answer

2
