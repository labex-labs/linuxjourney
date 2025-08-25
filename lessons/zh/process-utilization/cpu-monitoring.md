---
index: 4
lang: "zh"
title: "CPU 监控"
meta_title: "CPU 监控 - 进程利用率"
meta_description: "使用 uptime 命令学习 CPU 监控。了解负载平均值、CPU 使用率以及如何为 Linux 初学者解释系统性能。"
meta_keywords: "uptime 命令，Linux CPU 监控，负载平均值，系统性能，Linux 教程，初学者指南"
---

## Lesson Content

让我们来看一个有用的命令：**uptime**。

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

我们在本课程的第一课中讨论过 uptime，但我们还没有详细介绍负载平均值字段。负载平均值是查看系统 CPU 负载的好方法。这些数字表示 1 分钟、5 分钟和 15 分钟间隔内的平均 CPU 负载。CPU 负载是什么意思？CPU 负载是等待 CPU 执行的平均进程数。

假设你有一个单核 CPU；把这个核心想象成交通中的单车道。如果高速公路正值高峰期，这条车道会非常繁忙，交通会达到 100% 或负载为 1。现在交通变得如此糟糕，以至于高速公路堵塞，并且常规道路的汽车数量是平时的两倍；我们可以说你的负载是 200% 或负载为 2。现在假设交通有所缓解，高速公路车道上的汽车数量只有一半；我们可以说车道的负载是 0.5。当交通不存在时，我们可以更快地回家，理想情况下负载应该非常低，就像凌晨 2 点的交通一样低。在这种情况下，汽车就是进程，这些进程只是在等待离开高速公路回家。

现在，仅仅因为你的负载平均值为 1 并不意味着你的电脑运行缓慢。现在大多数现代机器都有多个核心。如果你有一个四核处理器（4 个核心），并且你的负载平均值为 1，那实际上只影响了你 CPU 的 25%。把每个核心想象成交通中的一条车道。你可以使用 **cat /proc/cpuinfo** 命令查看系统上的核心数量。

观察负载平均值时，你必须考虑核心数量。如果你发现你的机器总是使用高于平均水平的负载，那可能出了问题。

## Exercise

熟能生巧！以下是一些动手实验，旨在巩固你对监控 Linux 系统性能和 CPU 负载的理解：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习与进程交互和检查，并使用 `ps` 和 `top` 等工具监控资源，这与理解 CPU 负载直接相关。
2. **[Linux top 命令：实时系统监控](https://labex.io/zh/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - 学习使用 `top` 命令进行实时系统监控，包括进程排序和过滤，从而更深入地了解 CPU 和进程活动。
3. **[Linux free 命令：监控系统内存](https://labex.io/zh/labs/linux-linux-free-command-monitoring-system-memory-388496)** - 学习监控和分析系统内存使用情况，这通常是与 CPU 负载一起影响整体系统性能的关键因素。

这些实验将帮助你在实际场景中应用系统监控和资源管理的概念，并增强分析系统性能的信心。

## Quiz Question

你可以使用什么命令查看负载平均值？

## Quiz Answer

uptime
