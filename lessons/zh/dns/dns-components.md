---
index: 2
lang: "zh"
title: "DNS 组件"
meta_title: "DNS 组件 - DNS"
meta_description: "了解 DNS 组件：域名服务器、区域文件和资源记录。了解 DNS 如何为初学者工作。开始您的 Linux 网络之旅！"
meta_keywords: "DNS 组件，域名服务器，区域文件，资源记录，DNS 教程，Linux 网络，初学者指南"
---

## Lesson Content

互联网的 DNS 数据库依赖于站点和组织提供部分数据库。为此，它们需要：

### 域名服务器

我们通过“域名服务器”设置 DNS。域名服务器加载我们的 DNS 设置和配置，并回答来自客户端或其他服务器的任何问题，例如“google.com 是谁？”。如果域名服务器不知道该查询的答案，它会将请求重定向到其他域名服务器。域名服务器可以是“权威的”，这意味着它们持有您正在寻找的实际 DNS 记录，也可以是“递归的”，这意味着它们会询问其他服务器，而这些服务器会询问其他服务器，直到它们找到包含 DNS 记录的权威服务器。递归服务器也可以缓存我们想要的信息，而不是到达权威服务器。

### 区域文件

域名服务器内部有一个叫做区域文件的东西。区域文件是域名服务器存储域信息或在不知道域的情况下如何到达域的方式。

### 资源记录

区域文件由资源记录条目组成。每行都是一条记录，包含有关主机、域名服务器、其他资源等的信息。字段包括：

- 记录名称
- TTL - 我们丢弃记录并获取新记录的时间。在 DNS 中，TTL 以时间表示，因此记录的 TTL 可以为一小时。我们这样做是因为互联网在不断变化；前一分钟主机可以映射到 X IP 地址，下一分钟它可以映射到 Y IP 地址。
- Class - 记录信息的命名空间。最常见的是，IN 用于 Internet。
- Type - 记录数据中存储的信息类型。我们不会深入探讨记录类型，但您可能见过常见的类型，例如用于地址的 A、用于邮件交换器的 MX 等。
- Data - 此字段可以包含 IP 地址（如果是 A 记录）或根据记录类型包含其他内容。

```plaintext
patty    IN  A      192.168.0.4
```

## Exercise

熟能生巧！以下是一些动手实验，可帮助您加深对 DNS 和主机名解析的理解：

1. **[在 Linux 上设置本地权威 DNS 服务器](https://labex.io/zh/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803-592803)** - 练习安装和配置本地 DNS 服务器 (`bind9`)，定义区域，并验证您的设置。
2. **[使用 dig 和 nslookup 在 Linux 中查询 DNS 记录](https://labex.io/zh/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - 学习使用基本命令行工具 (`dig`, `nslookup`) 查询各种 DNS 记录类型并排除 DNS 问题。
3. **[在 Linux 中管理本地主机名解析](https://labex.io/zh/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - 了解如何通过编辑 `/etc/hosts` 文件来管理本地主机名解析，这是开发和测试的关键技能。

这些实验将帮助您在实际场景中应用 DNS 和主机名解析的概念，并增强您对网络服务的信心。

## Quiz Question

邮件交换器使用哪种资源记录类型？

## Quiz Answer

MX
