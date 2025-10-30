---
index: 3
lang: "zh"
title: "/etc/passwd 文件"
meta_title: "/etc/passwd - 用户管理"
meta_description: "关于 Linux 中 /etc/passwd 文件的全面指南。了解如何解释用户数据字段、理解 UID，并查看 root:x:0:0:root:/root:/bin/bash 等示例。"
meta_keywords: "/etc/passwd, Linux 中的/etc/passwd, root:x:0:0:root:/root:/bin/bash, 用户 ID, UID, 用户管理，Linux 教程"
---

## Lesson Content

在 Linux 中，用户名是人类可读的标签，但系统使用唯一的**用户 ID (UID)** 来识别用户。用户名和 UID 之间的映射关系存储在 `/etc/passwd` 文件中，这是用户管理的关键组成部分。

要查看其内容，您可以使用一个简单的命令：

```bash
cat /etc/passwd
```

该文件会显示所有系统用户及其详细信息的列表。每一行代表一个用户账户。

### 解析 /etc/passwd 字段

该文件中典型的一行，通常是第一行，看起来像这样：

```plaintext
root:x:0:0:root:/root:/bin/bash
```

这个 `root` 用户的条目包含七个由冒号（`:`）分隔的字段。理解 Linux 中 `/etc/passwd` 的结构是管理用户的关键。让我们分解每个字段：

1.  **用户名**: 用户的登录名称（例如 `root`）。
2.  **密码**: 用户加密密码的占位符。出于安全原因，实际密码不会存储在这里。
    - `x` 表示加密密码存储在 `/etc/shadow` 文件中。
    - `*`（星号）表示账户被锁定，不能用于登录。
    - 空字段表示用户没有密码。
3.  **用户 ID (UID)**: 用户的唯一数字标识符。`root` 用户的 UID 始终为 `0`。
4.  **组 ID (GID)**: 用户主组的数字标识符。
5.  **GECOS 字段**: 一个注释字段，传统上用于保存额外信息，如用户的全名、电话号码或办公室位置。它由逗号分隔。
6.  **主目录**: 用户主目录的绝对路径（例如 `/root`）。
7.  **默认 Shell**: 用户的默认命令行解释器，用户登录时会执行它（例如 `/bin/bash`）。

### 系统用户和特殊账户

当您检查 `/etc/passwd` 文件时，会注意到许多不属于人类用户的账户。这些是系统账户，用于以有限的权限运行特定的服务或进程，从而增强系统安全性。例如，`daemon` 用户用于运行后台守护进程。

### 编辑 /etc/passwd 文件

虽然您可以使用文本编辑器或 `vipw` 命令直接编辑 `/etc/passwd` 文件，但强烈不建议这样做。手动编辑很容易引入语法错误，可能导致您被锁定在系统之外或导致系统不稳定。

使用 `useradd`、`usermod` 和 `userdel` 等专用命令行工具来管理用户账户始终更安全、更可靠。这些工具旨在正确修改文件并处理所有相关的配置。

## Exercise

为了巩固您的知识，请尝试以下实践实验。它们将帮助您在现实场景中应用用户 ID 和账户管理的概念，并增强您对 Linux 用户管理的信心。

1.  **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的全生命周期，从创建和保护新账户到修改和删除它们。
2.  **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 获得使用核心命令行工具进行组管理的实践经验，包括创建新组和修改用户组成员身份。
3.  **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户账户和 sudo 权限的基本技术，以增强 Linux 系统的安全性。

## Quiz Question

如果一个用户账户被锁定且不能用于登录，在 `/etc/passwd` 文件的密码字段中是如何表示的？请仅使用所需的字符回答。

## Quiz Answer

-
