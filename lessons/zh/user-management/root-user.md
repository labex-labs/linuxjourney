---
index: 2
lang: "zh"
title: "root"
meta_title: "root - 用户管理"
meta_description: "了解 Linux root 用户、su 命令和 /etc/sudoers 文件。通过这份初学者指南了解 Linux 中的超级用户访问和权限。"
meta_keywords: "Linux root, su 命令，sudoers 文件，Linux 权限，超级用户，Linux 教程，初学者指南"
---

## Lesson Content

我们已经了解了使用 `sudo` 命令获取超级用户访问权限的一种方法。您还可以使用 `su` 命令以超级用户身份运行命令。如果未指定用户名，此命令将“切换用户”并打开一个 root shell。只要您知道密码，就可以使用此命令切换到任何用户。

```bash
su
```

使用此方法有一些缺点：以 root 身份运行所有操作更容易犯下严重错误，您将没有更改系统配置所用命令的记录等。基本上，如果您需要以超级用户身份运行命令，请坚持使用 `sudo`。

现在您知道要以超级用户身份运行哪些命令了，问题是如何知道谁有权这样做？系统不会让每个普通用户都以超级用户身份运行命令，那么它是如何知道的呢？有一个名为 `/etc/sudoers` 的文件；此文件列出了可以运行 `sudo` 的用户。您可以使用 **visudo** 命令编辑此文件。

## Exercise

熟能生巧！以下是一些动手实验，以加强您对超级用户访问和权限的理解：

1. **[在 Linux 中配置用户帐户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 练习强制执行密码策略、锁定和解锁用户帐户、保护 root 帐户以及授予管理权限，这直接关系到超级用户访问的管理。

本实验将帮助您在实际场景中应用这些概念，并增强管理用户权限和超级用户访问的信心。

## Quiz Question

哪个文件显示了有权使用 `sudo` 的用户？

## Quiz Answer

/etc/sudoers
