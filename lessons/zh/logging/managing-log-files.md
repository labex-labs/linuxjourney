---
title: "管理日志文件"
description: "学习如何使用 logrotate 有效管理 Linux 日志文件。了解日志轮换、压缩和配置以节省磁盘空间。立即开始学习！"
keywords: "logrotate, Linux 日志，日志管理，日志轮换，Linux 教程，初学者，指南，磁盘空间"
---

## Lesson Content

日志文件生成大量数据并将其存储在硬盘上。然而，这带来了许多问题。大多数情况下，我们只想查看最新的日志。我们还希望有效地管理磁盘空间。那么，我们如何做到这一切呢？答案是使用 `logrotate`。

`logrotate` 工具为我们执行日志管理。它有一个配置文件，允许我们指定要保留多少日志以及哪些日志，如何压缩日志以节省空间等等。`logrotate` 工具通常每天通过 cron 运行一次，配置文件可以在 `/etc/logrotate.d` 中找到。

您可以使用其他日志轮换工具来管理日志，但 `logrotate` 是最常见的。

## Exercise

查看您的 `logrotate` 配置文件，了解它是如何管理某些日志的。

## Quiz Question

什么工具用于管理日志？

## Quiz Answer

logrotate
