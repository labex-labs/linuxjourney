---
index: 10
lang: "en"
title: "/proc filesystem"
meta_title: "/proc filesystem - Processes"
meta_description: "Learn about the /proc filesystem in Linux, how it stores process information, and its structure. Explore process details with this essential Linux guide."
meta_keywords: "/proc filesystem, Linux processes, process information, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Remember, everything in Linux is a file, even processes. Process information is stored in a special filesystem known as the `/proc` filesystem.

```bash
ls /proc
```

You should see multiple values here; there are subdirectories for every PID. If you looked at a PID in the `ps` output, you would be able to find it in the `/proc` directory.

Go ahead and enter one of the processes and look at that file:

```bash
cat /proc/12345/status
```

You should see process state information as well as more detailed information. The `/proc` directory is how the kernel views the system, so there is a lot more information here than what you would see in `ps`.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux processes and system monitoring:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - In this lab, you will learn essential skills for managing and monitoring processes on a Linux system. You will explore how to interact with foreground and background processes, inspect them with `ps`, monitor resources with `top`, adjust priority with `renice`, and terminate them with `kill`.

These labs will help you apply the concepts in real scenarios and build confidence with process management and system observation.

## Quiz Question

What filesystem stores process information?

## Quiz Answer

/proc
