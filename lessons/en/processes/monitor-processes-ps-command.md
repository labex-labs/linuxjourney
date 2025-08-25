---
index: 1
lang: "en"
title: "ps (Processes)"
meta_title: "ps (Processes) - Processes"
meta_description: "Learn about the Linux 'ps' command to view running processes and understand process IDs (PIDs). Get a beginner's guide to process management."
meta_keywords: "ps command, Linux processes, process ID, PID, Linux tutorial, beginner, guide, top command"
---

## Lesson Content

Processes are the programs that are running on your machine. They are managed by the kernel, and each process has an ID associated with it called the **process ID (PID)**. This PID is assigned in the order that processes are created.

Go ahead and run the `ps` command to see a list of running processes:

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

This shows you a quick snapshot of the current processes:

- PID: Process ID
- TTY: Controlling terminal associated with the process (we'll go into detail about this later)
- STAT: Process status code
- TIME: Total CPU usage time
- CMD: Name of executable/command

If you look at the man page for `ps`, you'll see that there are lots of command options you can pass. They will vary depending on what options you want to use — BSD, GNU, or Unix. In my opinion, the BSD style is more popular to use, so we're going to go with that. If you are curious, the difference between the styles is the amount of dashes you use and the flags.

```bash
ps aux
```

The **a** displays all processes running, including the ones being run by other users. The **u** shows more details about the processes. And finally, the **x** lists all processes that don't have a TTY associated with them. These programs will show a `?` in the TTY field; they are most common in daemon processes that launch as part of the system startup.

You'll notice you're seeing a lot more fields now. No need to memorize them all; in a later course on advanced processes, we'll go over some of these again:

- USER: The effective user (the one whose access we are using)
- PID: Process ID
- %CPU: CPU time used divided by the time the process has been running
- %MEM: Ratio of the process's resident set size to the physical memory on the machine
- VSZ: Virtual memory usage of the entire process
- RSS: Resident set size, the non-swapped physical memory that a task has used
- TTY: Controlling terminal associated with the process
- STAT: Process status code
- START: Start time of the process
- TIME: Total CPU usage time
- COMMAND: Name of executable/command

The `ps` command can get a little messy to look at. For now, the fields we will look at the most are PID, STAT, and COMMAND.

Another very useful command is the **top** command. `top` gives you real-time information about the processes running on your system instead of a snapshot. By default, you'll get a refresh every 10 seconds. `top` is an extremely useful tool to see what processes are taking up a lot of your resources.

```bash
top
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux processes and their monitoring:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice essential skills for managing and monitoring processes on a Linux system, including interacting with foreground/background processes, inspecting with `ps`, monitoring with `top`, and terminating with `kill`.
2. **[Linux top Command: Real-time System Monitoring](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Learn to use the Linux `top` command for real-time system monitoring, including sorting processes, adjusting update intervals, and filtering by user.

These labs will help you apply the concepts of process identification and monitoring in real scenarios and build confidence with Linux system administration.

## Quiz Question

What `ps` flag is used to view detailed information about processes?

## Quiz Answer

u
