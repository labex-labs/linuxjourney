---
lesson_id: "samba"
course_id: "network-sharing"
lang: "zh"
order_index: 5
title: "Samba"
description: "学习如何配置、验证、访问并保护基本 Samba 文件共享。"
meta_title: "Samba - 网络共享"
meta_description: "学习如何在 Linux 上设置 Samba 网络共享。本指南介绍 Samba 协议、安装、配置，以及使用 Linux SMB 客户端连接共享。"
meta_keywords: "Samba, Linux SMB, Samba 网络, Samba 协议, SMB Samba, 文件共享, smb.conf, cifs, smbclient, Linux 教程"
---

Samba 在类 Unix 系统上实现服务器消息块协议，使 Linux、Windows、macOS 和其他客户端能够共享文件与打印机。现代部署使用当前 SMB 方言；旧称 CIFS 仍出现在 Linux 客户端工具中，但这并不意味着应该启用已经过时的 SMB1。

## 规划共享

安装或更改 Samba 前，应定义授权客户端、身份、读写需求、网络区域、数据所有者、备份策略和所需 SMB 方言。使用专用目录，避免无意中公开主目录或系统目录树。

访问同时受 Samba 策略和底层文件系统权限控制。在 `smb.conf` 中允许写入，无法为本来没有文件系统访问权限的账户授予权限。

:::single-choice{#samba-two-permission-layers} 用户通过 Samba 共享写入时，哪些部分必须允许？

::option[只有共享显示的注释。]{#samba-comment-permission explanation="注释是描述性文本，不会授予访问。"}
::option[Samba 规则与文件系统权限都必须允许。]{#samba-policy-and-filesystem .correct explanation="请求必须通过协议层规则和本地文件系统授权。"}
::option[只有客户端桌面壁纸设置。]{#samba-wallpaper explanation="客户端外观设置不控制服务器文件。"}
:::

## 定义基本共享

主配置通常是 `/etc/samba/smb.conf`。下面是一个受限示例：

```ini
[team]
    path = /srv/samba/team
    browseable = yes
    read only = no
    valid users = @teamshare
```

创建目录，并为 Unix 组应用经过审查的所有权和权限：

```bash
$ sudo install -d -o root -g teamshare -m 2770 /srv/samba/team
```

设置组 ID 位有助于新条目继承目录组，但协作访问可能还需要 ACL 或谨慎选择的创建掩码。应测试实际文件和目录结果，而不是假定继承已经足够。

:::single-choice{#samba-valid-users} `valid users = @teamshare` 表达什么？

::option[每个匿名网络用户都获得写权限。]{#samba-every-anonymous explanation="该规则限制访问，而不是启用来宾写入。"}
::option[服务器必须把共享重命名为 `teamshare`。]{#samba-rename-share explanation="可见共享名称仍是节名称 [team]。"}
::option[该共享规则只允许指定组的成员。]{#samba-valid-group .correct explanation="@ 形式在 Samba 用户列表语法中表示组。"}
:::

## 配置身份

在独立 Samba 配置中，账户通常需要对应的 Unix 身份和已启用的 Samba 凭据：

```bash
$ sudo smbpasswd -a alice
```

目录域部署使用不同的身份设计。不要把密码放入 shell 历史记录或无关用户可读的配置中，也不要假定 Samba 密码自动与 Unix 账户密码相同。

:::single-choice{#samba-password-database} 在独立服务器上，`smbpasswd -a alice` 通常会做什么？

::option[删除 Unix 用户的主目录。]{#samba-delete-home explanation="该命令管理 Samba 凭据，不会移除主目录。"}
::option[为账户添加或初始化 Samba 凭据。]{#samba-add-credential .correct explanation="SMB 身份验证数据库与仅创建 Unix 用户分开管理。"}
::option[以 Alice 身份挂载每个可见 SMB 共享。]{#samba-mount-all explanation="服务器凭据登记与客户端挂载相互独立。"}
:::

## 验证并应用配置

重新加载服务前检查解析后的配置：

```bash
$ testparm -s
```

审查意外默认值和错误，然后通过服务管理器重新加载发行版的 Samba 服务。服务名称各不相同，常见名称包括 `smbd.service` 或 `smb.service`。支持时，重新加载比重启中断更小，但仍要验证状态、监听套接字、防火墙范围和日志。

使用明确用户从客户端测试：

```bash
$ smbclient //server.example.net/team -U alice
```

:::single-choice{#samba-testparm-purpose} 应用 Samba 更改前为什么运行 `testparm -s`？

::option[它会把每个共享文件复制到备份服务器。]{#samba-testparm-backup explanation="该工具解析并报告配置，而不是复制共享数据。"}
::option[它会验证并显示生效的 Samba 配置。]{#samba-testparm-validate .correct explanation="解析器输出可以在影响服务前发现配置错误并揭示解释后的设置。"}
::option[它会授予所有客户端管理员权限。]{#samba-testparm-admin explanation="验证不会改变客户端授权。"}
:::

## 从 Linux 挂载

Linux 客户端通常使用 `cifs` 文件系统驱动程序和挂载辅助工具。不要在命令行中放入密码，因为参数可能通过历史记录或进程检查泄漏。应使用只有 root 可读的凭据文件或获准的凭据机制：

```bash
$ sudo mount -t cifs //server.example.net/team /mnt/team \
    -o credentials=/root/.smb-team,vers=3.1.1
```

保护凭据文件，确认双方支持的方言，并有意定义 UID、GID、权限和加密要求。挂载后使用 `findmnt` 验证，执行获得授权的读写测试，并在协调活动用户后卸载。

:::single-choice{#samba-command-line-password} 为什么要避免直接在挂载命令中使用 `password=...`？

::option[秘密可能通过历史记录或进程参数暴露。]{#samba-password-exposure .correct explanation="受保护的凭据来源可以减少意外泄漏，但仍需谨慎设置权限。"}
::option[SMB 不支持任何形式的密码身份验证。]{#samba-no-passwords explanation="基于密码的 SMB 身份验证很常见，尽管也存在其他身份系统。"}
::option[该选项会让共享永久只读。]{#samba-password-readonly explanation="秘密放置方式不决定写入策略。"}
:::

## 总结

现在，你可以在同时考虑协议与文件系统安全的情况下配置 Samba 共享。

1. 首先定义客户端、身份、网络范围和数据策略。
2. 限制共享，并调整底层权限。
3. 通过正确的身份模型管理 Samba 凭据。
4. 使用 `testparm` 验证，并执行端到端客户端测试。
5. 保护客户端凭据，并验证挂载后的访问。
