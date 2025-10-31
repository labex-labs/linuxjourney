---
index: 6
lang: "en"
title: "Memory Monitoring"
meta_title: "Memory Monitoring - Process Utilization"
meta_description: "Master Linux memory monitoring with the vmstat command. This guide explains how to use this powerful memory utilization monitor to analyze system performance metrics."
meta_keywords: "memory monitoring, memory utilization monitor, vmstat, linux memory, system performance, memory usage, linux tutorial"
---

## Lesson Content

Effective system administration requires keeping a close eye on resource usage, and **memory monitoring** is a critical part of this process. When a system runs low on memory, its performance can degrade significantly. Linux provides several tools to help you track memory consumption, and one of the most versatile is `vmstat`.

### Introduction to vmstat

The `vmstat` (virtual memory statistics) command is a powerful **memory utilization monitor** that reports information about processes, memory, paging, block I/O, traps, and CPU activity. Running it without any arguments provides a snapshot of the system's current state since the last boot.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

The output is organized into several columns. Let's break down what each field means.

### Procs

- `r`: The number of runnable processes waiting for run time.
- `b`: The number of processes in uninterruptible sleep, typically waiting for I/O.

### Memory

- `swpd`: The amount of virtual memory used (in kilobytes).
- `free`: The amount of idle memory (in kilobytes).
- `buff`: The amount of memory used as buffers.
- `cache`: The amount of memory used as a page cache.

### Swap

- `si`: The amount of memory swapped in from disk per second (in kilobytes). High values indicate the system is low on physical memory.
- `so`: The amount of memory swapped out to disk per second (in kilobytes). This should ideally be zero.

### IO

- `bi`: Blocks received from a block device (blocks/s).
- `bo`: Blocks sent to a block device (blocks/s).

### System

- `in`: The number of interrupts per second, including the clock.
- `cs`: The number of context switches per second.

### CPU

These are percentages of total CPU time.

- `us`: Time spent running non-kernel code (user time).
- `sy`: Time spent running kernel code (system time).
- `id`: Time spent idle.
- `wa`: Time spent waiting for I/O.
- `st`: Time stolen from a virtual machine (for virtualized environments).

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of system and memory monitoring:

1. **[Linux free Command: Monitoring System Memory](https://labex.io/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Learn to monitor and analyze system memory usage, understanding various display formats and total memory consumption.
2. **[Linux top Command: Real-time System Monitoring](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Learn to monitor system performance in real-time, including processes, CPU, and memory usage, using various options for sorting and filtering.

These labs will help you apply the concepts of system resource monitoring in real scenarios and build confidence with analyzing Linux system performance.

## Quiz Question

What tool is used to view memory utilization? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

vmstat
