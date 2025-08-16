---
lang: "en"
title: "Process Details"
description: "Learn about Linux process details, how the kernel manages resources, and what processes are. Understand process concepts for beginners."
keywords: "Linux processes, kernel, process management, ps aux, Linux tutorial, beginner guide"
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

No exercises for this lesson.

## Quiz Question

What manages and controls processes?

## Quiz Answer

kernel
