---
lang: "en"
title: "Umask"
description: "Learn how to use the `umask` command to control default file permissions in Linux. Understand numerical permissions and manage new file access easily."
keywords: "umask, linux permissions, file permissions, linux commands, beginner linux, linux tutorial, default permissions"
---

## Lesson Content

Every file that gets created comes with a default set of permissions. If you ever want to change that default set of permissions, you can do so with the `umask` command. This command uses the 3-bit permission set we see in numerical permissions.

Instead of adding these permissions, however, `umask` takes away these permissions.

```bash
umask 021
```

In the above example, we are stating that we want the default permissions of new files to allow users access to everything, but for groups, we want to take away their write permission, and for others, we want to take away their executable permission. The default `umask` on most distributions is `022`, meaning full user access, but no write access for group and other users.

When you run the `umask` command, it will apply that default set of permissions to any new file you create. However, if you want it to persist, you'll have to modify your startup file (`.profile`), but we'll discuss that in a later lesson.

## Exercise

1. Create a new file, then note its permissions.
2. Modify the `umask` and then create another new file.
3. Check the permissions once more on the new file. What do you expect to see?

## Quiz Question

What command is used to change default file permissions?

## Quiz Answer

umask
