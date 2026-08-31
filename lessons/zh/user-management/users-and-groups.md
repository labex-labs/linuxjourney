---
lesson_id: "users-and-groups"
course_id: "user-management"
lang: "zh"
order_index: 1
title: "用户和组"
description: "学习 Linux 如何标识用户和组，以及进程凭据如何影响访问决策。"
meta_title: "用户和组 - 用户管理"
meta_description: "Linux 基础知识的关键部分是理解用户和组的管理。本指南涵盖了 Linux 用户和组、root 超级用户以及使用 sudo 命令提升权限。这是最适合初学者的 Linux 教程课程之一。"
meta_keywords: "linux 用户和组，linux 基础，sudo, root 用户，UID, GID, 用户管理，最佳 linux 教程，最快学习 linux 高级知识"
---

Linux 使用用户和组身份来标记进程、拥有文件系统对象并做出访问控制决策。人类可读的名称方便管理员使用，而内核主要处理数值标识符和进程凭据。

## 使用 UID 标识用户

每个账户都有一个数值用户 ID，即 **UID**。用户名通过系统账户数据库映射到 UID。文件存储的是数值所有权，而工具通常会将其显示为对应名称。

运行 `id` 检查当前进程的身份信息：

```bash
$ id
uid=1000(alice) gid=1000(alice) groups=1000(alice),27(sudo)
```

具体值因系统而异。人类登录账户通常有 `/home/alice` 等主目录，但账户也可以使用其他路径，甚至没有普通主目录。服务账户往往用于以受限身份运行软件，而不是支持交互式登录。

:::single-choice{#users-uid-purpose}
内核主要使用哪个标识符表示用户身份？

::option[主目录路径]{#users-home-path explanation="主目录路径是账户配置，可以不同或不存在；它不是内核的用户标识符。"}
::option[数值 UID]{#users-numeric-uid .correct explanation="账户数据库把名称映射到数值 UID，UID 用于进程凭据和所有权记录。"}
::option[终端窗口编号]{#users-terminal-number explanation="终端设备和会话与数值用户身份相互独立。"}
:::

## 使用组组织访问权限

组有一个数值组 ID，即 **GID**。账户通常有一个主组，还可以属于多个附加组。组成员身份让管理员能够一次为一组用户授予访问权限，而无需逐个账户设置权限。

使用以下命令检查成员身份：

```bash
$ id alice
$ groups alice
```

这些命令会报告已配置或解析的身份信息。目录服务和缓存也可能参与，因此直接读取 `/etc/group` 不一定能显示完整的有效成员关系。

:::single-choice{#users-primary-supplementary-groups}
一个 Linux 账户通常可以如何加入组？

::option[在其整个生命周期中只能属于一个组。]{#users-single-group explanation="Linux 进程可以带有一个主组和一份附加组列表。"}
::option[它属于自己能够读取其文件的每个组。]{#users-readable-groups explanation="文件可读性取决于权限和凭据，不会自动创建组成员身份。"}
::option[它有一个主组，还可以拥有附加组。]{#users-group-memberships .correct explanation="主 GID 属于账户记录，附加成员身份则提供额外的组身份。"}
:::

## 理解进程凭据

进程拥有实际和有效 UID、GID 以及附加组等凭据。有效凭据是许多权限检查的核心。用户启动的进程通常从父进程继承凭据，但受控机制可以改变它们。

这比“进程始终只以启动它的用户身份运行”更准确。set-user-ID 可执行文件、服务管理器、容器、命名空间和改变权限的系统调用，都可能影响特定上下文中可见或有效的身份。

:::single-choice{#users-process-access-identity}
内核根据文件权限检查进程时，通常会考虑哪些信息？

::option[进程的有效 UID、有效 GID 和附加组。]{#users-effective-credentials .correct explanation="在普通自主访问控制检查中，这些凭据会与所有权和权限数据比较。"}
::option[启动进程的终端配色主题。]{#users-terminal-theme explanation="显示偏好不会参与文件系统权限检查。"}
::option[账户用户名的拼写长度。]{#users-username-length explanation="内核处理数值凭据；用户名长度不会授予访问权限。"}
:::

## 认识 root 身份

传统上名为 `root` 的账户拥有 UID 0。许多 Linux 权限机制会特殊对待 UID 0，使其拥有广泛的管理能力。现代 Linux 也可以通过 capabilities、命名空间、强制访问控制和服务隔离来划分权限，因此“在任何上下文中都拥有无限权力”是一种过度简化。

日常工作应使用非特权账户。管理权限会放大路径错误、不受信任命令和受攻陷软件造成的影响。

:::single-choice{#users-root-uid}
哪个数值 UID 传统上标识 root 账户？

::option[`0`]{#users-uid-zero .correct explanation="Linux 和类 Unix 系统传统上为超级用户身份保留 UID 0。"}
::option[`1000`]{#users-uid-thousand explanation="许多发行版会把接近 1000 的值分配给第一个普通人类账户，但这不是 root UID。"}
::option[`1`]{#users-uid-one explanation="UID 1 可以属于系统账户，并不是传统超级用户身份。"}
:::

## 在策略控制下使用 sudo

`sudo` 会询问其配置的策略：调用用户是否可以目标用户身份运行某个命令。默认目标通常是 root，但策略或 `-u USER` 可以选择其他账户。认证提示和日志记录也取决于配置。

列出当前账户获准运行的命令：

```bash
$ sudo -l
```

只有任务确实需要且你理解其影响时，才使用获准的管理命令。不要只为消除权限错误而使用 `sudo`，也不要把 `/etc/shadow` 等密码哈希数据库作为随意练习内容显示出来。

:::single-choice{#users-sudo-policy}
`sudo` 在运行请求的命令前会做什么？

::option[查询配置的策略，确认是否允许使用所请求的目标身份。]{#users-sudo-policy-check .correct explanation="`sudo` 根据策略授权，获准后再建立配置的目标凭据。"}
::option[始终向每个本地用户授予不受限制的 root 访问权限。]{#users-sudo-always-root explanation="授权受策略控制，被拒绝的用户或命令不会获得全面 root 访问。"}
::option[把调用账户的永久 UID 改为 0。]{#users-sudo-permanent-uid explanation="`sudo` 使用目标凭据运行命令，不会永久重写调用者的账户身份。"}
:::

要在受控环境中练习账户和组管理，可以尝试以下动手实验：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新账户到修改和删除账户。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 练习组管理的核心命令行工具，包括创建新组、修改用户成员身份和删除组。
3. **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户账户和 `sudo` 权限的重要技术，包括授予管理权限，以增强 Linux 系统安全性。

## 总结

现在，你可以说明 Linux 如何表示身份并委派管理命令。

1. 使用 UID 标识账户，使用 GID 标识组。
2. 区分主组和附加组成员身份。
3. 把进程凭据与访问检查联系起来。
4. 认识 UID 0 这一传统 root 身份。
5. 把 `sudo` 视为受策略控制的委派工具。
