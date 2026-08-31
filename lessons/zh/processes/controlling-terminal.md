---
lesson_id: "controlling-terminal"
course_id: "processes"
lang: "zh"
order_index: 2
title: "控制终端"
description: "学习控制终端如何把会话与交互式输入、信号和 shell 作业控制连接起来。"
meta_title: "控制终端 - 进程"
meta_description: "探索 Linux 中控制终端的概念。了解什么是 TTY，TTY 与 PTS 的区别，以及如何使用'ps tty'输出来识别没有控制终端的进程，例如守护进程。"
meta_keywords: "控制终端，ps tty, 什么是 tty, 如何使用 ps, TTY, PTS, Linux 终端，守护进程，Linux 进程"
---

交互式登录会话可以拥有控制终端：它是与会话关联的终端设备，内核用它处理终端生成的信号和作业控制。进程列表中的 `TTY` 字段有助于识别这种关联。

## 终端和伪终端设备

TTY 这个名称源自历史上的电传打字机。在现代 Linux 上，终端接口是设备抽象，不一定对应物理设备。

系统虚拟控制台可能使用 `tty1` 等名称。切换控制台的桌面快捷键因发行版而异，不应想当然。终端模拟器、远程登录或多路复用器通常使用伪终端对，交互端显示为 `pts/3` 等名称。

使用以下命令显示与当前命令标准输入相连的终端：

```bash
$ tty
/dev/pts/3
```

该结果与更广义的控制终端概念相关，但并不完全相同。进程可以重定向标准输入或输出，同时仍处于拥有控制终端的会话中。

:::single-choice{#controlling-terminal-pts-meaning}
`pts/3` 这样的名称通常标识什么？

::option[分配给第三个 shell 的进程 ID。]{#controlling-terminal-pts-pid explanation="PID 是数值进程元数据，不会表示为 `pts/N` 设备名称。"}
::option[交互式会话使用的伪终端设备。]{#controlling-terminal-pts-device .correct explanation="`/dev/pts` 下的目录项是终端模拟器和远程会话常用的伪终端从设备。"}
::option[包含终端程序的文件系统分区。]{#controlling-terminal-pts-partition explanation="该名称标识终端设备接口，而不是存储分区。"}
:::

## 会话、进程组和作业控制

控制终端属于会话，而不只是恰好打开窗口的命令。在该会话中，终端会跟踪前台进程组。Shell 会把前台管道放入该组，使其可以读取输入并接收终端生成的信号。

例如，按下 `Ctrl-C` 通常会让终端驱动程序向前台进程组发送 `SIGINT`。尝试从终端读取的后台组可能收到 `SIGTTIN`。这些规则让 shell 能够协调前台和后台作业。

:::single-choice{#controlling-terminal-ctrl-c-target}
终端通常会把 `Ctrl-C` 生成的信号发送给哪些进程？

::option[当前用户拥有的每个进程。]{#controlling-terminal-ctrl-c-user explanation="终端生成的信号仅限于前台进程组，而不是用户的所有进程。"}
::option[无论前台作业是什么都只发送给登录 shell。]{#controlling-terminal-ctrl-c-shell explanation="另一个作业位于前台时，该作业的进程组才是通常的信号目标。"}
::option[终端的前台进程组。]{#controlling-terminal-ctrl-c-foreground .correct explanation="终端驱动程序会向当前前台进程组发送 `SIGINT`。"}
:::

## 阅读 `TTY` 列

如果需要稳定视图，应明确请求选定的进程字段：

```bash
$ ps -o pid,tty,stat,cmd
```

`pts/3` 等终端名称标识为该进程记录的控制终端。问号（`?`）通常表示进程没有控制终端。

许多服务进程没有控制终端，因为服务管理器会独立于交互式登录会话启动它们。不过，缺少 TTY 本身并不能证明进程是守护进程，后台 shell 作业也仍然可以拥有控制终端。

:::single-choice{#controlling-terminal-question-mark}
`ps` 的 `TTY` 列中，`?` 通常表示什么？

::option[进程没有控制终端。]{#controlling-terminal-no-tty .correct explanation="没有控制终端与进程关联时，通常用问号显示。"}
::option[终端正忙，无法读取。]{#controlling-terminal-busy-tty explanation="该标记表示缺少控制终端，而不是临时设备争用。"}
::option[该进程始终是内核线程。]{#controlling-terminal-kernel-only explanation="内核线程通常没有终端，但许多用户空间服务也没有。"}
:::

## 终端关闭和挂断

终端连接消失时，内核或终端/会话软件可以向相关进程发送 `SIGHUP`。进程可能终止、捕获信号、忽略信号，也可能已经被安排为在信号后继续运行。`disown` 等 shell 功能、`nohup` 等工具、多路复用器和服务管理器都会影响生命周期行为。

因此，关闭终端并不保证从中启动的每个命令都会退出。需要确认持久性时，应检查进程的会话、信号处理、重定向和监督程序。

:::single-choice{#controlling-terminal-close-effect}
为什么“关闭终端始终会终止从中启动的每个进程”这一说法不准确？

::option[Linux 终端关闭时从不生成任何信号。]{#controlling-terminal-never-signals explanation="挂断信号确实是终端和会话行为，但结果并不保证一定终止。"}
::option[只有带数值 PID 的进程才能收到挂断信号。]{#controlling-terminal-pid-hangup explanation="所有普通进程都有数值 PID；这并不决定它们是否能在终端关闭后存活。"}
::option[进程可以处理或避开挂断，也可能由独立机制管理。]{#controlling-terminal-hangup-handling .correct explanation="信号处置、shell 行为、多路复用器和监督程序都可以让进程在终端关闭后继续运行。"}
:::

[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)实验提供了安全环境，可比较前台作业、后台作业及其 `TTY` 字段。

## 总结

现在，你可以把控制终端与交互式进程管理联系起来。

1. 区分虚拟终端和伪终端。
2. 把终端信号与前台进程组联系起来。
3. 解释 `ps` 输出中的终端名称和 `?`。
4. 把终端关闭视为发出信号，而不是保证进程终止。
