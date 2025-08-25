---
index: 1
lang: "zh"
title: "ps (进程)"
meta_title: "ps (进程) - 进程"
meta_description: "了解 Linux 'ps' 命令以查看正在运行的进程并理解进程 ID (PID)。获取进程管理的初学者指南。"
meta_keywords: "ps 命令，Linux 进程，进程 ID, PID, Linux 教程，初学者，指南，top 命令"
---

## Lesson Content

进程是您的机器上正在运行的程序。它们由内核管理，每个进程都有一个与之关联的 ID，称为**进程 ID (PID)**。PID 是按照进程创建的顺序分配的。

运行 `ps` 命令以查看正在运行的进程列表：

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

这为您展示了当前进程的快速快照：

- PID: 进程 ID
- TTY: 与进程关联的控制终端（我们稍后会详细介绍）
- STAT: 进程状态码
- TIME: 总 CPU 使用时间
- CMD: 可执行文件/命令的名称

如果您查看 `ps` 的 man 页面，您会发现有很多可以传递的命令选项。它们会根据您想使用的选项（BSD、GNU 或 Unix）而有所不同。在我看来，BSD 风格更受欢迎，所以我们将使用它。如果您好奇，不同风格之间的区别在于您使用的破折号数量和标志。

```bash
ps aux
```

**a** 显示所有正在运行的进程，包括其他用户运行的进程。**u** 显示更多关于进程的详细信息。最后，**x** 列出所有没有关联 TTY 的进程。这些程序将在 TTY 字段中显示 `?`；它们在作为系统启动一部分启动的守护进程中最常见。

您会注意到现在看到了更多的字段。无需记住所有这些；在稍后的高级进程课程中，我们将再次回顾其中一些：

- USER: 有效用户（我们正在使用其访问权限的用户）
- PID: 进程 ID
- %CPU: CPU 使用时间除以进程运行时间
- %MEM: 进程常驻集大小与机器物理内存的比率
- VSZ: 整个进程的虚拟内存使用量
- RSS: 常驻集大小，任务已使用的非交换物理内存
- TTY: 与进程关联的控制终端
- STAT: 进程状态码
- START: 进程启动时间
- TIME: 总 CPU 使用时间
- COMMAND: 可执行文件/命令的名称

`ps` 命令看起来可能有点混乱。目前，我们最常查看的字段是 PID、STAT 和 COMMAND。

另一个非常有用的命令是 **top** 命令。`top` 为您提供系统上正在运行的进程的实时信息，而不是快照。默认情况下，您将每 10 秒刷新一次。`top` 是一个极其有用的工具，可以查看哪些进程占用了您的大量资源。

```bash
top
```

## Exercise

熟能生巧！以下是一些动手实验，以加强您对 Linux 进程及其监控的理解：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习在 Linux 系统上管理和监控进程的基本技能，包括与前台/后台进程交互，使用 `ps` 检查，使用 `top` 监控，以及使用 `kill` 终止。
2. **[Linux top 命令：实时系统监控](https://labex.io/zh/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - 学习使用 Linux `top` 命令进行实时系统监控，包括进程排序、调整更新间隔和按用户过滤。

这些实验将帮助您在实际场景中应用进程识别和监控的概念，并增强您在 Linux 系统管理方面的信心。

## Quiz Question

哪个 `ps` 标志用于查看进程的详细信息？

## Quiz Answer

u
