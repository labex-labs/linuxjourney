---
index: 3
lang: "en"
title: "System Calls"
meta_title: "System Calls - Kernel"
meta_description: "Learn about Linux system calls (syscalls) and how they interact with the kernel. Understand user and kernel modes, and use `strace` for debugging. Start your Linux journey!"
meta_keywords: "Linux system calls, syscalls, kernel mode, user mode, strace command, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Remember Britney in the previous lesson? Let's say we want to see her and get some drinks together. How do we get from standing outside in the crowds of people to inside her innermost circle? We would use system calls. System calls are like the VIP passes that get you to a secret side door that leads directly to Britney.

System calls (syscalls) provide user-space processes a way to request the kernel to do something for us. The kernel makes certain services available through the system call API. These services allow us to read or write to a file, modify memory usage, modify our network, etc. The amount of services is fixed, so you can't be adding system calls willy-nilly. Your system already has a table of what system calls exist, and each system call has a unique ID.

I won't get into specifics of system calls, as that will require you to know a bit of C, but the basics are that when you call a program like `ls`, the code inside this program contains a system call wrapper (so not the actual system call yet). Inside this wrapper, it invokes the system call which will execute a trap. This trap then gets caught by the system call handler and then references the system call in the system call table. Let's say we are trying to call the `stat()` system call; it's identified by a syscall ID, and the purpose of the `stat()` system call is to query the status of a file. Now remember, you were running the `ls` program in non-privileged mode. So now it sees you're trying to make a syscall, it then switches you over to kernel mode. There it does lots of things, but most importantly, it looks up your syscall number, finds it in a table based on the syscall ID, and then executes the function you wanted to run. Once it's done, it will return back to user mode, and your process will receive a return status if it was successful or if it had an error. The inner workings of syscalls get really detailed; I would recommend looking at information online if you want to learn more.

You can actually view the system calls that a process makes with the `strace` command. The `strace` command is useful for debugging how a program executed.

```bash
strace ls
```

## Exercise

Practice makes perfect! While the inner workings of system calls are complex, understanding how user-space programs interact with the kernel is fundamental. The best way to grasp this interaction is by practicing with commands that perform these underlying operations. Here are some hands-on labs to reinforce your understanding of file system interactions, which are heavily reliant on system calls:

1. **[Navigate the Filesystem in Linux](https://labex.io/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Practice essential commands like `ls`, `cd`, and `pwd` to move around and inspect your Linux file system, directly engaging with the kernel's file system services.
2. **[Manage Files and Directories in Linux](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835)** - Learn to create, remove, copy, and move files and directories using commands like `mkdir`, `rm`, `cp`, and `mv`, all of which involve system calls to perform their actions.
3. **[Find Files and Commands in Linux](https://labex.io/labs/comptia-find-files-and-commands-in-linux-590834)** - Master techniques for locating files and commands using `find`, `whereis`, and `which`, further illustrating how user commands leverage kernel services to interact with the file system.

These labs will help you apply the concepts of file system interaction in real scenarios and build confidence with fundamental Linux operations that implicitly rely on system calls.

## Quiz Question

What is used to switch from user mode to kernel mode?

## Quiz Answer

System call
