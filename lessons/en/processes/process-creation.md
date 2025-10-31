---
index: 4
lang: "en"
title: "Process Creation"
meta_title: "Process Creation - Processes"
meta_description: "Explore the fundamentals of process creation in Linux. This guide covers the fork and execve system calls, parent/child relationships (PID and PPID), and the role of the init process. Learn how to create a process in Linux and understand the core concepts of process creation in the operating system."
meta_keywords: "process creation in linux, linux process creation, create a process in linux, process creation in operating system, process creation, fork, execve, PID, PPID, init process, Linux processes"
---

## Lesson Content

This lesson explores the fundamental concepts of how new processes are started on a Linux system. Understanding this mechanism provides insight into the inner workings of the operating system.

### The Fork and Exec Model

The primary mechanism for **process creation in Linux** involves an existing process cloning itself using the `fork` system call. The `fork` call creates a nearly identical child process. This new child process receives its own unique Process ID (PID), while the original process becomes its parent, identified by a Parent Process ID (**PPID**).

After forking, the child process can either continue running the same program as its parent or, more commonly, use the `execve` system call to load and run a new program. The `execve` call effectively replaces the process's memory space with that of the new program, allowing a different task to begin. This two-step "fork-exec" model is a cornerstone of how you **create a process in Linux**.

### Observing Parent-Child Relationships

We can observe this parent-child relationship in action using the `ps` command:

```bash
ps l
```

The `l` option provides a "long format" view, showing more detail about running processes. You will see a column labeled **PPID**, which stands for Parent Process ID. Look at the process for your current shell (e.g., `bash`). When you run the `ps l` command, you'll notice that the **PID** of your shell process matches the **PPID** of the `ps l` process. This is because your shell forked itself to create the `ps` process.

### The Init Process

If every process is a child of another, there must be an original ancestor. This is the `init` process. When the system boots, the kernel creates `init` as the very first user-space process, assigning it a PID of 1. The `init` process is the ultimate parent of all other processes and runs with root privileges to manage the system. It cannot be terminated until the system shuts down and is responsible for spawning many of the services that keep the system running.

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of Linux processes and their management:

- **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - In this lab, you will learn essential skills for managing and monitoring processes on a Linux system. You will explore how to interact with foreground and background processes, inspect them with `ps`, monitor resources with `top`, adjust priority with `renice`, and terminate them with `kill`.

This lab will help you apply the concepts of process IDs, parent process IDs, and process monitoring in a real scenario and build confidence with process management.

## Quiz Question

What system call creates a new process? (Please answer in a single lowercase English word.)

## Quiz Answer

fork
