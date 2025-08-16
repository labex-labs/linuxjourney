---
title: "tail"
description: "Learn how to use the `tail` command in Linux to view file ends and monitor logs. Discover `tail -f` for real-time updates. Start your Linux journey!"
keywords: "tail command, Linux tail, tail -f, view logs, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Similar to the `head` command, the `tail` command lets you see the last 10 lines of a file by default.

```bash
tail /var/log/syslog
```

Along with `head`, you can change the number of lines you want to see.

```bash
tail -n 10 /var/log/syslog
```

Another great option you can use is the `-f` (follow) flag; this will follow the file as it grows. Give it a try and see what happens.

```bash
tail -f /var/log/syslog
```

Your `syslog` file will be continually changing while you interact with your system, and using `tail -f` you can see everything that is getting added to that file.

## Exercise

Look at the man page of `tail` and read some of the other commands we didn't discuss.

```bash
man tail
```

## Quiz Question

What is the flag used to follow a file in `tail`?

## Quiz Answer

-f
