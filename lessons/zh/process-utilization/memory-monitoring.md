---
index: 6
lang: "zh"
title: "内存监控"
meta_title: "内存监控 - 进程利用率"
meta_description: "学习使用 vmstat 监控 Linux 内存使用情况。了解内存、交换空间和 CPU 指标，以优化系统性能。开始您的 Linux 之旅！"
meta_keywords: "vmstat, Linux 内存监控，系统性能，Linux 教程，内存使用，Linux 初学者，Linux 指南"
---

## Lesson Content

In addition to CPU monitoring and I/O monitoring, you can monitor your memory usage with **vmstat**.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

The fields are as follows:

### procs

- r - 运行时间进程数
- b - 处于不可中断睡眠状态的进程数

### memory

- swpd - 已使用的虚拟内存量
- free - 可用内存量
- buff - 用作缓冲区的内存量
- cache - 用作缓存的内存量

### swap

- si - 从磁盘换入的内存量
- so - 换出到磁盘的内存量

### io

- bi - 从块设备接收的块量
- bo - 发送到块设备的块量

### system

- in - 每秒中断次数
- cs - 每秒上下文切换次数

### cpu

- us - 用户时间消耗
- sy - 内核时间消耗
- id - 空闲时间消耗
- wa - 等待 I/O 的时间消耗

## Exercise

Look at your memory usage with vmstat.

## Quiz Question

用于查看内存使用情况的工具是什么？

## Quiz Answer

vmstat
