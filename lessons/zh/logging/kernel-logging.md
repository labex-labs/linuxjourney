---
lang: "zh"
title: "内核日志记录"
meta_description: "了解 Linux 内核日志记录，包括 dmesg 和 kern.log。理解启动消息和硬件问题。探索内核日志以获取系统洞察。"
meta_keywords: "dmesg, kern.log, Linux 日志记录，内核消息，启动日志，Linux 教程，初学者指南"
---

## Lesson Content

### /var/log/dmesg

在启动时，您的系统会记录有关内核环形缓冲区的信息。这向我们展示了硬件驱动程序、内核信息以及启动期间的状态等信息。此日志文件位于 `/var/log/dmesg`，并在每次启动时重置。您现在可能看不到它的任何用处，但如果您在启动期间遇到问题或硬件问题，`dmesg` 是最佳查看位置。您还可以使用 `dmesg` 命令查看此日志。

### /var/log/kern.log

另一个可用于查看内核信息的日志是 `/var/log/kern.log` 文件。它记录您系统上的内核信息和事件；它还记录 `dmesg` 输出。

## Exercise

查看您的 `dmesg` 和 `kern` 日志。您发现了什么不同？

## Quiz Question

可以使用什么命令查看内核启动消息？

## Quiz Answer

dmesg
