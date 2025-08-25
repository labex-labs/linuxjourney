---
index: 7
lang: "en"
title: "Continuous Monitoring"
meta_title: "Continuous Monitoring - Process Utilization"
meta_description: "Learn continuous Linux system monitoring with sar. Understand installation, data collection, and how to analyze historical resource usage for performance. Get started!"
meta_keywords: "sar, sysstat, Linux monitoring, system performance, continuous monitoring, beginner, tutorial, guide"
---

## Lesson Content

These monitoring tools are good to look at when your machine is having issues, but what about machines that are having issues when you aren't looking? For those, you'll need to use a continuous monitoring tool, something that will collect, report, and save your system activity information. In this lesson, we will go over a great tool to use: **sar**.

### Installing sar

Sar is a tool that is used to do historical analysis on your system. First, make sure you have it installed by installing the `sysstat` package: `sudo apt install sysstat`.

### Setting up data collection

Usually, once you install `sysstat`, your system will automatically start collecting data. If it doesn't, you can enable it by modifying the `ENABLED` field in `/etc/default/sysstat`.

### Using sar

```bash
sudo sar -q
```

This command will list the details from the start of the day.

```bash
sudo sar -r
```

This will list the details of memory usage from the start of the day.

```bash
sudo sar -P
```

This will list the details of CPU usage.

To see a view of a different day, you can go into `/var/log/sysstat/saXX` where `XX` is the day you want to view.

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of system monitoring and resource analysis:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with foreground and background processes, inspecting them with `ps`, monitoring resources with `top`, and terminating them with `kill`.
2. **[Linux top Command: Real-time System Monitoring](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Learn to use various options with the `top` command to sort processes, adjust update intervals, filter by user, and focus on active processes to effectively monitor system performance.
3. **[Linux df Command: Disk Space Reporting](https://labex.io/labs/linux-linux-df-command-disk-space-reporting-219188)** - This lab introduces the `df` command in Linux, a utility that displays information about disk space usage on mounted file systems, which is a key aspect of system monitoring.

These labs will help you apply the concepts of system resource monitoring in real scenarios and build confidence with analyzing system activity.

## Quiz Question

What is a good tool to use for monitoring system resources?

## Quiz Answer

sar
