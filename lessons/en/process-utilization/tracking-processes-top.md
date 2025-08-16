---
title: "Tracking processes: top"
description: "Learn how to use the Linux `top` command to monitor system resources and track processes. Understand CPU, memory, and process details for performance analysis."
keywords: "Linux top command, monitor processes, system utilization, Linux performance, beginner, tutorial, guide"
---

## Lesson Content

In this course, we'll go over how to read and analyze the resource utilization on your system. This lesson shows some great tools to use when you need to track what a process is doing.

### top

We've discussed `top` before, but we're going to dig into the specifics of what it's actually displaying. Remember, `top` is the tool we used to get a real-time view of the system utilization by our processes:

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

Let's go over what this output means. You don't have to memorize this, but come back to this when you need a reference.

### 1st line: This is the same information you would see if you ran the `uptime` command (more to come)

The fields are from left to right:

1. Current time
2. How long the system has been running
3. How many users are currently logged on
4. System load average (more to come)

### 2nd line: Tasks that are running, sleeping, stopped, and zombied

### 3rd line: CPU information

1. `us`: user CPU time - Percentage of CPU time spent running users’ processes that aren’t niced.
2. `sy`: system CPU time - Percentage of CPU time spent running the kernel and kernel processes.
3. `ni`: nice CPU time - Percentage of CPU time spent running niced processes.
4. `id`: CPU idle time - Percentage of CPU time that is spent idle.
5. `wa`: I/O wait - Percentage of CPU time that is spent waiting for I/O. If this value is low, the problem probably isn’t disk or network I/O.
6. `hi`: hardware interrupts - Percentage of CPU time spent serving hardware interrupts.
7. `si`: software interrupts - Percentage of CPU time spent serving software interrupts.
8. `st`: steal time - If you are running virtual machines, this is the percentage of CPU time that was stolen from you for other tasks.

### 4th and 5th line: Memory Usage and Swap Usage

### Processes List that are Currently in Use

1. `PID`: ID of the process
2. `USER`: user that is the owner of the process
3. `PR`: Priority of process
4. `NI`: The nice value
5. `VIRT`: Virtual memory used by the process
6. `RES`: Physical memory used by the process
7. `SHR`: Shared memory of the process
8. `S`: Indicates the status of the process: `S`=sleep, `R`=running, `Z`=zombie, `D`=uninterruptible, `T`=stopped
9. `%CPU`: this is the percent of CPU used by this process
10. `%MEM`: percentage of RAM used by this process
11. `TIME+`: total time of activity of this process
12. `COMMAND`: name of the process

You can also specify a process ID if you just want to track certain processes:

```bash
top -p 1
```

## Exercise

Play around with the `top` command and see what processes are using the most resources.

## Quiz Question

What command displays the same output as the first line in `top`?

## Quiz Answer

uptime
