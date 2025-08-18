---
lang: "en"
title: "Filesystem Repair"
meta_description: "Learn to use fsck for Linux filesystem repair and data recovery. Understand how to check and fix disk errors with this essential command. Start your Linux journey!"
meta_keywords: "fsck, filesystem repair, Linux commands, disk errors, data recovery, Linux tutorial, beginner guide"
---

## Lesson Content

Sometimes our filesystem isn't always in the best condition. If we have a sudden shutdown, our data can become corrupt. It's up to the system to try to get us back into a working state (although we certainly can try ourselves).

The **fsck** (filesystem check) command is used to check the consistency of a filesystem and can even try to repair it for us. Usually, when you boot up a disk, fsck will run before your disk is mounted to make sure everything is okay. Sometimes, though, your disk is so bad that you'll need to manually do this. However, be sure to do this while you are in a rescue disk or somewhere where you can access your filesystem without it being mounted.

```bash
sudo fsck /dev/sda
```

## Exercise

Look at the manpage for fsck to see what else it can do.

## Quiz Question

What command is used to check the integrity of a filesystem?

## Quiz Answer

fsck
