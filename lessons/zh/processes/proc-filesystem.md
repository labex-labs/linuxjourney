---
lesson_id: "proc-filesystem"
course_id: "processes"
lang: "zh"
order_index: 10
title: "/proc 文件系统"
description: "了解 Linux 如何通过虚拟 `/proc` 文件系统公开实时的进程和内核信息。"
meta_title: "/proc 文件系统 - 进程管理"
meta_description: "探索 Linux /proc 文件系统，这是一个提供内核和运行进程仪表板式视图的虚拟目录。了解如何访问标准命令之外的额外进程详细信息。"
meta_keywords: "/proc 文件系统，linux proc, 进程信息，linux proc 扩展，系统仪表板，Linux 进程，内核信息"
---

Linux 通常把 `procfs` 挂载到 `/proc`。这个虚拟文件系统以文件和目录的形式呈现由内核生成的接口；其中的内容并不是存储在磁盘上的普通持久文件。它既公开进程状态，也公开部分系统级内核信息。

## 查找进程目录

可以用以下命令查看挂载信息和顶层条目：

```bash
$ findmnt /proc
$ ls /proc
```

数字目录名对应调用者所在 PID 命名空间中可见的进程 ID。例如，在 PID 12345 存在的那个时刻，`/proc/12345` 代表该进程。`/proc/self` 是一个符号链接，会解析为执行观察的进程自身目录；`/proc/thread-self` 则标识当前线程。

可见性和访问权限取决于凭据、命名空间、安全策略以及 `hidepid` 等 procfs 挂载选项。进程可能在列出目录之后、打开其中某个文件之前退出，因此目录消失是检查工具必须妥善处理的正常竞态。

:::single-choice{#proc-filesystem-numeric-directory} 数字目录 `/proc/12345` 通常表示什么？

::option[编号为 12345 的磁盘块。]{#proc-filesystem-disk-block explanation="`/proc` 是虚拟内核接口，不是存放原始磁盘块的目录。"}
::option[当前可见、PID 为 12345 的进程。]{#proc-filesystem-pid-directory .correct explanation="procfs 会把每个进程的数据集中在以其可见 PID 命名的目录下。"}
::option[UID 为 12345 的用户账户。]{#proc-filesystem-user-directory explanation="顶层数字进程目录以 PID 而不是 UID 为键。"}
:::

## 读取进程信息

权限允许时，可以检查进程的状态文件：

```bash
$ less /proc/12345/status
```

其中包含进程名称、状态、各种 ID、凭据、内存计数器、权能和信号掩码等字段。其他常用条目包括：

- `/proc/12345/cmdline`：以空字符分隔的命令行参数
- `/proc/12345/environ`：受访问控制且可能包含敏感信息的环境变量条目
- `/proc/12345/fd/`：表示已打开文件描述符的符号链接
- `/proc/12345/maps`：当前内存映射
- `/proc/12345/cwd`：指向当前工作目录的符号链接

应把这些内容视为不断变化的观察结果。字段可能随内核版本而异，进程也可能在读取多个文件期间改变状态，而且某些计数器还存在名称本身没有体现的细节。

:::single-choice{#proc-filesystem-status-file} 哪个路径包含 PID 12345 易于阅读的字段式摘要？

::option[`/proc/status/12345`]{#proc-filesystem-status-reversed explanation="每个进程的文件位于以 PID 命名的目录中，而不是顶层 `status` 目录下。"}
::option[`/proc/12345/status`]{#proc-filesystem-process-status .correct explanation="每进程 `status` 接口会呈现标识符、状态、内存、信号和凭据字段。"}
::option[`/proc/cpuinfo/12345`]{#proc-filesystem-cpuinfo-pid explanation="`/proc/cpuinfo` 是系统级接口，不是存放每个 PID 状态文件的目录。"}
:::

## 读取系统级接口

并非 `/proc` 中的所有条目都属于某个进程。例如：

- `/proc/cpuinfo`：内核报告的 CPU 信息
- `/proc/meminfo`：系统内存计数器
- `/proc/mounts`：当前进程所看到的挂载信息
- `/proc/loadavg`：平均负载和可运行任务信息
- `/proc/sys/`：运行时内核参数

某些文件是可写的配置接口，尤其是 `/proc/sys` 下的文件。不要仅仅因为它们看起来像普通文件就向其中写入内容。进行已获授权的系统变更前，应先了解参数含义、作用范围、持久化机制和回滚方法。

:::single-choice{#proc-filesystem-system-interface} 哪个条目提供系统级内存计数器，而不是单个进程的状态？

::option[`/proc/self/status`]{#proc-filesystem-self-status explanation="该路径会解析为执行观察的进程自身的每进程状态。"}
::option[`/proc/meminfo`]{#proc-filesystem-memory-info .correct explanation="`meminfo` 包含内核报告的系统内存统计信息。"}
::option[`/proc/1/fd`]{#proc-filesystem-one-fd explanation="在访问控制允许时，此目录表示 PID 1 所拥有的文件描述符。"}
:::

## 通过工具使用 `/proc`

Linux 上的 `ps`、`top` 和 `free` 等工具会从 procfs 和其他内核接口获取大量数据，然后添加标签、执行计算并格式化结果。在日常工作中，如果这些工具已经提供所需字段，应优先使用它们。只有研究过接口文档后，才应为获取特定细节或编写脚本而直接读取 `/proc`。

直接读取程序必须正确解析格式、容忍进程消失、保护敏感输出，并避免假定一次读取就是系统的原子快照。

:::single-choice{#proc-filesystem-live-data} 为什么 `/proc/PID` 可能会在两次检查命令之间消失？

::option[每个 procfs 文件都会每秒自动重命名一次。]{#proc-filesystem-renamed explanation="procfs 不存在定期重命名所有条目的规则。"}
::option[读取 `status` 会删除进程目录。]{#proc-filesystem-read-delete explanation="检查状态是只读操作，不会终止进程或删除目录。"}
::option[进程可能会在观察期间退出。]{#proc-filesystem-process-exit .correct explanation="procfs 反映实时状态，因此进程消失后，内核会移除其对应目录。"}
:::

## 总结

现在，你可以把 procfs 作为一个实时且受访问控制的内核接口使用。

1. 将 `/proc` 下的数字目录与可见 PID 对应起来。
2. 读取选定的每进程文件时，应考虑竞态与信息敏感性。
3. 区分进程目录和系统级接口。
4. 在可靠的日常检查中，优先使用有文档说明的工具和格式。
