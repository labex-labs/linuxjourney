---
index: 6
lang: "en"
title: "User Management Tools"
meta_title: "User Management Tools - User Management"
meta_description: "Master Linux user management with essential command-line tools. This guide covers using useradd, userdel, and passwd for managing accounts in Linux, perfect for beginners."
meta_keywords: "linux user management, the command-line tool for managing accounts in linux, useradd, userdel, passwd, linux accounts, manage users linux"
---

## Lesson Content

While many enterprise environments rely on dedicated systems for identity management, understanding the fundamentals of **Linux user management** directly on a single machine is a crucial skill. Several utilities serve as **the command-line tool for managing accounts in Linux**, allowing for efficient administration from the terminal.

### Adding Users

To create a new user, you can use the `useradd` command. It is a low-level utility that creates a new user account based on default values found in `/etc/default/useradd`. While some systems also offer `adduser`, a more interactive and user-friendly script, `useradd` is the universal standard.

```bash
sudo useradd bob
```

Executing this command adds an entry for the user "bob" in the `/etc/passwd` file, sets up default group memberships, and creates a corresponding entry in the `/etc/shadow` file to store password information securely.

### Removing Users

To remove a user account, you can use the `userdel` command. This command effectively reverses the changes made by `useradd` by removing the user's entries from the system account files.

```bash
sudo userdel bob
```

By default, this command may not remove the user's home directory. You can use the `-r` flag (`userdel -r bob`) to ensure the home directory and mail spool are also deleted.

### Changing Passwords

The `passwd` command is used to set or change a user's password. A regular user can run this command to change their own password. The root user can run it to change any user's password.

```bash
passwd bob
```

When run by an administrator, the system will prompt for a new password for the specified user without asking for the old one. This is a fundamental task in **Linux user management**.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of user and account management in Linux:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practice the complete lifecycle of user administration, from creating and securing new accounts to modifying and deleting them.
2. **[Manage Linux Groups with groupadd, usermod, and groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Gain hands-on experience with core command-line utilities for group administration, including adding, modifying, and deleting groups.
3. **[Configure User Accounts and Sudo Privileges in Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Learn essential techniques for managing user accounts and sudo privileges to enhance the security of a Linux system.

These labs will help you apply the concepts in real scenarios and build confidence with Linux user and group management.

## Quiz Question

What command is used to change a password? Please answer with the command name in lowercase English letters only.

## Quiz Answer

passwd
