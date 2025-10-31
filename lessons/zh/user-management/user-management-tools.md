---
index: 6
lang: "zh"
title: "用户管理工具"
meta_title: "用户管理工具 - 用户管理"
meta_description: "使用必备的命令行工具掌握 Linux 用户管理。本指南涵盖 useradd、userdel 和 passwd 的用法，非常适合 Linux 账户管理初学者。"
meta_keywords: "linux 用户管理，linux 账户管理命令行工具，useradd, userdel, passwd, linux 账户，管理 linux 用户"
---

## Lesson Content

虽然许多企业环境依赖专用的身份管理系统，但直接在单台机器上理解**Linux 用户管理**的基础知识是一项关键技能。有几个实用程序充当**在 Linux 中管理帐户的命令行工具**，允许从终端进行高效管理。

### 添加用户

要创建新用户，可以使用 `useradd` 命令。它是一个低级实用程序，根据 `/etc/default/useradd` 中找到的默认值创建新的用户帐户。虽然有些系统也提供 `adduser`（一个更具交互性和用户友好性的脚本），但 `useradd` 是通用的标准。

```bash
sudo useradd bob
```

执行此命令会在 `/etc/passwd` 文件中为用户 "bob" 添加一个条目，设置默认组隶属关系，并在 `/etc/shadow` 文件中创建相应的条目以安全地存储密码信息。

### 删除用户

要删除用户帐户，可以使用 `userdel` 命令。此命令通过从系统帐户文件中删除用户的条目，有效地撤销了 `useradd` 所做的更改。

```bash
sudo userdel bob
```

默认情况下，此命令可能不会删除用户的主目录。您可以使用 `-r` 标志 (`userdel -r bob`) 来确保主目录和邮件假脱机也被删除。

### 更改密码

`passwd` 命令用于设置或更改用户的密码。普通用户可以运行此命令来更改自己的密码。root 用户可以运行它来更改任何用户的密码。

```bash
passwd bob
```

当由管理员运行时，系统将提示输入指定用户的新密码，而无需询问旧密码。这是**Linux 用户管理**中的一项基本任务。

## Exercise

实践造就完美！以下是一些实践实验，可加强您对 Linux 中用户和帐户管理的理解：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户帐户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新帐户到修改和删除它们。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 获得有关组管理核心命令行实用程序的实践经验，包括添加、修改和删除组。
3. **[在 Linux 中配置用户帐户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户帐户和 sudo 权限的基本技术，以增强 Linux 系统的安全性。

这些实验将帮助您在真实场景中应用这些概念，并增强对 Linux 用户和组管理的信心。

## Quiz Question

用于更改密码的命令是什么？请仅以小写英文字母回答命令名称。

## Quiz Answer

passwd
