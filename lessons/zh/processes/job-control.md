---
index: 11
lang: "zh"
title: "作业控制"
meta_title: "作业控制 - 进程管理"
meta_description: "探索我们的 Linux 教程，学习如何使用作业控制来有效管理后台进程。了解如何使用 jobs、bg、fg 和 kill 命令实现强大的 shell 多任务处理。"
meta_keywords: "Linux 作业控制，后台进程，jobs 命令，bg 命令，fg 命令，kill 命令，Linux 教程，初学者 Linux"
---

## Lesson Content

在 Linux 中，您经常会遇到需要很长时间才能完成的命令。您不必等待并让终端无法使用，而是可以使用 **Linux 作业控制 (job control)** 来管理这些任务。此强大功能允许您在单个 shell 会话中运行和管理多个 **后台进程 (background processes)**，从而显著提高您的工作效率。

### 在后台运行命令

要直接在后台启动一个进程，只需在命令后附加一个和号（`&`）。这会立即返回您的 shell 提示符，允许您在命令执行时继续工作。

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### 列出后台作业

您可以使用 `jobs` 命令查看所有在后台运行的作业。

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

输出在第一列提供了作业 ID、其状态以及原始命令。`+` 符号表示最近启动的后台作业，而 `-` 符号标记第二个最近的作业。

### 管理活动进程

如果一个命令已经在前台运行，而您决定需要收回终端控制权怎么办？您不必停止它。首先，按 `Ctrl-Z` 暂停正在运行的进程。然后，使用 `bg` 命令将该暂停的作业发送到后台。

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &
```

现在，`sleep 1003` 进程作为后台作业正在运行，您可以使用 `jobs` 命令进行验证。

### 将作业调至前台

要将后台进程调回前台，请使用 `fg` 命令。您可以指定一个特定的作业及其 ID（例如 `fg %1`）。如果您在没有参数的情况下运行 `fg` 命令，它将把最近的后台作业（标记为 `+` 的作业）调到前台。

```bash
fg %1
```

### 终止后台作业

如果您需要停止一个后台进程，可以使用 `kill` 命令。与 `fg` 命令类似，您使用百分号（`%`）前缀来引用作业的 ID。这是 Linux 作业控制的一个关键功能。

```bash
kill %1
```

掌握这些命令对于任何希望在 shell 中高效多任务处理的 Linux 初学者来说都是至关重要的。

## Exercise

为了将您对 Linux 作业控制的知识付诸实践，请尝试此动手实验。它将帮助您巩固对管理前台和后台进程的理解。

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 直接解决长时间运行命令的场景，练习与前台和后台进程交互、监控资源以及终止进程。

## Quiz Question

用于列出后台作业的命令是什么？ (请用英文回答，仅使用小写字母。)

## Quiz Answer

jobs
