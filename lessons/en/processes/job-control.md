---
index: 11
lang: "en"
title: "Job Control"
meta_title: "Job Control - Processes"
meta_description: "Explore our Linux tutorial on job control to effectively manage background processes. Learn to use the jobs, bg, fg, and kill commands for powerful shell multitasking."
meta_keywords: "Linux job control, background processes, jobs command, bg command, fg command, kill command, Linux tutorial, beginner Linux"
---

## Lesson Content

In Linux, you often encounter commands that take a long time to complete. Instead of waiting and leaving your terminal unusable, you can use **Linux job control** to manage these tasks. This powerful feature allows you to run and manage multiple **background processes** within a single shell session, significantly improving your workflow.

### Running a Command in the Background

To start a process directly in the background, simply append an ampersand (`&`) to your command. This immediately returns your shell prompt, allowing you to continue working while the command executes.

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### Listing Background Jobs

You can view all the jobs running in the background by using the `jobs` command.

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

The output provides the job ID in the first column, its status, and the original command. The `+` symbol indicates the most recently started background job, while the `-` symbol marks the second most recent one.

### Managing Active Processes

What if a command is already running in the foreground and you decide you need your terminal back? You don't need to stop it. First, suspend the running process by pressing `Ctrl-Z`. Then, use the `bg` command to send that suspended job to the background.

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &
```

Now, the `sleep 1003` process is running as a background job, and you can verify this with the `jobs` command.

### Bringing a Job to the Foreground

To bring a background process back to the foreground, use the `fg` command. You can specify a particular job by its ID (e.g., `fg %1`). If you run the `fg` command without any arguments, it will bring the most recent background job (the one marked with `+`) to the foreground.

```bash
fg %1
```

### Terminating Background Jobs

If you need to stop a background process, you can use the `kill` command. Similar to the `fg` command, you reference the job using its ID prefixed with a percent sign (`%`). This is a key function of Linux job control.

```bash
kill %1
```

Mastering these commands is essential for any beginner Linux user looking to multitask efficiently in the shell.

## Exercise

To put your knowledge of Linux job control into practice, try this hands-on lab. It will help you solidify your understanding of managing foreground and background processes.

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with foreground and background processes, monitoring resources, and terminating processes, directly addressing the scenario of long-running commands.

## Quiz Question

What command is used to list background jobs? (Please answer in English, using only lowercase letters.)

## Quiz Answer

jobs
