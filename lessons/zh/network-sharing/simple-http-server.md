---
index: 3
lang: "zh"
title: "简易 HTTP 服务器"
meta_title: "简易 HTTP 服务器 - 网络共享"
meta_description: "了解如何使用 Python 的 http.server 模块在 Linux 中快速设置一个简单的 HTTP 服务器。本指南解释了如何创建一个简单的 Linux Web 服务器，以便在您的网络中轻松共享文件。"
meta_keywords: "linux 简易 http 服务器，简易 http 服务器 linux, 简易 linux web 服务器，python http.server, 什么是 python simplehttpserver, 文件共享，网络服务器"
---

## Lesson Content

Python 包含一个内置模块，可让您即时创建 Web 服务器，这对于在网络上共享文件非常有用。设置一个 **linux 简单 http 服务器** 是一个直接的过程，只需要一个命令。

### 在 Linux 中启动一个简单的 HTTP 服务器

要开始，请使用终端导航到您希望共享的目录。进入所需目录后，如果您使用的是 Python 3，可以使用以下命令启动 **simple http server linux** 环境：

```bash
python -m http.server
```

此命令会启动一个基本的 Web 服务器，使您当前目录的内容可通过 HTTP 访问。

### Python 2 的旧方法

对于仍在使用 Python 2 的旧系统，命令略有不同。该模块以前命名为 `SimpleHTTPServer`。如果您曾想知道 **what is python simplehttpserver**，它只是 `http.server` 模块的 Python 2 等效项。您可以使用以下命令运行它：

```bash
python -m SimpleHTTPServer
```

### 访问您的简单 Linux Web 服务器

运行命令后，您的 **simple linux web server** 将处于活动状态。您可以通过在另一台机器上打开 Web 浏览器并导航到 `http://IP_ADDRESS:8000` 来访问同一网络上的共享文件，将 `IP_ADDRESS` 替换为运行服务器的机器的本地 IP 地址。

要在同一台机器上查看文件，您可以使用 localhost 地址：`http://localhost:8000`。

## Exercise

实践造就完美！以下是一些实践实验，可加强您对网络连接和 IP 地址的理解，这对通过网络共享文件至关重要：

1. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 练习识别不同的 IP 地址类型并测试网络可达性，这对确保您的 Python HTTP 服务器可访问至关重要。
2. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - 学习使用 `ip a` 命令查找机器的 IP 地址，这是从另一台设备访问共享文件前的必要步骤。
3. **[管理 Linux 中的本地主机名解析](https://labex.io/zh/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - 学习通过编辑 /etc/hosts 文件来管理 Linux 中的本地主机名解析，这是 Web 开发和网络测试中的一项关键技能。

这些实验将帮助您在实际场景中应用这些概念，并建立对 Linux 中基本网络操作的信心。

## Quiz Question

对于 Python 3，用于创建简单 HTTP 服务器的模块名称是什么？（请用英语回答，注意区分大小写）。

## Quiz Answer

http.server
