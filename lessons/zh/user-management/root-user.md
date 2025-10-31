---
index: 2
lang: "zh"
title: "根目录"
meta_title: "root - 用户管理"
meta_description: "探索 Linux 中 root 用户的角色。本课程涵盖 su 和 sudo 在获取超级用户权限方面的区别，并解释 /etc/sudoers 文件如何管理访问权限。"
meta_keywords: "linux root 用户，linux root, su, sudo, sudoers, visudo, 超级用户，用户管理，linux 权限"
---

## Lesson Content

在 Linux 中，某些管理任务需要提升的权限。这些权限属于一个特殊的账户，即 **Linux root 用户**。虽然你可以直接以 root 身份登录，但临时获得超级用户访问权限通常更安全、更易于管理。

### `su` 命令

除了 `sudo` 命令外，您还可以使用 `su`（替代用户）来获得超级用户权限。当不带用户名运行时，`su` 会尝试为 **Linux root 用户** 打开一个新的 shell 会话，并提示您输入 root 密码。

```bash
su
```

只要知道其他用户的密码，您也可以使用此命令切换到系统上的任何其他用户。

### 持续使用 Root Shell 的风险

使用 `su` 打开 root shell 有明显的缺点。持续以 root 用户身份操作会增加犯下关键的、改变系统的错误的风险。此外，在 root shell 中执行的操作不会记录在您的个人用户账户下，这使得审计系统更改变得困难。因此，最佳实践是为需要超级用户访问权限的单个命令使用 `sudo`。

### `sudoers` 文件

那么，系统如何确定谁被允许使用 `sudo` 呢？访问权限由位于 `/etc/sudoers` 的配置文件控制。该文件列出了被授予以超级用户身份运行命令权限的用户和组。

要安全地编辑此文件，您应该始终使用 `visudo` 命令。该实用程序会在文本编辑器中打开 `sudoers` 文件，并在保存前执行语法检查，这有助于防止可能导致您无法进行管理访问的配置错误。

## Exercise

将您的知识付诸实践。以下动手实验将帮助您巩固对超级用户访问和权限的理解：

1. **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 练习强制执行密码策略、锁定和解锁用户账户、保护 root 账户以及授予管理权限，这些都与超级用户访问的管理直接相关。

此实验将帮助您在实际场景中应用这些概念，并增强管理用户权限和超级用户访问的信心。

## Quiz Question

哪个文件列出了具有 `sudo` 权限的用户和组？请提供完整路径。（注意：您的答案必须是英文且区分大小写）。

## Quiz Answer

/etc/sudoers
