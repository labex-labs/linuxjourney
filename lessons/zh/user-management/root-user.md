---
index: 2
lang: "zh"
title: "root"
meta_title: "root - 用户管理"
meta_description: "了解 Linux root 用户、su 命令和 /etc/sudoers 文件。通过这份初学者指南，理解 Linux 中的超级用户访问和权限。"
meta_keywords: "Linux root, su command, sudoers file, Linux permissions, superuser, Linux tutorial, beginner guide"
---

## Lesson Content

我们已经了解了使用 `sudo` 命令获取超级用户访问权限的一种方法。你也可以使用 `su` 命令以超级用户身份运行命令。如果未指定用户名，此命令将“切换用户”并打开一个 root shell。只要你知道密码，就可以使用此命令切换到任何用户。

```bash
su
```

使用这种方法有一些缺点：以 root 身份运行所有操作更容易犯下严重错误，你将没有更改系统配置所用命令的记录，等等。基本上，如果你需要以超级用户身份运行命令，只需坚持使用 `sudo`。

现在你已经知道要以超级用户身份运行哪些命令，问题是你如何知道谁有权这样做？系统不会让每个普通用户都以超级用户身份运行命令，那么它是如何知道的呢？有一个名为 `/etc/sudoers` 的文件；此文件列出了可以运行 `sudo` 的用户。你可以使用 **visudo** 命令编辑此文件。

## Exercise

打开 `/etc/sudoers` 文件，查看机器上其他用户拥有哪些超级用户权限。

## Quiz Question

哪个文件显示了有权使用 `sudo` 的用户？

## Quiz Answer

/etc/sudoers
