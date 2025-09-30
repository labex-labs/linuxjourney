---
index: 6
lang: "zh"
title: "DNS 工具"
meta_title: "DNS 工具 - DNS"
meta_description: "学习 nslookup 和 dig 命令，用于 Linux 上的 DNS 查询和故障排除。通过我们为初学者提供的指南，了解如何使用这些基本的 DNS 工具。"
meta_keywords: "nslookup, dig 命令，DNS 工具，Linux DNS, DNS 故障排除，Linux 教程，Linux 初学者"
---

## Lesson Content

### nslookup

“名称服务器查找”工具用于查询名称服务器以查找有关资源记录的信息。让我们查找 google.com 的名称服务器在哪里：

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### dig

Dig (domain information groper) 是一个强大的工具，用于获取有关 DNS 名称服务器的信息。它比 nslookup 更灵活，非常适合排查 DNS 问题。

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

## Exercise

熟能生巧！这是一个动手实验，旨在巩固您对网络接口设置的理解：

1. **[使用 Linux 中的 ethtool 检查网络接口设置](https://labex.io/zh/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - 学习使用 `ethtool` 命令检查和管理网络接口设置，包括查看和设置接口速度和双工模式，以及分析链路模式以排除物理层网络问题。

本实验将帮助您在实际场景中应用这些概念，并增强管理网络接口的信心。

## Quiz Question

什么工具用于获取有关 DNS 名称服务器的详细信息？

## Quiz Answer

dig
