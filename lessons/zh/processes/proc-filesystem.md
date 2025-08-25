---
index: 10
lang: "zh"
title: "/proc 文件系统"
meta_title: "/proc 文件系统 - 进程"
meta_description: "了解 Linux 中的 /proc 文件系统，它如何存储进程信息及其结构。通过这份重要的 Linux 指南探索进程详细信息。"
meta_keywords: "/proc 文件系统，Linux 进程，进程信息，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

请记住，在 Linux 中，一切皆文件，甚至进程也是。进程信息存储在一个特殊的 文件系统 中，称为 `/proc` 文件系统。

```bash
ls /proc
```

您应该会在这里看到多个值；每个 PID 都有子目录。如果您在 `ps` 输出中查看了某个 PID，您将能够在 `/proc` 目录中找到它。

继续，进入其中一个进程并查看该文件：

```bash
cat /proc/12345/status
```

您应该会看到进程状态信息以及更详细的信息。`/proc` 目录是内核查看系统的方式，因此这里的信息比您在 `ps` 中看到的要多得多。

## Exercise

熟能生巧！以下是一些动手实验，旨在加深您对 Linux 进程和系统监控的理解：

1. **[管理和监控 Linux 进程](https://labex.io/zh/labs/comptia-manage-and-monitor-linux-processes-590864)** - 在此实验中，您将学习在 Linux 系统上管理和监控进程的基本技能。您将探索如何与前台和后台进程交互，使用 `ps` 检查它们，使用 `top` 监控资源，使用 `renice` 调整优先级，以及使用 `kill` 终止它们。

这些实验将帮助您在实际场景中应用概念，并增强您在进程管理和系统观察方面的信心。

## Quiz Question

哪个文件系统存储进程信息？

## Quiz Answer

/proc
