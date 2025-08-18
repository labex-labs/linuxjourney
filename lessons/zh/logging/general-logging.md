---
lang: "zh"
title: "通用日志记录"
meta_title: "通用日志记录 - 日志"
meta_description: "了解 Linux 日志文件，如 /var/log/messages 和 syslog。理解它们之间的区别，以便有效地进行系统故障排除。开始您的 Linux 之旅！"
meta_keywords: "Linux 日志，syslog, var/log/messages, Linux 故障排除，Linux 初学者，Linux 指南，系统日志"
---

## Lesson Content

您的系统上有很多日志文件可以查看；许多重要的日志文件都可以在 `/var/log` 下找到。我们不会一一介绍它们，但我们会讨论其中几个主要的。

您可以查看两个通用日志文件，以了解您的系统正在做什么：

### `/var/log/messages`

此日志包含所有非关键和非调试消息，包括启动期间（dmesg）、auth、cron、daemon 等记录的消息。它对于了解您的机器运行情况非常有用。

### `/var/log/syslog`

此日志记录除 auth 消息之外的所有内容；它对于调试机器上的错误非常有用。

当您排除系统故障时，这两个日志应该绰绰有余。但是，如果您只想查看特定的日志组件，那么也有单独的日志。

## Exercise

查看您的 `/var/log/messages` 和 `/var/log/syslog` 文件，看看它们有什么区别。

## Quiz Question

哪个日志文件记录了除 auth 消息之外的所有内容？

## Quiz Answer

syslog
