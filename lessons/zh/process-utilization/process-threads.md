---
index: 3
lang: "zh"
title: "进程线程"
meta_title: "进程线程 - 进程利用"
meta_description: "了解 Linux 进程线程、单线程与多线程概念，以及如何使用 'ps m' 查看它们。高效理解轻量级进程！"
meta_keywords: "Linux 线程，进程线程，ps m 命令，多线程，单线程，Linux 进程，Linux 初学者，Linux 教程"
---

## Lesson Content

您可能听说过单线程和多线程进程这两个术语。线程与进程非常相似，它们都用于执行相同的程序；它们通常被称为轻量级进程。如果一个进程有一个线程，它是单线程的；如果一个进程有多个线程，它是多线程的。然而，所有进程至少有一个线程。

进程使用自己独立的系统资源运行；然而，线程可以轻松地共享这些资源，使它们之间的通信更加容易。有时，多线程应用程序比多进程应用程序更高效。

基本上，假设您打开 LibreOffice Writer 和 Chrome；每个都是独立的进程。现在您进入 Writer 并开始编辑文本。当您编辑文本时，它会自动保存。保存和编辑这两个并行的“轻量级进程”就是线程。

要查看进程线程，您可以使用：

```plaintext
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
```

进程由每个 PID 表示，进程下方是它们的线程（由 `--` 表示）。因此，您可以看到上面的进程都是单线程的。

## Exercise

熟能生巧！这里有一些动手实验，可以加深您对 Linux 进程及其管理的理解：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 在此实验中，您将学习在 Linux 系统上管理和监控进程的基本技能。您将探索如何与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，使用 `renice` 调整优先级，以及使用 `kill` 终止它们。

此实验将帮助您在实际场景中应用进程管理的概念，并增强监控系统活动的信心。

## Quiz Question

判断题，所有进程都以单线程启动。

## Quiz Answer

True
