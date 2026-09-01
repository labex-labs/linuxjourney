---
lesson_id: "process-creation"
course_id: "processes"
lang: "zh"
order_index: 4
title: "进程创建"
description: "学习 fork、exec、PID 和父进程关系如何参与 Linux 进程创建。"
meta_title: "进程创建 - 进程管理"
meta_description: "探索 Linux 中进程创建的基础知识。本指南涵盖 fork 和 execve 系统调用、父/子关系（PID 和 PPID）以及 init 进程的作用。了解如何在 Linux 中创建进程并理解操作系统中进程创建的核心概念。"
meta_keywords: "linux 进程创建，linux 进程创建，在 linux 中创建进程，操作系统进程创建，进程创建，fork, execve, PID, PPID, init 进程，Linux 进程"
---

Linux 进程会形成父子关系。Shell 通常先创建子进程，再安排该子进程执行所请求的程序，从而启动外部命令。经典解释会把这项工作分成 `fork` 和 `exec` 操作。

## 使用 `fork` 创建子进程

`fork()` 系统调用会根据调用进程创建子进程。父进程和子进程都会从 `fork` 的返回点继续，但获得不同的返回值和不同的 PID。

子进程获得逻辑上独立的进程状态。Linux 最初可以使用写时复制共享物理内存页面，只有某个进程修改页面时才复制。打开的文件描述符会被继承，并引用相同的底层打开文件描述，因此文件偏移等细节可能继续共享。

:::single-choice{#process-creation-fork-result} 成功的 `fork()` 会创建什么？

::option[只在同一进程内创建替代程序。]{#process-creation-fork-replacement explanation="替换当前程序映像是 `exec` 操作的职责。"}
::option[拥有新 PID 的子进程。]{#process-creation-fork-child .correct explanation="`fork()` 会建立独立的子进程和父子关系。"}
::option[立即永久复制每一个物理内存页。]{#process-creation-fork-full-copy explanation="Linux 通常使用写时复制，而不是立即复制所有物理页面。"}
:::

## 使用 `execve` 替换程序

`execve()` 调用会把新程序加载到调用进程中。成功时，它会替换进程映像，不会返回旧程序。PID 保持不变，因为 `execve()` 不会创建新进程。

因此，许多 shell 命令遵循 fork-exec 模式：

1. Shell 创建子进程。
2. 子进程准备重定向和其他执行状态。
3. 子进程执行所请求的程序。
4. Shell 根据前台或后台执行选择等待或继续。

库和应用程序可以提供 `posix_spawn()` 等更高层接口，Linux 也有 `clone()` 等其他原语。熟悉的 fork-exec 模型仍然有用，但不是唯一可能的接口。

:::single-choice{#process-creation-exec-pid} 成功执行 `execve()` 后，进程的 PID 会发生什么？

::option[变得与父进程 PID 相同。]{#process-creation-exec-parent-pid explanation="父进程和子进程仍然保留不同的进程 ID。"}
::option[程序映像被替换，但 PID 保持不变。]{#process-creation-exec-same-pid .correct explanation="`execve()` 会转换调用进程，而不是创建另一个进程。"}
::option[在新程序启动前被移除。]{#process-creation-exec-pid-removed explanation="现有进程会以原 PID 继续运行新的代码、数据、栈和相关程序状态。"}
:::

## 检查父进程和子进程 ID

`PID` 标识进程，`PPID` 标识其父进程。明确请求这些字段：

```bash
$ ps -o pid,ppid,stat,cmd
```

如果 shell 启动 `ps`，该 shell 的 PID 通常会显示为 `ps` 进程的 `PPID`。时机很重要：短生命周期进程可能在单独的观察命令捕获之前就已经退出。

:::single-choice{#process-creation-ppid} 进程列表中的 `PPID` 表示什么？

::option[之前曾分配给该进程的 PID。]{#process-creation-previous-pid explanation="PID 可以重复使用，但 `PPID` 不记录标识符历史。"}
::option[进程的调度优先级标识符。]{#process-creation-priority-id explanation="调度优先级由 priority 或 nice 值等其他字段表示。"}
::option[父进程的进程 ID。]{#process-creation-parent-pid .correct explanation="PPID 记录进程当前的父进程关系。"}
:::

## PID 1 和重新指定父进程

内核会以 PID 1 启动第一个用户空间进程。根据系统，它可能是 `systemd`、其他 init 实现，或容器/PID 命名空间中的小型 init。PID 1 会启动并监督部分用户空间环境，还承担特殊的信号和孤儿进程回收职责。

父进程先于子进程退出时，子进程会被重新指定给适当的 subreaper，或其 PID 命名空间中的 init 进程。它不必仅因原父进程结束而终止。

:::single-choice{#process-creation-pid-one} 关于 PID 1，哪个说法准确？

::option[它必须始终是可执行名称恰好为 `init` 的程序。]{#process-creation-pid-one-name explanation="具体实现可以是 `systemd`、其他 init 或容器特定程序。"}
::option[它是直接创建当前每个运行进程的父进程。]{#process-creation-pid-one-direct explanation="大多数进程是经过许多代中间父进程创建的。"}
::option[它是其 PID 命名空间中的第一个进程，并承担类似 init 的职责。]{#process-creation-pid-one-init .correct explanation="PID 1 在一个 PID 命名空间中承担用户空间进程监督和回收的核心职责。"}
:::

[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)实验让你可以在运行前台和后台命令时观察父进程与子进程 ID。

## 总结

现在，你可以追踪经典的 Linux 进程创建顺序。

1. 使用 `fork()` 创建具有不同 PID 的子进程。
2. 使用 `execve()` 替换进程映像而不改变 PID。
3. 读取 PID 和 PPID 以识别父子关系。
4. 认识 PID 1 和 subreaper 是重新指定父进程后的子进程去向。
