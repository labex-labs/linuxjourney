---
lesson_id: "process-details"
course_id: "processes"
lang: "zh"
order_index: 3
title: "进程详情"
description: "学习哪些状态和资源把运行中的进程与存储在磁盘上的程序区分开来。"
meta_title: "进程详情 - 进程管理"
meta_description: "探索 Linux 进程详情的基础知识。本初学者指南解释了什么是进程，Linux 内核如何处理进程管理，以及如何分配 CPU 和内存等系统资源。"
meta_keywords: "Linux 进程，进程详情，内核，进程管理，系统资源，ps aux, CPU, 内存，Linux 教程，初学者指南"
---

程序是存储在文件中的可执行代码和数据。进程则是活动的执行上下文：它包含已映射代码、内存、凭据、打开的文件描述符、信号状态、调度信息和一个或多个线程。同一个程序可以有许多相互独立的进程实例。

## 程序实例和 PID

例如，在两个终端中不带操作数启动 `cat`。每个实例都会等待输入并拥有自己的进程 ID：

```bash
$ pgrep -a cat
18420 cat
18457 cat
```

两个进程执行同一个程序，但可以拥有不同的输入流、内存内容、凭据、工作目录和生命周期。PID 每次只标识一个活动进程，进程退出后可以重复使用。

:::single-choice{#process-details-program-versus-process} 同一程序的两个运行实例有什么区别？

::option[每个实例都必须复制一份可执行文件。]{#process-details-copied-executable explanation="多个进程可以映射和共享同一可执行文件的代码页，无需复制文件。"}
::option[只有一个实例能拥有内存或打开的文件。]{#process-details-one-instance-resources explanation="每个进程都可以拥有自己的内存映射和文件描述符表。"}
::option[每个实例都有自己的进程上下文和 PID。]{#process-details-independent-context .correct explanation="即使可执行代码来自同一文件，不同执行也会获得独立的活动进程状态。"}
:::

## 内核跟踪的状态

内核维护调度和控制每个进程所需的信息，包括：

- 进程和父进程标识符
- 用户和组凭据
- 虚拟内存映射
- 打开的文件描述符和当前目录
- 信号处置和待处理信号
- 调度策略、优先级和执行状态
- CPU 时间等计量数据

某些底层资源可以共享。相关进程可以共享映射内存，一个进程中的线程也共享地址空间和许多进程范围资源。因此，进程提供隔离边界，但并不表示每个字节或内核对象在物理上都私有。

:::single-choice{#process-details-kernel-state} 哪个组件维护 Linux 进程的调度和凭据状态？

::option[内核。]{#process-details-kernel .correct explanation="内核跟踪进程状态，并应用调度、内存、信号和访问控制规则。"}
::option[可执行文件所在目录。]{#process-details-directory explanation="目录存储名称到 inode 的映射，不会调度运行中的进程。"}
::option[只由用户的终端模拟器维护。]{#process-details-terminal explanation="终端可以与进程交互，但进程管理仍是内核职责。"}
:::

## CPU 调度和内存

可运行线程会争用 CPU 时间。内核调度器根据调度类别、优先级、CPU 亲和性、负载和策略，选择哪个线程在哪个 CPU 上运行。这并不保证每个进程获得相等份额。

每个进程通常看到一个虚拟地址空间。内核和硬件会把虚拟地址映射到物理内存或其他后备存储、实施保护，并在适当时共享页面。因此，`ps` 或 `top` 中的内存数值不一定是唯一归属于该进程的物理 RAM 量。

:::single-choice{#process-details-scheduler-role} Linux 调度器选择什么？

::option[哪个可运行线程在可用 CPU 上执行。]{#process-details-runnable-thread .correct explanation="调度策略会在可运行执行上下文中做选择并分配 CPU 时间。"}
::option[格式化磁盘时记录哪个文件所有者。]{#process-details-format-owner explanation="文件系统所有权与 CPU 调度无关。"}
::option[允许用户输入哪条命令行。]{#process-details-command-entry explanation="调度器管理执行时间，而不是交互式命令语法。"}
:::

## 进程退出和资源清理

进程退出时，内核会释放其大多数私有资源、关闭剩余描述符，并为父进程记录终止信息。父进程取回退出状态前，少量进程表记录可以作为僵尸进程保留。因此，“进程已经执行完毕”和“进程表中的所有痕迹都已消失”并不总是同时发生。

:::single-choice{#process-details-exit-status} 为什么已退出进程可能短暂地作为僵尸进程保留？

::option[它仍在分配完整内存的情况下执行指令。]{#process-details-zombie-running explanation="僵尸进程已经完成执行，不再保留正常的运行地址空间。"}
::option[父进程尚未收集记录的终止状态。]{#process-details-parent-wait .correct explanation="内核会保留最少量的退出信息，直到父进程执行 wait 操作。"}
::option[其可执行文件被内核永久锁定。]{#process-details-zombie-file-lock explanation="僵尸状态涉及父子退出计量，而不是永久的可执行文件锁。"}
:::

使用[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)实验启动多个实例并比较 PID 和状态。[Linux `top` 命令](https://labex.io/zh/labs/linux-linux-top-command-real-time-system-monitoring-388500)实验提供不断变化的调度和资源指标视图。

## 总结

现在，你可以把进程描述为不只是一个程序文件。

1. 区分存储的可执行代码和活动进程实例。
2. 识别内核跟踪的状态和资源。
3. 把调度与可运行线程联系起来，而不是相等份额。
4. 认识到退出状态会保留到父进程收集它为止。
