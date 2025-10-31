---
index: 4
lang: "zh"
title: "/etc/shadow"
meta_title: "/etc/shadow - 用户管理"
meta_description: "探索 Linux 中的 /etc/shadow 文件，它是用户身份验证的关键组件。了解如何使用 'cat /etc/shadow' 查看它，并理解存储加密密码和策略信息的 etc shadow 文件结构。"
meta_keywords: "etc shadow, etc/shadow 文件在 linux, cat /etc/shadow, linux 中的 etc shadow, /etc/shadow, 用户身份验证，密码安全，Linux 系统管理"
---

## Lesson Content

`/etc/shadow` 文件是 Linux 系统中存储敏感用户身份验证信息的关键组件。与可供所有人读取的 `/etc/passwd` 文件不同，它需要超级用户权限才能访问，为密码数据提供了一个安全的位置。

### etc/shadow 文件在 Linux 中的作用

**etc/shadow 文件在 Linux 中**的主要目的是存储加密的用户密码和密码有效期策略。通过将这些敏感数据与 `/etc/passwd` 中的常规用户信息分开，系统增强了安全性。如果一个非特权用户能够读取密码哈希，他们可能会尝试离线破解它们。

### 使用 cat /etc/shadow 查看文件

要检查此文件的内容，您必须使用具有超级用户权限的命令，例如 `sudo`。`cat /etc/shadow` 命令常用于此目的。

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

**etc shadow** 文件输出格式是一系列由冒号分隔的字段，每行代表一个用户。

### 理解文件结构

`/etc/shadow` 中的每行包含九个由冒号分隔的字段：

1. **用户名**: 用户的登录名称。
2. **加密密码**: 哈希后的用户密码。此处出现星号 (`*`) 或感叹号 (`!`) 表示账户被锁定。
3. **上次更改密码的日期**: 自 1970 年 1 月 1 日以来密码上次更改的天数。值为 `0` 会强制用户在下次登录时更改密码。
4. **最小密码年龄**: 用户再次更改密码前必须经过的最少天数。
5. **最大密码年龄**: 密码有效期的最长天数。超过此期限，用户必须更改密码。
6. **密码警告期限**: 在密码过期前的天数内，用户将收到警告消息。
7. **密码不活动期限**: 密码过期后禁用账户的天数。
8. **账户过期日期**: 一个绝对日期，表示为自 1970 年 1 月 1 日以来的天数，届时用户账户将被禁用。
9. **保留字段**: 此字段为将来使用而保留。

虽然 `/etc/shadow` 文件是基础性的，但大多数现代发行版会用其他身份验证机制（如可插拔身份验证模块 (PAM)）来补充它，PAM 提供了更灵活和先进的身份验证方案。

## Exercise

熟能生巧！以下是一些实践操作实验，以加强您对 Linux 中用户身份验证和密码管理的理解：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从使用 `useradd` 和 `passwd` 创建和保护新账户到修改和删除它们。
2. **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户账户和 sudo 权限的基本技术，包括实施密码策略和保护账户。

这些实验将帮助您在真实场景中应用用户和密码管理的概念，并增强您对 Linux 系统管理的信心。

## Quiz Question

没有问题，请继续！
