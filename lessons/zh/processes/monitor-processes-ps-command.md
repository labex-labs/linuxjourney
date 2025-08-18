---
lang: "zh"
title: "ps (进程)"
meta_title: "ps (进程) - 进程"
meta_description: "了解 Linux 'ps' 命令以查看正在运行的进程并理解进程 ID (PID)。获取进程管理的初学者指南。"
meta_keywords: "ps 命令，Linux 进程，进程 ID, PID, Linux 教程，初学者，指南，top 命令"
---

## Lesson Content

进程是您的机器上正在运行的程序。它们由内核管理，每个进程都有一个与之关联的 ID，称为**进程 ID (PID)**。此 PID 按进程创建的顺序分配。

运行 `ps` 命令以查看正在运行的进程列表：

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

这向您展示了当前进程的快速快照：

- PID: 进程 ID
- TTY: 与进程关联的控制终端（我们稍后会详细介绍）
- STAT: 进程状态码
- TIME: 总 CPU 使用时间
- CMD: 可执行文件/命令的名称

如果您查看 `ps` 的 man page，您会看到有很多可以传递的命令选项。它们将根据您想要使用的选项（BSD、GNU 或 Unix）而异。在我看来，BSD 风格更受欢迎，所以我们将使用它。如果您好奇，不同风格之间的区别在于您使用的破折号数量和标志。

```bash
ps aux
```

**a** 显示所有正在运行的进程，包括其他用户运行的进程。**u** 显示有关进程的更多详细信息。最后，**x** 列出所有没有关联 TTY 的进程。这些程序将在 TTY 字段中显示 `?`；它们在作为系统启动一部分启动的守护进程中最为常见。

您会注意到现在看到了更多字段。无需记住所有这些；在稍后的高级进程课程中，我们将再次介绍其中一些：

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

另一个非常有用的命令是 **top** 命令。`top` 为您提供系统上正在运行的进程的实时信息，而不是快照。默认情况下，您将每 10 秒刷新一次。`top` 是一个非常有用的工具，可以查看哪些进程占用了您的大量资源。

```bash
top
```

## Exercise

使用带有不同标志的 `ps` 命令，看看输出如何变化。

## Quiz Question

What `ps` flag is used to view detailed information about processes?

## Quiz Answer

u
