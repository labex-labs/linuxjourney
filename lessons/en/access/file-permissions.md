---
index: 1
lang: "en"
title: "File Permissions"
meta_title: "File Permissions - Permissions"
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

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux file permissions, users, and groups:

1. **[Linux User Group and File Permissions](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002)** - Learn essential Linux user and group management concepts, including creating users, exploring group memberships, understanding file permissions, and manipulating file ownership.
2. **[Add New User and Group](https://labex.io/labs/linux-add-new-user-and-group-17987)** - Practice creating new user accounts, setting up custom groups, and managing group memberships, simulating real-world system administration tasks.
3. **[Find a File](https://labex.io/labs/linux-find-a-file-17993)** - Apply your knowledge of file permissions by finding a specific file and setting its access authority, ensuring you're the only authorized user.

These labs will help you apply the concepts in real scenarios and build confidence with managing permissions and users in Linux.

## Quiz Question

What permission bit is used for executable?

## Quiz Answer

x
