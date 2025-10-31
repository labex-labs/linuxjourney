---
index: 5
lang: "zh"
title: "/etc/group 文件"
meta_title: "/etc/group - 用户管理"
meta_description: "探索 Linux 中的 /etc/group 文件以了解组管理。学习如何使用 cat /etc/group 查看组数据，并理解包括 GID 和用户列表在内的结构。本指南涵盖 etc group linux 文件的要点。"
meta_keywords: "/etc/group, /etc/group linux, linux 中的/etc/group 文件，cat /etc/group, etc group linux, 组管理，GID, Linux 权限，Linux 组"
---

## Lesson Content

在 Linux 中，通过使用组可以简化对多个用户的权限管理。核心文件是 `/etc/group`，它定义了系统上的组及其成员。

### 什么是 /etc/group 文件？

Linux 中的 `/etc/group` 文件是一个纯文本文件，其中包含所有用户组的列表。可以为每个组分配对文件和目录的特定权限，从而使管理员能够高效地同时管理多个用户的访问权限。理解此文件对于在任何 `etc group linux` 环境中进行正确的用户和权限管理至关重要。

### 查看组信息

要检查此文件的内容，您可以使用一个简单的命令。在终端中运行 `cat /etc/group` 将显示系统上的所有组定义。

```bash
$ cat /etc/group

root:*:0:pete
```

### /etc/group 文件结构

与 `/etc/passwd` 文件类似，`/etc/group` 文件中的每一行代表一个组，包含四个由冒号（`:`）分隔的字段。

1. **组名**: 组的唯一名称。
2. **组密码**: 此字段是一个遗留功能，很少使用。现代系统使用 `sudo` 等工具来提升权限，而不是使用组密码。您通常会看到一个占位符，如星号（`*`）或 'x'。
3. **组 ID (GID)**: 组的唯一数字标识符。系统通常在内部使用 GID 而不是组名。
4. **用户列表**: 属于该组的用户名逗号分隔列表。

在示例 `root:*:0:pete` 中，组名是 `root`，没有密码，GID 是 `0`，用户 `pete` 是其成员。

## Exercise

熟能生巧！以下是一些实践实验室，以加强您对 Linux 用户和组管理的理解：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户帐户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新帐户到修改和删除它们。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 获得使用核心命令行实用程序进行组管理的实践经验，包括 `groupadd`、`usermod` 和 `groupdel`。
3. **[添加新用户和组](https://labex.io/zh/labs/linux-add-new-user-and-group-17987)** - 通过创建新用户帐户、设置自定义组和管理组成员身份，模拟向服务器环境添加新团队成员。

这些实验室将帮助您在实际场景中应用这些概念，并建立对 Linux 用户和组管理的信心。

## Quiz Question

root 的 GID 是多少？

## Quiz Answer

0
