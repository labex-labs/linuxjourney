---
index: 1
lang: "zh"
title: "跟踪进程：top"
meta_title: "跟踪进程：top - 进程利用率"
meta_description: "了解如何使用 Linux `top` 命令监控系统资源和跟踪进程。理解 CPU、内存和进程详细信息以进行性能分析。"
meta_keywords: "Linux top 命令，监控进程，系统利用率，Linux 性能，初学者，教程，指南"
---

## Lesson Content

在本课程中，我们将介绍如何读取和分析系统上的资源利用率。本课程展示了一些在需要跟踪进程正在做什么时使用的出色工具。

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

让我们回顾一下这个输出的含义。您不必记住这些，但需要参考时可以回来查看。

### 第 1 行：这是您运行 `uptime` 命令时会看到的信息（更多内容即将推出）

字段从左到右依次是：

1. 当前时间
2. 系统已运行多长时间
3. 当前登录的用户数量
4. 系统平均负载（更多内容即将推出）

### 第 2 行：正在运行、休眠、停止和僵尸进程的任务

### 第 3 行：CPU 信息

1. `us`：用户 CPU 时间 - CPU 时间中用于运行未经过 nice 处理的用户进程的百分比。
2. `sy`：系统 CPU 时间 - CPU 时间中用于运行内核和内核进程的百分比。
3. `ni`：nice CPU 时间 - CPU 时间中用于运行经过 nice 处理的进程的百分比。
4. `id`：CPU 空闲时间 - CPU 时间中处于空闲状态的百分比。
5. `wa`：I/O 等待 - CPU 时间中等待 I/O 的百分比。如果此值较低，则问题可能不是磁盘或网络 I/O。
6. `hi`：硬件中断 - CPU 时间中用于处理硬件中断的百分比。
7. `si`：软件中断 - CPU 时间中用于处理软件中断的百分比。
8. `st`：窃取时间 - 如果您正在运行虚拟机，这是从您那里窃取用于其他任务的 CPU 时间百分比。

### 第 4 行和第 5 行：内存使用和交换使用

### 当前正在使用的进程列表

1. `PID`：进程 ID
2. `USER`：进程所有者用户
3. `PR`：进程优先级
4. `NI`：nice 值
5. `VIRT`：进程使用的虚拟内存
6. `RES`：进程使用的物理内存
7. `SHR`：进程的共享内存
8. `S`：指示进程状态：`S`=休眠，`R`=运行，`Z`=僵尸，`D`=不可中断，`T`=停止
9. `%CPU`：此进程使用的 CPU 百分比
10. `%MEM`：此进程使用的 RAM 百分比
11. `TIME+`：此进程的总活动时间
12. `COMMAND`：进程名称

如果您只想跟踪某些进程，也可以指定进程 ID：

```bash
top -p 1
```

## Exercise

熟能生巧！这里有一些动手实验，可以帮助您巩固对 Linux 资源利用和进程管理的理解：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 在真实的 Linux 环境中练习与进程交互、检查、监控和终止进程。
2. **[Linux top 命令：实时系统监控](https://labex.io/zh/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - 学习使用 `top` 命令实时监控 CPU 使用率、内存和运行中的进程。
3. **[Linux free 命令：监控系统内存](https://labex.io/zh/labs/linux-linux-free-command-monitoring-system-memory-388496)** - 学习使用 `free` 命令监控和分析系统内存使用情况。

这些实验将帮助您在实际场景中应用这些概念，并增强您在系统监控和进程管理方面的信心。

## Quiz Question

哪个命令显示与 `top` 第一行相同的输出？

## Quiz Answer

uptime
