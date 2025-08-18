---
lang: "en"
title: "Setgid"
meta_description: "Learn about Linux SGID (Set Group ID) permissions, how they work, and how to modify them. Understand this crucial Linux security concept."
meta_keywords: "Linux SGID, Set Group ID, Linux permissions, chmod g+s, Linux security, beginner Linux, Linux tutorial"
---

## Lesson Content

Similar to the set user ID permission bit, there is a set group ID (SGID) permission bit. This bit allows a program to run as if it were a member of that group.

Let's look at one example:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

We can now see that the permission bit is in the group permission set.

### Modifying SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

The numerical representation for SGID is 2.

## Exercise

No exercises for this lesson.

## Quiz Question

What number represents the SGID?

## Quiz Answer

2
