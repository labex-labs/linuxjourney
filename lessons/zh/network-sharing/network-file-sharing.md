---
lang: "zh"
title: "文件共享概述"
description: "了解 Linux 文件共享和安全复制 (scp) 命令。在网络上的主机之间传输文件。通过这份适合初学者的指南开始学习！"
keywords: "Linux 文件共享，scp 命令，安全复制，网络文件传输，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

您通常不是网络中唯一的计算机，尤其是在商业环境中工作时。当我们需要将数据从一台机器传输到另一台机器时，有时连接 USB 驱动器并手动复制可能更容易。但在大多数情况下，如果您在同一网络上的机器之间工作，传输数据的方式是通过网络文件共享。

在本课程中，我们将介绍几种不同的方法，用于在网络上的不同机器之间复制数据。我们将讨论一些简单的文件复制，然后我们将讨论在您的机器上挂载整个目录，使其充当单独的驱动器。

一个简单的文件共享工具是 **scp** 命令。scp 命令代表安全复制；它的工作方式与 cp 命令完全相同，但允许您将文件从一个主机复制到同一网络上的另一个主机。它通过 ssh 工作，因此您的所有操作都使用与 ssh 相同的身份验证和安全性。

### To copy a file from a local host to a remote host

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### To copy a file from a remote host to your local host

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### To copy a directory from your local host to a remote host

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

## Exercise

尝试使用 scp 将文件从一台机器复制到另一台机器。

## Quiz Question

您可以使用什么命令安全地将文件从一个主机复制到另一个主机？

## Quiz Answer

scp
