---
index: 6
lang: "zh"
title: "内存监控"
meta_title: "内存监控 - 进程利用率"
meta_description: "使用 vmstat 命令掌握 Linux 内存监控。本指南解释了如何使用此强大的内存利用率监视器来分析系统性能指标。"
meta_keywords: "内存监控，内存利用率监视器，vmstat, linux 内存，系统性能，内存使用，linux 教程"
---

## Lesson Content

有效的系统管理需要密切关注资源使用情况，而**内存监控**是这一过程的关键部分。当系统内存不足时，其性能可能会显著下降。Linux 提供了多种工具来帮助您跟踪内存消耗，其中最通用的是 `vmstat`。

### vmstat 简介

`vmstat`（虚拟内存统计）命令是一个强大的**内存利用率监视器**，它报告有关进程、内存、分页、块 I/O、中断和 CPU 活动的信息。在不带任何参数的情况下运行它，可以提供自系统启动以来的当前状态快照。

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

输出分为几个部分。让我们分解一下每个字段的含义。

### Procs (进程)

- `r`: 正在等待运行时间的就绪进程数。
- `b`: 处于不可中断睡眠状态的进程数，通常在等待 I/O。

### Memory (内存)

- `swpd`: 使用的虚拟内存量（以千字节为单位）。
- `free`: 空闲内存量（以千字节为单位）。
- `buff`: 用作缓冲区的内存量。
- `cache`: 用作页面缓存的内存量。

### Swap (交换)

- `si`: 每秒从磁盘换入的内存量（以千字节为单位）。高值表示系统物理内存不足。
- `so`: 每秒换出到磁盘的内存量（以千字节为单位）。理想情况下，此值应为零。

### IO (输入/输出)

- `bi`: 从块设备接收的块数（块/秒）。
- `bo`: 发送到块设备的块数（块/秒）。

### System (系统)

- `in`: 每秒中断次数，包括时钟中断。
- `cs`: 每秒上下文切换次数。

### CPU (中央处理器)

这些是总 CPU 时间的百分比。

- `us`: 运行非内核代码所花费的时间（用户时间）。
- `sy`: 运行内核代码所花费的时间（系统时间）。
- `id`: 空闲时间。
- `wa`: 等待 I/O 所花费的时间。
- `st`: 从虚拟机窃取的时间（适用于虚拟化环境）。

## Exercise

实践造就完美！以下是一些实践实验，以加强您对系统和内存监控的理解：

1. **[Linux free 命令：监控系统内存](https://labex.io/zh/labs/linux-linux-free-command-monitoring-system-memory-388496)** - 学习监控和分析系统内存使用情况，理解各种显示格式和总内存消耗。
2. **[Linux top 命令：实时系统监控](https://labex.io/zh/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - 学习使用各种选项进行排序和过滤，实时监控系统性能，包括进程、CPU 和内存使用情况。

这些实验将帮助您在实际场景中应用系统资源监控的概念，并建立分析 Linux 系统性能的信心。

## Quiz Question

What tool is used to view memory utilization? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

vmstat
