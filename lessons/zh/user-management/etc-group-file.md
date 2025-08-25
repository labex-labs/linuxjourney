---
index: 5
lang: "zh"
title: "/etc/group"
meta_title: "/etc/group - 用户管理"
meta_description: "了解 Linux 中的 /etc/group 文件，理解组管理、GID 和用户权限。针对初学者的重要 Linux 组文件教程。"
meta_keywords: "/etc/group, Linux 组，组管理，GID, Linux 权限，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

另一个用于用户管理的文件是 `/etc/group` 文件。该文件允许不同的组拥有不同的权限。

```bash
$ cat /etc/group

root:*:0:pete
```

与 `/etc/passwd` 文件非常相似，`/etc/group` 文件的字段如下：

1. 组名
2. 组密码 - 无需设置组密码；使用 `sudo` 等提升权限是标准做法。默认值将用星号 (`*`) 代替。
3. 组 ID (GID)
4. 用户列表 - 您可以手动指定要加入特定组的用户

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对 Linux 用户和组管理的理解：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新账户到修改和删除它们。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 获得使用核心命令行工具进行组管理的实践经验，包括 `groupadd`、`usermod` 和 `groupdel`。
3. **[添加新用户和组](https://labex.io/zh/labs/linux-add-new-user-and-group-17987)** - 模拟向服务器环境添加新团队成员，通过创建新用户账户、设置自定义组和管理组成员资格。

这些实验将帮助您在实际场景中应用概念，并增强对 Linux 用户和组管理的信心。

## Quiz Question

root 的 GID 是多少？

## Quiz Answer

0
