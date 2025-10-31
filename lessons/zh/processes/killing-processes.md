---
index: 7
lang: "zh"
title: "kill (终止)"
meta_title: "kill (终止) - 进程管理"
meta_description: "掌握 Linux kill 命令以管理和终止进程。本指南涵盖 kill 与 terminate 的区别，并解释了如 kill sigterm (SIGTERM)、SIGKILL 和 kill sighup (SIGHUP) 等信号。"
meta_keywords: "kill 命令，kill sigterm, kill sighup, linux kill -0, kill 与 terminate, kill -15 linux, SIGTERM, SIGKILL, 进程管理，终止进程"
---

## Lesson Content

在 Linux 中，您可以通过向进程发送信号来管理它们。主要的命令是 `kill`，尽管其名称如此，但它可以发送各种信号，而不仅仅是终止进程的信号。

### 使用 kill sigterm 进行默认终止

当您仅使用进程 ID (PID) 执行 `kill` 命令时，它默认发送一个 `TERM` 信号。这是请求程序终止的标准、优雅的方式。

```bash
kill 12445
```

`kill sigterm` 信号（也称为 `SIGTERM` 或信号 15）请求进程干净地关闭。这给了进程一个机会来保存其进度并正确释放资源。您也可以明确使用信号编号，使 `kill -15 12445` 等同于上述命令。这解决了常见的 `kill -15 linux` 查询。

### 使用 SIGKILL 强制终止

有时进程会无响应，不会对 `SIGTERM` 信号作出反应。在这些情况下，您可以使用 `KILL` 信号强制停止它。

```bash
kill -9 12445
```

`SIGKILL` 信号（信号 9）会立即终止进程，不给它清理的机会。这是 `kill vs terminate` 争论中的一个关键区别；`SIGKILL` 是无条件终止，而 `SIGTERM` 是礼貌的请求。

### 理解其他常见信号

虽然 `SIGTERM` 和 `SIGKILL` 最常见，但其他信号对于进程管理也很有用。

- **SIGHUP**: `kill sighup` 信号（挂断，信号 1）传统上在控制终端关闭时发送给进程。它可以用来告诉守护进程重新加载其配置文件。
- **SIGINT**: 当您按下 `Ctrl-C` 时，会发送中断信号（信号 2）。它请求进程中断当前操作。
- **SIGSTOP**: 此信号（信号 19）在不终止进程的情况下暂停它。进程稍后可以用 `SIGCONT` 信号恢复。

### 使用 kill -0 检查进程是否存在

一个特殊的用例是 `linux kill -0`。此命令实际上不发送信号，而是检查具有指定 PID 的进程是否存在以及您是否有权限向其发送信号。

```bash
kill -0 12445
```

如果命令成功执行（退出代码为 0），则进程存在。如果失败，则进程不存在或您没有权限。

## Exercise

为了应用所学知识，请尝试此动手实验，以加强您对进程管理和终止的理解：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 在此实验中，您将学习在 Linux 系统上管理和监控进程的基本技能。您将探索如何与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，使用 `renice` 调整优先级，以及使用 `kill` 终止它们。

此实验将帮助您在实际场景中应用进程控制和终止的概念，并增强管理 Linux 进程的信心。

## Quiz Question

默认 `kill` 命令的信号名称是什么？请用英文回答。请注意，答案区分大小写。

## Quiz Answer

SIGTERM
