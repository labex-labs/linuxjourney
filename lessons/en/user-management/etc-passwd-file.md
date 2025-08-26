---
index: 3
lang: "en"
title: "/etc/passwd"
meta_title: "/etc/passwd - User Management"
meta_description: "Learn about the /etc/passwd file in Linux, understand user information fields, and how UIDs work. Explore this essential configuration file."
meta_keywords: "/etc/passwd, Linux users, user ID, UID, Linux tutorial, beginner, guide, Linux commands"
---

## Lesson Content

Remember that usernames aren't really identifications for users. The system uses a user ID (UID) to identify a user. To find out what users are mapped to what ID, look at the `/etc/passwd` file.

```bash
cat /etc/passwd
```

This file shows you a list of users and detailed information about them. For example, the first line in this file most likely looks like this:

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Each line displays user information for one user; most commonly, you'll see the root user as the first line. There are many fields separated by colons that tell you additional information about the user. Let's look at them all:

1. **Username**
2. **User's password** - The password is not really stored in this file; it's usually stored in the `/etc/shadow` file. We'll discuss more about `/etc/shadow` in the next lesson, but for now, know that it contains encrypted user passwords. You can see many different symbols in this field: if you see an "x," that means the password is stored in the `/etc/shadow` file; a "\*" means the user doesn't have login access; and if there is a blank field, that means the user doesn't have a password.
3. **The user ID** - As you can see, root has the UID of 0.
4. **The group ID**
5. **GECOS field** - This is used to generally leave comments about the user or account, such as their real name or phone number. It is comma-delimited.
6. **User's home directory**
7. **User's shell** - You'll probably see a lot of users defaulting to bash for their shell.

Normally, in a user's setting page, you would expect to see just human users. However, you'll notice `/etc/passwd` contains other users. Remember that users are really only on the system to run processes with different permissions. Sometimes we want to run processes with predetermined permissions. For example, the `daemon` user is used for daemon processes.

Also, it should be noted that you can edit the `/etc/passwd` file by hand if you want to add users and modify information with the `vipw` tool. However, things like these are best left to the tools we will discuss in a later lesson, such as `useradd` and `userdel`.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux user accounts and their management:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practice the complete lifecycle of user administration, from creating and securing new accounts to modifying and deleting them.
2. **[Manage Linux Groups with groupadd, usermod, and groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Gain hands-on experience with core command-line utilities for group administration, including creating new groups and modifying user memberships.
3. **[Configure User Accounts and Sudo Privileges in Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Learn essential techniques for managing user accounts and sudo privileges to enhance the security of a Linux system.

These labs will help you apply the concepts of user IDs and account management in real scenarios and build confidence with Linux user administration.

## Quiz Question

If a user doesn't have login access, how is that denoted in `/etc/passwd`?

## Quiz Answer

*
