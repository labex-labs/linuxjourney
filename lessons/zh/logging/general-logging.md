---
index: 3
lang: "zh"
title: "通用日志"
meta_title: "通用日志 - 日志"
meta_description: "了解 Linux 日志文件，如 /var/log/messages 和 syslog。了解它们之间的区别，以便有效进行系统故障排除。开始您的 Linux 之旅！"
meta_keywords: "Linux 日志，syslog, var/log/messages, Linux 故障排除，Linux 初学者，Linux 指南，系统日志"
---

## Lesson Content

您的系统上有很多日志文件可以查看；许多重要的日志文件都可以在 `/var/log` 下找到。我们不会一一介绍所有日志文件，但会讨论其中几个主要的日志文件。

您可以查看两个通用日志文件，以了解您的系统正在做什么：

### `/var/log/messages`

此日志包含所有非关键和非调试消息，包括启动期间（dmesg）、auth、cron、daemon 等记录的消息。它对于了解机器的运行情况非常有用。

### `/var/log/syslog`

此日志记录除 auth 消息之外的所有内容；它对于调试机器上的错误非常有用。

这两个日志在排除系统故障时应该绰绰有余。但是，如果您只想查看特定的日志组件，也有单独的日志文件。

## Exercise

熟能生巧！以下是一些动手实验，以加强您对查看和分析日志文件的理解：

1. **[Linux tail 命令：文件尾部显示](https://labex.io/zh/labs/linux-linux-tail-command-file-end-display-214303)** - 学习 Linux `tail` 命令，用于查看和监控文本文件的末尾，这对于日志分析至关重要。
2. **[Linux head 命令：文件开头显示](https://labex.io/zh/labs/linux-linux-head-command-file-beginning-display-214302)** - 探索 `head` 命令，用于显示文本文件的初始行，这对于快速检查日志头很有用。
3. **[快速威胁检测](https://labex.io/zh/labs/linux-rapid-threat-detection-387930)** - 练习基本的 Linux 命令行技能，用于网络安全分析，使用 `tail` 和 `head` 快速提取和分析最近的日志条目。

这些实验将帮助您在实际场景中应用日志文件查看的概念，并增强系统监控的信心。

## Quiz Question

哪个日志文件记录了除 auth 消息之外的所有内容？

## Quiz Answer

syslog
