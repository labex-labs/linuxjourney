---
lang: "zh"
title: "信号"
meta_title: "信号 - 进程"
meta_description: "了解 Linux 信号、它们的用途、常见的类型如 SIGINT 和 SIGKILL，以及进程如何处理它们。理解信号基础知识以更好地控制 Linux。"
meta_keywords: "Linux 信号，SIGKILL, SIGINT, 进程通信，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

信号是通知进程发生了某些事情。

### 为什么会有信号

它们是软件中断，有许多用途：

- 用户可以输入特殊的终端字符（Ctrl-C）或（Ctrl-Z）来终止、中断或暂停进程。
- 可能会发生硬件问题，内核希望通知进程。
- 可能会发生软件问题，内核希望通知进程。
- 它们基本上是进程之间通信的方式。

### 信号处理过程

当某个事件生成信号时，它会被传递给一个进程；在它被传递之前，它被认为是处于挂起状态。当进程运行时，信号将被传递。但是，进程有信号掩码，如果指定，它们可以设置信号传递为被阻塞。当信号被传递时，进程可以执行多种操作：

- 忽略信号。
- “捕获”信号并执行特定的处理程序例程。
- 进程可以被终止，而不是正常的 exit 系统调用。
- 阻塞信号，取决于信号掩码。

### 常见信号

每个信号都由整数定义，并带有符号名称，形式为 SIGxxx。一些最常见的信号是：

- SIGHUP or HUP or 1: Hangup
- SIGINT or INT or 2: Interrupt
- SIGKILL or KILL or 9: Kill
- SIGSEGV or SEGV or 11: Segmentation fault
- SIGTERM or TERM or 15: Software termination
- SIGSTOP or STOP: Stop

信号的数字可能不同，因此通常通过它们的名称来引用它们。

有些信号是不可阻塞的；一个例子是 SIGKILL 信号。KILL 信号会销毁进程。

## Exercise

No exercises for this lesson.

## Quiz Question

什么信号是不可阻塞的？

## Quiz Answer

SIGKILL
