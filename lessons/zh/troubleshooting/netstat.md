---
index: 4
lang: "zh"
title: "netstat 命令"
meta_title: "netstat 命令 - 网络故障排除"
meta_description: "掌握 Linux netstat 命令以分析网络连接、端口和套接字。本指南涵盖 SYN_SENT 和 netstat close_wait 等常见状态，以实现有效的故障排除。"
meta_keywords: "linux netstat, netstat, netstat 命令，syn_sent netstat, netstat close_wait, 网络连接，linux 网络，网络分析，linux 教程"
---

## Lesson Content

### 常用端口

我们已经讨论了数据如何通过我们机器上的端口传输。让我们来看看一些常见、广为人知的端口。您可以在 **/etc/services** 文件中找到这些端口的列表：

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

第一列显示服务名称，后跟其分配的端口号和使用的传输层协议。

### Linux netstat 简介

一个用于收集详细网络信息的极其有用的工具是 **netstat**。`linux netstat` 命令显示了广泛的网络相关数据，包括活动的网络连接、路由表和接口统计信息。它通常被称为网络工具中的瑞士军刀。

本课程将重点介绍使用 `netstat` 来检查网络连接的状态。在深入研究示例之前，让我们澄清套接字（socket）和端口（port）之间的区别。**端口** 是用于将数据导向特定应用程序的数字标识符。**套接字** 是通信的端点，允许程序发送和接收数据。套接字地址是 IP 地址和端口号的唯一组合。主机和目标之间的每次连接都需要一个唯一的套接字。例如，虽然 HTTP 服务运行在端口 80 上，但可以同时存在多个 HTTP 连接，并且每个连接都会创建一个唯一的套接字。

让我们检查 `netstat -at` 的输出：

```bash
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 icebox:domain           *:*                     LISTEN
tcp        0      0 localhost:ipp           *:*                     LISTEN
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN
tcp6       1      0 ip6-localhost:35094     ip6-localhost:ipp       CLOSE_WAIT
tcp6       0      0 ip6-localhost:ipp       ip6-localhost:35094     FIN_WAIT2
```

`netstat -a` 命令显示所有正在监听和未在监听的套接字，而 `-t` 标志将输出过滤为仅显示 TCP 连接。

这些列如下所示：

- **Proto**: 使用的协议（例如，TCP 或 UDP）。
- **Recv-Q**: 等待接收的数据队列。
- **Send-Q**: 等待发送的数据队列。
- **Local Address**: 本地主机的地址。
- **Foreign Address**: 远程主机的地址。
- **State**: 套接字的当前状态。

### 理解连接状态

**State** 列提供了有关连接状态的关键信息。以下是一些您会遇到的常见状态：

- **LISTENING**: 套接字正在等待传入连接。对于 TCP 连接的建立，目标必须处于监听状态。
- **SYN_SENT**: 当使用 `netstat` 时，`SYN_SENT` 状态表示套接字正在主动尝试建立连接。
- **ESTABLISHED**: 套接字具有完全建立的连接。
- **CLOSE_WAIT**: `netstat close_wait` 状态意味着远程主机已关闭，本地系统正在等待应用程序关闭套接字。
- **TIME_WAIT**: 套接字在关闭后等待，以处理网络中可能仍然存在的任何数据包。

You can see a full list of socket states in the `netstat` man page. (您可以在 `netstat` 手册页中看到套接字状态的完整列表。)

## Exercise

练习造就完美！这是一个强化您对网络接口设置理解的动手实验：

1. **[在 Linux 中使用 ethtool 检查网络接口设置](https://labex.io/zh/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - 学习使用 `ethtool` 命令来检查和管理网络接口设置，包括查看和设置接口速度和双工模式，以及分析链路模式以解决物理层网络问题。

此实验将帮助您在实际场景中应用这些概念，并建立管理网络接口的信心。

## Quiz Question

HTTPS 使用哪个端口？

## Quiz Answer

443
