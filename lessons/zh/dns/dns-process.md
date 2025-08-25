---
index: 3
lang: "zh"
title: "DNS 过程"
meta_title: "DNS 过程 - DNS"
meta_description: "了解 DNS 如何一步步工作，从根服务器到权威 DNS。为初学者和中级用户理解 DNS 查找过程。"
meta_keywords: "DNS 过程，DNS 查找，DNS 工作原理，DNS 教程，DNS 初学者，Linux DNS, TLD, 根服务器"
---

## Lesson Content

让我们看一个您的主机如何通过 DNS 找到一个域 (catzontheinterwebz.com) 的例子。本质上，我们层层深入，直到找到知道该域的 DNS 服务器。

### 本地 DNS 服务器

首先，我们的主机问道：“catzontheinterwebz.com 在哪里？”我们的本地 DNS 服务器不知道，所以它从漏斗的顶部开始，去询问根服务器。请记住，我们的主机不是直接发出这些请求来查找 catzontheinterwebz.com；大多数用户与他们的 ISP 提供的递归 DNS 服务器通信，然后该服务器负责查找 catzontheinterwebz.com 的位置。

### 根服务器

互联网有 13 个根服务器。它们在全球范围内进行镜像和分布式部署，以处理互联网的 DNS 请求，因此实际上有数百台服务器在工作。它们由不同的组织控制，并包含有关顶级域的信息。顶级域就是您所知的 .org、.com、.net 等地址。所以根服务器不知道 catzontheinterwebz.com 在哪里，但它告诉我们去询问它给我们的 IP 地址处的 .com 顶级域 DNS 服务器。

### 顶级域

所以现在我们向知道“.com”地址的名称服务器发送另一个请求，询问它是否知道 catzontheinterwebz.com 在哪里。TLD 的区域文件中没有 catzontheinterwebz.com，但它确实看到了 catzontheinterwebz.com 的名称服务器记录。所以它给我们该名称服务器的 IP 地址，并告诉我们去那里查找。

### 权威 DNS 服务器

现在我们向实际拥有我们所需记录的 DNS 服务器发送最后一个请求。该名称服务器看到它有一个 catzontheinterwebz.com 的区域文件，并且该主机有一个“www”的资源记录。然后它给我们该主机的 IP 地址，我们终于可以在互联网上看到一些猫了。

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对 DNS 解析和管理的理解：

1. **[在 Linux 中使用 dig 和 nslookup 查询 DNS 记录](https://labex.io/zh/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup)** - 学习查询 A、PTR 和 MX 等 DNS 记录，并识别您的默认 DNS 服务器，这对于网络故障排除至关重要。
2. **[在 Linux 上设置本地权威 DNS 服务器](https://labex.io/zh/labs/linux-set-up-a-local-authoritative-dns-server-on-linux)** - 通过安装和配置本地权威 DNS 服务器、定义区域和测试 DNS 解析来获得实践经验。
3. **[在 Linux 中管理本地主机名解析](https://labex.io/zh/labs/linux-manage-local-hostname-resolution-in-linux)** - 练习通过编辑 `/etc/hosts` 文件来管理本地主机名解析，这是 Web 开发和网络测试的关键技能。

这些实验将帮助您在实际场景中应用概念，并增强对 DNS 的信心。

## Quiz Question

.com、.net、.org 等地址所在的名称服务器的缩写是什么？

## Quiz Answer

TLD
