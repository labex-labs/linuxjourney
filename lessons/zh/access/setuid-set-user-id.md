---
lang: "zh"
title: "Setuid"
meta_description: "了解 Linux Setuid (SUID) 权限、它们的工作原理以及如何修改它们。理解 SUID 在 Linux 中安全文件访问的重要性。"
meta_keywords: "Linux Setuid, SUID, Linux 权限，chmod, passwd 命令，Linux 安全，Linux 初学者，Linux 教程"
---

## Lesson Content

在许多情况下，普通用户需要提升权限才能执行某些操作。系统管理员不可能每次用户需要访问受保护文件时都输入 root 密码，因此存在特殊的 文件权限位 来允许这种行为。Set User ID (SUID) 允许用户以程序文件所有者的身份而不是以其自身的身份运行程序。

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

哦，等一下，这个文件是 root 拥有的？我们怎么可能修改一个 root 拥有的文件呢？

让我们看看另一组权限，这次是我们运行的命令的权限：

```bash
$ ls -l /usr/bin/passwd

-rwsr-xr-x 1 root root 47032 Dec 1 11:45 /usr/bin/passwd
```

你会注意到这里有一个新的权限位 **s**。这个权限位就是 SUID。当一个文件设置了这个权限时，它允许启动该程序的用户获得文件所有者的权限以及执行权限，在本例中是 root。所以本质上，当用户运行 `passwd` 命令时，他们是以 root 身份运行的。

这就是为什么当我们运行 `passwd` 命令时，我们能够访问像 `/etc/shadow` 这样的受保护文件。现在如果你删除了那个位，你会发现你将无法修改 `/etc/shadow`，因此也无法更改你的密码。

### Modifying SUID

就像常规权限一样，有两种方法可以修改 SUID 权限。

_Symbolic way:_

```bash
sudo chmod u+s myfile
```

_Numerical way:_

```bash
sudo chmod 4755 myfile
```

如你所见，SUID 由数字 4 表示，并放在权限集的前面。你可能会看到 SUID 表示为大写 **S**。这意味着它仍然做同样的事情，但它没有执行权限。

## Exercise

Look at the permissions for `/etc/passwd` in detail. Do you notice anything else? Files with SUID enabled are also easily distinguishable.

## Quiz Question

代表 SUID 的数字是什么？

## Quiz Answer

4
