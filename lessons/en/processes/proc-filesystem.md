---
index: 10
lang: "en"
title: "/proc filesystem"
meta_title: "/proc filesystem - Processes"
meta_description: "Discover the Linux /proc filesystem, a virtual directory that provides a dashboard-like view into the kernel and running processes. Learn how to access extra process details beyond standard commands."
meta_keywords: "/proc filesystem, linux proc, process information, linux proc extras, system dashboard, Linux processes, kernel information"
---

## Lesson Content

In Linux, a core principle is that everything is treated as a file. This concept extends to running processes, whose information is dynamically stored in a special virtual filesystem known as `/proc`.

### Exploring the /proc Directory

The `/proc` filesystem is not a real filesystem on your hard drive; it's created in memory by the kernel. It provides a window into the kernel's internal data structures and the state of the system.

To see its contents, you can list the files and directories within it:

```bash
ls /proc
```

You will see many numbered directories. Each number corresponds to the Process ID (PID) of a currently running process. You'll also find other files like `cpuinfo` and `meminfo` that provide system hardware information.

### Accessing Specific Process Information

If you identify a PID using a command like `ps`, you can find its corresponding directory in `/proc` to get more detailed information. For example, to inspect a process with PID 12345, you can look inside its status file:

```bash
cat /proc/12345/status
```

This command will display detailed information about the process, including its state (e.g., sleeping, running), memory usage, and user ID. The `/proc` directory offers the kernel's direct view of the process, providing far more data than standard tools.

### A Dashboard of System Data

Think of the `/proc` filesystem as the raw data source for many system monitoring tools. Utilities like `top`, `ps`, and `htop` read from `/proc` to present information in a user-friendly format. It contains a wealth of **extra** details that these tools might not show by default.

By directly accessing files within `/proc`, you can gather specific metrics to build custom scripts or a monitoring **dashboard** tailored to your needs. It's a powerful interface for observing and understanding the inner workings of your Linux system.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux processes and system monitoring:

1.  **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - In this lab, you will learn essential skills for managing and monitoring processes on a Linux system. You will explore how to interact with foreground and background processes, inspect them with `ps`, monitor resources with `top`, adjust priority with `renice`, and terminate them with `kill`.

These labs will help you apply the concepts in real scenarios and build confidence with process management and system observation.

## Quiz Question

What virtual filesystem stores process information? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

/proc
