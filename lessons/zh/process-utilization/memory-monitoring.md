---
index: 6
lang: "zh"
title: "内存监控"
meta_title: "内存监控 - 进程利用率"
meta_description: "学习使用 vmstat 监控 Linux 内存使用情况。了解内存、交换和 CPU 指标以优化系统性能。开始您的 Linux 之旅！"
meta_keywords: "vmstat, Linux 内存监控，系统性能，Linux 教程，内存使用，Linux 初学者，Linux 指南"
---

## Lesson Content

除了 CPU 监控和 I/O 监控之外，您还可以使用 **vmstat** 监控内存使用情况。

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

字段如下：

### 进程

- r - 处于运行状态的进程数
- b - 处于不可中断睡眠状态的进程数

### 内存

- swpd - 已使用的虚拟内存量
- free - 可用内存量
- buff - 用作缓冲区的内存量
- cache - 用作缓存的内存量

### 交换

- si - 从磁盘交换进来的内存量
- so - 交换到磁盘的内存量

### 输入/输出

- bi - 从块设备接收到的块量
- bo - 发送到块设备的块量

### 系统

- in - 每秒中断次数
- cs - 每秒上下文切换次数

### 中央处理器

- us - 用户时间花费的时间
- sy - 内核时间花费的时间
- id - 空闲时间花费的时间
- wa - 等待 I/O 的时间

## Exercise

熟能生巧！以下是一些动手实验，旨在加深您对系统和内存监控的理解：

1. **[Linux free 命令：监控系统内存](https://labex.io/zh/labs/linux-linux-free-command-monitoring-system-memory-388496)** - 学习监控和分析系统内存使用情况，理解各种显示格式和总内存消耗。
2. **[Linux top 命令：实时系统监控](https://labex.io/zh/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - 学习实时监控系统性能，包括进程、CPU 和内存使用情况，使用各种选项进行排序和过滤。

这些实验将帮助您在实际场景中应用系统资源监控的概念，并增强分析 Linux 系统性能的信心。

## Quiz Question

用于查看内存使用情况的工具是什么？

## Quiz Answer

vmstat
