---
index: 1
lang: "zh"
title: "什么是 DNS？"
meta_title: "什么是 DNS？- DNS"
meta_description: "如果你想学习 Linux 网络知识，理解 DNS 至关重要。本指南解释了什么是域名系统 (DNS)，它如何将域名翻译成 IP 地址，以及为什么它是互联网的基本地址簿。对于任何想学习 Linux 的人来说，这是一个完美的起点。"
meta_keywords: "DNS, 域名系统，IP 地址，学习 Linux, Linux 学习，主机名，Linux 网络，初学者，教程，指南，labex linux"
---

## Lesson Content

### 互联网的电话簿

想象一下，如果每次你想访问谷歌时，都必须输入 `http://192.78.12.4` 而不是 `www.google.com`。没有域名系统（DNS），互联网就会是这个样子。底层网络协议只能识别数字 IP 地址来标识主机。DNS 允许我们人类使用易于记忆的名称来代替一长串数字来访问网站和服务器。把它想象成互联网的联系人列表：你查找一个名称以找到相应的数字。

### DNS 的工作原理

从本质上讲，DNS 将人类可读的主机名（如 `www.google.com`）转换为机器可读的 IP 地址（如 `192.78.12.4`）。这个过程称为解析。当你在浏览器中输入域名时，你的计算机向 DNS 服务器发送一个查询，该服务器查找正确的 IP 地址并将其发送回来，从而允许你的浏览器连接到网站的服务器。

### 分布式全球系统

DNS 不是一个单一的中央数据库。相反，它是一个庞大、分布式的系统。网站所有者管理自己的 DNS 记录，以告知世界如何找到他们的域名。这些单独的域相互通信，形成了覆盖整个互联网的庞大互联目录。这种去中心化的结构使系统具有极强的弹性和可扩展性。

### 为什么你应该学习 Linux DNS

如果你想学习 **Linux** 用于系统管理或 Web 开发，了解 DNS 至关重要。配置、管理和排除 DNS 故障的能力是一项基本技能。本课程将介绍基础知识，但请注意，DNS 是一个深入而复杂的主题。要真正掌握它，你需要进行额外的研究和练习。这是你开始 **linux learn** 之旅的绝佳第一步。

## Exercise

熟能生巧！以下是一些实践实验，以加强你对 DNS 和主机名解析的理解。使用 **labex linux 终端** 进行这些练习是获得实践经验的好方法。

1. **[使用 dig 和 nslookup 在 Linux 中查询 DNS 记录](https://labex.io/zh/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - 学习使用 `dig` 和 `nslookup` 等基本的 Linux 工具来查询各种 DNS 记录类型，帮助你了解主机名是如何解析为 IP 地址的。
2. **[在 Linux 中管理本地主机名解析](https://labex.io/zh/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - 练习编辑 `/etc/hosts` 文件以管理本地主机名解析，这是一项基本技能，用于控制 Linux 系统如何在不依赖外部 DNS 服务器的情况下解析名称。
3. **[在 Linux 上设置本地权威 DNS 服务器](https://labex.io/zh/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - 通过使用 `bind9` 设置和配置你自己的本地权威 DNS 服务器来获得实践经验，使你能够深入了解 DNS 区域和记录的管理方式。

这些实验将帮助你在真实场景中应用这些概念，并在 Linux 环境中建立对 DNS 和主机名解析的信心。

## Quiz Question

True or false: DNS helps us find MAC addresses for hostnames?

## Quiz Answer

False
