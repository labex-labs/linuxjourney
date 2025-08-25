---
index: 4
lang: "zh"
title: "netstat"
meta_title: "netstat - 故障排除"
meta_description: "学习用于 Linux 网络分析的 netstat 命令。通过这份适合初学者的指南，了解网络连接、端口和套接字。"
meta_keywords: "netstat, netstat 命令，Linux 网络，网络连接，Linux 教程，初学者，指南"
---

## Lesson Content

### 知名端口

我们已经讨论了通过机器上的端口进行数据传输；现在我们来看看一些知名端口。

您可以通过查看文件 **/etc/services** 来获取知名端口列表：

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

第一列是服务名称，然后是端口号，以及它使用的传输层协议。

### netstat

一个极其有用的工具，可以获取关于您的网络的详细信息，那就是 **netstat**。Netstat 显示各种与网络相关的信息，例如网络连接、路由表、网络接口信息等等；它是网络工具中的瑞士军刀。我们将主要关注 netstat 的一个功能，那就是网络连接的状态。在我们看一个例子之前，我们先来谈谈套接字和端口。套接字是一个允许程序发送和接收数据的接口，而端口用于识别哪个应用程序应该发送或接收数据。套接字地址是 IP 地址和端口的组合。主机和目的地之间的每个连接都需要一个唯一的套接字。例如，HTTP 是一种在端口 80 上运行的服务；但是，我们可以有许多 HTTP 连接，为了维护每个连接，每个连接都会创建一个套接字。

```bash
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 icebox:domain           *:*                     LISTEN
tcp        0      0 localhost:ipp           *:*                     LISTEN
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT
tcp6       0      0 ip6-localhost:ipp       [::]:*                     LISTEN
tcp6       1      0 ip6-localhost:35094     ip6-localhost:ipp       CLOSE_WAIT
tcp6       0      0 ip6-localhost:ipp       ip6-localhost:35094     FIN_WAIT2
```

`netstat -a` 命令显示网络连接的监听和非监听套接字；`-t` 标志仅显示 TCP 连接。

列从左到右依次是：

- **Proto**：使用的协议，TCP 或 UDP。
- **Recv-Q**：排队等待接收的数据。
- **Send-Q**：排队等待发送的数据。
- **Local Address**：本地连接的主机。
- **Foreign Address**：远程连接的主机。
- **State**：套接字的状态。

有关套接字状态的列表，请参阅手册页，但这里有几个：

- **LISTENING**：套接字正在监听传入连接。请记住，当我们建立 TCP 连接时，我们的目的地必须在我们可以连接之前监听我们。
- **SYN_SENT**：套接字正在积极尝试建立连接。
- **ESTABLISHED**：套接字已建立连接。
- **CLOSE_WAIT**：远程主机已关闭，我们正在等待套接字关闭。
- **TIME_WAIT**：套接字在关闭后等待处理仍在网络中的数据包。

## Exercise

熟能生巧！这是一个动手实验，旨在巩固您对网络接口设置的理解：

1. **[使用 ethtool 在 Linux 中检查网络接口设置](https://labex.io/zh/labs/linux-examine-network-interface-settings-with-ethtool-in-linux-592759)** - 学习使用 `ethtool` 命令检查和管理网络接口设置，包括查看和设置接口速度和双工模式，以及分析链路模式以排除物理层网络问题。

本实验将帮助您在实际场景中应用这些概念，并增强管理网络接口的信心。

## Quiz Question

HTTPS 使用哪个端口？

## Quiz Answer

443
