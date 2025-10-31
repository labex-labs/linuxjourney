---
index: 2
lang: "en"
title: "System V Service"
meta_title: "System V Service - Init"
meta_description: "Learn to manage traditional System V (SysV) services in Linux. This guide covers using the `service` command to list, start, stop, and restart services on a System V init system."
meta_keywords: "system v, sysv init, linux services, service command, manage linux services, start service, stop service, restart service, linux system v"
---

## Lesson Content

**System V** (or SysV) is one of the classic initialization systems in Unix-like operating systems. Although many modern Linux distributions have moved to newer systems like `systemd`, understanding how to manage **System V** services is still a valuable skill, as many systems maintain backward compatibility.

### The service Command

The primary tool for interacting with services on a **System V** init system is the `service` command. It acts as a wrapper script, simplifying the process of controlling services.

### Listing All Services

To get an overview of all available services and their current status, you can use the `--status-all` flag. This command lists each service and indicates whether it is running (`+`), stopped (`-`), or if its state is unknown (`?`).

```bash
service --status-all
```

### Controlling a Specific Service

To manage an individual service, you specify the service name followed by an action like `start`, `stop`, or `restart`. These actions require administrative privileges, so you'll typically use `sudo`.

To start a service, such as the networking service:

```bash
sudo service networking start
```

To stop a running service:

```bash
sudo service networking stop
```

To stop and then immediately start a service, which is useful for applying configuration changes:

```bash
sudo service networking restart
```

These commands are not exclusive to **System V** init systems; you can often use them to manage Upstart services as well. As Linux distributions continue to evolve, compatibility layers like the `service` command are kept in place to help ease the transition from traditional init scripts.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of process and task management, which are fundamental to managing services in Linux:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with, inspecting, monitoring, and terminating processes in a real Linux environment.
2. **[Schedule Tasks with at and cron in Linux](https://labex.io/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Learn to automate tasks using `at` for one-time jobs and `cron` for recurring tasks, a key skill for service automation.

These labs will help you apply the concepts in real scenarios and build confidence with managing system operations.

## Quiz Question

What is the full command to stop a service named `peanut` on a System V system? Please provide the exact command in English, paying attention to case.

## Quiz Answer

sudo service peanut stop
