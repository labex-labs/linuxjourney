---
index: 4
lang: "en"
title: "Process Creation"
meta_title: "Process Creation - Processes"
meta_description: "Learn about Linux process creation, fork, and parent/child processes. Understand PID, PPID, and the init process. Get a beginner's guide to Linux process management."
meta_keywords: "Linux process creation, fork, PID, PPID, init process, Linux processes, beginner, tutorial, guide"
---

## Lesson Content

Again, this lesson and the next are purely informational to let you see what's under the hood. Feel free to circle back to this once you've worked with processes a bit more.

When a new process is created, an existing process basically clones itself using something called the `fork` system call (system calls will be discussed very far into the future). The `fork` system call creates a mostly identical child process. This child process takes on a new process ID (PID), and the original process becomes its parent process and has something called a parent process ID **PPID**. Afterwards, the child process can either continue to use the same program its parent was using before or, more often, use the `execve` system call to launch a new program. This system call destroys the memory management that the kernel put into place for that process and sets up new ones for the new program.

We can see this in action:

```bash
ps l
```

The `l` option gives us a "long format" or even more detailed view of our running processes. You'll see a column labeled **PPID**; this is the parent ID. Now look at your terminal; you'll see a process running that is your shell. So on my system, I have a process running `bash`. Now remember when you ran the `ps l` command, you were running it from the process that was running `bash`. You'll see that the **PID** of the `bash` shell is the **PPID** of the `ps l` command.

So if every process has to have a parent and they are just forks of each other, there must be a mother of all processes, right? You are correct. When the system boots up, the kernel creates a process called **init**; it has a PID of 1. The `init` process can't be terminated unless the system shuts down. It runs with root privileges and runs many processes that keep the system running. We will take a closer look at `init` in the system bootup course; for now, just know it is the process that spawns all other processes.

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of Linux processes and their management:

- **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - In this lab, you will learn essential skills for managing and monitoring processes on a Linux system. You will explore how to interact with foreground and background processes, inspect them with `ps`, monitor resources with `top`, adjust priority with `renice`, and terminate them with `kill`.

This lab will help you apply the concepts of process IDs, parent process IDs, and process monitoring in a real scenario and build confidence with process management.

## Quiz Question

What system call creates a new process?

## Quiz Answer

fork
