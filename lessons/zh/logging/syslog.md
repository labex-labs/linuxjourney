---
lang: "zh"
title: "syslog"
meta_description: "了解 Linux 中的 syslog 和 rsyslog，如何管理系统日志以及使用 logger 命令。通过这个适合初学者的教程开始学习！"
meta_keywords: "syslog, rsyslog, Linux 日志，logger 命令，/var/log/syslog, Linux 教程，Linux 初学者，系统日志记录"
---

## Lesson Content

syslog 服务管理日志并将其发送到系统日志记录器。Rsyslog 是 syslog 的高级版本；大多数 Linux 发行版都应该使用这个新版本。syslog 服务收集的所有日志的输出都可以在 `/var/log/syslog` 中找到（除了身份验证消息之外的所有消息）。

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

这些日志文件的规则由左栏的选择器和右栏的操作表示。操作告诉我们将日志信息发送到哪里：文件、控制台等。请记住，并非所有应用程序和服务都使用 rsyslog 来管理其日志，因此如果您想具体了解记录了什么，则必须查看此目录。

让我们实际看看日志记录是如何工作的；您可以使用 `logger` 命令手动发送日志：

```bash
logger -s Hello
```

现在查看您的 `/var/log/syslog`，您应该会在日志中看到此条目！

## Exercise

查看您的 `/etc/rsyslog.d` 配置文件，看看还有什么通过系统日志记录器进行日志记录。

## Quiz Question

您可以使用哪个命令手动记录消息？

## Quiz Answer

logger
