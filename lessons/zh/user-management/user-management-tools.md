---
title: "用户管理工具"
description: "学习 Linux 用户管理：使用 useradd、userdel 和 passwd 命令添加、删除和更改密码。通过这份适合初学者的指南快速入门！"
keywords: "Linux 用户管理，adduser, userdel, passwd, Linux 教程，Linux 初学者，用户账户，Linux 命令"
---

## Lesson Content

大多数企业环境都使用管理系统来管理用户、账户和密码。然而，在单机计算机上，有一些有用的命令可以用来管理用户。

### Adding Users

您可以使用 `adduser` 或 `useradd` 命令。`adduser` 命令包含更多有用的功能，例如创建主目录等。有用于添加新用户的配置文件，可以根据您希望分配给默认用户的内容进行自定义。

```bash
sudo useradd bob
```

您会看到上述命令在 `/etc/passwd` 中为 bob 创建了一个条目，设置了默认组，并在 `/etc/shadow` 文件中添加了一个条目。

### Removing Users

要删除用户，可以使用 `userdel` 命令。

```bash
sudo userdel bob
```

这基本上会尽力撤销 `useradd` 所做的文件更改。

### Changing Passwords

```bash
passwd bob
```

这将允许您更改自己或另一个用户（如果您是 root 用户）的密码。

## Exercise

创建一个新用户，然后更改其密码并以新用户身份登录。

## Quiz Question

用于更改密码的命令是什么？

## Quiz Answer

passwd
