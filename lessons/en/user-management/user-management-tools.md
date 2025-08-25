---
index: 6
lang: "en"
title: "User Management Tools"
meta_title: "User Management Tools - User Management"
meta_description: "Learn Linux user management: add, remove, and change passwords with useradd, userdel, and passwd commands. Get started with this beginner-friendly guide!"
meta_keywords: "Linux user management, adduser, userdel, passwd, Linux tutorial, beginner Linux, user accounts, Linux commands"
---

## Lesson Content

Most enterprise environments use management systems to manage users, accounts, and passwords. However, on a single machine computer, there are useful commands to run to manage users.

### Adding Users

You can use the `adduser` or the `useradd` command. The `adduser` command contains more helpful features, such as making a home directory and more. There are configuration files for adding new users that can be customized depending on what you want to allocate to a default user.

```bash
sudo useradd bob
```

You'll see that the above command creates an entry in `/etc/passwd` for bob, sets up default groups, and adds an entry to the `/etc/shadow` file.

### Removing Users

To remove a user, you can use the `userdel` command.

```bash
sudo userdel bob
```

This basically does its best to undo the file changes made by `useradd`.

### Changing Passwords

```bash
passwd bob
```

This will allow you to change the password of yourself or another user (if you are root).

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of user and account management in Linux:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practice the complete lifecycle of user administration, from creating and securing new accounts to modifying and deleting them.
2. **[Manage Linux Groups with groupadd, usermod, and groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Gain hands-on experience with core command-line utilities for group administration, including adding, modifying, and deleting groups.
3. **[Configure User Accounts and Sudo Privileges in Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Learn essential techniques for managing user accounts and sudo privileges to enhance the security of a Linux system.

These labs will help you apply the concepts in real scenarios and build confidence with Linux user and group management.

## Quiz Question

What command is used to change a password?

## Quiz Answer

passwd
