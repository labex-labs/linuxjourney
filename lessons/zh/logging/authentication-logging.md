---
index: 5
lang: "zh"
title: "身份验证日志记录"
meta_title: "身份验证日志 - 日志记录"
meta_description: "通过检查 /var/log/auth.log 文件，探索 Linux 身份验证日志记录。本指南帮助初学者理解用户登录事件、身份验证方法以及如何排除访问问题以提高 Linux 安全性。"
meta_keywords: "Linux 身份验证，auth.log, Linux 日志记录，用户登录，Linux 安全，系统授权，登录故障排除，身份验证方法，初学者，教程，指南，安全日志"
---

## Lesson Content

在 Linux 中，跟踪谁访问系统以及他们如何访问至关重要，这关系到安全和故障排除。此过程通过身份验证日志记录来管理，它记录所有与授权相关的事件，例如用户登录和所使用的方法。

### auth.log 文件

在基于 Debian 的系统（如 Ubuntu）上，跟踪此活动的主要文件是 `/var/log/auth.log`。此日志文件包含系统授权信息，包括成功和失败的用户登录尝试，以及触发的任何身份验证机制。查看此文件是诊断登录问题或调查安全事件的关键步骤。

这是 `auth.log` 文件的一个示例片段：

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

### 理解日志条目

日志中的每一行都提供了有价值的详细信息。在上面的示例中：

- **`Jan 31 10:37:50`**：事件的时间戳。
- **`icebox`**：事件发生的机器的主机名。
- **`pkexec`**：启动事件的程序。
- **`pam_unix(polkit-1:session)`**：使用的身份验证模块和服务。
- **`session opened for user root by (uid=1000)`**：执行的操作——由 UID 为 `1000` 的用户为 `root` 用户打开了一个会话。

### 替代日志文件

重要的是要注意，不同 Linux 发行版中身份验证日志的位置可能会有所不同。例如，在基于 Red Hat 的系统（如 CentOS 和 Fedora）上，这些事件通常记录在 `/var/log/secure` 中，而不是 `/var/log/auth.log`。

## Exercise

熟能生巧！以下是一些实践操作实验，以加强您对用户身份验证和帐户管理的理解：

1. **[在 Linux 中配置用户帐户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 练习强制执行密码策略、锁定/解锁用户帐户、保护 root 帐户以及授予管理权限，所有这些对于理解身份验证安全都至关重要。

这些实验将帮助您在真实场景中应用概念，并增强您对 Linux 用户和安全管理的信心。

## Quiz Question

在基于 Debian 的系统上，用于用户身份验证的日志文件叫什么名字？请仅使用文件名作答。答案区分大小写。

## Quiz Answer

auth.log
