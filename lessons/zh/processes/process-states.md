---
index: 9
lang: "zh"
title: "进程状态"
meta_title: "进程状态 - 进程"
meta_description: "使用 `ps aux` 学习 Linux 进程状态 (R, S, D, Z, T)。了解常见的 STAT 代码并有效管理进程。开始您的 Linux 之旅！"
meta_keywords: "Linux 进程状态，ps aux, 进程管理，Linux 教程，Linux 初学者，STAT 代码，Linux 指南"
---

## Lesson Content

让我们再次查看 `ps aux` 命令：

```bash
ps aux
```

在 STAT 列中，您会看到许多值。Linux 进程可以处于多种不同的状态。您将看到的最常见的状态代码如下所述：

- **R**: 运行中或可运行；它只是等待 CPU 处理它。
- **S**: 可中断睡眠；等待事件完成，例如来自终端的输入。
- **D**: 不可中断睡眠；无法被信号杀死或中断的进程。通常，要使它们消失，您必须重新启动或解决问题。
- **Z**: 僵尸；我们在之前的课程中讨论过，僵尸是已终止的进程，正在等待收集它们的状态。
- **T**: 已停止；已暂停/停止的进程。

## Exercise

查看您系统上正在运行的进程，并检查它们的进程状态。

## Quiz Question

哪个 STAT 代码用于表示不可中断睡眠？

## Quiz Answer

D
