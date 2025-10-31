---
index: 8
lang: "zh"
title: "进程优先级（Nice 值）"
meta_title: "进程优先级（Nice 值）- 进程管理"
meta_description: "了解 Linux 中的进程优先级（Nice 值）及其如何影响进程调度。本教程解释了 Linux 进程的 Nice 值，并介绍使用 nice 和 renice 命令来管理 CPU 调度和提高系统性能。"
meta_keywords: "Linux Nice 值，Linux 进程优先级，Linux Nice 值是什么，Linux 进程 Nice 值，进程优先级，nice 命令，renice 命令，CPU 调度"
---

## Lesson Content

当您在计算机上运行多个应用程序时，它们似乎是同时运行的。实际上，CPU 在它们之间快速切换，为每个进程分配一小部分处理时间。

### CPU 如何管理进程

每个进程都会获得一小段 CPU 时间，称为“时间片”。时间片结束后，进程会被暂停，CPU 会转到下一个进程。默认情况下，Linux 内核以轮询（round-robin）方式调度进程，确保每个进程都能公平地获得 CPU 时间，直到完成。内核调度器在管理这些快速切换方面非常高效。

### 什么是 Linux 中的 Niceness

虽然进程不能直接控制它们的 CPU 时间，但您可以影响内核的调度决策。这是通过调整进程的 **linux niceness** 值来实现的。“Niceness”一词指的是一个进程对系统中其他进程有多“友好”。

**进程的 Niceness** 用一个数字表示，范围从 -20（最高优先级）到 19（最低优先级）。

- 高的 Niceness 值（例如 19）意味着该进程非常“友好”，优先级较低，会将 CPU 时间让给其他进程。
- 低或负的 Niceness 值（例如 -20）意味着该进程不“友好”，会要求更多的 CPU 时间，从而获得更高的优先级。

理解 **linux process niceness** 是有效管理系统资源的关键。

### 调整进程优先级

您可以使用 `top` 命令查看正在运行进程的当前 Niceness 级别。查找显示 Niceness 值的 `NI` 列。

```bash
top
```

要控制 **niceness linux** 值，您可以使用 `nice` 和 `renice` 命令。

使用 `nice` 命令以特定的 Niceness 级别启动一个新进程。例如，以下命令以 Niceness 值为 5 启动 `apt upgrade`。

```bash
nice -n 5 apt upgrade
```

要更改已运行进程的优先级，请使用 `renice` 命令。以下命令将 PID 为 3245 的进程的 Niceness 更改为 10。

```bash
renice 10 -p 3245
```

## Exercise

通过这个动手实验来巩固您对 Linux 进程管理和调度的理解：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习与前台和后台进程的交互，使用 `ps` 检查它们，使用 `top` 监控资源，使用 `renice` 调整优先级，以及使用 `kill` 终止它们。

此实验将帮助您在实际场景中应用进程调度和 Niceness 的概念，并增强管理 Linux 进程的信心。

## Quiz Question

If you want a process to get more CPU priority, should you use a lower or higher nice number? Please answer in a single English word, all lowercase.

## Quiz Answer

lower
