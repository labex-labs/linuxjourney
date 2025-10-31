---
index: 7
lang: "zh"
title: "网络层"
meta_title: "网络层 - 网络基础知识"
meta_description: "探索 Linux 网络中的网络层。本指南解释了 IP 地址和子网如何实现数据包路由，以实现在网络间的数据传输。"
meta_keywords: "网络层，IP 地址，子网，Linux 网络，数据包路由，数据传输，OSI 模型，IP 数据包"
---

## Lesson Content

网络层负责将数据包从源主机逻辑寻址并路由到目标主机。虽然数据包有时可能在单个本地网络内传输，但互联网是由相互连接的网络的巨大集合构成的。

### 数据包路由的作用

网络层的首要功能是确定数据传输的最佳路径。这个过程被称为**数据包路由**，它确保信息能够高效地到达预定目的地，即使它需要跨越多个网络边界。在 **Linux 网络**中，这一层是所有互联网通信的基础。

### 理解子网和 IP 地址

构成互联网的较小网络称为**子网**。所有子网都是相互连接的，这使得一个网络上的设备能够与另一个网络上的设备通信，例如访问像 `google.com` 这样的网站。在这些不同子网之间传输的规则由**IP 地址**定义。IP 地址为网络上的设备提供唯一的标识符，就像房子的街道地址一样。

### 网络层的封装

在网络层，从传输层接收到的数据段被封装成一个称为 IP 数据包的新单元。在此过程中，会向数据包添加一个头部，其中包含源 IP 地址（数据包来自哪里）和目标 IP 地址（数据包要去哪里）。附带了这些关键的寻址信息后，数据包就具备了旅程所需的一切，然后被传递到数据链路层，准备进行物理传输。

## Exercise

实践造就完美！以下是一些旨在巩固您对网络层、IP 寻址和子网理解的动手实验：

1. **[在 Linux 中模拟网络层连接](https://labex.io/zh/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - 练习使用 Docker 容器在子网内部和跨子网分配静态 IP 地址并测试连通性。
2. **[在 Linux 终端中执行 IP 子网划分和二进制转换](https://labex.io/zh/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - 直接在 Linux 终端中掌握 IP 子网划分和二进制转换，包括计算可用主机和子网。
3. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 探索各种 IP 地址类型（私有、公共、多播），并使用 `ping` 和 `ip a` 测试网络可达性。

这些实验将帮助您在实际场景中应用 IP 寻址和子网划分的概念，并增强对网络层基础知识的信心。

## Quiz Question

构成互联网的较小网络称为？请用一个单独的小写英文字词回答。

## Quiz Answer

subnets
