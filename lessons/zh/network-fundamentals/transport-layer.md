---
lang: "zh"
title: "传输层"
description: "了解 Linux 网络中的传输层，包括 TCP/UDP 协议、端口和数据分段。理解数据如何可靠传输。"
keywords: "Linux 传输层，TCP/UDP, 网络端口，数据分段，Linux 网络，初学者教程，网络协议"
---

## Lesson Content

传输层帮助我们以网络可读取的方式传输数据。它将数据分解成块，这些块将被传输并按正确顺序重新组合。这些块被称为段。段使数据在网络中传输变得更容易。

### Ports

尽管我们知道通过 IP 地址将数据发送到哪里，但它们不够具体，无法将数据发送到特定的进程或服务。HTTP 等服务通过端口使用通信通道。如果我们要发送网页数据，我们需要通过 HTTP 端口（端口 80）发送。除了形成段之外，传输层还会将源端口和目标端口附加到段上，这样当接收方收到最终数据包时，它就会知道要使用哪个端口。

### UDP

有两种流行的传输协议：UDP 和 TCP。我们将简要讨论 UDP，并将大部分时间花在 TCP 上，因为它最常用。

UDP 不是一种可靠的数据传输方法；事实上，它并不真正关心你是否收到了所有原始数据。这听起来可能很糟糕，但它确实有其用途，例如用于媒体流。即使丢失一些帧也没关系；作为回报，你可以更快地获取数据。

### TCP

TCP 提供可靠的、面向连接的数据流。TCP 使用端口向主机发送和接收数据。应用程序从其主机上的一个端口打开到远程主机上的另一个端口的连接。为了建立连接，我们使用 TCP 握手。

- The client (connecting process) sends a SYN segment to the server to request a connection.
- The server sends the client a SYN-ACK segment to acknowledge the client's connection request.
- The client sends an ACK to the server to acknowledge the server's connection request.

一旦建立此连接，数据就可以通过 TCP 连接进行交换。数据以不同的段发送，并使用 TCP 序列号进行跟踪，以便在交付时可以按正确顺序排列。在我们的电子邮件示例中，传输层将目标端口 (25) 附加到源主机的源端口。

## Exercise

No exercises for this lesson.

## Quiz Question

什么是可靠的传输协议？

## Quiz Answer

TCP
