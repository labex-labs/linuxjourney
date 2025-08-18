---
index: 2
lang: "zh"
title: "DNS 组件"
meta_title: "DNS 组件 - DNS"
meta_description: "了解 DNS 组件：名称服务器、区域文件和资源记录。了解 DNS 如何为初学者工作。开始您的 Linux 网络之旅！"
meta_keywords: "DNS 组件，名称服务器，区域文件，资源记录，DNS 教程，Linux 网络，初学者指南"
---

## Lesson Content

互联网的 DNS 数据库依赖于站点和组织提供部分数据库。为此，它们需要：

### Name Server

我们通过“name servers”设置 DNS。名称服务器加载我们的 DNS 设置和配置，并回答来自客户端或其他服务器的任何问题，例如“google.com 是谁？”。如果名称服务器不知道该查询的答案，它会将请求重定向到其他名称服务器。名称服务器可以是“authoritative”（权威的），这意味着它们持有您正在查找的实际 DNS 记录，也可以是“recursive”（递归的），这意味着它们会询问其他服务器，而这些服务器又会询问其他服务器，直到找到包含 DNS 记录的权威服务器。递归服务器也可以缓存我们想要的信息，而不是每次都访问权威服务器。

### Zone File

名称服务器内部存在一种叫做区域文件（zone files）的东西。区域文件是名称服务器存储有关域的信息或在不知道域的情况下如何获取域信息的方式。

### Resource Records

区域文件由资源记录（resource records）条目组成。每行都是一条记录，包含有关主机、名称服务器、其他资源等的信息。字段包括以下内容：

- Record name
- TTL - 我们丢弃记录并获取新记录的时间。在 DNS 中，TTL 以时间表示，因此记录的 TTL 可以是一小时。我们这样做是因为互联网不断变化；一分钟前，一个主机可能映射到 X IP 地址，下一分钟它可能在 Y IP 地址。
- Class - 记录信息的命名空间。最常见的是，IN 用于 Internet。
- Type - 记录数据中存储的信息类型。我们不会深入探讨记录类型，但您可能已经见过常见的类型，例如用于地址的 A 记录，用于邮件交换器的 MX 记录等。
- Data - 如果是 A 记录，此字段可以包含 IP 地址，或者根据记录类型包含其他内容。

```plaintext
patty    IN  A      192.168.0.4
```

## Exercise

本课程没有练习。

## Quiz Question

用于邮件交换器的资源记录类型是什么？

## Quiz Answer

MX
