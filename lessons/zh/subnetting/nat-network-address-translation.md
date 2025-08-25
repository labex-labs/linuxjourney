---
index: 6
lang: "zh"
title: "NAT"
meta_title: "NAT - 子网划分"
meta_description: "了解 Linux 中的 NAT（网络地址转换）、其工作原理及其在网络安全中的作用。理解私有 IP 与公共 IP。Linux 网络指南。"
meta_keywords: "NAT, 网络地址转换，Linux 网络，私有 IP, 公共 IP, Linux 教程，初学者指南"
---

## Lesson Content

我们之前提到过 NAT（网络地址转换），但没有深入探讨。当我们在网络上工作时，这是否意味着互联网可以看到我们的 IP 地址？不完全是。

NAT 使像我们的路由器这样的设备充当互联网和私有网络之间的中介。因此，只需要一个唯一的 IP 地址就可以代表一整组计算机。

将 NAT 想象成一个大型办公室的接待员。如果有人想联系你，他们只知道整个办公室的电话号码。接待员会查找你的分机号码并将电话转接给你。

### 它是如何工作的？

一个简单的例子是这样的：

1. Patty 想要连接到 `www.google.com`，所以她的机器通过路由器发送这个请求。
2. 路由器接收该请求并打开自己与 google.com 的连接，然后一旦建立连接，它就发送 Patty 的请求。
3. 路由器是 Patty 和 `www.google.com` 之间的中介。Google 不知道 Patty；相反，它只能看到路由器。

NAT 和一般的包路由可能会变得相当复杂，但我们不会深入探讨细节。

## Exercise

熟能生巧！这里有一些动手实验，以加强你对网络寻址和连接的理解，这些是理解 NAT 等概念的基础：

1. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - 练习使用 `ip a` 命令在 Linux 系统上识别网络寻址信息，包括 IPv4 和 IPv6 地址。
2. **[在 Linux 中管理 IP 寻址](https://labex.io/zh/labs/linux-manage-ip-addressing-in-linux-592736)** - 学习通过配置静态和动态 IP 以及验证网络配置来管理 IP 寻址，这有助于理解设备如何获取其地址。
3. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - 探索不同的 IP 地址类型（私有、公共、多播）并测试网络可达性，为 NAT 如何区分内部和外部地址提供实际背景。

这些实验将帮助你在实际场景中应用这些概念，并增强在 Linux 中进行网络配置和故障排除的信心。

## Quiz Question

什么用于将单个私有地址表示给互联网？

## Quiz Answer

NAT
