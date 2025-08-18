---
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

Run the command `groups`. What do you see?

## Quiz Question

What is the GID of root?

## Quiz Answer

0
