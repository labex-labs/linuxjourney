---
index: 3
lang: "zh"
title: "TCP/IP 模型"
meta_title: "TCP/IP 模型 - 网络基础知识"
meta_description: "了解 TCP/IP 模型层：应用层、传输层、网络层和链路层。理解数据如何在网络中传输。开始你的 Linux 网络之旅！"
meta_keywords: "TCP/IP 模型，网络基础知识，Linux 网络，TCP, IP, 初学者教程，网络层，指南"
---

## Lesson Content

OSI 模型催生了最终成为 TCP/IP 模型的模型，而这个模型实际上是互联网的基础。它是网络实际的实现。TCP/IP 模型使用 TCP/IP 协议套件，我们通常称之为 TCP/IP。这些协议协同工作，规定了数据如何被收集、寻址、传输和路由通过网络。通过使用 TCP/IP 模型，我们可以看到这些协议是如何被用来展示数据包如何在网络中传输的。

### 应用层

TCP/IP 模型的顶层。它决定了你的计算机程序（例如你的网络浏览器）如何与传输层服务交互，以查看发送或接收的数据。

此层使用：

- HTTP (Hypertext Transfer Protocol) - 用于互联网上的网页。
- SMTP (Simple Mail Transfer Protocol) - 电子邮件传输

### 传输层

数据将如何传输，包括检查正确的端口、数据的完整性，以及基本上传递我们的数据包。

此层使用：

- TCP (Transmission Control Protocol) - 可靠的数据传输
- UDP (User Datagram Protocol) - 不可靠的数据传输

### 网络层

此层规定了如何在主机之间和网络之间移动数据包。

此层使用：

- IP (Internet Protocol) - 帮助将数据包从一台机器路由到另一台机器。
- ICMP (Internet Control Message Protocol) - 帮助我们了解发生了什么，例如错误消息和调试信息。

### 链路层

此层规定了如何通过物理硬件发送数据，例如数据通过以太网、光纤等传输。

上面列出的每层使用的协议并不详尽，你还会遇到许多其他协议。

在接下来的课程中，我们将深入探讨这些层，并讨论我们的数据包在 TCP/IP 模型中是如何在网络中传输的（关于数据包如何在网络中传输有许多观点；我们不会全部探讨，但请注意它们的存在）。

## Exercise

熟能生巧！以下是一些动手实验，以巩固你对 TCP/IP 模型和网络基础知识的理解：

1. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - 练习使用 `ip a` 命令识别关键网络寻址信息，如 MAC 和 IP 地址，这对于理解 TCP/IP 模型的网络层和数据链路层至关重要。
2. **[在 Linux 中使用 ping 和 arp 探索网络层交互](https://labex.io/zh/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - 学习 `ping` 和 `arp` 命令如何演示网络层和数据链路层之间的交互，从而提供设备如何在 TCP/IP 堆栈中通信的实用见解。
3. **[在 Linux 中模拟网络层连接](https://labex.io/zh/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - 获得在 Linux 节点之间模拟网络连接、分配 IP 地址和测试通信的动手经验，直接应用与 TCP/IP 模型网络层相关的概念。

这些实验将帮助你在实际场景中应用 TCP/IP 模型的概念，并增强网络配置和故障排除的信心。

## Quiz Question

TCP/IP 模型的顶层是什么？

## Quiz Answer

Application
