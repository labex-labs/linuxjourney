---
lang: "en"
title: "The Sticky Bit"
meta_title: "The Sticky Bit - Permissions"
meta_description: "Learn about the Linux sticky bit, its purpose in shared directories like /tmp, and how to set it using chmod. Understand this key file permission!"
meta_keywords: "Linux sticky bit, chmod +t, /tmp directory, Linux permissions, file security, Linux tutorial, beginner Linux"
---

## Lesson Content

One last special permission bit I want to talk about is the sticky bit.

This permission bit "sticks a file/directory," meaning that only the owner or the root user can delete or modify the file. This is very useful for shared directories. Take a look at the example below:

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

You'll see a special permission bit at the end here **t**. This means everyone can add files, write files, and modify files in the `/tmp` directory, but only root can delete the `/tmp` directory.

### Modify sticky bit

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

The numerical representation for the sticky bit is **1**.

## Exercise

What other files and directories do you think have a sticky bit enabled?

## Quiz Question

What symbol represents the sticky bit?

## Quiz Answer

t
