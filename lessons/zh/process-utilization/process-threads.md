---
lesson_id: "process-threads"
course_id: "process-utilization"
lang: "zh"
order_index: 3
title: "进程线程"
description: "了解 Linux 线程如何共享进程资源，以及如何使用 ps 检查线程。"
meta_title: "进程线程 - 进程资源利用"
meta_description: "Linux 进程线程指南。了解单线程和多线程进程的区别，以及如何使用 ps 命令显示线程。"
meta_keywords: "Linux 线程，进程线程，ps 显示线程，ps m, 多线程，单线程，轻量级进程，Linux 进程管理"
---

线程是在进程中受到调度的一条执行流。每个运行中的进程至少包含一个线程，而多线程进程则包含多条可以并发推进的执行流。

## 进程与线程

同一进程中的线程共享虚拟地址空间和打开的文件描述符等资源。每个线程仍拥有自己的执行状态，包括寄存器和栈。共享让通信更高效，但也意味着一个线程未同步的修改可能影响其他线程。

不同进程通常拥有各自独立的地址空间，并通过明确的进程间通信机制交换数据。这两种设计都不会天然更快或更安全；取舍取决于工作负载和实现方式。

:::single-choice{#threads-shared-resource} 同一进程中的线程通常共享哪项资源？

::option[进程的虚拟地址空间。]{#threads-shared-address-space .correct explanation="线程可以访问同一进程内存，但程序必须进行适当同步。"}
::option[每个线程各自独立的一套内核。]{#threads-separate-kernel explanation="所有线程都使用当前正在运行的系统内核。"}
::option[每个线程各自不同的文件系统根目录。]{#threads-different-root explanation="线程通常共享进程的文件系统上下文，而不会获得独立根目录。"}
:::

## 线程标识符

Linux 把每个线程表示为拥有自己线程 ID 的可调度任务。线程组首进程的 ID 通常显示为进程 ID，而所有成员共享一个线程组 ID。不同工具会使用 `PID`、`TID`、`LWP` 和 `SPID` 等标签；应检查工具的字段定义，不要假定所有标签含义相同。

:::single-choice{#threads-own-scheduling-state} 每个线程独立维护什么？

::option[进程完整的打开文件表。]{#threads-open-files-shared explanation="同一进程中的线程通常共享打开的文件描述符。"}
::option[机器的系统级用户数据库。]{#threads-user-database explanation="账户数据库并不是线程私有状态。"}
::option[自身的执行状态和栈。]{#threads-stack-state .correct explanation="即使共享进程资源，线程仍需要自己的执行上下文。"}
:::

## 使用 ps 列出线程

使用明确的输出字段，可以避免含义模糊的默认布局：

```bash
$ ps -eLo pid,tid,psr,stat,comm
```

在 procps `ps` 中，`-L` 显示线程，`-e` 选择所有进程。`pid` 标识线程组，`tid` 标识单个线程，`psr` 显示线程上次运行所在的 CPU，`stat` 报告状态。若只检查一个进程，可以使用：

```bash
$ ps -L -p 1234 -o pid,tid,stat,pcpu,comm
```

线程列表只是快照。线程可能在下一刻退出或改变状态。

:::single-choice{#threads-ps-one-process} 哪个命令会使用明确字段列出 PID 1234 所属的线程？

::option[`ps -p 1234 -o pid,ppid,stat,pcpu,comm`]{#threads-process-only explanation="该输出并未请求逐线程显示。"}
::option[`ps -L -p 1234 -o pid,tid,stat,pcpu,comm`]{#threads-ps-l .correct explanation="`-L` 选项会为选中的进程请求线程记录。"}
::option[`ps -e -o pid,user,stat,pcpu,comm`]{#threads-all-processes explanation="该命令选择系统中的进程，但不显示线程 ID。"}
:::

## 解读线程活动

单个线程的高 CPU 使用率可能被进程级平均值掩盖。应把线程级 CPU 样本与应用日志、栈跟踪和性能剖析工具结合起来。不了解暂停、权限和服务影响时，不要对生产任务附加调试器或发送信号。

:::single-choice{#threads-snapshot-limit} 为什么不应把 `ps` 线程列表视为永久状态？

::option[`ps` 会为显示的每一行创建替代线程。]{#threads-ps-creates explanation="该命令只是观察任务，不会克隆列出的线程。"}
::option[所有 Linux 主机上的线程 ID 都完全相同。]{#threads-identical-ids explanation="标识符在运行中的系统内分配，并不具有全局通用性。"}
::option[快照生成后，线程可能改变状态或退出。]{#threads-change-after-snapshot .correct explanation="进程检查只能观察持续变化系统中的某个瞬间。"}
:::

## 总结

现在，你可以区分进程资源与每个线程独有的执行状态。

1. 认识到每个进程至少包含一个线程。
2. 识别同一进程中线程共享的资源。
3. 使用 `ps -L` 明确列出进程 ID 和线程 ID。
4. 将线程输出视为快照，并与其他证据相互印证。
