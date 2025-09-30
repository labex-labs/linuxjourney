---
index: 7
lang: "zh"
title: "网络层"
meta_title: "网络层 - 网络基础"
meta_description: "了解 Linux 中的网络层，IP 地址如何跨子网路由数据包，以及它在数据传输中的作用。开始您的 Linux 网络之旅！"
meta_keywords: "网络层，IP 地址，子网，Linux 网络，数据包路由，初学者，教程，指南"
---

## Lesson Content

网络层决定了数据包从源主机到目标主机的路由。幸运的是，在我们的示例中，数据包只在同一网络内传输，但互联网由许多网络组成。构成互联网的这些较小的网络被称为子网。所有子网都以某种方式相互连接，这就是为什么我们能够访问 `https://www.google.com`，即使它在自己的网络上。我不会详细介绍，因为我们有一整门课程专门讲解子网，但就目前而言，关于我们的网络层，要知道 IP 地址定义了前往不同子网的规则。

在网络层，它接收来自传输层的段，并将此段封装在 IP 数据包中，然后将源主机的 IP 地址和目标主机的 IP 地址附加到数据包头。因此，此时，我们的数据包包含了它要去哪里以及它来自哪里的信息。现在它将我们的数据包发送到物理硬件层。

## Exercise

熟能生巧！以下是一些动手实验，旨在加深您对网络层、IP 寻址和子网的理解：

1. **[在 Linux 中模拟网络层连接](https://labex.io/zh/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - 练习使用 Docker 容器分配静态 IP 地址并测试同一子网内和跨不同子网的连接。
2. **[在 Linux 终端中执行 IP 子网划分和二进制转换](https://labex.io/zh/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - 直接在 Linux 终端中掌握 IP 子网划分和二进制转换，包括计算可用主机和子网。
3. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 探索各种 IP 地址类型（私有、公共、多播）并使用 `ping` 和 `ip a` 测试网络可达性。

这些实验将帮助您在实际场景中应用 IP 寻址和子网划分的概念，并增强对网络层基础知识的信心。

## Quiz Question

构成互联网的较小网络称为什么？

## Quiz Answer

subnets
