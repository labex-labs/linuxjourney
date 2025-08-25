---
index: 3
lang: "zh"
title: "/etc/passwd"
meta_title: "/etc/passwd - 用户管理"
meta_description: "了解 Linux 中的 /etc/passwd 文件，理解用户信息字段以及 UID 的工作原理。探索这个重要的配置文件。"
meta_keywords: "/etc/passwd, Linux 用户，用户 ID, UID, Linux 教程，初学者，指南，Linux 命令"
---

## Lesson Content

请记住，用户名并不是用户的真正标识。系统使用用户 ID（UID）来标识用户。要了解哪些用户映射到哪些 ID，请查看 `/etc/passwd` 文件。

```bash
cat /etc/passwd
```

此文件显示了用户列表及其详细信息。例如，此文件中的第一行很可能如下所示：

```plaintext
root:x:0:0:root:/root:/bin/bash
```

每一行显示一个用户的用户信息；最常见的是，您会看到 root 用户作为第一行。有许多由冒号分隔的字段，它们提供了关于用户的额外信息。让我们来看看所有这些字段：

1. **用户名**
2. **用户密码** - 密码实际上并未存储在此文件中；它通常存储在 `/etc/shadow` 文件中。我们将在下一课中详细讨论 `/etc/shadow`，但现在，您只需知道它包含加密的用户密码。您可能会在此字段中看到许多不同的符号：如果您看到一个“x”，则表示密码存储在 `/etc/shadow` 文件中；一个“*”表示用户没有登录权限；如果这是一个空白字段，则表示用户没有密码。
3. **用户 ID** - 如您所见，root 的 UID 为 0。
4. **组 ID**
5. **GECOS 字段** - 这通常用于留下关于用户或账户的注释，例如他们的真实姓名或电话号码。它是逗号分隔的。
6. **用户主目录**
7. **用户 shell** - 您可能会看到许多用户默认使用 bash 作为他们的 shell。

通常，在用户设置页面中，您会期望只看到人类用户。但是，您会注意到 `/etc/passwd` 包含其他用户。请记住，用户在系统上实际上只是为了以不同的权限运行进程。有时我们希望以预定的权限运行进程。例如，`daemon` 用户用于守护进程。

此外，应该注意的是，如果您想添加用户和修改信息，可以手动编辑 `/etc/passwd` 文件，使用 `vipw` 工具。然而，这些事情最好留给我们将在后续课程中讨论的工具，例如 `useradd` 和 `userdel`。

## Exercise

熟能生巧！以下是一些动手实验，以加强您对 Linux 用户账户及其管理的理解：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新账户到修改和删除它们。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 获得使用核心命令行工具进行组管理的实践经验，包括创建新组和修改用户成员资格。
3. **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户账户和 sudo 权限的基本技术，以增强 Linux 系统的安全性。

这些实验将帮助您在实际场景中应用用户 ID 和账户管理的概念，并增强您对 Linux 用户管理的信心。

## Quiz Question

如果用户没有登录权限，在 `/etc/passwd` 中如何表示？

## Quiz Answer

-
