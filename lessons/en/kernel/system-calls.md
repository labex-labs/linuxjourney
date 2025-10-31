---
index: 3
lang: "en"
title: "System Calls"
meta_title: "System Calls - Kernel"
meta_description: "Explore the fundamentals of a system call in Linux. Learn how user-space processes use system calls (syscalls) to request services from the kernel, switch modes, and how the syscall table works. Use `strace` to see system calls in action."
meta_keywords: "system call linux, system calls, syscall table, kernel mode, user mode, strace, linux kernel, syscall API"
---

## Lesson Content

Imagine you are at a large concert. To get from the general audience area to the exclusive backstage, you can't just walk through. You need a special pass that grants you access through a specific, guarded door. In the world of computing, **system calls** are those special passes.

### What Are System Calls?

System calls, often abbreviated as syscalls, provide a way for user-space processes to request services directly from the kernel. The kernel exposes a set of services through the system call API. These services are essential for operations like reading or writing to a file, managing memory, or handling network connections. The number of available system calls is fixed; you cannot add new ones arbitrarily. Your system maintains a `syscall table` where each system call is registered with a unique ID.

### The System Call Mechanism in Linux

When you run a program like `ls`, the code within it doesn't execute the **system call linux** command directly. Instead, it uses a library function, which acts as a wrapper. This wrapper function sets up the necessary parameters and then triggers a software interrupt, or a "trap."

This trap signals the processor to switch from the non-privileged user mode to the privileged kernel mode. Once in kernel mode, a system call handler takes over. It uses the unique ID to look up the requested function in the `syscall table` and then executes it. For example, the `stat()` system call, used to query a file's status, is found and run this way. After the kernel completes the task, it switches the context back to user mode and returns a status code to your process, indicating success or an error.

### Viewing System Calls with strace

You can observe the system calls a process makes in real-time using the `strace` command. This tool is incredibly useful for debugging and understanding how a program interacts with the kernel.

To see the system calls made by the `ls` command, you would run:

```bash
strace ls
```

This will output a detailed list of every system call `ls` performs during its execution.

## Exercise

Practice makes perfect! While the inner workings of system calls are complex, understanding how user-space programs interact with the kernel is fundamental. The best way to grasp this interaction is by practicing with commands that perform these underlying operations. Here are some hands-on labs to reinforce your understanding of file system interactions, which are heavily reliant on system calls:

1. **[Navigate the Filesystem in Linux](https://labex.io/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Practice essential commands like `ls`, `cd`, and `pwd` to move around and inspect your Linux file system, directly engaging with the kernel's file system services.
2. **[Manage Files and Directories in Linux](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835)** - Learn to create, remove, copy, and move files and directories using commands like `mkdir`, `rm`, `cp`, and `mv`, all of which involve system calls to perform their actions.
3. **[Find Files and Commands in Linux](https://labex.io/labs/comptia-find-files-and-commands-in-linux-590834)** - Master techniques for locating files and commands using `find`, `whereis`, and `which`, further illustrating how user commands leverage kernel services to interact with the file system.

These labs will help you apply the concepts of file system interaction in real scenarios and build confidence with fundamental Linux operations that implicitly rely on system calls.

## Quiz Question

What is used to switch from user mode to kernel mode? Please answer in English, using two words.

## Quiz Answer

System call
