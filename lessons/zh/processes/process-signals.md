---
index: 6
lang: "zh"
title: "信号"
meta_title: "信号 - 进程"
meta_description: "了解 Linux 信号、其用途、常见的类型如 SIGINT 和 SIGKILL，以及进程如何处理它们。理解信号基础知识以更好地控制 Linux。"
meta_keywords: "Linux 信号，SIGKILL, SIGINT, 进程通信，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

信号是向进程发出的通知，表明发生了某些事情。

### 为什么会有信号

它们是软件中断，有许多用途：

- 用户可以输入特殊的终端字符 (Ctrl-C) 或 (Ctrl-Z) 来终止、中断或暂停进程。
- 可能发生硬件问题，内核希望通知进程。
- 可能发生软件问题，内核希望通知进程。
- 它们基本上是进程之间通信的方式。

### 信号处理

当某个事件生成信号时，它会被传递给一个进程；在它被传递之前，它被认为是处于挂起状态。当进程运行时，信号将被传递。然而，进程有信号掩码，如果指定，它们可以设置信号传递为阻塞。当信号被传递时，进程可以做很多事情：

- 忽略信号。
- “捕获”信号并执行特定的处理程序例程。
- 进程可以被终止，而不是正常的 exit 系统调用。
- 根据信号掩码阻塞信号。

### 常见信号

每个信号都由整数定义，并带有 SIGxxx 形式的符号名称。一些最常见的信号是：

- SIGHUP 或 HUP 或 1: Hangup
- SIGINT 或 INT 或 2: Interrupt
- SIGKILL 或 KILL 或 9: Kill
- SIGSEGV 或 SEGV 或 11: Segmentation fault
- SIGTERM 或 TERM 或 15: Software termination
- SIGSTOP 或 STOP: Stop

信号的数字可能不同，因此通常通过它们的名称来引用它们。

有些信号是不可阻塞的；一个例子是 SIGKILL 信号。KILL 信号会销毁进程。

## Exercise

熟能生巧！这是一个动手实验，旨在加深您对进程以及如何使用信号与它们交互的理解：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 在此实验中，您将学习在 Linux 系统上管理和监控进程的基本技能。您将探索如何与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，使用 `renice` 调整优先级，以及使用 `kill` 终止它们。使用 `kill` 终止进程是发送信号的直接应用。

此实验将帮助您在实际场景中应用进程管理和信号底层使用的概念，并增强您对 Linux 系统管理的信心。

## Quiz Question

什么信号是不可阻塞的？

## Quiz Answer

SIGKILL
