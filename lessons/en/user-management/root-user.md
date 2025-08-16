---
title: "root"
description: "Learn about Linux root user, su command, and /etc/sudoers file. Understand superuser access and permissions in Linux with this beginner guide."
keywords: "Linux root, su command, sudoers file, Linux permissions, superuser, Linux tutorial, beginner guide"
---

## Lesson Content

We've looked at one way to get superuser access using the `sudo` command. You can also run commands as the superuser with the `su` command. This command will "substitute users" and open a root shell if no username is specified. You can use this command to substitute to any user as long as you know the password.

```bash
su
```

There are some downsides to using this method: it's much easier to make a critical mistake running everything as root, you won't have records of the commands you use to change system configurations, etc. Basically, if you need to run commands as the superuser, just stick to `sudo`.

Now that you know what commands to run as the superuser, the question is how do you know who has access to do that? The system doesn't let every single Joe Schmoe run commands as the superuser, so how does it know? There is a file called the `/etc/sudoers` file; this file lists users who can run `sudo`. You can edit this file with the **visudo** command.

## Exercise

Open up the `/etc/sudoers` file and see what superuser permissions other users on the machine have.

## Quiz Question

What file shows the users who have access to `sudo`?

## Quiz Answer

/etc/sudoers
