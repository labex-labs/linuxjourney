---
index: 5
lang: "en"
title: "Process Termination"
meta_title: "Process Termination - Processes"
meta_description: "Learn about Linux process termination, including orphan and zombie processes. Understand _exit and wait system calls for effective process management."
meta_keywords: "Linux process termination, zombie processes, orphan processes, wait system call, _exit, Linux tutorial, beginner Linux"
---

## Lesson Content

Now that we know what goes on when a process gets created, what is happening when we don't need it anymore? Be forewarned, sometimes Linux can get a little dark...

A process can exit using the `_exit` system call. This will free up the resources that process was using for reallocation. So when a process is ready to terminate, it lets the kernel know why it's terminating with something called a termination status. Most commonly, a status of 0 means that the process succeeded. However, that's not enough to completely terminate a process. The parent process has to acknowledge the termination of the child process by using the `wait` system call, and what this does is it checks the termination status of the child process. I know it's gruesome to think about, but the `wait` call is a necessity; after all, what parent wouldn't want to know how their child died?

There is another way to terminate a process, and that involves using signals, which we will discuss soon.

### Orphan Processes

When a parent process dies before a child process, the kernel knows that it's not going to get a `wait` call, so instead it makes these processes "orphans" and puts them under the care of `init` (remember, mother of all processes). `init` will eventually perform the `wait` system call for these orphans so they can die.

### Zombie Processes

What happens when a child terminates and the parent process hasn't called `wait` yet? We still want to be able to see how a child process terminated, so even though the child process finished, the kernel turns the child process into a zombie process. The resources the child process used are still freed up for other processes; however, there is still an entry in the process table for this zombie. Zombie processes also cannot be killed, since they are technically "dead," so you can't use signals to kill them. Eventually, if the parent process calls the `wait` system call, the zombie will disappear; this is known as "reaping." If the parent doesn't perform a `wait` call, `init` will adopt the zombie and automatically perform `wait` and remove the zombie. It can be a bad thing to have too many zombie processes, since they take up space on the process table; if it fills up, it will prevent other processes from running.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux processes and their management:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with foreground and background processes, inspecting them with `ps`, monitoring resources with `top`, adjusting priority with `renice`, and terminating them with `kill`. This lab will give you practical experience with the lifecycle of processes, including how to terminate them.

This lab will help you apply the concepts of process management and termination in real scenarios and build confidence with Linux system administration.

## Quiz Question

What is the most common termination status for a process succeeding?

## Quiz Answer

0
