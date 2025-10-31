---
index: 5
lang: "zh"
title: "Samba"
meta_title: "Samba - 网络共享"
meta_description: "了解如何在 Linux 上设置 Samba 网络共享。本指南涵盖 Samba 协议、安装、配置以及使用 smb linux 客户端连接共享。"
meta_keywords: "Samba, smb linux, linux smb, samba 网络，samba 协议，smb samba, 文件共享，smb.conf, cifs, smbclient, linux 教程"
---

## Lesson Content

几十年来，在混合操作系统环境中，一个主要的挑战一直是共享 Windows 和 Linux 机器之间的文件。解决方案是服务器消息块 (SMB) 协议。SMB 协议最初是为 Windows 开发的，后来被精炼成一种称为通用互联网文件系统 (CIFS) 的方言。如今，现代系统使用更新版本的 SMB，但这些术语通常一起使用。

Samba 是一个强大的软件套件，它在 Linux 和其他类 Unix 系统上实现了 **SMB/CIFS** 协议。它是 **smb linux** 集成的关键，允许 Linux 服务器充当 Windows、macOS 和其他 Linux 客户端的文件和打印服务器，从而创建一个无缝的 **samba network**。**smb samba** 之间的关系很简单：Samba 是使用 SMB 语言的软件。

### 在 Linux 上安装 Samba

首先，您需要安装 Samba 软件包。命令根据您 Linux 发行版的包管理器而异。对于基于 Debian 的系统（如 Ubuntu），请使用以下命令：

```bash
sudo apt update
sudo apt install samba
```

### 配置 Samba 共享

Samba 的主配置文件位于 `/etc/samba/smb.conf`。此文件决定了哪些目录被共享、谁可以访问它们以及它们的权限。默认文件包含许多注释掉的示例，可作为很好的参考。

让我们逐步配置一个基本共享。

首先，在文本编辑器中打开配置文件：

```bash
sudo nano /etc/samba/smb.conf
```

在文件末尾，为您的共享添加一个新部分。方括号中的名称将是网络上可见的共享名称。

```ini
[myshare]
    comment = My First Samba Share
    path = /my/directory/to/share
    read only = no
    browsable = yes
```

接下来，创建您在配置中指定的目录：

```bash
mkdir -p /my/directory/to/share
```

最后，您需要为 Samba 访问设置特定的密码。Samba 维护自己的密码数据库，它与系统的用户密码是分开的。

```bash
sudo smbpasswd -a [username]
```

将 `[username]` 替换为您系统上现有的 Linux 用户。系统将提示您为该用户创建 Samba 访问的新密码。

### 管理 Samba 服务

修改 `smb.conf` 文件后，您必须重新启动 Samba 服务以使更改生效。

```bash
sudo service smbd restart
```

### 访问 Samba 共享

配置好共享后，网络上的客户端就可以访问它了。

**从 Windows 访问：**
打开“运行”提示符 (Win + R) 或文件资源管理器，然后输入网络路径：`\\HOST\sharename`，其中 `HOST` 是您的 Linux 机器的 IP 地址或主机名。

**从 Linux 访问：**
Samba 包包含一个名为 **smbclient** 的命令行工具，它允许您与任何 **linux smb** 或 Windows 共享进行交互。

```bash
smbclient //HOST/myshare -U username
```

连接后，您将看到一个 `smb: \>` 提示符，您可以在其中使用 `ls`、`get` 和 `put` 等命令来管理文件。

### 挂载 Samba 共享

为了实现更永久的访问，您可以将网络共享直接挂载到您的文件系统，使其看起来像一个本地目录。

```bash
sudo mount -t cifs //SERVER/sharename /mnt/mountpoint -o user=username,pass=password
```

此命令使用 `cifs` 文件系统类型将远程共享附加到本地挂载点。

## Exercise

尝试在您自己的 Linux 机器上设置一个简单的 Samba 共享。创建一个目录，在 `smb.conf` 中配置它，并尝试使用同一台机器上的 `smbclient` 访问它以测试配置。为了获得更多实践经验，请探索综合性的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

什么是 SMB 的早期方言，它是为文件共享而开发的协议的名称？请用英语回答，注意大小写。

## Quiz Answer

CIFS
