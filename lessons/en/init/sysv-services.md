---
index: 2
lang: "en"
title: "System V Service"
meta_title: "System V Service - Init"
meta_description: "Learn to manage System V services using command-line tools. Discover how to list, start, stop, and restart services with this beginner-friendly Linux tutorial."
meta_keywords: "System V services, Linux services, service command, SysV init, Linux tutorial, beginner Linux, service management, Linux guide"
---

## Lesson Content

There are many command-line tools you can use to manage Sys V services.

### List services

```bash
service --status-all
```

### Start a service

```bash
sudo service networking start
```

### Stop a service

```bash
sudo service networking stop
```

### Restart a service

```bash
sudo service networking restart
```

These commands aren't specific to Sys V init systems; you can use them to manage Upstart services as well. Since Linux is trying to move away from the more traditional Sys V init scripts, there are still things in place to help that transition.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of process and task management, which are fundamental to managing services in Linux:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with, inspecting, monitoring, and terminating processes in a real Linux environment.
2. **[Schedule Tasks with at and cron in Linux](https://labex.io/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Learn to automate tasks using `at` for one-time jobs and `cron` for recurring tasks, a key skill for service automation.

These labs will help you apply the concepts in real scenarios and build confidence with managing system operations.

## Quiz Question

What is the command to stop a service named `peanut` with Sys V?

## Quiz Answer

sudo service peanut stop
