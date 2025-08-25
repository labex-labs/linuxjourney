---
index: 3
lang: "en"
title: "Ownership Permissions"
meta_title: "Ownership Permissions - Permissions"
meta_description: "Learn how to change file ownership in Linux using chown and chgrp commands. Understand user and group permissions with this beginner-friendly Linux tutorial."
meta_keywords: "chown, chgrp, Linux file ownership, Linux permissions, Linux commands, beginner Linux, Linux tutorial, Linux guide"
---

## Lesson Content

In addition to modifying permissions on files, you can also modify the group and user ownership of the file.

### Modify user ownership

```bash
sudo chown patty myfile
```

This command will set the owner of `myfile` to `patty`.

### Modify group ownership

```bash
sudo chgrp whales myfile
```

This command will set the group of `myfile` to `whales`.

### Modify both user and group ownership at the same time

If you add a colon and group name after the user, you can set both the user and group at the same time.

```bash
sudo chown patty:whales myfile
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of file ownership and permissions:

1. **[Linux User Group and File Permissions](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002)** - Learn essential Linux user and group management concepts, including understanding file permissions and manipulating file ownership. This lab provides practical experience in securing a multi-user Linux environment.
2. **[Add New User and Group](https://labex.io/labs/linux-add-new-user-and-group-17987)** - In this challenge, you'll simulate adding new team members to a server environment by creating new user accounts, setting up custom groups, and managing group memberships. This will test your skills in Linux user and group administration.

These labs will help you apply the concepts in real scenarios and build confidence with managing file ownership and permissions in Linux.

## Quiz Question

What command do you use to change user ownership?

## Quiz Answer

chown
