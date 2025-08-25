---
index: 9
lang: "en"
title: "Process States"
meta_title: "Process States - Processes"
meta_description: "Learn Linux process states (R, S, D, Z, T) using `ps aux`. Understand common STAT codes and manage processes effectively. Start your Linux journey!"
meta_keywords: "Linux process states, ps aux, process management, Linux tutorial, beginner Linux, STAT codes, Linux guide"
---

## Lesson Content

Let's take a look at the `ps aux` command again:

```bash
ps aux
```

In the STAT column, you'll see many values. A Linux process can be in a number of different states. The most common state codes you'll see are described below:

- **R**: Running or runnable; it is just waiting for the CPU to process it.
- **S**: Interruptible sleep; waiting for an event to complete, such as input from the terminal.
- **D**: Uninterruptible sleep; processes that cannot be killed or interrupted with a signal. Usually, to make them go away, you have to reboot or fix the issue.
- **Z**: Zombie; we discussed in a previous lesson that zombies are terminated processes that are waiting to have their statuses collected.
- **T**: Stopped; a process that has been suspended/stopped.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux process management and states:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - In this lab, you will learn essential skills for managing and monitoring processes on a Linux system. You will explore how to interact with foreground and background processes, inspect them with `ps`, monitor resources with `top`, adjust priority with `renice`, and terminate them with `kill`.

This lab will help you apply the concepts of process states in real scenarios and build confidence with Linux process management.

## Quiz Question

What STAT code is used to represent an uninterruptible sleep?

## Quiz Answer

D
