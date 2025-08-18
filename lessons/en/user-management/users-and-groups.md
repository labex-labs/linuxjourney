---
index: 1
lang: "en"
title: "Users and Groups"
meta_title: "Users and Groups - User Management"
meta_description: "Learn about Linux users and groups, understand UIDs, GIDs, and the root user. Discover how to use the sudo command for elevated permissions. Start your Linux journey!"
meta_keywords: "Linux users, Linux groups, sudo command, root user, Linux permissions, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

In any traditional operating system, there are users and groups. They exist solely for access and permissions. When running a process, it will run as the owner of that process, whether that is Jane or Bob. File access and ownership is also permission-dependent. You wouldn't want Jane to see Bob's documents and vice versa.

Each user has their own home directory where their user-specific files are stored. This is usually located in `/home/username`, but can vary in different distributions.

The system uses user IDs (UID) to manage users. Usernames are the friendly way to associate users with identification, but the system identifies users by their UID. The system also uses groups to manage permissions. Groups are just sets of users with permissions set by that group; they are identified by the system with their group ID (GID).

In Linux, you'll have users in addition to the normal humans that use the system. Sometimes these users are system daemons that continuously run processes to keep the system functioning. One of the most important users is `root` or `superuser`. `root` is the most powerful user on the system; `root` can access any file and start and terminate any process. For that reason, it can be dangerous to operate as `root` all the time; you could potentially remove system-critical files. Luckily, if `root` access is needed and a user has `root` access, they can run a command as `root` instead with the `sudo` command. The `sudo` command (superuser do) is used to run a command with `root` access. We'll go more in depth on how a user receives `root` access in a later lesson.

Go ahead and try to view a protected file like `/etc/shadow`:

```bash
cat /etc/shadow
```

Notice how you get a permission denied error. Look at the permissions with:

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

We haven't gone through permissions yet, but what's happening here is that `root` is the owner of the file, and you'll need `root` access or be part of the `shadow` group to read the contents. Now run the command with `sudo`:

```bash
sudo cat /etc/shadow
```

Now you'll be able to see the contents of the file!

## Exercise

No exercises for this lesson.

## Quiz Question

What command do you use to run as `root`?

## Quiz Answer

sudo
