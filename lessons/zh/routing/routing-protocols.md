---
index: 4
lang: "zh"
title: "路由协议"
meta_title: "路由协议 - 路由"
meta_description: "了解距离矢量和链路状态等路由协议。理解网络收敛以及路由器如何适应变化。开始您的 Linux 网络之旅！"
meta_keywords: "路由协议，网络收敛，距离矢量，链路状态，Linux 网络，初学者指南，网络教程"
---

## Lesson Content

为网络上的每个设备手动配置路由表将是一件很痛苦的事情。相反，我们使用所谓的路由协议。路由协议帮助我们的系统适应网络变化；它们学习不同的路由，将其构建到路由表中，然后以这种方式路由我们的数据包。路由协议主要有两种类型：距离矢量协议和链路状态协议。

### 收敛

在讨论协议之前，我们应该先了解路由中使用的“收敛”一词。当使用路由协议时，路由器会与其他路由器通信，以收集和交换有关网络的信息。当它们就网络应如何呈现达成一致时，每个路由表都会映射出网络的完整拓扑，从而实现“收敛”。当网络拓扑发生变化时，收敛会暂时中断，直到所有路由器都意识到这一变化。

## Exercise

熟能生巧！以下是一些动手实验，可帮助您巩固对网络路由和 IP 寻址的理解：

1. **[在 Linux 中管理 IP 寻址](https://labex.io/zh/labs/comptia-manage-ip-addressing-in-linux-592736)** - 练习配置静态和动态 IP 地址，设置默认网关，并验证网络配置，这对于理解路由表如何构建和使用至关重要。
2. **[在 Linux 中使用 ping 和 arp 探索网络层交互](https://labex.io/zh/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - 了解设备如何在网络层进行交互，观察 ARP 以及默认网关如何处理远程流量，从而深入了解路由协议管理的机制。
3. **[在 Linux 中模拟网络层连接](https://labex.io/zh/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - 使用 Docker 模拟网络节点，分配 IP 地址，并测试跨子网的连接，直接应用与网络变化和路由决策相关的概念。

这些实验将帮助您在实际场景中应用网络配置和连接的概念，从而对路由协议自动化的基本要素建立信心。

## Quiz Question

当所有路由表都知道网络拓扑时，使用的术语是什么？

## Quiz Answer

Convergence
