---
title: "所有权权限"
description: "学习如何使用 chown 和 chgrp 命令在 Linux 中更改文件所有权。通过这个适合初学者的 Linux 教程了解用户和组权限。"
keywords: "chown, chgrp, Linux 文件所有权，Linux 权限，Linux 命令，Linux 初学者，Linux 教程，Linux 指南"
---

## Lesson Content

除了修改文件的权限，你还可以修改文件的组和用户所有权。

### Modify user ownership

```bash
sudo chown patty myfile
```

此命令将 `myfile` 的所有者设置为 `patty`。

### Modify group ownership

```bash
sudo chgrp whales myfile
```

此命令将 `myfile` 的组设置为 `whales`。

### Modify both user and group ownership at the same time

如果你在用户后面添加冒号和组名，你可以同时设置用户和组。

```bash
sudo chown patty:whales myfile
```

## Exercise

修改一些测试文件的组和用户。之后，使用 `ls -l` 查看权限。

## Quiz Question

你使用哪个命令来更改用户所有权？

## Quiz Answer

chown
