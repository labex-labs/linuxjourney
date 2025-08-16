---
lang: "zh"
title: "/proc 文件系统"
description: "了解 Linux 中的 /proc 文件系统，它如何存储进程信息及其结构。通过这份重要的 Linux 指南探索进程详情。"
keywords: "/proc 文件系统，Linux 进程，进程信息，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

请记住，在 Linux 中，一切皆文件，甚至进程也是如此。进程信息存储在一个特殊的 文件系统 中，称为 `/proc` 文件系统。

```bash
ls /proc
```

您应该会在这里看到多个值；每个 PID 都有子目录。如果您在 `ps` 输出中查看了某个 PID，您将能够在 `/proc` 目录中找到它。

继续进入其中一个进程并查看该文件：

```bash
cat /proc/12345/status
```

您应该会看到进程状态信息以及更详细的信息。`/proc` 目录是内核查看系统的方式，因此这里的信息比您在 `ps` 中看到的信息要多得多。

## Exercise

本课程没有练习。

## Quiz Question

哪个文件系统存储进程信息？

## Quiz Answer

/proc
