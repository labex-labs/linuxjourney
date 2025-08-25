---
index: 7
lang: "zh"
title: "kill (终止)"
meta_title: "kill (终止) - 进程"
meta_description: "了解如何使用 Linux 'kill' 命令终止进程。理解 SIGTERM、SIGKILL 和其他用于进程管理的信号。立即开始学习！"
meta_keywords: "kill 命令，Linux 进程，SIGTERM, SIGKILL, Linux 教程，初学者，进程管理，Linux 指南"
---

## Lesson Content

您可以发送终止进程的信号；这样的命令恰当地命名为 `kill` 命令。

```bash
kill 12445
```

`12445` 是您要终止的进程的 PID。默认情况下，它发送一个 `TERM` 信号。`SIGTERM` 信号被发送到进程以请求其终止，允许它干净地释放其资源并保存其状态。

您还可以使用 `kill` 命令指定一个信号：

```bash
kill -9 12445
```

这将运行 `SIGKILL` 信号并终止进程。

### SIGHUP、SIGINT、SIGTERM、SIGKILL、SIGSTOP 之间有什么区别？

这些信号听起来都相当相似，但它们确实有其区别。

- SIGHUP - 挂断，当控制终端关闭时发送给进程。例如，如果您关闭了一个正在运行进程的终端窗口，您将收到一个 `SIGHUP` 信号。所以，基本上，您被挂断了。
- SIGINT - 是一个中断信号，因此您可以使用 Ctrl-C，系统将尝试优雅地终止进程。
- SIGTERM - 终止进程，但允许它首先进行一些清理。
- SIGKILL - 终止进程，用火杀死它，不进行任何清理。
- SIGSTOP - 停止/暂停进程。

## Exercise

熟能生巧！这里有一些动手实验来巩固您对进程管理和终止的理解：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 在此实验中，您将学习在 Linux 系统上管理和监控进程的基本技能。您将探索如何与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，使用 `renice` 调整优先级，以及使用 `kill` 终止它们。

此实验将帮助您在实际场景中应用进程控制和终止的概念，并建立管理 Linux 进程的信心。

## Quiz Question

默认 `kill` 命令的信号名称是什么？

## Quiz Answer

SIGTERM
