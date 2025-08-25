---
index: 3
lang: "en"
title: "Process Threads"
meta_title: "Process Threads - Process Utilization"
meta_description: "Learn about Linux process threads, single-threaded vs. multi-threaded concepts, and how to view them using 'ps m'. Understand lightweight processes efficiently!"
meta_keywords: "Linux threads, process threads, ps m command, multi-threaded, single-threaded, Linux processes, beginner Linux, Linux tutorial"
---

## Lesson Content

You may have heard of the terms single-threaded and multi-threaded processes. Threads are very similar to processes, in that they are used to execute the same program; they are often referred to as lightweight processes. If a process has one thread, it is single-threaded, and if a process has more than one thread, it is multi-threaded. However, all processes have at least one thread.

Processes operate with their own isolated system resources; however, threads can share these resources among each other easily, making it easier for them to communicate. At times, it is more efficient to have a multi-threaded application than a multi-process application.

Basically, let's say you open LibreOffice Writer and Chrome; each is its own separate process. Now you go inside Writer and start editing text. When you edit the text, it gets automatically saved. These two parallel "lightweight processes" of saving and editing are threads.

To view process threads, you can use:

```plaintext
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
```

The processes are denoted with each PID, and underneath the processes are their threads (denoted by a `--`). So you can see that the processes above are both single-threaded.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux processes and their management:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - In this lab, you will learn essential skills for managing and monitoring processes on a Linux system. You will explore how to interact with foreground and background processes, inspect them with `ps`, monitor resources with `top`, adjust priority with `renice`, and terminate them with `kill`.

This lab will help you apply the concepts of process management in real scenarios and build confidence with monitoring system activity.

## Quiz Question

True or false, all processes start out single-threaded.

## Quiz Answer

True
