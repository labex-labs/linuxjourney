---
index: 5
lang: "zh"
title: "Samba"
meta_title: "Samba - 网络共享"
meta_description: "学习如何在 Linux 上为 Windows 和 macOS 设置 Samba 文件共享。这个初学者指南涵盖了安装、配置和访问共享。立即开始！"
meta_keywords: "Samba, Linux 文件共享，smb.conf, CIFS, smbclient, Linux 教程，初学者指南"
---

## Lesson Content

在计算的早期，Windows 机器与 Linux 机器共享文件变得很有必要；因此，服务器消息块 (SMB) 协议应运而生。SMB 用于在 Windows 操作系统之间共享文件（macOS 也可以通过 SMB 共享文件），后来以通用互联网文件系统 (CIFS) 协议的形式进行了清理和优化。

Samba 是我们所说的在 Linux 上使用 CIFS 的 Linux 实用程序。除了文件共享，您还可以共享打印机等资源。

### 使用 Samba 创建网络共享

让我们来看看创建 Windows 机器可以访问的网络共享的基本步骤：

### 安装 Samba

```bash
sudo apt update
sudo apt install samba
```

### 设置 smb.conf

Samba 的配置文件位于 `/etc/samba/smb.conf`。此文件应告诉系统哪些目录应该共享、它们的访问权限以及更多选项。默认的 `smb.conf` 已经包含许多注释掉的代码，您可以将它们作为示例来编写自己的配置。

```bash
sudo vi /etc/samba/smb.conf
```

### 为 Samba 设置密码

```bash
sudo smbpasswd -a [username]
```

### 创建共享目录

```bash
mkdir /my/directory/to/share
```

### 重启 Samba 服务

```bash
sudo service smbd restart
```

### 通过 Windows 访问 Samba 共享

在 Windows 中，只需在“运行”提示符中输入网络连接：`\\HOST\sharename`。

### 通过 Linux 访问 Samba/Windows 共享

```bash
smbclient //HOST/directory -U user
```

Samba 软件包包含一个名为 **smbclient** 的命令行工具，您可以使用它来访问任何 Windows 或 Samba 服务器。连接到共享后，您可以导航和传输文件。

### 将 Samba 共享附加到您的系统

您无需逐个传输文件，只需将网络共享挂载到您的系统上即可。

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

虽然本主题没有具体的实验，但我们建议您探索全面的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

Windows 和 Linux 之间用于文件传输的最新协议是什么？

## Quiz Answer

CIFS
