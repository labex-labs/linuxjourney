---
index: 5
lang: "zh"
title: "身份验证日志记录"
meta_title: "身份验证日志记录 - 日志记录"
meta_description: "通过本基本指南了解 Linux 身份验证日志记录与 /var/log/auth.log。了解用户登录并排查访问问题。"
meta_keywords: "Linux 身份验证，auth.log, Linux 日志记录，用户登录，Linux 安全，初学者，教程，指南"
---

## Lesson Content

如果登录遇到问题，查看身份验证日志会非常有用。

### /var/log/auth.log

此文件包含系统授权日志，例如用户登录和使用的身份验证方法。

示例片段：

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

## Exercise

熟能生巧！以下是一些动手实验，旨在加深您对用户身份验证和账户管理的理解：

1. **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 练习强制执行密码策略、锁定/解锁用户账户、保护 root 账户以及授予管理权限，所有这些对于理解身份验证安全都至关重要。

这些实验将帮助您在实际场景中应用概念，并增强对 Linux 用户和安全管理的信心。

## Quiz Question

哪个日志文件用于用户身份验证？

## Quiz Answer

auth.log
