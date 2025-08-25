---
index: 4
lang: "zh"
title: "内核日志记录"
meta_title: "内核日志记录 - 日志记录"
meta_description: "了解如何使用 dmesg 和 kern.log 进行 Linux 内核日志记录。理解启动消息和硬件问题。探索内核日志以获取系统洞察。"
meta_keywords: "dmesg, kern.log, Linux 日志记录，内核消息，启动日志，Linux 教程，初学者指南"
---

## Lesson Content

### /var/log/dmesg

在启动时，您的系统会记录有关内核环形缓冲区的信息。这向我们展示了硬件驱动程序、内核信息以及启动期间的状态等信息。此日志文件位于 `/var/log/dmesg`，并在每次启动时重置。您现在可能看不到它的任何用途，但如果您在启动期间遇到问题或硬件问题，`dmesg` 是最好的查看位置。您还可以使用 `dmesg` 命令查看此日志。

### /var/log/kern.log

另一个可用于查看内核信息的日志是 `/var/log/kern.log` 文件。它记录您系统上的内核信息和事件；它还记录 `dmesg` 输出。

## Exercise

熟能生巧！以下是一些动手实验，可帮助您加深对 Linux 用户和组管理的理解：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户帐户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新帐户到修改和删除它们。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 获得使用核心命令行实用程序进行组管理的实践经验，包括创建新组、修改用户成员资格和删除组。
3. **[在 Linux 中配置用户帐户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户帐户和 Sudo 权限的基本技术，以增强 Linux 系统的安全性，包括强制执行密码策略和授予管理权限。

这些实验将帮助您在实际场景中应用概念，并增强您在 Linux 中进行用户和组管理的信心。

## Quiz Question

可以使用哪个命令查看内核启动消息？

## Quiz Answer

dmesg
