---
index: 1
lang: "en"
title: "System V Overview"
meta_title: "System V Overview - Init"
meta_description: "Learn about System V init, its runlevels, and how it manages processes in Linux. Understand SysV basics for beginners and intermediate users."
meta_keywords: "System V, SysV init, Linux runlevels, init system, Linux tutorial, beginner guide, process management"
---

## Lesson Content

The main purpose of init is to start and stop essential processes on the system. There are three major implementations of init in Linux: System V, Upstart, and systemd. In this lesson, we're going to go over the most traditional version of init, System V init or Sys V (pronounced as 'System Five').

To find out if you are using the Sys V init implementation, check for an `/etc/inittab` file; if it exists, you are most likely running Sys V.

Sys V starts and stops processes sequentially. For example, if you wanted to start a service named `foo-a`, `foo-b` cannot work until `foo-a` is already running. Sys V accomplishes this with scripts. These scripts start and stop services for us. We can write our own scripts, or most of the time, use the ones that are already built into the operating system and are used to load essential services.

The pros of using this init implementation are that it's relatively easy to solve dependencies, since you know `foo-a` comes before `foo-b`. However, performance isn't great because usually only one thing is starting or stopping at a time.

When using Sys V, the state of the machine is defined by runlevels, which are set from 0 to 6. These different modes will vary depending on the distribution, but most of the time will look like the following:

- 0: Shutdown
- 1: Single User Mode
- 2: Multiuser mode without networking
- 3: Multiuser mode with networking
- 4: Unused
- 5: Multiuser mode with networking and GUI
- 6: Reboot

When your system starts up, it looks to see what runlevel you are in and executes scripts located inside that runlevel configuration. The scripts are located in **/etc/rc.d/rc[runlevel number].d/** or **/etc/init.d**. Scripts that start with S (start) or K (kill) will run on startup and shutdown, respectively. The numbers next to these characters indicate the sequence in which they run.

For example:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

We see that when we switch to runlevel 0 or shutdown mode, our machine will try to run a script to kill the updates services and then OpenVPN. To find out what runlevel your machine is booting into, you can see the default runlevel in the `/etc/inittab` file. You can also change your default runlevel in this file.

One thing to note: System V is slowly getting replaced, maybe not today, or even years from now. However, you may see runlevels come up in other init implementations. This is primarily to support those services that are only started or stopped using System V init scripts.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux process management and system configuration, which are foundational to how init systems operate:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with foreground and background processes, inspecting them with `ps`, monitoring resources with `top`, and terminating them with `kill`. This directly relates to the 'start and stop essential processes' aspect of init.
2. **[Schedule Tasks with at and cron in Linux](https://labex.io/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Learn to schedule one-time and recurring tasks, which builds on the concept of automated execution similar to how init scripts manage services.
3. **[Manage File and Directory Permissions in Linux](https://labex.io/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Understand how to manage file and directory permissions, a critical skill for working with system configuration files and scripts like those found in `/etc/init.d`.

These labs will help you apply the concepts in real scenarios and build confidence with fundamental Linux system administration tasks.

## Quiz Question

What runlevel is usually used for shutdown?

## Quiz Answer

0
