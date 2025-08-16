---
title: "kill (终止)"
description: "学习如何使用 Linux 'kill' 命令来终止进程。了解 SIGTERM、SIGKILL 和其他用于进程管理的信号。立即开始学习！"
keywords: "kill 命令，Linux 进程，SIGTERM, SIGKILL, Linux 教程，初学者，进程管理，Linux 指南"
---

## Lesson Content

你可以发送信号来终止进程；这样的命令恰如其分地命名为 `kill` 命令。

```bash
kill 12445
```

`12445` 是你想要终止的进程的 PID。默认情况下，它发送一个 `TERM` 信号。`SIGTERM` 信号被发送给一个进程，以请求其终止，允许它干净地释放资源并保存其状态。

你也可以使用 `kill` 命令指定一个信号：

```bash
kill -9 12445
```

这将运行 `SIGKILL` 信号并终止进程。

### SIGHUP、SIGINT、SIGTERM、SIGKILL、SIGSTOP 之间有什么区别？

这些信号听起来都相当相似，但它们确实有其不同之处。

- SIGHUP - 挂断，当控制终端关闭时发送给进程。例如，如果你关闭了一个正在运行进程的终端窗口，你将收到一个 `SIGHUP` 信号。所以，基本上，你被挂断了。
- SIGINT - 是一个中断信号，所以你可以使用 Ctrl-C，系统会尝试优雅地终止进程。
- SIGTERM - 终止进程，但允许它首先进行一些清理工作。
- SIGKILL - 终止进程，彻底终止，不进行任何清理。
- SIGSTOP - 停止/暂停一个进程。

## Exercise

使用不同的信号终止一些进程。

## Quiz Question

默认 `kill` 命令的信号名称是什么？

## Quiz Answer

SIGTERM
