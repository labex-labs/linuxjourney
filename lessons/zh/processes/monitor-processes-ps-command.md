---
lesson_id: "monitor-processes-ps-command"
course_id: "processes"
lang: "zh"
order_index: 1
title: "ps（进程）"
description: "学习使用 `ps` 获取进程快照，并使用 `top` 监控不断变化的活动。"
meta_title: "ps (进程) - 进程管理"
meta_description: "使用我们全面的指南探索 Linux ps 命令。了解如何在 Linux 中使用 ps -ef 命令和其他选项来查看正在运行的进程、理解 PID 以及管理系统任务。开启您的 Linux 之旅的完美起点。"
meta_keywords: "ps 命令，ps -ef linux, ps -ef 命令，linux ps -ef, ps -e linux, Linux 进程，进程 ID, PID, top 命令，Linux 之旅"
---

进程是程序的运行实例，包含其内存、凭据、打开的资源和执行状态。Linux 使用数值进程 ID（PID）标识每个活动进程。PID 在同时存在的进程中是唯一的，但进程退出后，内核可以重复使用它。

## 获取基本快照

不带选项运行 `ps`，可以查看由当前实现默认规则选择的快照，通常是与当前终端和用户关联的进程：

```text
$ ps
    PID TTY          TIME CMD
  41230 pts/4    00:00:00 bash
  51224 pts/4    00:00:00 ps
```

常见字段包括：

- `PID`：进程 ID
- `TTY`：控制终端；没有关联时为 `?`
- `TIME`：累计 CPU 时间，而不是实际经过的墙上时钟时间
- `CMD`：命令名称或命令行，取决于所选格式

确切列和默认选择规则因 `ps` 实现及环境而异。

:::single-choice{#ps-command-pid-meaning} `PID` 列标识什么？

::option[进程的当前目录编号。]{#ps-command-pid-directory explanation="当前目录是文件系统引用，不由 PID 表示。"}
::option[以秒为单位的累计 CPU 时间。]{#ps-command-pid-cpu explanation="CPU 使用量显示在 `TIME` 等独立字段中。"}
::option[内核分配的进程 ID。]{#ps-command-pid-kernel .correct explanation="PID 是用于引用活动进程的数值标识符。"}
:::

## 使用 BSD 风格选项列出进程

Linux `ps` 接受多种选项风格。BSD 风格选项通常不带开头的连字符：

```bash
$ ps aux
```

在这个组合中：

- `a` 扩大选择范围，包含拥有终端的其他用户进程。
- `x` 也包含没有控制终端的进程，与 `a` 组合时进一步扩大选择。
- `u` 选择面向用户的输出格式，包含 `USER`、`%CPU`、`%MEM`、`VSZ` 和 `RSS` 等字段。

由于选项含义可能相互作用，应解释完整组合，而不是把每个字母视为独立命令。

:::single-choice{#ps-command-aux-user-format} 在 `ps aux` 中，哪个选项请求面向用户的输出格式？

::option[`u`]{#ps-command-aux-u .correct explanation="BSD 风格的 `u` 选项会选择一组面向用户的输出列。"}
::option[`x`]{#ps-command-aux-x explanation="`x` 选项影响进程选择，尤其是没有控制终端的进程。"}
::option[`a`]{#ps-command-aux-a explanation="`a` 选项把选择范围扩大到当前用户终端进程之外。"}
:::

## 使用标准风格选项

广泛使用的标准风格命令 `ps -ef` 会为选项添加开头连字符：

```bash
$ ps -ef
```

- `-e` 选择调用者可见的每个进程。
- `-f` 请求完整格式列表。

输出通常包含 `UID`、`PID`、`PPID`、启动时间和命令信息。`PPID` 是父进程 ID。该列表本身并非层次结构；父子布局很重要时，可使用实现支持的 `--forest` 等选项，或 `pstree` 等专用树查看器。

:::single-choice{#ps-command-ef-selection} `ps -ef` 中的 `-e` 请求什么？

::option[每秒更新一次，直到被中断。]{#ps-command-e-refresh explanation="`ps` 生成快照；持续刷新是 `top` 等工具的功能。"}
::option[包含调用者可见的每个进程。]{#ps-command-e-every .correct explanation="标准风格的 `-e` 选项会把快照扩展到所有可选进程。"}
::option[只包含命令以错误结束的进程。]{#ps-command-e-errors explanation="进程选择并不依据命令最终的退出状态。"}
:::

## 随时间监控活动

`ps` 输出一次快照后便退出。使用 `top` 可获得定期刷新的交互式视图：

```bash
$ top
```

`top` 有助于找出不断变化的 CPU 和内存消耗者，但其数值是会波动的采样结果。应通过多次观察确认疑似问题，并结合机器的 CPU 数量、内存计算方式和工作负载解释百分比。

:::single-choice{#ps-command-snapshot-versus-top} 本课介绍的哪个工具默认会定期刷新进程显示？

::option[`top`]{#ps-command-top-refresh .correct explanation="`top` 是会定时更新显示的交互式监控工具。"}
::option[`ps -ef`]{#ps-command-ps-ef-snapshot explanation="该命令会输出完整格式的进程快照，然后退出。"}
::option[`ls -l`]{#ps-command-ls-files explanation="`ls -l` 显示文件系统目录项，而不是实时进程监控器。"}
:::

要动手练习，可以使用[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)比较快照与交互式监控器，或在 [Linux `top` 命令](https://labex.io/zh/labs/linux-linux-top-command-real-time-system-monitoring-388500)实验中探索排序与筛选。

## 总结

现在，你可以选择进程视图并解释其基本标识符。

1. 把 PID 视为当前活动进程可重复使用的标识符。
2. 使用普通 `ps` 获取较小的默认快照。
3. 使用 `ps aux` 或 `ps -ef` 获得更广的选择范围和更丰富的列。
4. 需要观察随时间变化时使用 `top`。
