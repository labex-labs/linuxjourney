---
index: 3
lang: "zh"
title: "简单 HTTP 服务器"
meta_title: "简单 HTTP 服务器 - 网络共享"
meta_description: "学习使用 Python 的 http.server 模块创建简单的 HTTP 服务器。通过这个适合初学者的 Linux 教程，快速在网络上共享文件。"
meta_keywords: "http.server, SimpleHTTPServer, Python web server, 文件共享，Linux 教程，初学者指南"
---

## Lesson Content

Python 有一个非常有用的工具，可以通过 HTTP 提供文件服务。如果你只是想创建一个快速的网络共享，让网络上的其他机器可以访问，这非常有用。为此，只需进入你想要共享的目录并运行：

```bash
python -m http.server
```

或者，如果你还在使用 Python 2：

```bash
python -m SimpleHTTPServer
```

这会建立一个基本的 Web 服务器，你可以通过 localhost 地址访问它。因此，获取运行此命令的机器的 IP 地址，然后在另一台机器上，在浏览器中通过 `http://IP_ADDRESS:8000` 访问它。在你自己的机器上，你可以通过在 Web 浏览器中输入 `http://localhost:8000` 来查看可用文件。

## Exercise

熟能生巧！以下是一些动手实验，旨在加强你对网络连接和 IP 寻址的理解，这对于通过网络共享文件至关重要：

1. **[探索 Linux 中的 IP 地址类型和可达性](https://labex.io/zh/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 练习识别不同的 IP 地址类型并测试网络可达性，这对于确保你的 Python HTTP 服务器可访问至关重要。
2. **[识别 Linux 中的 MAC 和 IP 地址](https://labex.io/zh/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - 学习使用 `ip a` 命令查找你机器的 IP 地址，这是从另一台设备访问共享文件之前的必要步骤。
3. **[管理 Linux 中的本地主机名解析](https://labex.io/zh/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - 学习通过编辑 /etc/hosts 文件来管理 Linux 中的本地主机名解析，这是 Web 开发和网络测试的关键技能。

这些实验将帮助你在实际场景中应用这些概念，并增强你在 Linux 中进行基本网络操作的信心。

## Quiz Question

你可以使用什么工具通过 Python 创建一个简单的 HTTP 服务器？

## Quiz Answer

http.server
