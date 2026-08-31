---
lesson_id: "process-signals"
course_id: "processes"
lang: "zh"
order_index: 6
title: "信号"
description: "学习 Linux 如何生成、阻塞、传递和处理信号，以控制进程并通知事件。"
meta_title: "信号 - 进程"
meta_description: "探索 Linux 信号的基础知识，这是进程管理的关键机制。了解 Linux 进程信号，如 SIGTERM（信号 15 Linux）和 SIGKILL 的工作原理，并理解它们的操作系统信号代码。"
meta_keywords: "linux 信号，linux 进程信号，信号 15 linux, os 信号代码，SIGKILL, SIGTERM, SIGINT, 进程管理，linux 教程"
---

信号是传递给进程或特定线程的异步通知。信号用于报告事件和请求操作，但与面向数据的进程间通信机制相比，只能携带有限信息。

## 信号的来源

信号可以来自多个地方：

- 终端可以为 `Ctrl-C` 生成 `SIGINT`，为 `Ctrl-Z` 生成 `SIGTSTP`，并发送给前台进程组。
- 线程进行无效内存引用时，内核可以生成 `SIGSEGV` 等同步信号。
- 进程可以向另一个进程或进程组发送获准信号。
- 定时器、子进程状态变化和终端挂断可以生成其他信号。

发送者必须拥有适当权限，通常由凭据或 capabilities 决定。因此，信号是由内核中介的控制接口，而不是任意用户之间不受限制的消息。

:::single-choice{#process-signals-ctrl-c}
终端通常会为 `Ctrl-C` 生成哪个信号？

::option[`SIGTSTP`]{#process-signals-ctrl-c-tstp explanation="`SIGTSTP` 通常与 `Ctrl-Z` 等终端暂停字符相关。"}
::option[`SIGCONT`]{#process-signals-ctrl-c-cont explanation="`SIGCONT` 会恢复已停止进程，而不是表示键盘中断。"}
::option[`SIGINT`]{#process-signals-ctrl-c-int .correct explanation="终端中断字符通常会为前台进程组生成 `SIGINT`。"}
:::

## 处置方式和默认操作

大多数信号都有进程范围的处置方式，从三种响应中选择一种：

- 执行该信号定义的默认操作
- 忽略信号
- 调用用户安装的处理程序

默认操作各不相同：信号可以终止、终止并创建 core dump、停止、继续，也可以被忽略。捕获 `SIGTERM` 可以让程序开始有序关闭，但处理程序必须遵循严格的异步信号安全规则，程序也仍可能延迟或拒绝退出。

信号名称比数字更易移植和阅读。虽然常见 Linux 架构使用 15 表示 `SIGTERM`，但除相关标准保证的数字外，不要假设所有信号编号在各处都相同。使用 `kill -l` 检查本地映射。

:::single-choice{#process-signals-term-behavior}
为什么进程可以优雅地响应 `SIGTERM`？

::option[它可以为该信号安装处理程序。]{#process-signals-term-handler .correct explanation="与 `SIGKILL` 不同，`SIGTERM` 可以被捕获，让程序启动自己的关闭逻辑。"}
::option[内核始终自动保存每个打开的文档。]{#process-signals-term-kernel-save explanation="应用程序清理取决于程序代码；内核无法理解并保存任意文档状态。"}
::option[`SIGTERM` 默认不能导致终止。]{#process-signals-term-no-default explanation="进程未改变处置方式时，其默认操作就是终止。"}
:::

## 被阻塞和待处理的信号

线程拥有信号掩码，可以暂时阻塞选定信号的传递。已经生成但被阻塞的信号会保持待处理状态，直到可以传递，但仍受标准信号和实时信号规则约束。同一类型的标准信号可能合并，而不是按每次出现逐个排队。

在多线程进程中，面向进程的信号可以传递给未阻塞它的适当线程；面向线程的信号则以指定线程为目标。因此，正确的信号设计不能只检查“进程是否阻塞了它”。

:::single-choice{#process-signals-blocked-state}
目标阻塞一个可阻塞信号时，生成该信号通常会发生什么？

::option[它会保持待处理，直到可以传递。]{#process-signals-pending .correct explanation="阻塞会推迟处理；解除阻塞后，待处理信号可以传递。"}
::option[它会自动转换为 `SIGKILL`。]{#process-signals-convert-kill explanation="内核不会把普通被阻塞信号升级为不可捕获信号。"}
::option[它会改变目标进程的用户 ID。]{#process-signals-change-uid explanation="信号掩码影响传递，不会改变进程凭据。"}
:::

## 无法处理的信号

`SIGKILL` 会终止进程，`SIGSTOP` 会停止进程。这两个信号都不能被捕获、忽略或阻塞。这保证内核保留最终控制权，但也意味着 `SIGKILL` 不会给应用层清理留下机会。

即使是 `SIGKILL`，从观察者角度看也可能不会让任务立即消失。任务可能正在等待不可中断的内核操作，终止后其父进程仍需回收状态。

:::single-choice{#process-signals-uncatchable-pair}
哪一对信号不能被捕获、忽略或阻塞？

::option[`SIGKILL` 和 `SIGSTOP`]{#process-signals-kill-stop .correct explanation="内核保留这两个信号，使进程无法覆盖或推迟其基本操作。"}
::option[`SIGINT` 和 `SIGTERM`]{#process-signals-int-term explanation="两者都可以安装用户处理程序，也可以被阻塞。"}
::option[`SIGHUP` 和 `SIGCONT`]{#process-signals-hup-cont explanation="这些信号具有特殊语义，但并非不可捕获的一对。"}
:::

## 总结

现在，你可以说明 Linux 信号处理的主要阶段和限制。

1. 识别由终端、内核和进程生成的信号。
2. 区分默认操作、忽略信号和处理程序。
3. 把阻塞与待处理传递及线程掩码联系起来。
4. 记住 `SIGKILL` 和 `SIGSTOP` 无法被处理或阻塞。
