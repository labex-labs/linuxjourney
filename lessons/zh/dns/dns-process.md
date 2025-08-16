---
title: "DNS 过程"
description: "逐步了解 DNS 的工作原理，从根服务器到权威 DNS。帮助初学者和中级用户理解 DNS 查找过程。"
keywords: "DNS 过程，DNS 查找，DNS 工作原理，DNS 教程，DNS 初学者，Linux DNS, TLD, 根服务器"
---

## Lesson Content

让我们看看您的主机如何通过 DNS 找到一个域 (catzontheinterwebz.com) 的示例。本质上，我们层层深入，直到找到知道该域的 DNS 服务器。

### 本地 DNS 服务器

首先，我们的主机问道：“catzontheinterwebz.com 在哪里？”我们的本地 DNS 服务器不知道，所以它从漏斗的顶部开始，向根服务器询问。请记住，我们的主机不是直接发出这些请求来查找 catzontheinterwebz.com；大多数用户与他们的 ISP 提供的递归 DNS 服务器通信，然后该服务器负责查找 catzontheinterwebz.com 的位置。

### 根服务器

互联网有 13 个根服务器。它们在全球范围内镜像和分发，以处理互联网的 DNS 请求，因此实际上有数百台服务器在工作。它们由不同的组织控制，并包含有关顶级域的信息。顶级域就是您所知的 .org、.com、.net 等地址。所以根服务器不知道 catzontheinterwebz.com 在哪里，但它告诉我们向它给出的 IP 地址的 .com 顶级域 DNS 服务器询问。

### 顶级域

所以现在我们向知道“.com”地址的名称服务器发送另一个请求，询问它是否知道 catzontheinterwebz.com 在哪里。TLD 的区域文件中没有 catzontheinterwebz.com，但它确实看到了 catzontheinterwebz.com 的名称服务器记录。所以它给了我们该名称服务器的 IP 地址，并告诉我们去那里查找。

### 权威 DNS 服务器

现在我们向实际拥有我们所需记录的 DNS 服务器发送最终请求。该名称服务器看到它有一个 catzontheinterwebz.com 的区域文件，并且该主机有一个“www”的资源记录。然后它给了我们该主机的 IP 地址，我们终于可以在互联网上看到一些猫了。

## Exercise

No exercises for this lesson.

## Quiz Question

.com、.net、.org 等地址所在的名称服务器的缩写是什么？

## Quiz Answer

TLD
