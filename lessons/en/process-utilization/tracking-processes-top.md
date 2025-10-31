---
index: 1
lang: "en"
title: "Tracking processes: top"
meta_title: "Tracking processes: top - Process Utilization"
meta_description: "Discover the best way to learn Linux by mastering the `top` command. This guide explains how to monitor system resources, track processes, and understand metrics like VIRT and RES. A key part of understanding how Linux works."
meta_keywords: "Linux top command, monitor processes, system utilization, how linux works, linux top virt res, best way to learn linux, linux performance, process management, free online linux training with certificate"
---

## Lesson Content

Understanding how to read and analyze resource utilization is a critical skill for any Linux user. Many consider mastering command-line tools the **best way to learn Linux** from the ground up, as they provide deep insight into **how Linux works**. This lesson introduces `top`, a powerful utility for tracking what your processes are doing in real-time.

### Understanding the top Command

We have briefly mentioned `top` before, but now we will dig into the specifics of what it displays. The `top` command gives you a dynamic, real-time view of the processes and system utilization on your machine.

```plaintext
top - 18:06:26 up 6 days,  4:07,  2 users,  load average: 0.92, 0.62, 0.59
Tasks: 389 total,   1 running, 387 sleeping,   0 stopped,   1 zombie
%Cpu(s):  1.8 us,  0.4 sy,  0.0 ni, 97.6 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:  32870888 total, 27467976 used,  5402912 free,   518808 buffers
KiB Swap: 33480700 total,    39892 used, 33440808 free. 19454152 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 6675 patty    20   0 1731472 520960  30876 S   8.3  1.6 160:24.79 chrome
 6926 patty    20   0  935888 163456  25576 S   4.3  0.5   5:28.13 chrome
```

Let's go over what this output means. You don't have to memorize this, but you can use this lesson as a reference.

### System Summary

The first few lines provide a high-level summary of the system's state.

- **1st line**: This is the same information you would see if you ran the `uptime` command. It shows the current time, system uptime, number of logged-in users, and the system load average over the last 1, 5, and 15 minutes.
- **2nd line**: A summary of all tasks (processes), categorized as running, sleeping, stopped, or zombie.

### CPU Usage Breakdown

The third line details the CPU utilization.

- `us`: Percentage of CPU time spent running user processes that are not niced.
- `sy`: Percentage of CPU time spent running the kernel and its processes.
- `ni`: Percentage of CPU time spent running niced (low priority) user processes.
- `id`: Percentage of CPU time that is idle.
- `wa`: Percentage of CPU time spent waiting for I/O operations to complete. A high value might indicate a disk or network bottleneck.
- `hi`: Percentage of CPU time spent servicing hardware interrupts.
- `si`: Percentage of CPU time spent servicing software interrupts.
- `st`: Steal time. In virtualized environments, this is the percentage of CPU time a virtual CPU waits for a real CPU, while the hypervisor is servicing another virtual processor.

### Memory and Swap Information

The fourth and fifth lines show memory and swap space usage, respectively. This includes total, used, and free amounts.

### The Process List

The main body of `top` is a list of the most resource-intensive processes.

- `PID`: The unique Process ID.
- `USER`: The user who owns the process.
- `PR`: The scheduling priority of the process.
- `NI`: The "nice" value, which affects its priority.
- `VIRT`: Virtual Memory used by the process. This is the total amount of memory the process can access.
- `RES`: Resident Memory used by the process. This is the non-swapped physical memory a task is using. Understanding the difference between **linux top virt res** is key for memory analysis.
- `SHR`: Shared Memory used by the process.
- `S`: The status of the process: `S`=sleep, `R`=running, `Z`=zombie, `D`=uninterruptible sleep, `T`=stopped.
- `%CPU`: The percentage of CPU time used by this process since the last update.
- `%MEM`: The percentage of physical RAM used by this process.
- `TIME+`: The total CPU time the process has used since it started.
- `COMMAND`: The command name or command line that started the process.

You can also monitor a specific process by its ID, which is useful for focused troubleshooting:

```bash
top -p 1
```

## Exercise

Practice is essential for mastery. These hands-on labs are some of the **best resources to learn Linux** process management, providing a practical environment to apply what you've learned.

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with, inspecting, monitoring, and terminating processes in a real Linux environment.
2. **[Linux top Command: Real-time System Monitoring](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Learn to use the `top` command to monitor CPU usage, memory, and running processes in real-time.
3. **[Linux free Command: Monitoring System Memory](https://labex.io/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Learn to use the `free` command to monitor and analyze system memory usage.

## Quiz Question

What command displays the same output as the first line in `top`? Please answer using only the lowercase English command name.

## Quiz Answer

uptime
