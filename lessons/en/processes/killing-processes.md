---
index: 7
lang: "en"
title: "kill (Terminate)"
meta_title: "kill (Terminate) - Processes"
meta_description: "Master the Linux kill command to manage and terminate processes. This guide covers the differences between kill vs terminate, and explains signals like kill sigterm (SIGTERM), SIGKILL, and kill sighup (SIGHUP)."
meta_keywords: "kill command, kill sigterm, kill sighup, linux kill -0, kill vs terminate, kill -15 linux, SIGTERM, SIGKILL, process management, terminate process"
---

## Lesson Content

In Linux, you can manage processes by sending them signals. The primary command for this is `kill`, which, despite its name, can send various signals, not just ones that terminate a process.

### Default Termination with kill sigterm

When you use the `kill` command with only a Process ID (PID), it sends a `TERM` signal by default. This is the standard, graceful way to ask a program to terminate.

```bash
kill 12445
```

The `kill sigterm` signal (also known as `SIGTERM` or signal 15) requests that the process shut down cleanly. This gives the process a chance to save its progress and release resources properly. You can also explicitly use the signal number, making `kill -15 12445` equivalent to the command above. This addresses the common `kill -15 linux` query.

### Forcing Termination with SIGKILL

Sometimes a process becomes unresponsive and won't react to a `SIGTERM` signal. In these cases, you can force it to stop using the `KILL` signal.

```bash
kill -9 12445
```

The `SIGKILL` signal (signal 9) terminates the process immediately, without giving it a chance to clean up. This is a key difference in the `kill vs terminate` debate; `SIGKILL` is an unconditional termination, while `SIGTERM` is a polite request.

### Understanding Other Common Signals

While `SIGTERM` and `SIGKILL` are the most common, other signals are also useful for process management.

- **SIGHUP**: The `kill sighup` signal (Hangup, signal 1) is traditionally sent to a process when its controlling terminal is closed. It can be used to tell daemon processes to reload their configuration files.
- **SIGINT**: The Interrupt signal (signal 2) is sent when you press `Ctrl-C`. It requests the process to interrupt its current operation.
- **SIGSTOP**: This signal (signal 19) pauses a process without terminating it. The process can be resumed later with the `SIGCONT` signal.

### Checking Process Existence with kill -0

A special use case is `linux kill -0`. This command doesn't actually send a signal but instead checks if a process with the specified PID exists and if you have permission to signal it.

```bash
kill -0 12445
```

If the command executes successfully (exit code 0), the process exists. If it fails, the process does not exist or you lack permissions.

## Exercise

To apply what you've learned, try this hands-on lab to reinforce your understanding of process management and termination:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - In this lab, you will learn essential skills for managing and monitoring processes on a Linux system. You will explore how to interact with foreground and background processes, inspect them with `ps`, monitor resources with `top`, adjust priority with `renice`, and terminate them with `kill`.

This lab will help you apply the concepts of process control and termination in real scenarios and build confidence with managing Linux processes.

## Quiz Question

What is the signal name for the default `kill` command? Please answer in English. Note that the answer is case-sensitive.

## Quiz Answer

SIGTERM
