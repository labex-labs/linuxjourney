---
lesson_id: "process-states"
course_id: "processes"
lang: "zh"
order_index: 9
title: "进程状态"
description: "学习如何解读 `ps` 快照中常见的 Linux 进程状态码。"
meta_title: "进程状态 - 进程管理"
meta_description: "Linux 进程状态的综合指南。了解 Linux 中的不同进程状态（R、S、D、Z、T）以及如何使用 `ps` 命令解释它们。"
meta_keywords: "linux 进程状态，linux 中的进程状态，linux 进程状态，linux 中的进程状态，linux 进程状态详解，ps 命令，STAT 代码，进程管理"
---

Linux 任务在运行、等待、停止和退出的过程中，会在不同执行状态之间转换。`ps` 的 `STAT` 字段只记录某一瞬间，因此诊断行为时，反复观察通常比只看一个字母更有用。

```bash
$ ps -o pid,ppid,stat,wchan:24,cmd
```

`STAT` 的第一个字符表示主要状态，后续字符则是修饰符，用于描述会话首进程、前台进程组成员等属性。完整列表请查阅本机的 `ps` 手册。

## 运行与可中断睡眠

- `R` 表示正在运行或可运行。任务正在 CPU 上执行，或正在运行队列中等待 CPU 时间。
- `S` 表示可中断睡眠。任务正在等待某个事件，并可由适当的信号或事件唤醒。

睡眠是正常现象。交互式程序和服务的大部分时间都在等待输入、定时器、网络流量、锁或其他事件，而不是持续占用 CPU。

:::single-choice{#process-states-runnable-code}
主要状态 `R` 表示什么？

::option[正在 CPU 上运行或已准备好运行。]{#process-states-r-running .correct explanation="`R` 同时包括当前正在执行的任务和等待 CPU 调度的可运行任务。"}
::option[父进程已收集其状态，因此进程已被回收。]{#process-states-r-reaped explanation="被完全回收的进程不会再作为普通进程表条目出现。"}
::option[正在不可中断睡眠中等待。]{#process-states-r-uninterruptible explanation="不可中断睡眠由 `D` 表示。"}
:::

:::single-choice{#process-states-interruptible-code}
哪个主要状态表示可中断睡眠？

::option[`D`]{#process-states-sleep-d explanation="`D` 表示不可中断睡眠。"}
::option[`Z`]{#process-states-sleep-z explanation="`Z` 表示已经退出、但状态尚未被回收的子进程。"}
::option[`S`]{#process-states-sleep-s .correct explanation="`S` 是 `ps` 表示可中断等待的传统代码。"}
:::

## 不可中断睡眠

`D` 表示不可中断睡眠，常见于任务等待某项内核操作时，例如某些存储或网络文件系统 I/O。任务离开这种等待前不会响应普通信号；在此期间，信号可以保持待处理状态。

短暂处于 `D` 状态可能完全正常。长期或大量的 `D` 状态任务可能意味着 I/O 缓慢、不可用或发生故障，但仅凭这个状态无法确定原因。下结论前，应检查等待通道、内核日志、存储与网络健康状况以及相关子系统。

:::single-choice{#process-states-uninterruptible-code}
哪个主要状态表示不可中断睡眠？

::option[`T`]{#process-states-d-stopped explanation="`T` 表示已停止的任务。"}
::option[`D`]{#process-states-d-uninterruptible .correct explanation="`D` 用于表示正在内核中进行不可中断睡眠等待的任务。"}
::option[`R`]{#process-states-d-runnable explanation="`R` 表示正在执行或可运行的任务。"}
:::

## 停止与僵尸状态

- `T` 通常表示进程被 `SIGTSTP` 等作业控制操作或 `SIGSTOP` 停止。某些工具用小写 `t` 表示由跟踪造成的停止。
- `Z` 表示僵尸进程：进程已经退出，但父进程尚未收集其终止记录。

适当时，可用 `SIGCONT` 恢复因作业控制而停止的进程。僵尸进程已经不再执行，因此无法被恢复或杀死；必须由其父进程或接管它的回收进程收集状态。

:::single-choice{#process-states-zombie-code}
主要状态 `Z` 表示什么？

::option[已退出、终止记录正等待回收的进程。]{#process-states-z-zombie .correct explanation="执行结束后，僵尸进程仍保留最少量的、可供父进程读取的状态。"}
::option[被终端挂起信号暂停的进程。]{#process-states-z-terminal-stop explanation="作业控制造成的停止通常显示为 `T`。"}
::option[当前占满一个 CPU 核心的进程。]{#process-states-z-cpu explanation="正在活动运行的任务用 `R` 表示，而僵尸进程不执行任何指令。"}
:::

## 结合上下文解读状态

状态码是观察结果，而不是诊断结论。应结合运行时长、CPU 使用率、等待通道、父子关系、日志和多次采样进行分析。从内核报告状态到你看到屏幕内容之间，任务可能已经切换状态。

[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)实验提供了一个安全环境，可用于观察前台、睡眠、停止和已终止的任务。

## 总结

现在，你可以解读最常见的主要进程状态。

1. 将 `R` 理解为正在运行或可运行，将 `S` 理解为可中断睡眠。
2. 把持续的 `D` 状态作为等待症状调查，而不是直接当作诊断结论。
3. 区分已停止的 `T` 与已退出但未回收的 `Z`。
4. 使用重复观察和周边证据进行判断。
