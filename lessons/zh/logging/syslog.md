---
index: 2
lang: "zh"
title: "syslog"
meta_title: "syslog - 日志记录"
meta_description: "了解 Linux 中的 syslog 和 rsyslog，如何管理系统日志，以及使用 logger 命令。通过这个适合初学者的教程开始学习！"
meta_keywords: "syslog, rsyslog, Linux 日志，logger 命令，/var/log/syslog, Linux 教程，Linux 初学者，系统日志"
---

## Lesson Content

syslog 服务管理并将日志发送到系统日志记录器。Rsyslog 是 syslog 的高级版本；大多数 Linux 发行版都应该使用这个新版本。syslog 服务收集的所有日志的输出都可以在 `/var/log/syslog` 中找到（除了身份验证消息之外的所有消息）。

要了解我们的系统日志记录器维护了哪些文件，请查看 `/etc/rsyslog.d` 中的配置文件：

```plaintext
pete@icebox:~$ less /etc/rsyslog.d/50-default.conf
# First some standard log files.  Log by facility.
#
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog
#cron.*                         /var/log/cron.log
#daemon.*                       -/var/log/daemon.log
kern.*                          -/var/log/kern.log
#lpr.*                          -/var/log/lpr.log
mail.*                          -/var/log/mail.log
#user.*                         -/var/log/user.log
```

这些日志文件的规则由左栏的选择器和右栏的操作表示。操作告诉我们将日志信息发送到哪里：文件、控制台等。请记住，并非所有应用程序和服务都使用 rsyslog 来管理它们的日志，因此如果您想具体了解记录了什么，则必须查看此目录。

让我们实际看看日志记录的运行情况；您可以使用 `logger` 命令手动发送日志：

```bash
logger -s Hello
```

现在查看您的 `/var/log/syslog`，您应该会在日志中看到此条目！

## Exercise

熟能生巧！以下是一些动手实验，可帮助您加深对 Linux 日志记录和文件查看的理解：

1. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 练习基本的 Linux 命令行技能，以高效地查看和导航文本文件，包括系统日志和配置文件。
2. **[Linux tail 命令：文件末尾显示](https://labex.io/zh/labs/linux-linux-tail-command-file-end-display-214303)** - 学习 Linux `tail` 命令，用于查看和监控文本文件的末尾，这对于实时日志分析特别有用。
3. **[使用 grep 在 Linux 中搜索文本](https://labex.io/zh/labs/comptia-search-text-with-grep-in-linux-590841)** - 学习在文件中搜索特定的文本模式，这是筛选日志条目以查找关键信息的宝贵技能。

这些实验将帮助您在实际场景中应用日志管理和文件检查的概念，并增强您对 Linux 系统管理的信心。

## Quiz Question

您可以使用哪个命令手动记录消息？

## Quiz Answer

logger
