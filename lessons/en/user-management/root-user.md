---
index: 2
lang: "en"
title: "root"
meta_title: "root - User Management"
meta_description: "Explore the role of the root user in Linux. This lesson covers the differences between su and sudo for gaining superuser privileges and explains how the /etc/sudoers file manages access."
meta_keywords: "root user in linux, linux root user, su, sudo, sudoers, visudo, superuser, user management, linux permissions"
---

## Lesson Content

In Linux, certain administrative tasks require elevated privileges. These privileges belong to a special account known as the **root user in Linux**. While you can log in directly as root, it is often safer and more manageable to gain superuser access temporarily.

### The `su` Command

Besides the `sudo` command, you can use `su` (substitute user) to gain superuser privileges. When run without a username, `su` attempts to open a new shell session for the **linux root user**, prompting you for the root password.

```bash
su
```

You can also use this command to switch to any other user on the system, provided you know their password.

### Risks of a Persistent Root Shell

Using `su` to open a root shell has significant downsides. Operating continuously as the root user increases the risk of making a critical, system-altering mistake. Furthermore, actions performed in a root shell are not logged under your personal user account, making it difficult to audit system changes. For these reasons, it is best practice to use `sudo` for individual commands that require superuser access.

### The `sudoers` File

So, how does the system determine who is allowed to use `sudo`? Access is controlled by a configuration file located at `/etc/sudoers`. This file lists the users and groups who are granted permission to run commands as the superuser.

To edit this file safely, you should always use the `visudo` command. This utility opens the `sudoers` file in a text editor and performs a syntax check before saving, which helps prevent configuration errors that could lock you out of administrative access.

## Exercise

Put your knowledge into practice. The following hands-on lab will help reinforce your understanding of superuser access and privileges:

1. **[Configure User Accounts and Sudo Privileges in Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Practice enforcing password policies, locking and unlocking user accounts, securing the root account, and granting administrative permissions, directly relating to the management of superuser access.

This lab will help you apply the concepts in real scenarios and build confidence with managing user privileges and superuser access.

## Quiz Question

What file lists the users and groups with `sudo` privileges? Please provide the full path. (Note: Your answer must be in English and is case-sensitive).

## Quiz Answer

/etc/sudoers
