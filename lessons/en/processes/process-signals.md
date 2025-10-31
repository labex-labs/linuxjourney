---
index: 6
lang: "en"
title: "Signals"
meta_title: "Signals - Processes"
meta_description: "Explore the fundamentals of Linux signals, a key mechanism for process management. Learn how Linux process signals like SIGTERM (signal 15 linux) and SIGKILL work, and understand their OS signal codes."
meta_keywords: "linux signals, linux process signals, signal 15 linux, os sig code, SIGKILL, SIGTERM, SIGINT, process management, linux tutorial"
---

## Lesson Content

In Linux, a signal is a software interrupt sent to a process to notify it that an important event has occurred. Understanding **linux signals** is fundamental to managing processes and system behavior effectively.

### The Purpose of Signals

Signals serve as a primary method of inter-process communication (IPC). They have many uses:

- **User Interaction**: A user can type special terminal characters, like `Ctrl-C` (SIGINT) or `Ctrl-Z` (SIGTSTP), to interrupt or suspend foreground processes.
- **Kernel Notifications**: The kernel can send signals to a process to notify it of hardware or software issues, such as an illegal memory access (SIGSEGV).
- **Process Management**: System administrators and other processes use signals to manage the lifecycle of other processes, such as requesting termination or a configuration reload.

### The Signal Lifecycle

When an event generates a signal, it is first delivered to a target process. The signal remains in a "pending" state until the kernel runs the process. When the process is scheduled, the signal is delivered. However, processes have signal masks, which can be configured to block the delivery of specific signals.

When a signal is delivered, the process can take one of several actions:

- **Ignore the signal**: The process simply discards the signal and continues execution.
- **Catch the signal**: The process executes a custom function called a signal handler to respond to the event.
- **Perform the default action**: If not caught or ignored, the default action is taken. For many signals, this means terminating the process.
- **Block the signal**: If the signal is in the process's signal mask, it remains pending until it is unblocked.

### Common Linux Process Signals

Each signal is defined by an integer, but they are almost always referred to by their symbolic names (the **os sig code**), which start with `SIG`. While the numbers can vary slightly between architectures, the names are consistent. Here are some of the most common **linux process signals**:

- **SIGHUP (1)**: Hangup. Often used to tell a daemon to reload its configuration.
- **SIGINT (2)**: Interrupt. Sent by `Ctrl-C`. It's a request to terminate the process.
- **SIGKILL (9)**: Kill. This is an immediate, forceful termination. The process cannot catch, ignore, or block this signal.
- **SIGSEGV (11)**: Segmentation Fault. Indicates the process made an invalid memory reference.
- **SIGTERM (15)**: Termination. This is the standard, polite way to ask a process to terminate. It is the default signal sent by the `kill` command. A process can catch this signal to perform cleanup before exiting. This is often referred to as **signal 15 linux**.
- **SIGSTOP**: Stop. Pauses the process. Like SIGKILL, it cannot be caught or ignored.

The key difference between `SIGTERM` (**linux signal 15**) and `SIGKILL` is that `SIGTERM` is a request that can be handled, while `SIGKILL` is a command that destroys the process immediately.

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of processes and how signals are used to interact with them:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - In this lab, you will learn essential skills for managing and monitoring processes on a Linux system. You will explore how to interact with foreground and background processes, inspect them with `ps`, monitor resources with `top`, adjust priority with `renice`, and terminate them with `kill`. Terminating processes with `kill` is a direct application of sending signals.

This lab will help you apply the concepts of process management and the underlying use of signals in real scenarios and build confidence with Linux system administration.

## Quiz Question

What signal is unblockable? Please answer in English, using the exact signal name and paying attention to capitalization.

## Quiz Answer

SIGKILL
