---
lang: "zh"
title: "系统日志记录"
description: "了解 Linux 系统日志记录、syslog 以及如何查看 /var/log 中的日志文件。通过这份初学者指南了解 rsyslogd 并监控系统事件。"
keywords: "Linux 日志记录，syslog, rsyslogd, var log, 系统日志，Linux 教程，初学者指南"
---

## Lesson Content

您系统上的服务、内核、守护进程等都在不断地运行。这些数据实际上以日志的形式发送并保存在您的系统上。这使我们能够拥有一个人可读的、关于系统上正在发生的事件的日志。这些数据通常保存在 `/var` 目录中；`/var` 目录是我们保存变量数据的地方，例如日志！

这些消息是如何被您的系统接收的呢？有一个名为 syslog 的服务将这些信息发送到系统日志记录器。

syslog 实际上包含许多组件。其中一个重要的组件是一个名为 `syslogd` 的守护进程（较新的 Linux 发行版使用 `rsyslogd`），它等待事件消息的发生并过滤它想要了解的消息。根据它应该如何处理该消息，它会将其发送到文件、您的控制台，或者不进行任何处理。

您可能会认为这个系统日志记录器是管理日志的集中位置，但不幸的是，它并非如此。您会看到许多应用程序编写自己的日志记录规则并生成不同的日志文件。然而，通常情况下，日志的格式应包含时间戳和事件详细信息。

以下是 syslog 中的一行示例：

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

在这里我们可以看到，在 1 月 27 日 07:41:32，我们的 cron 服务运行了 `cron.weekly` 作业。您可以在 `/var/log/syslog` 文件中查看 syslog 收集的所有事件消息。

## Exercise

查看您的 `/var/log/syslog` 文件，看看您的机器上还在发生什么。

## Quiz Question

在较新的 Linux 系统上管理日志的守护进程是什么？

## Quiz Answer

rsyslogd
