---
index: 1
lang: "zh"
title: "ps (进程)"
meta_title: "ps (进程) - 进程管理"
meta_description: "使用我们全面的指南探索 Linux ps 命令。了解如何在 Linux 中使用 ps -ef 命令和其他选项来查看正在运行的进程、理解 PID 以及管理系统任务。开启您的 Linux 之旅的完美起点。"
meta_keywords: "ps 命令，ps -ef linux, ps -ef 命令，linux ps -ef, ps -e linux, Linux 进程，进程 ID, PID, top 命令，Linux 之旅"
---

## Lesson Content

### 理解 Linux 进程

进程是当前在您的机器上运行的程序。Linux 内核管理它们，每个进程都会被分配一个唯一的数字，称为**进程 ID (PID)**。PID 通常在新进程创建时按顺序分配。

### ps 命令基本用法

要快速查看活动的进程，只需运行 `ps` 命令。这会提供与您当前终端会话相关的进程的快速快照。

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

此输出显示了几个关键细节：

- **PID**: 唯一的进程 ID。
- **TTY**: 控制进程的终端。
- **STAT**: 进程的当前状态。
- **TIME**: 进程使用的总 CPU 时间。
- **CMD**: 启动进程的命令。

### 使用 BSD 风格选项探索 ps

`ps` 命令用途非常广泛，它有很多选项属于不同的语法风格（BSD、System V、GNU）。BSD 风格不使用连字符 (-) 作为选项前缀，非常常见。一个流行的组合是 `ps aux`：

```bash
ps aux
```

这些选项的含义如下：

- **a**: 显示所有用户的所有进程。
- **u**: 提供详细的、面向用户的格式。
- **x**: 包括未附加到任何终端的进程。这些通常是系统守护进程，它们在启动时运行，并在 TTY 列中显示 `?`。

此命令提供了更丰富的输出，包含 `USER`、`%CPU`、`%MEM`、`VSZ` 和 `RSS` 等额外列。目前，我们将重点关注 PID、STAT 和 COMMAND。

### 在 Linux 中使用 ps -ef 命令

另一种极其流行的语法是 System V 风格。系统管理员经常使用 **ps -ef 命令**。这是全面了解系统上所有运行内容的强大方法。

```bash
ps -ef
```

**ps -ef linux** 命令提供所有进程的完整列表。

- **-e**: 选择系统上的每个进程。
- **-f**: 显示“完整格式”列表，其中包含 UID、PPID（父进程 ID）、C（CPU 利用率）和 STIME（启动时间）等详细信息。

许多用户更喜欢 `ps -ef` 而不是 `ps aux`，因为它提供了清晰的层次结构视图和详细信息。在 Linux 系统上进行故障排除时，运行 **linux ps -ef** 通常是诊断问题的首要步骤之一。一个更简单的变体 `ps -e linux` 也会列出所有进程，但格式不太详细。

### 使用 top 进行实时监控

虽然 `ps` 提供快照，但 `top` 命令提供了系统上进程的实时、动态视图。它是识别哪些进程占用了最多 CPU 或内存的绝佳工具。默认情况下，显示每隔几秒刷新一次。

```bash
top
```

## Exercise

实践是掌握 Linux 命令的关键。以下动手实验将帮助您巩固对进程监控和管理的理解：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 练习管理和监控 Linux 系统进程的基本技能，包括与前台/后台进程交互、使用 `ps` 检查、使用 `top` 监控以及使用 `kill` 终止。
2. **[Linux top 命令：实时系统监控](https://labex.io/zh/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - 学习使用 Linux `top` 命令进行实时系统监控，包括排序进程、调整更新间隔和按用户过滤。

这些实验将帮助您在现实场景中应用进程识别和监控的概念，增强您作为 Linux 系统管理员的信心。

## Quiz Question

与 `a` 和 `x` 标志一起使用时，哪个 `ps` 标志用于查看有关进程的详细、面向用户的信息？请用单个小写英文字母回答。

## Quiz Answer

u
