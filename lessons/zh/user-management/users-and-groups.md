---
index: 1
lang: "zh"
title: "用户和组"
meta_title: "用户和组 - 用户管理"
meta_description: "Linux 基础知识的关键部分是理解用户和组的管理。本指南涵盖了 Linux 用户和组、root 超级用户以及使用 sudo 命令提升权限。这是最适合初学者的 Linux 教程课程之一。"
meta_keywords: "linux 用户和组，linux 基础，sudo, root 用户，UID, GID, 用户管理，最佳 linux 教程，最快学习 linux 高级知识"
---

## Lesson Content

在任何多用户操作系统中，管理用户和组是一个基本概念。这是 **linux 基础知识** 的核心部分，旨在实现访问控制和权限管理。当一个进程运行时，它以启动该进程的用户身份运行。同样，文件访问和所有权取决于权限，这可以防止一个用户访问另一个用户的私有文档。

### Linux 用户和组基础知识

Linux 系统中的每个用户都被分配了一个个人主目录，通常位于 `/home/username`。此目录用于存储其特定于用户的文件和配置，尽管确切路径在不同的 Linux 发行版之间可能有所不同。

系统使用用户 ID (UID) 来识别用户，使用组 ID (GID) 来识别组。虽然我们使用人类可读的用户名，但操作系统在所有与权限相关的任务中都依赖于这些唯一的数字 ID。组本质上是用户的集合，使得一次性管理多个帐户的权限变得更加容易。

### 超级用户和 Sudo 命令

在 **linux 用户和组** 的层级结构中，有一个用户凌驾于所有其他用户之上：`root`，也称为超级用户。`root` 用户拥有无限的权力，能够访问任何文件和管理任何进程。持续以 `root` 身份运行存在风险，因为一个简单的错误就可能损坏系统。

为了减轻这种风险，授权用户可以使用 `sudo`（superuser do）命令以 root 权限执行命令。这使得在不以 `root` 用户身份登录的情况下执行管理任务成为可能。对于任何希望掌握 `quickest way to linux advanced`（最快掌握 Linux 高级技能）的人来说，了解如何正确使用 `sudo` 至关重要。

让我们尝试查看一个受保护的文件，例如存储加密用户密码的 `/etc/shadow`。

```bash
cat /etc/shadow
```

您将收到一个“Permission denied”（权限被拒绝）错误。让我们检查一下文件的权限：

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

虽然我们稍后会详细介绍权限，但此输出显示只有 `root` 用户和 `shadow` 组的成员可以读取此文件。现在，使用 `sudo` 再次运行该命令：

```bash
sudo cat /etc/shadow
```

这次，系统会提示您输入密码，成功验证后，将显示文件内容。

## Exercise

虽然存在许多学习 linux 的应用程序，但动手实践至关重要。以下是一些用于巩固您对 Linux 用户、组和 `sudo` 理解的实验：

1. **[使用 useradd, usermod 和 userdel 管理 Linux 用户帐户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新帐户到修改和删除它们。
2. **[使用 groupadd, usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 获得使用核心命令行实用程序进行组管理的实践经验，包括创建新组、修改用户组成员身份和删除组。
3. **[在 Linux 中配置用户帐户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户帐户和 `sudo` 权限的基本技术，以增强 Linux 系统的安全性，包括授予管理权限。

这些实验将帮助您在实际场景中应用用户和组管理以及 `sudo` 使用的概念，并增强您对 Linux 系统管理的信心。

## Quiz Question

哪个命令允许您以 `root` 权限运行单个命令？ (请用英语回答，只使用小写字母)

## Quiz Answer

sudo
