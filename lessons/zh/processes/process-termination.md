---
lesson_id: "process-termination"
course_id: "processes"
lang: "zh"
order_index: 5
title: "进程终止"
description: "学习退出状态、等待、僵尸进程和重新指定父进程如何完成 Linux 进程生命周期。"
meta_title: "进程终止 - 进程管理"
meta_description: "探索 Linux 进程终止、wait 系统调用，以及僵尸进程与孤儿进程争论中的关键区别。了解如何管理 Linux 杀死子进程状态以确保系统稳定。"
meta_keywords: "Linux 进程终止，僵尸进程，孤儿进程，僵尸进程与孤儿进程，linux 杀死子进程，wait 系统调用，_exit, 进程管理"
---

进程可以通过从 main 函数返回、调用退出接口，或被信号终止而结束。内核会释放其大多数资源，但父子进程计量会继续，直到父进程收集终止信息。

## 退出状态

正常退出的程序会提供一个整数状态。按惯例，状态 `0` 表示成功，非零值表示某种失败或其他结果。非零值的确切含义属于程序接口。

在 shell 中，可以这样检查最近一个前台管道的状态：

```bash
$ command
$ printf '%s\n' "$?"
```

Shell 只公开范围有限的编码状态，也会表示信号终止，因此该值不是完整的诊断记录。程序应记录自己的退出代码。

:::single-choice{#process-termination-success-status}
按照 Unix 惯例，哪个正常退出状态表示成功？

::option[`1`]{#process-termination-status-one explanation="许多程序使用 `1` 表示一般失败，但含义取决于具体命令。"}
::option[`0`]{#process-termination-status-zero .correct explanation="正常状态零通常表示成功完成。"}
::option[`255`]{#process-termination-status-255 explanation="这是非零值，通常不表示成功。"}
:::

## 等待和回收

内核会记录子进程如何终止，并通知其父进程。父进程使用 `wait()` 系统调用族中的成员取回该信息。收集这条记录称为回收。

等待也可以协调执行：shell 会等待前台命令完成后再显示提示符，而对于后台作业则可以推迟等待。设计良好的长期运行父进程必须安排回收子进程，同时不阻塞无关工作。

:::single-choice{#process-termination-wait-purpose}
成功的 wait 操作让父进程取回什么？

::option[子进程的终止信息。]{#process-termination-wait-status .correct explanation="wait 调用族会报告子进程如何停止或终止，并回收已完成的子进程。"}
::option[子进程原地址空间的副本。]{#process-termination-wait-memory explanation="大多数进程内存已经释放，不会由 `wait()` 返回给父进程。"}
::option[子进程打开的每个文件的所有权。]{#process-termination-wait-files explanation="等待不会转移文件系统所有权元数据。"}
:::

## 僵尸进程

子进程退出后、终止记录被回收前，它会显示为僵尸进程，在 `ps` 中通常是状态 `Z`。它不再执行，也不保留普通地址空间，但最小的进程表条目和计量信息仍然存在。

向僵尸进程发送信号不能让它再次退出。如果僵尸持续积累，应诊断未执行 wait 的父进程，通过适当运维流程重启或修正该父进程，或让僵尸重新指定给会回收它的进程。大量僵尸可能耗尽 PID 或进程表容量。

:::single-choice{#process-termination-zombie-definition}
哪个描述符合僵尸进程？

::option[父进程已经退出的运行中子进程。]{#process-termination-zombie-orphan explanation="这描述的是孤儿子进程，而不是僵尸状态。"}
::option[已经完成但终止记录尚未回收的子进程。]{#process-termination-zombie-unreaped .correct explanation="该进程已经停止执行，但内核会为其父进程保留最少量的状态。"}
::option[在不可中断循环中消耗 CPU 的进程。]{#process-termination-zombie-cpu explanation="僵尸进程不会执行指令或消耗 CPU 时间。"}
:::

## 孤儿进程和重新指定父进程

父进程退出而子进程仍在运行时，内核会把该子进程重新指定给适当的 subreaper，或相关 PID 命名空间中的 init 进程。子进程可能正在运行、休眠、停止，或之后成为僵尸；“孤儿”描述的是失去原父进程关系，而不是某种执行状态。

收养进程会负责收集终止状态。现代服务管理器和容器环境意味着不能假设新父进程始终是主机的 PID 1。

:::single-choice{#process-termination-orphan-definition}
进程比原父进程存活得更久时会发生什么？

::option[它会重新指定给适当的 subreaper 或命名空间 init 进程。]{#process-termination-orphan-reparented .correct explanation="内核会分配一个收养进程，以保持有效的父进程关系。"}
::option[即使尚未退出，也会立即成为僵尸。]{#process-termination-orphan-zombie explanation="只有执行结束且状态等待收集时，才会进入僵尸状态。"}
::option[它会永久失去 PID 并匿名继续运行。]{#process-termination-orphan-no-pid explanation="活动的孤儿进程会保留进程身份，只改变父进程关系。"}
:::

使用[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)实验观察退出代码和进程状态，而不干扰生产工作负载。

## 总结

现在，你可以区分执行结束与父进程侧清理。

1. 把零解释为惯例上的成功，并按程序文档解释非零状态。
2. 使用等待收集子进程的终止信息。
3. 把僵尸进程识别为已退出但尚未回收。
4. 把孤儿进程识别为原父进程退出后被重新指定父进程的子进程。
