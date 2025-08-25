---
index: 4
lang: "zh"
title: "/etc/shadow"
meta_title: "/etc/shadow - 用户管理"
meta_description: "了解 Linux 中的 /etc/shadow 文件、其字段以及它如何保护用户密码。了解 Linux 认证基础知识。"
meta_keywords: "/etc/shadow, Linux 安全，用户认证，密码管理，Linux 教程，初学者指南"
---

## Lesson Content

`/etc/shadow` 文件用于存储用户认证信息。它需要超级用户读取权限。

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

你会注意到它看起来与 `/etc/passwd` 的内容非常相似；然而，在密码字段中，你会看到一个加密的密码。字段之间用冒号分隔，如下所示：

1. 用户名
2. 加密密码
3. 上次密码更改日期 - 表示自 1970 年 1 月 1 日以来的天数。如果为 0，则表示用户下次登录时应更改密码。
4. 最小密码有效期 - 用户在能够再次更改密码之前必须等待的天数。
5. 最大密码有效期 - 用户必须更改密码前的最大天数。
6. 密码警告期 - 密码即将过期前的天数。
7. 密码不活动期 - 密码过期后允许使用其密码登录的天数。
8. 账户过期日期 - 用户将无法登录的日期。
9. 为将来使用保留的字段。

在当今大多数发行版中，用户认证不仅仅依赖于 `/etc/shadow` 文件；还有其他机制，例如 PAM (可插拔认证模块)，它们取代了认证。

## Exercise

熟能生巧！这里有一些动手实验来巩固你对 Linux 中用户认证和密码管理的理解：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从使用 `useradd` 和 `passwd` 创建和保护新账户到修改和删除它们。
2. **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户账户和 sudo 权限的基本技术，包括强制执行密码策略和保护账户。

这些实验将帮助你在实际场景中应用用户和密码管理的概念，并增强对 Linux 系统管理的信心。

## Quiz Question

没有问题，继续吧！

## Quiz Answer
