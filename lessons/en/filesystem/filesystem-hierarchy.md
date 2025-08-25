---
index: 1
lang: "en"
title: "Filesystem Hierarchy"
meta_title: "Filesystem Hierarchy - The Filesystem"
meta_description: "Learn the Linux Filesystem Hierarchy Standard (FHS) and understand key directories like /bin, /etc, and /var. Explore the Linux directory structure."
meta_keywords: "Linux Filesystem Hierarchy, FHS, Linux directory structure, Linux commands, beginner Linux, Linux tutorial, Linux guide"
---

## Lesson Content

At this point, you're probably well familiar with the directory structure of your system; if not, you will be soon. Filesystems can vary in how they are structured, but for the most part, they should conform to the Filesystem Hierarchy Standard.

Go ahead and do an `ls -l /` to see the directories listed under the root directory. Yours may look different from mine, but the directories should for the most part look like the following:

- `/` - The root directory of the entire filesystem hierarchy; everything is nestled under this directory.
- `/bin` - Essential ready-to-run programs (binaries); includes the most basic commands such as `ls` and `cp`.
- `/boot` - Contains kernel boot loader files.
- `/dev` - Device files.
- `/etc` - Core system configuration directory; should hold only configuration files and not any binaries.
- `/home` - Personal directories for users; holds your documents, files, settings, etc.
- `/lib` - Holds library files that binaries can use.
- `/media` - Used as an attachment point for removable media like USB drives.
- `/mnt` - Temporarily mounted filesystems.
- `/opt` - Optional application software packages.
- `/proc` - Information about currently running processes.
- `/root` - The root user's home directory.
- `/run` - Information about the running system since the last boot.
- `/sbin` - Contains essential system binaries, usually can only be run by root.
- `/srv` - Site-specific data which are served by the system.
- `/tmp` - Storage for temporary files.
- `/usr` - This is unfortunately named; most often it does not contain user files in the sense of a home folder. This is meant for user-installed software and utilities; however, that is not to say you can't add personal directories in there. Inside this directory are sub-directories for `/usr/bin`, `/usr/local`, etc.
- `/var` - Variable directory; it's used for system logging, user tracking, caches, etc. Basically anything that is subject to change all the time.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of the Linux filesystem:

1. **[Navigate the Filesystem in Linux](https://labex.io/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Practice using essential shell commands like `pwd`, `cd`, and `ls` to move between directories and explore the filesystem.
2. **[Manage Files and Directories in Linux](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835)** - Learn to create, remove, copy, and move files and directories, and understand symbolic and hard links.
3. **[Find Files and Commands in Linux](https://labex.io/labs/comptia-find-files-and-commands-in-linux-590834)** - Master techniques for locating files and commands using `find`, `locate`, `whereis`, `which`, and `type`.

These labs will help you apply the concepts in real scenarios and build confidence with Linux filesystem management.

## Quiz Question

What directory is used to store logs?

## Quiz Answer

/var
