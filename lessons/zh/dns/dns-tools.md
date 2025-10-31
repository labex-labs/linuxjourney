---
index: 6
lang: "zh"
title: "DNS 工具"
meta_title: "DNS 工具 - DNS 查询与排错"
meta_description: "探索 nslookup 和强大的 dig 命令等必备的 Linux DNS 工具。本面向初学者的 Linux 教程涵盖 DNS 查询和 DNS 故障排除技术。"
meta_keywords: "nslookup, dig 命令，DNS 工具，Linux DNS, DNS 故障排除，名称服务器查询，Linux 教程，初学者 Linux"
---

## Lesson Content

在 Linux 中，有几种命令行实用程序可用于网络诊断。当涉及到域名系统 (DNS) 问题时，两个主要的**DNS 工具**脱颖而出：`nslookup` 和 `dig`。了解如何使用它们对于在 **Linux DNS** 服务器或客户端上进行任何**DNS 故障排除**至关重要。

### 使用 nslookup 进行基本 DNS 查询

`nslookup`（名称服务器查找）工具是一个经典的实用程序，用于查询 DNS 服务器以获取域名或 IP 地址映射信息。尽管它有时被认为已过时，不如 `dig` 强大，但它仍然是一个用于简单查找的快速简便的工具。

要查找像 `www.google.com` 这样的域的 IP 地址，您可以运行：

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

在此输出中，`Server` 和 `Address` 显示了回答查询的 DNS 服务器。`Non-authoritative answer`（非权威应答）意味着服务器提供了缓存的结果，而不是直接查询权威源。`Name` 和 `Address` 显示了该域解析出的 IP 地址。

### 使用 dig 进行高级 DNS 故障排除

`dig`（域名信息搜寻器）命令是一个强大而灵活的工具，用于查询 DNS 名称服务器。它提供比 `nslookup` 更详细的信息，使其成为进行严肃**DNS 故障排除**的首选工具。

以下是使用 **dig 命令**的一个示例：

```bash
pete@icebox:~$ dig www.google.com

; <<>> DiG 9.9.5-3-Ubuntu <<>> www.google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42376
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0005 , udp: 512
;; QUESTION SECTION:
;www.google.com.                        IN      A

;; ANSWER SECTION:
www.google.com.         5       IN      A       74.125.239.147
www.google.com.         5       IN      A       74.125.239.144
www.google.com.         5       IN      A       74.125.239.146
www.google.com.         5       IN      A       74.125.239.145
www.google.com.         5       IN      A       74.125.239.148

;; Query time: 27 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Feb 07 10:14:00 PST 2016
;; MSG SIZE  rcvd: 123
```

`dig` 的输出组织成几个部分：

- **QUESTION SECTION**（问题部分）：显示发送的查询。在这里，我们查询了 `www.google.com` 的 `A`（地址）记录。
- **ANSWER SECTION**（答案部分）：显示从 DNS 服务器收到的答案。在这种情况下，Google 的域关联了多个 IP 地址。
- **Statistics**（统计信息）：最后一部分提供了有关查询的元数据，例如查询时间和响应服务器。

由于其详细的输出和灵活性，`dig` 是任何在 Linux 上管理或排除网络服务故障的人不可或缺的实用程序。

## Exercise

为了获得更多使用 Linux 网络实用程序的经验，请考虑尝试以下实践实验：

1. **[在 Linux 中使用 ethtool 检查网络接口设置](https://labex.io/zh/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - 学习使用 `ethtool` 命令来检查和管理网络接口设置，包括查看和设置接口速度和双工模式，以及分析链路模式以排除物理层网络问题。

此实验将帮助您在实际场景中应用这些概念，并增强管理网络接口的信心。

## Quiz Question

哪个工具用于获取有关 DNS 名称服务器的详细信息？请仅使用小写英文字母回答。

## Quiz Answer

dig
