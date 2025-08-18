---
lang: "zh"
title: "什么是路由器？"
meta_description: "了解路由器是什么、它的工作原理以及它在网络中的作用。帮助初学者理解路由、跳数和数据包传输。"
meta_keywords: "路由器，网络，路由，跳数，数据包交换，Linux 网络，初学者教程，网络指南"
---

## Lesson Content

我们之前用过“路由器”这个词；希望你知道它是什么，因为你家里可能就有一个。路由器使网络上的机器能够相互通信，并与其他网络通信。在一个典型的路由器上，你会看到 LAN 端口，它允许你的机器连接到同一个局域网，你还会有一个互联网上行端口，它将你连接到互联网。有时你会看到这个端口被标记为 WAN，因为它本质上是将你连接到一个更广阔的网络。当我们进行任何网络活动时，都必须通过路由器。路由器决定我们的网络数据包去向何处以及哪些数据包可以进入。它在多个网络之间路由我们的数据包，使其从源主机到达目标主机。

### How does a router work?

把路由想象成邮件投递。我们有一个想要寄信的地址。当我们把信寄到邮局时，他们拿到信一看，“哦，这封信是要寄到加利福尼亚的。”我就会把它放到去加利福尼亚的卡车上（我真的不知道邮政系统是如何运作的）。然后这封信被寄到旧金山。在旧金山内部有不同的邮政编码，然后在这些邮政编码内部有更小的地址编码，直到最终有人能够将你的信件投递到你想要的地址。另一方面，如果你已经住在旧金山并且在同一个邮政编码内，邮件投递员可能就会确切地知道信件要送到哪里，而无需将其转交给其他人。

当我们路由数据包时，它们使用类似的地址“路由”，例如“要到达网络 A，将这些数据包发送到网络 B”。当我们没有为某个目的地设置路由时，我们的数据包将使用默认路由。这些路由设置在路由表中，我们的系统使用该表在网络之间导航。

### Hops

当数据包在网络中移动时，它们以“跳”（hops）的方式传输。跳数是我们粗略衡量数据包从源到目的地所需传输距离的方式。假设我有两台路由器连接主机 A 到主机 B；因此，我们说主机 A 和主机 B 之间有两跳。每一跳都是一个中间设备，比如路由器，我们必须经过它。

### Understanding the basic difference between Switching, Routing & Flooding?

- **Packet SWITCHING** is basically receiving, processing, and forwarding data to the destination device.
- **ROUTING** is a process of creating the routing table so that we can do SWITCHING better.
- Before routing, **FLOODING** was used. If a router doesn't know which way to send a packet, then every incoming packet is sent through every outgoing link except the one it arrived on.

## Exercise

No exercises for this lesson.

## Quiz Question

数据包如何衡量距离？

## Quiz Answer

Hops
