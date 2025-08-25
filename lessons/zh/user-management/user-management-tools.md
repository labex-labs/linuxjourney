---
index: 6
lang: "zh"
title: "用户管理工具"
meta_title: "用户管理工具 - 用户管理"
meta_description: "学习 Linux 用户管理：使用 useradd、userdel 和 passwd 命令添加、删除和更改密码。通过这份适合初学者的指南开始学习！"
meta_keywords: "Linux 用户管理，adduser, userdel, passwd, Linux 教程，Linux 初学者，用户账户，Linux 命令"
---

## Lesson Content

大多数企业环境都使用管理系统来管理用户、账户和密码。然而，在单机计算机上，有一些有用的命令可以用来管理用户。

### 添加用户

您可以使用 `adduser` 或 `useradd` 命令。`adduser` 命令包含更多有用的功能，例如创建主目录等。有用于添加新用户的配置文件，可以根据您希望分配给默认用户的内容进行自定义。

```bash
sudo useradd bob
```

您会看到上述命令在 `/etc/passwd` 中为 bob 创建了一个条目，设置了默认组，并向 `/etc/shadow` 文件添加了一个条目。

### 删除用户

要删除用户，可以使用 `userdel` 命令。

```bash
sudo userdel bob
```

这基本上会尽力撤销 `useradd` 所做的文件更改。

### 更改密码

```bash
passwd bob
```

这将允许您更改您自己或另一个用户（如果您是 root 用户）的密码。

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对 Linux 中用户和账户管理的理解：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新账户到修改和删除它们。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 获得使用核心命令行工具进行组管理的实践经验，包括添加、修改和删除组。
3. **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户账户和 sudo 权限的基本技术，以增强 Linux 系统的安全性。

这些实验将帮助您在实际场景中应用这些概念，并增强您对 Linux 用户和组管理的信心。

## Quiz Question

用于更改密码的命令是什么？

## Quiz Answer

passwd
