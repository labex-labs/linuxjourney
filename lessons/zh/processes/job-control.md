---
lesson_id: "job-control"
course_id: "processes"
lang: "zh"
order_index: 11
title: "作业控制"
description: "了解交互式 shell 如何管理前台、后台和已停止的作业。"
meta_title: "作业控制 - 进程管理"
meta_description: "探索我们的 Linux 教程，学习如何使用作业控制来有效管理后台进程。了解如何使用 jobs、bg、fg 和 kill 命令实现强大的 shell 多任务处理。"
meta_keywords: "Linux 作业控制，后台进程，jobs 命令，bg 命令，fg 命令，kill 命令，Linux 教程，初学者 Linux"
---

交互式 shell 使用作业控制来协调同一终端会话中的管道。一个作业可以包含一个进程，也可以包含整条管道；这些进程通常被放进同一个进程组，以便终端和 shell 将其作为一个整体操作。

## 启动后台作业

在命令末尾添加 `&`，可以异步启动管道：

```bash
$ sleep 1000 &
[1] 18420
```

shell 不会等待作业结束，而是直接返回提示符。后台状态并不会自动重定向输出、脱离控制终端，也不能保证作业在退出登录后继续运行。需要时应显式重定向输入和输出；必须在交互式 shell 结束后继续运行的工作，则应使用服务管理器、调度器或终端复用器。

后台作业若试图从控制终端读取输入，通常会收到 `SIGTTIN` 并停止，因为它并不是终端的前台进程组。

:::single-choice{#job-control-ampersand-effect}
末尾的 `&` 会要求交互式 shell 做什么？

::option[保证作业在退出登录和系统重启后继续运行。]{#job-control-survive-restart explanation="仅仅放到后台既不能提供持久监管，也不能让作业在重启后继续运行。"}
::option[把管道作为后台作业运行，并在显示下一个提示符前不等待它完成。]{#job-control-background-job .correct explanation="shell 会异步启动作业，并可继续接收其他命令。"}
::option[丢弃作业的标准输出和错误。]{#job-control-discard-output explanation="如果没有重定向，后台作业仍然可以向终端写入内容。"}
:::

## 列出 shell 作业

`jobs` 内建命令会列出当前 shell 已知的作业：

```text
$ jobs
[1]    Running    sleep 1000 &
[2]-   Running    sleep 1001 &
[3]+   Stopped    sleep 1002
```

方括号中的数字是 shell 作业 ID，而不是 PID。添加 `%` 前缀即可组成 `%1` 这样的作业说明符。`+` 标记表示当前作业，许多命令在未提供操作数时会选择它；`-` 则表示上一个作业。

由于作业表属于单个 shell，另一个终端中的 shell 通常无法通过自己的 `jobs`、`fg` 或 `bg` 内建命令列出或操作这些作业。

:::single-choice{#job-control-jobs-scope}
`jobs` 内建命令会列出什么？

::option[当前 shell 会话跟踪的作业。]{#job-control-jobs-current-shell .correct explanation="作业 ID 和状态由启动或接管这些作业的交互式 shell 维护。"}
::option[系统当前可见的所有进程。]{#job-control-jobs-all-processes explanation="系统级进程检查应使用 `ps` 等工具；shell 作业表的范围更小。"}
::option[仅列出系统启动期间启动的服务。]{#job-control-jobs-boot-services explanation="启动服务通常由服务管理器监管，而不属于交互式 shell 的作业表。"}
:::

## 停止与继续作业

作业在前台运行时，按下 `Ctrl-Z` 通常会让终端向其前台进程组发送 `SIGTSTP`。作业停止后，shell 会重新取得控制权：

```text
$ sleep 1002
^Z
[3]+  Stopped    sleep 1002
```

使用以下命令，可以让当前已停止的作业在后台继续运行：

```bash
$ bg
```

`bg` 会发送继续信号，并让作业留在终端前台之外。它只对已停止的作业有用；已经在后台运行的命令不需要恢复。

:::single-choice{#job-control-bg-purpose}
`bg %3` 会对已停止的作业 3 做什么？

::option[把它的文件移动到名为 `bg` 的目录。]{#job-control-bg-files explanation="`bg` 是 shell 的作业控制内建命令，不会移动文件系统对象。"}
::option[让它作为后台作业继续运行。]{#job-control-bg-continue .correct explanation="shell 会恢复选定的已停止作业，但不会把终端前台分配给它。"}
::option[用 `SIGKILL` 终止它。]{#job-control-bg-kill explanation="该内建命令会继续作业，而不是终止作业。"}
:::

## 把作业移到前台

使用 `fg` 和作业说明符，可以让作业成为终端的前台进程组并等待它：

```bash
$ fg %1
```

未提供操作数时，`fg` 通常选择由 `+` 标记的当前作业。已停止的作业进入前台时会同时恢复运行。

:::single-choice{#job-control-fg-effect}
`fg %1` 会做什么？

::option[把作业 1 分配到终端前台并等待它。]{#job-control-fg-foreground .correct explanation="shell 会把选定作业移到前台，使其能够与终端交互。"}
::option[把作业 1 改成 PID 1。]{#job-control-fg-pid-one explanation="shell 作业 ID 不会取代或改写进程 ID。"}
::option[在后台启动作业 1 的另一个副本。]{#job-control-fg-copy explanation="`fg` 操作现有作业，不会创建副本。"}
:::

## 向作业发送信号

shell 允许 `kill` 接受作业说明符：

```bash
$ kill -TERM %1
```

这通常会向作业的进程组发送信号，而不只是管道中的某一个成员。应先检查选中的作业，并在考虑强制升级前使用 `SIGTERM`。作业说明符属于 shell 语法；脚本和外部工具更常使用核实过的 PID 或进程组 ID。

:::single-choice{#job-control-job-specification}
哪个操作数表示 shell 作业 1，而不是进程 ID 1？

::option[`1`]{#job-control-plain-one explanation="`kill` 通常会把纯数字操作数解释为 PID。"}
::option[`#1`]{#job-control-hash-one explanation="这里介绍的 shell 作业 ID 语法并不使用井号前缀。"}
::option[`%1`]{#job-control-percent-one .correct explanation="百分号前缀表示 shell 作业说明符。"}
:::

可以在[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)实验中使用 `sleep` 等无害命令练习这些操作。

## 总结

现在，你可以有意识地在 shell 控制的不同状态之间移动作业。

1. 使用 `&` 启动后台作业，但不要把它误认为自动脱离终端。
2. 使用 `jobs` 检查当前 shell 的作业表。
3. 使用 `Ctrl-Z` 停止作业，再用 `bg` 让它在后台继续。
4. 使用 `fg` 把选定作业带回终端。
5. 发送信号时，用 `%JOB_ID` 指定 shell 作业。
