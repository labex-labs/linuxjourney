---
index: 3
lang: "en"
title: "Process Details"
meta_title: "Process Details - Processes"
meta_description: "Learn about Linux process details, how the kernel manages resources, and what processes are. Understand process concepts for beginners."
meta_keywords: "Linux processes, kernel, process management, ps aux, Linux tutorial, beginner guide"
---

## Lesson Content

Before we get into more practical applications of processes, we have to first understand what they are and how they work. This part can get confusing since we are diving into the nitty-gritty, so feel free to come back to this lesson if you don't want to learn about it now.

A process, as we said before, is a running program on the system. More precisely, it's the system allocating memory, CPU, and I/O to make the program run. A process is an instance of a running program. Go ahead and open 3 terminal windows. In two windows, run the `cat` command without passing any options (the `cat` process will stay open as a process because it expects stdin). Now in the third window run: `ps aux | grep cat`. You'll see that there are two processes for `cat`, even though they are calling the same program.

The kernel is in charge of processes. When we run a program, the kernel loads up the code of the program in memory, determines and allocates resources, and then keeps tabs on each process. It knows:

- The status of the process
- The resources the process is using and receives
- The process owner
- Signal handling (more on that later)
- And basically everything else

All processes are trying to get a taste of that sweet resource pie. It's the kernel's job to make sure that processes get the right amount of resources depending on process demands. When a process ends, the resources it used are now freed up for other processes.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux processes and their management:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Learn essential skills for managing and monitoring processes on a Linux system, including interacting with foreground/background processes, inspecting with `ps`, monitoring with `top`, and terminating with `kill`.
2. **[Linux top Command: Real-time System Monitoring](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Learn to use the `top` command for real-time system monitoring, including sorting processes, adjusting update intervals, and filtering by user.
3. **[Linux free Command: Monitoring System Memory](https://labex.io/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Learn to use the `free` command to monitor and analyze system memory usage, understanding how the kernel allocates resources to processes.

These labs will help you apply the concepts in real scenarios and build confidence with process management in Linux.

## Quiz Question

What manages and controls processes?

## Quiz Answer

kernel
