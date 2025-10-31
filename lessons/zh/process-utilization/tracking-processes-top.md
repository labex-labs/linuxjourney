---
index: 1
lang: "zh"
title: "进程跟踪：top"
meta_title: "进程跟踪：top - 进程利用率"
meta_description: "通过掌握 `top` 命令，发现学习 Linux 的最佳方式。本指南解释了如何监控系统资源、跟踪进程以及理解 VIRT 和 RES 等指标。这是理解 Linux 工作原理的关键部分。"
meta_keywords: "Linux top 命令，进程监控，系统利用率，Linux 工作原理，linux top virt res, 学习 Linux 的最佳方法，Linux 性能，进程管理，免费在线 Linux 培训带证书"
---

## Lesson Content

理解如何读取和分析资源利用率是每位 Linux 用户的一项关键技能。许多人认为掌握命令行工具是从头开始学习 Linux 的**最佳方式**，因为它们能深入了解**Linux 的工作原理**。本课程将介绍 `top`，这是一个强大的实用工具，用于实时跟踪进程的活动。

### 理解 top 命令

我们之前简要提到了 `top`，但现在我们将深入研究它所显示内容的具体细节。`top` 命令为您提供机器上进程和系统利用率的动态、实时视图。

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

我们来解释一下这个输出的含义。您不必记住所有内容，但可以将本课程用作参考。

### 系统摘要

前几行提供了系统状态的高级摘要。

- **第 1 行**：这与您运行 `uptime` 命令时看到的信息相同。它显示当前时间、系统正常运行时间、登录用户数以及过去 1、5 和 15 分钟的系统负载平均值。
- **第 2 行**：所有任务（进程）的摘要，分类为运行中、休眠中、已停止或僵尸进程。

### CPU 使用率细分

第三行详细说明了 CPU 利用率。

- `us`：用户进程（未被 nice 化的）运行所花费的 CPU 时间百分比。
- `sy`：内核及其进程运行所花费的 CPU 时间百分比。
- `ni`：被 nice 化（低优先级）的用户进程运行所花费的 CPU 时间百分比。
- `id`：空闲的 CPU 时间百分比。
- `wa`：等待 I/O 操作完成所花费的 CPU 时间百分比。高值可能表明存在磁盘或网络瓶颈。
- `hi`：处理硬件中断所花费的 CPU 时间百分比。
- `si`：处理软件中断所花费的 CPU 时间百分比。
- `st`：窃取时间。在虚拟化环境中，这是虚拟 CPU 在等待真实 CPU 时所花费的 CPU 时间百分比，此时管理程序正在为另一个虚拟处理器服务。

### 内存和交换空间信息

第四行和第五行分别显示内存和交换空间的使用情况。这包括总量、已用量和可用量。

### 进程列表

`top` 的主体是资源消耗最多的进程列表。

- `PID`：唯一的进程 ID。
- `USER`：拥有该进程的用户。
- `PR`：进程的调度优先级。
- `NI`：“nice”值，它会影响其优先级。
- `VIRT`：进程使用的虚拟内存。这是进程可以访问的内存总量。
- `RES`：进程使用的常驻内存。这是任务正在使用的、未被交换出去的物理内存。理解**linux top virt res**之间的区别是内存分析的关键。
- `SHR`：进程使用的共享内存。
- `S`：进程的状态：`S`=休眠，`R`=运行，`Z`=僵尸，`D`=不可中断睡眠，`T`=已停止。
- `%CPU`：自上次更新以来该进程使用的 CPU 时间百分比。
- `%MEM`：该进程使用的物理 RAM 百分比。
- `TIME+`：该进程自启动以来使用的总 CPU 时间。
- `COMMAND`：启动该进程的命令名称或命令行。

您还可以通过其 ID 监控特定进程，这对于有针对性的故障排除非常有用：

```bash
top -p 1
```

## Exercise

实践是掌握的关键。这些动手实验是学习 Linux 进程管理**最佳资源**之一，提供了一个实际环境来应用您所学到的知识。

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 在真实的 Linux 环境中练习与进程交互、检查、监控和终止进程。
2. **[Linux top 命令：实时系统监控](https://labex.io/zh/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - 学习使用 `top` 命令实时监控 CPU 使用率、内存和运行中的进程。
3. **[Linux free 命令：监控系统内存](https://labex.io/zh/labs/linux-linux-free-command-monitoring-system-memory-388496)** - 学习使用 `free` 命令来监控和分析系统内存使用情况。

## Quiz Question

哪个命令会显示与 `top` 中第一行相同的信息？请仅使用小写英文字母命令名作答。

## Quiz Answer

uptime
