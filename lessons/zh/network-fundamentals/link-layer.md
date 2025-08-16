---
lang: "zh"
title: "链路层"
description: "了解 TCP/IP 中的链路层、ARP 如何解析 MAC 地址以及数据包遍历。通过此 Linux 网络教程了解网络基础知识。"
keywords: "链路层，ARP, TCP/IP, MAC 地址，网络基础知识，Linux 网络，初学者，教程"
---

## Lesson Content

TCP/IP 模型的底部是链路层。这一层是硬件特定的。

在链路层，我们的数据包再次被封装成一个称为帧的东西。帧头附加了我们主机的源和目的 MAC 地址、校验和以及数据包分隔符，以便接收方能够判断数据包何时结束。

幸运的是，我们处于同一个网络中，所以我们的数据包不必传输太远。首先，链路层将我的源 MAC 地址附加到帧头，但它也需要知道 Patty 的 MAC 地址。它怎么知道呢，既然 Patty 不在互联网上，我怎么找到它呢？我们使用 ARP！

### ARP (Address Resolution Protocol)

ARP 查找与 IP 地址关联的 MAC 地址。ARP 在同一网络内使用。如果 Patty 不在同一个网络中，我们将使用路由系统来确定接收数据包的下一个路由器，一旦我们在同一个网络中，我们就可以使用 ARP。

一旦我们在同一个网络中，系统首先会使用 ARP 查找表，该表存储了哪些 IP 地址与哪些 MAC 地址关联的信息。如果值不存在，则使用 ARP。然后系统将使用 ARP 协议向网络发送广播消息，以查找哪个主机拥有 IP 10.10.1.4。广播消息是一种特殊消息，发送给网络上的所有主机（恰如其名，用于发送广播）。任何具有请求 IP 地址的机器都将回复一个包含 IP 地址和 MAC 地址的 ARP 数据包。

现在我们拥有了所有必要的数据——IP 地址和 MAC 地址——我们的链路层通过我们的网络接口卡将此帧转发到下一个设备，并找到 Patty 的网络。这一步比我刚才解释的要复杂一些，但我们将在路由课程中讨论更多细节。

就是这样：一个简单（或不那么简单）的数据包在 TCP/IP 层中的遍历。请记住，数据包不会像这样单向传输。我们甚至还没有到达 Patty 的网络呢！在网络中传输时，在发送或接收任何数据之前，需要至少两次通过 TCP/IP 模型。实际上，这个数据包的样子会是这样的：

### Packet Traversal

1. Pete sends Patty an email: this data gets sent to the transport layer.
2. The transport layer encapsulates the data into a TCP or UDP header to form a segment. The segment attaches the destination and source TCP or UDP port, then the segment is sent to the network layer.
3. The network layer encapsulates the TCP segment inside an IP packet; it attaches the source and destination IP address. Then it routes the packet to the link layer.
4. The packet then reaches Pete's physical hardware and gets encapsulated in a frame. The source and destination MAC addresses get added to the frame.
5. Patty receives this data frame through her physical layer and checks each frame for data integrity, then de-encapsulates the frame contents and sends the IP packet to the network layer.
6. The network layer reads the packet to find the source and destination IP that was previously attached. It checks if its IP is the same as the destination IP, which it is! It de-encapsulates the packet and sends the segment to the transport layer.
7. The transport layer de-encapsulates the segments, checks the TCP or UDP port numbers, and makes a connection to the application layer based on those port numbers.
8. The application layer receives the data from the transport layer on the port that was specified and presents it to Patty in the form of the final email message.

## Exercise

No exercises for this lesson.

## Quiz Question

在同一网络中查找 MAC 地址使用什么？

## Quiz Answer

ARP
