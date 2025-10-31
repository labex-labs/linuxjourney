---
index: 1
lang: "zh"
title: "文件共享概述"
meta_title: "文件共享概述 - 网络共享"
meta_description: "通过我们的免费在线课程探索 Linux 文件共享。学习使用 scp 等命令进行安全网络文件传输的最佳 Linux 学习方法之一。是 Linux 编程的关键资源。"
meta_keywords: "linux 文件共享，scp 命令，安全复制，学习 linux 命令，最佳免费在线 linux 课程，linux 编程，网络文件传输，学习 linux 的最佳资源"
---

## Lesson Content

在大多数现代计算环境中，您的机器很少是孤立的。无论是在家庭还是在企业环境中，您通常都属于一个网络。当您需要在计算机之间传输数据时，您可以使用 USB 驱动器，但对于同一网络上的机器来说，网络文件共享效率要高得多。对于任何认真对待“在 Linux 中编码”或管理系统的人来说，这是一项基本技能。

本课程是许多人认为的“最佳免费在线 Linux 课程”的一部分，它将向您介绍通过网络复制数据的方法。我们将从简单的文件传输开始，稍后讨论挂载整个远程目录，使它们在您的机器上显示为本地驱动器。本网站旨在通过提供清晰、实用的示例，成为“学习 Linux 的最佳网站”。

### 安全复制命令 (scp)

用于此任务的最简单、最强大的工具之一是 `scp` 命令，它是“安全复制”的缩写。它的功能与标准 `cp` 命令非常相似，但将其功能扩展到了网络上。了解它是学习网络交互的“最佳 Linux 命令学习方式”之一。由于 `scp` 通过 SSH（安全外壳）运行，所有传输都受益于相同的强大身份验证和安全协议。

### 常见的 scp 命令示例

让我们探讨一些实用的示例。语法很简单：`scp [options] source destination`。与 `cp` 的关键区别在于源或目标包含远程主机规范，格式为 `username@remotehost:/path/to/file`。

### 将文件从本地主机复制到远程主机

此命令将本地文件发送到远程机器上的指定目录。

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### 将文件从远程主机复制到本地主机

此命令从远程机器检索文件并将其保存到本地目录。

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### 将目录从本地主机复制到远程主机

要复制整个目录及其内容，请使用 `-r`（递归）选项。

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

掌握 `scp` 是至关重要的一步，探索此类工具是许多人认为这是“最佳 Linux 学习资源”的原因之一。

## Exercise

实践是掌握新命令的关键。为了加强您对安全网络文件传输的理解，我们推荐以下实践实验室：

1. **[使用 SSH 在 Linux 中进行安全远程访问](https://labex.io/zh/labs/comptia-secure-remote-access-in-linux-with-ssh-592816)** - 练习基于密钥的身份验证，使用 `scp` 安全地传输文件，以及创建用于端口转发的 SSH 隧道。

此实验室将帮助您在真实场景中应用安全远程访问和文件传输的概念，并增强您对 `scp` 的信心。

## Quiz Question

您可以使用什么命令将文件从一台主机安全地复制到另一台主机？请仅以小写英文字母回答命令名称。

## Quiz Answer

scp
