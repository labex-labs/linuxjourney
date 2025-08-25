---
index: 1
lang: "zh"
title: "系统日志记录"
meta_title: "系统日志记录 - 日志记录"
meta_description: "了解 Linux 系统日志记录、syslog 以及如何在 /var/log 中查看日志文件。通过此初学者指南了解 rsyslogd 并监控系统事件。"
meta_keywords: "Linux 日志记录，syslog, rsyslogd, var log, 系统日志，Linux 教程，初学者指南"
---

## Lesson Content

系统上的服务、内核、守护进程等都在不断地运行。这些数据实际上以日志的形式保存到您的系统中。这使我们能够拥有一个人可读的系统事件日志。这些数据通常保存在 `/var` 目录中；`/var` 目录是我们保存可变数据（例如日志）的地方！

这些消息是如何被您的系统接收的呢？有一个名为 syslog 的服务将这些信息发送到系统日志记录器。

syslog 实际上包含许多组件。其中一个重要的组件是运行中的守护进程 `syslogd`（较新的 Linux 发行版使用 `rsyslogd`），它等待事件消息发生并过滤它想要了解的消息。根据它应该如何处理该消息，它会将其发送到文件、您的控制台，或者不进行任何处理。

您可能会认为这个系统日志记录器是管理日志的集中位置，但不幸的是，它不是。您会看到许多应用程序编写自己的日志记录规则并生成不同的日志文件。但是，通常，日志的格式应包括时间戳和事件详细信息。

以下是 syslog 中的一行示例：

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

在这里我们可以看到，在 1 月 27 日 07:41:32，我们的 cron 服务运行了 `cron.weekly` 作业。您可以在 `/var/log/syslog` 文件中查看 syslog 收集的所有事件消息。

## Exercise

熟能生巧！以下是一些动手实验，以加深您对 Linux 日志和文件查看的理解：

1. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 学习基本的 Linux 命令行技能，以高效地查看和导航文本文件，包括系统日志和配置文件。练习使用 `cat`、`more` 和 `less` 等命令从各种文件类型中提取关键信息。
2. **[Linux tail 命令：文件末尾显示](https://labex.io/zh/labs/linux-linux-tail-command-file-end-display-214303)** - 学习 Linux `tail` 命令，用于查看和监视文本文件的末尾。这对于实时日志分析特别有用。
3. **[在 Linux 中使用 grep 搜索文本](https://labex.io/zh/labs/comptia-search-text-with-grep-in-linux-590841)** - 在此实验中，您将学习如何使用 `grep` 命令在 Linux 系统上的文件中搜索文本。这对于在大型日志文件中查找特定条目非常宝贵。

这些实验将帮助您在实际场景中应用日志文件管理和分析的概念，并增强您对 Linux 系统监控的信心。

## Quiz Question

在较新的 Linux 系统上管理日志的守护进程是什么？

## Quiz Answer

rsyslogd
