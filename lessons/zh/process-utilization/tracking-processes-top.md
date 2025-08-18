---
index: 1
lang: "zh"
title: "跟踪进程：top"
meta_title: "跟踪进程：top - 进程利用率"
meta_description: "了解如何使用 Linux `top` 命令监控系统资源和跟踪进程。理解 CPU、内存和进程详细信息以进行性能分析。"
meta_keywords: "Linux top 命令，监控进程，系统利用率，Linux 性能，初学者，教程，指南"
---

## Lesson Content

在本课程中，我们将介绍如何读取和分析系统的资源利用率。本课程展示了一些在需要跟踪进程正在做什么时使用的出色工具。

### top

我们之前讨论过 `top`，但我们将深入探讨它实际显示的内容。请记住，`top` 是我们用来实时查看进程系统利用率的工具：

```plaintext
top - 18:06:26 up 6 days,  4:07,  2 users,  load average: 0.92, 0.62, 0.59
Tasks: 389 total,   1 running, 387 sleeping,   0 stopped,   1 zombie
%Cpu(s):  1.8 us,  0.4 sy,  0.0 ni, 97.6 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:  32870888 total, 27467976 used,  5402912 free,   518808 buffers
KiB Swap: 33480700 total,    39892 used, 33440808 free. 19454152 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 6675 patty    20   0 1731472 520960  30876 S   8.3  1.6 160:24.79 chrome
 6926 patty    20   0  935888 163456  25576 S   4.3  0.5   5:28.13 chrome
```

让我们来看看这个输出意味着什么。您不必记住这些，但当您需要参考时可以回来查看。

### 1st line: This is the same information you would see if you ran the `uptime` command (more to come)

字段从左到右依次是：

1. 当前时间
2. 系统已运行时间
3. 当前登录用户数
4. 系统平均负载（稍后介绍）

### 2nd line: Tasks that are running, sleeping, stopped, and zombied

### 3rd line: CPU information

1. `us`: user CPU time - CPU 时间百分比，用于运行未调整优先级的用户进程。
2. `sy`: system CPU time - CPU 时间百分比，用于运行内核和内核进程。
3. `ni`: nice CPU time - CPU 时间百分比，用于运行已调整优先级的进程。
4. `id`: CPU idle time - CPU 时间百分比，用于空闲。
5. `wa`: I/O wait - CPU 时间百分比，用于等待 I/O。如果此值较低，则问题可能不是磁盘或网络 I/O。
6. `hi`: hardware interrupts - CPU 时间百分比，用于处理硬件中断。
7. `si`: software interrupts - CPU 时间百分比，用于处理软件中断。
8. `st`: steal time - 如果您正在运行虚拟机，这是从您那里“窃取”用于其他任务的 CPU 时间百分比。

### 4th and 5th line: Memory Usage and Swap Usage

### Processes List that are Currently in Use

1. `PID`: 进程 ID
2. `USER`: 进程所有者用户
3. `PR`: 进程优先级
4. `NI`: nice 值
5. `VIRT`: 进程使用的虚拟内存
6. `RES`: 进程使用的物理内存
7. `SHR`: 进程的共享内存
8. `S`: 指示进程状态：`S`=睡眠，`R`=运行，`Z`=僵尸，`D`=不可中断，`T`=停止
9. `%CPU`: 此进程使用的 CPU 百分比
10. `%MEM`: 此进程使用的 RAM 百分比
11. `TIME+`: 此进程的总活动时间
12. `COMMAND`: 进程名称

如果您只想跟踪某些进程，也可以指定进程 ID：

```bash
top -p 1
```

## Exercise

试用 `top` 命令，看看哪些进程正在使用最多的资源。

## Quiz Question

哪个命令显示与 `top` 第一行相同的输出？

## Quiz Answer

uptime
