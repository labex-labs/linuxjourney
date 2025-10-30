---
index: 3
lang: "zh"
title: "所有权权限"
meta_title: "所有权权限 - 权限"
meta_description: "学习如何使用 chown 和 chgrp 命令在 Linux 中更改文件所有权。通过这个适合初学者的 Linux 教程了解用户和组权限。"
meta_keywords: "chown, chgrp, Linux 文件所有权，Linux 权限，Linux 命令，Linux 初学者，Linux 教程，Linux 指南"
---

## Lesson Content

除了修改文件的权限之外，您还可以修改文件的组和用户所有权。

### 修改用户所有权

```bash
sudo chown patty myfile
```

此命令将 `myfile` 的所有者设置为 `patty`。

### 修改组所有权

```bash
sudo chgrp whales myfile
```

此命令将 `myfile` 的组设置为 `whales`。

### 同时修改用户和组所有权

如果您在用户名后添加冒号和组名，您可以同时设置用户和组。

```bash
sudo chown patty:whales myfile
```

## Exercise

熟能生巧！这里有一些动手实验来巩固您对文件所有权和权限的理解：

1. **[Linux 用户组和文件权限](https://labex.io/zh/labs/linux-linux-user-group-and-file-permissions-18002)** - 学习基本的 Linux 用户和组管理概念，包括理解文件权限和操作文件所有权。本实验提供了在多用户 Linux 环境中进行安全实践的经验。
2. **[添加新用户和组](https://labex.io/zh/labs/linux-add-new-user-and-group-17987)** - 在此挑战中，您将通过创建新用户帐户、设置自定义组和管理组成员资格来模拟向服务器环境添加新团队成员。这将考验您在 Linux 用户和组管理方面的技能。

这些实验将帮助您在实际场景中应用这些概念，并增强您在 Linux 中管理文件所有权和权限的信心。

## Quiz Question

您使用什么命令来更改用户所有权？

## Quiz Answer

chown
