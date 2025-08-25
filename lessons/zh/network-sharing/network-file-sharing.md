---
index: 1
lang: "zh"
title: "文件共享概述"
meta_title: "文件共享概述 - 网络共享"
meta_description: "了解 Linux 文件共享和安全复制 (scp) 命令。在网络上的主机之间传输文件。通过这份适合初学者的指南开始学习！"
meta_keywords: "Linux 文件共享，scp 命令，安全复制，网络文件传输，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

您通常不是网络上唯一的计算机，尤其是在商业环境中工作时。当我们需要将数据从一台机器传输到另一台机器时，有时连接 USB 驱动器并手动复制可能更容易。但在大多数情况下，如果您在同一网络上的机器之间工作，传输数据的方式是通过网络文件共享。

在本课程中，我们将介绍几种不同的方法，用于在网络上的不同机器之间复制数据。我们将讨论一些简单的文件复制，然后我们将讨论在您的机器上挂载整个目录，使其充当单独的驱动器。

一个简单的文件共享工具是 **scp** 命令。scp 命令代表安全复制；它的工作方式与 cp 命令完全相同，但允许您在同一网络上的一个主机之间复制到另一个主机。它通过 ssh 工作，因此您的所有操作都使用与 ssh 相同的身份验证和安全性。

### 将文件从本地主机复制到远程主机

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### 将文件从远程主机复制到本地主机

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### 将目录从本地主机复制到远程主机

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

## Exercise

熟能生巧！这是一个动手实验，旨在加深您对安全网络文件传输的理解：

1. **[使用 SSH 在 Linux 中进行安全远程访问](https://labex.io/zh/labs/linux-secure-remote-access-in-linux-with-ssh-592816)** - 练习基于密钥的身份验证，使用 `scp` 安全传输文件，并创建 SSH 隧道进行端口转发。

本实验将帮助您在实际场景中应用安全远程访问和文件传输的概念，并增强您使用 `scp` 的信心。

## Quiz Question

您可以使用哪个命令安全地将文件从一个主机复制到另一个主机？

## Quiz Answer

scp
