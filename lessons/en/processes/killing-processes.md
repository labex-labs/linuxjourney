---
lang: "en"
title: "kill (Terminate)"
description: "Learn how to use the Linux 'kill' command to terminate processes. Understand SIGTERM, SIGKILL, and other signals for process management. Start learning now!"
keywords: "kill command, Linux processes, SIGTERM, SIGKILL, Linux tutorial, beginner, process management, Linux guide"
---

## Lesson Content

You can send signals that terminate processes; such a command is aptly named the `kill` command.

```bash
kill 12445
```

The `12445` is the PID of the process you want to kill. By default, it sends a `TERM` signal. The `SIGTERM` signal is sent to a process to request its termination, allowing it to cleanly release its resources and save its state.

You can also specify a signal with the `kill` command:

```bash
kill -9 12445
```

This will run the `SIGKILL` signal and kill the process.

### Differences between SIGHUP, SIGINT, SIGTERM, SIGKILL, SIGSTOP?

These signals all sound reasonably similar, but they do have their differences.

- SIGHUP - Hangup, sent to a process when the controlling terminal is closed. For example, if you closed a terminal window that had a process running in it, you would get a `SIGHUP` signal. So, basically, you've been hung up on.
- SIGINT - Is an interrupt signal, so you can use Ctrl-C, and the system will try to gracefully kill the process.
- SIGTERM - Kill the process, but allow it to do some cleanup first.
- SIGKILL - Kill the process, kill it with fire, doesn't do any cleanup.
- SIGSTOP - Stop/suspend a process.

## Exercise

Kill some processes using different signals.

## Quiz Question

What is the signal name for the default `kill` command?

## Quiz Answer

SIGTERM
