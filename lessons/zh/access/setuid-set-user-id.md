---
index: 5
lang: "zh"
title: "Setuid"
meta_title: "Setuid - 权限"
meta_description: "了解 Linux Setuid (SUID) 权限、它们的工作原理以及如何修改它们。理解 SUID 在 Linux 中安全文件访问的重要性。"
meta_keywords: "Linux Setuid, SUID, Linux 权限，chmod, passwd 命令，Linux 安全，Linux 初学者，Linux 教程"
---

## Lesson Content

在许多情况下，普通用户需要提升权限才能执行某些操作。系统管理员不可能每次用户需要访问受保护文件时都在场输入 root 密码，因此存在特殊的文件权限位来允许这种行为。Set User ID (SUID) 允许用户以程序文件所有者的身份而不是以其自己的身份运行程序。

让我们看一个例子：

假设我想更改我的密码，很简单对吧？我只需使用 `passwd` 命令：

```bash
passwd
```

`passwd` 命令在做什么？它正在修改几个文件，但最重要的是它正在修改 `/etc/shadow` 文件。让我们看一下这个文件：

```bash
$ ls -l /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

等等，这个文件是 root 拥有的？我们怎么可能修改一个由 root 拥有的文件？

让我们看看另一组权限，这次是我们运行的命令的权限：

```bash
$ ls -l /usr/bin/passwd

-rwsr-xr-x 1 root root 47032 Dec 1 11:45 /usr/bin/passwd
```

你会注意到这里有一个新的权限位 **s**。这个权限位就是 SUID。当一个文件设置了此权限时，它允许启动该程序的用户获得文件所有者的权限以及执行权限，在本例中是 root。所以本质上，当用户运行 `passwd` 命令时，他们是以 root 身份运行的。

这就是为什么当我们运行 `passwd` 命令时，我们能够访问像 `/etc/shadow` 这样的受保护文件。现在，如果你删除了那个位，你会发现你将无法修改 `/etc/shadow`，因此也无法更改你的密码。

### 修改 SUID

就像常规权限一样，有两种方法可以修改 SUID 权限。

_符号方式：_

```bash
sudo chmod u+s myfile
```

_数字方式：_

```bash
sudo chmod 4755 myfile
```

如你所见，SUID 用数字 4 表示，并添加到权限集的前面。你可能会看到 SUID 表示为大写 **S**。这意味着它仍然做同样的事情，但它没有执行权限。

## Exercise

熟能生巧！理解文件权限、用户组和像 SUID 这样的特殊位如何工作对于管理和保护 Linux 系统至关重要。动手实践将巩固你的知识。

这是一个动手实验，以加强你对文件权限和用户管理的理解：

1. **[Linux 用户组和文件权限](https://labex.io/zh/labs/linux-linux-user-group-and-file-permissions-18002)** - 练习创建和管理用户和组，理解文件权限，并操作文件所有权。本实验提供了理解 SUID 如何利用这些概念进行提升访问所需的基础知识。

本实验将帮助你在实际场景中应用这些概念，并增强对 Linux 用户和文件管理的信心。

## Quiz Question

哪个数字代表 SUID？

## Quiz Answer

4
