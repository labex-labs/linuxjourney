---
index: 1
lang: "zh"
title: "什么是 DNS？"
meta_title: "什么是 DNS？ - DNS"
meta_description: "了解 DNS 是什么以及它如何将域名转换为 IP 地址。通过我们适合初学者的 Linux 指南，理解这个核心互联网概念。"
meta_keywords: "DNS, 域名系统，IP 地址，主机名，Linux 网络，初学者，教程，指南"
---

## Lesson Content

想象一下，如果每次你想在 Google 上搜索时，都必须输入 `http://192.78.12.4` 而不是 `www.google.com`。如果没有 DNS（“域名系统”），这正是会发生的情况。底层网络只理解原始 IP 地址来识别主机。DNS 允许我们人类通过名称而不是 IP 地址来跟踪网站和主机。它就像互联网的联系人列表。如果你知道一个人的名字但不知道他们的电话号码，你可以简单地在你的联系人列表中查找。

DNS 本质上是一个分布式的主机名到 IP 地址的数据库。我们管理我们的数据库，以便人们知道如何访问我们的站点/域，而在其他地方，另一个人正在管理他们的数据库，以便其他人可以访问他们的域。然后这些域能够相互通信，并构建一个庞大的互联网联系人列表。

在本课程中，我们将介绍 DNS 的一些基础知识，但请注意，DNS 是一个详尽的主题，如果你真的想深入了解它，你需要做一些额外的研究。

## Exercise

熟能生巧！以下是一些动手实验，以加强你对 DNS 和主机名解析的理解：

1. **[使用 dig 和 nslookup 在 Linux 中查询 DNS 记录](https://labex.io/zh/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup)** - 学习使用 `dig` 和 `nslookup` 等基本 Linux 工具来查询各种 DNS 记录类型，帮助你理解主机名如何解析为 IP 地址。
2. **[在 Linux 中管理本地主机名解析](https://labex.io/zh/labs/linux-manage-local-hostname-resolution-in-linux)** - 练习编辑 `/etc/hosts` 文件来管理本地主机名解析，这是控制你的 Linux 系统如何在不依赖外部 DNS 服务器的情况下解析名称的基本技能。
3. **[在 Linux 上设置本地权威 DNS 服务器](https://labex.io/zh/labs/linux-set-up-a-local-authoritative-dns-server-on-linux)** - 通过使用 `bind9` 设置和配置你自己的本地权威 DNS 服务器来获得实践经验，让你更深入地了解 DNS 区域和记录是如何管理的。

这些实验将帮助你在实际场景中应用概念，并在 Linux 环境中建立对 DNS 和主机名解析的信心。

## Quiz Question

对或错：DNS 帮助我们查找主机名的 MAC 地址？

## Quiz Answer

False
