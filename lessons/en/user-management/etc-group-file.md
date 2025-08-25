---
index: 5
lang: "en"
title: "/etc/group"
meta_title: "/etc/group - User Management"
meta_description: "Learn about the /etc/group file in Linux, understanding group management, GID, and user permissions. Essential Linux group file tutorial for beginners."
meta_keywords: "/etc/group, Linux groups, group management, GID, Linux permissions, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Another file used in user management is the `/etc/group` file. This file allows for different groups with different permissions.

```bash
$ cat /etc/group

root:*:0:pete
```

Very similar to the `/etc/passwd` file, the `/etc/group` fields are as follows:

1. Group name
2. Group password - there isn't a need to set a group password; using an elevated privilege like `sudo` is standard. An asterisk (`*`) will be put in place as the default value.
3. Group ID (GID)
4. List of users - you can manually specify users you want in a specific group

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux user and group management:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practice the complete lifecycle of user administration, from creating and securing new accounts to modifying and deleting them.
2. **[Manage Linux Groups with groupadd, usermod, and groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Gain hands-on experience with core command-line utilities for group administration, including `groupadd`, `usermod`, and `groupdel`.
3. **[Add New User and Group](https://labex.io/labs/linux-add-new-user-and-group-17987)** - Simulate adding new team members to a server environment by creating new user accounts, setting up custom groups, and managing group memberships.

These labs will help you apply the concepts in real scenarios and build confidence with Linux user and group management.

## Quiz Question

What is the GID of root?

## Quiz Answer

0
