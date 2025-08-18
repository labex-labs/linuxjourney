---
index: 5
lang: "zh"
title: "身份验证日志"
meta_title: "身份验证日志 - 日志"
meta_description: "通过 /var/log/auth.log 了解 Linux 身份验证日志。通过这份基本指南，了解用户登录并排查访问问题。"
meta_keywords: "Linux 身份验证，auth.log, Linux 日志记录，用户登录，Linux 安全，初学者，教程，指南"
---

## Lesson Content

如果您在登录时遇到问题，查看身份验证日志会非常有用。

### /var/log/auth.log

此文件包含系统授权日志，例如用户登录和使用的身份验证方法。

示例片段：

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

## Exercise

执行几次失败的登录尝试，然后进行一次成功的登录。之后，检查您的 `/var/log/auth.log` 文件，看看发生了什么。

## Quiz Question

哪个日志文件用于用户身份验证？

## Quiz Answer

auth.log
