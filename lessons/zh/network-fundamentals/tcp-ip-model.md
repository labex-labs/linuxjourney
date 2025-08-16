---
title: "TCP/IP 模型"
description: "了解 TCP/IP 模型层：应用层、传输层、网络层和链路层。理解数据如何在网络中传输。开始您的 Linux 网络之旅！"
keywords: "TCP/IP 模型，网络基础，Linux 网络，TCP, IP, 初学者教程，网络层，指南"
---

## Lesson Content

OSI 模型催生了最终成为 TCP/IP 模型的模型，而这个模型实际上是互联网的基础。它是网络实际的实现。TCP/IP 模型使用 TCP/IP 协议套件，我们通常称之为 TCP/IP。这些协议协同工作，规定了数据应如何收集、寻址、传输和在网络中路由。使用 TCP/IP 模型，我们可以看到这些协议如何用于展示数据包如何在网络中传输的分解。

### Application Layer

TCP/IP 模型的顶层。它决定了您的计算机程序（例如您的网络浏览器）如何与传输层服务交互，以查看发送或接收的数据。

此层使用：

- HTTP (Hypertext Transfer Protocol) - 用于互联网上的网页。
- SMTP (Simple Mail Transfer Protocol) - 电子邮件传输

### Transport Layer

数据将如何传输，包括检查正确的端口、数据的完整性，以及基本上交付我们的数据包。

此层使用：

- TCP (Transmission Control Protocol) - 可靠的数据传输
- UDP (User Datagram Protocol) - 不可靠的数据传输

### Network Layer

此层规定了如何在主机之间以及跨网络移动数据包。

此层使用：

- IP (Internet Protocol) - 帮助将数据包从一台机器路由到另一台机器。
- ICMP (Internet Control Message Protocol) - 帮助我们了解发生了什么，例如错误消息和调试信息。

### Link Layer

此层规定了如何通过物理硬件发送数据，例如通过 Ethernet、光纤等传输数据。

上面列出的每层使用的协议并不详尽，您还会遇到许多其他协议。

在接下来的课程中，我们将深入探讨这些层，并讨论我们的数据包在 TCP/IP 模型看来是如何在网络中传输的（关于数据包如何在网络中传输有许多观点；我们不会全部探讨，但请注意它们的存在）。

## Exercise

No exercises for this lesson.

## Quiz Question

TCP/IP 模型的顶层是什么？

## Quiz Answer

Application
