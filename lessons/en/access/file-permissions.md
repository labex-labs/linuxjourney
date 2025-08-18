---
lang: "en"
title: "File Permissions"
meta_description: "Learn Linux file permissions: understand rwx bits, user, group, and other permissions. Master `ls -l` output for beginners. Start your Linux journey!"
meta_keywords: "Linux file permissions, ls -l command, rwx permissions, Linux tutorial, file modes, beginner Linux, Linux guide"
---

## Lesson Content

As we learned previously, files have different permissions or file modes. Let's look at an example:

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
```

There are four parts to a file's permissions. The first part is the file type, which is denoted by the first character in the permissions. In our case, since we are looking at a directory, it shows **d** for the file type. Most commonly, you will see a **-** for a regular file.

The next three parts of the file mode are the actual permissions. The permissions are grouped into 3 bits each. The first 3 bits are user permissions, then group permissions, and then other permissions. I've added the pipe to make it easier to differentiate.

```plaintext
d | rwx | r-x | r-x
```

Each character represents a different permission:

- r: readable
- w: writable
- x: executable (basically an executable program)
- -: empty

So in the above example, we see that the user pete has read, write, and execute permissions on the file. The group penguins has read and execute permissions. And finally, the other users (everyone else) have read and execute permissions.

## Exercise

Use the `ls -l` command on multiple files and recite their permissions, user, and group.

## Quiz Question

What permission bit is used for executable?

## Quiz Answer

x
