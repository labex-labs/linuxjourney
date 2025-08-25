---
index: 5
lang: "zh"
title: "数据包分析"
meta_title: "数据包分析 - 故障排除"
meta_description: "使用 tcpdump 学习数据包分析基础知识。通过这份适合初学者的 Linux 指南，了解网络流量、捕获数据并解释输出。"
meta_keywords: "tcpdump, 数据包分析，网络分析，Linux 网络，初学者教程，Wireshark, Linux 命令，网络流量"
---

## Lesson Content

数据包分析的主题本身就可以构成一门完整的课程，并且有许多专门关于数据包分析的书籍。然而，今天我们只学习基础知识。有两种极其流行的数据包分析器：Wireshark 和 tcpdump。这些工具扫描您的网络接口，捕获数据包活动，解析数据包，并输出信息供我们查看。它们使我们能够深入进行网络分析，并探究底层细节。我们将使用 tcpdump，因为它具有更简单的界面；但是，如果您想将数据包分析作为您的工具，我建议您研究 Wireshark。

### 安装 tcpdump

```bash
sudo apt install tcpdump
```

### 在接口上捕获数据包数据

```plaintext
pete@icebox:~$ sudo tcpdump -i wlan0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on wlan0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
11:28:24.960464 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 3, length 64
11:28:24.979299 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 3, length 64
11:28:25.961869 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 4, length 64
11:28:25.976176 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 4, length 64
11:28:26.963667 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 5, length 64
11:28:26.976137 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 5, length 64
11:28:30.674953 ARP, Request who-has 172.254.1.0 tell ThePickleParty.lan, length 28
11:28:31.190665 IP ThePickleParty.lan.51056 > 192.168.86.255.rfe: UDP, length 306
```

当您运行数据包捕获时，您会注意到很多事情发生。这是意料之中的；后台有很多网络活动。在我的上述示例中，我只截取了捕获的一部分，特别是我决定 ping `www.google.com` 的时间。

### 理解输出

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
```

- 第一个字段是网络活动的时间戳。
- IP：这包含协议信息。
- 接下来，您将看到源地址和目标地址：`icebox.lan > nuq04s29-in-f4.1e100.net`。
- `seq`：这是 TCP 数据包的起始和结束序列号。
- `length`：长度（字节）。

从我们的 tcpdump 输出中可以看出，我们正在向 `www.google.com` 发送一个 ICMP 回显请求数据包，并收到一个 ICMP 回显回复数据包！另外，请注意，不同的数据包会输出不同的信息；请参阅手册页以了解这些信息。

### 将 tcpdump 输出写入文件

```bash
sudo tcpdump -w /some/file
```

最后一些想法：我们只是触及了数据包分析主题的皮毛。您可以查看的内容太多了，我们甚至还没有深入探讨十六进制和 ASCII 输出。网上有很多资源可以帮助您了解更多关于数据包分析器的信息，我强烈建议您去寻找它们！

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对数据包分析的理解：

1. **[在 Linux 中使用 tcpdump 分析以太网帧](https://labex.io/zh/labs/linux-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - 练习捕获和检查以太网帧，生成流量，并使用 `tcpdump` 分析帧头和 MAC 地址。

本实验将帮助您在实际场景中应用数据包分析的概念，并增强网络故障排除的信心。

## Quiz Question

使用 tcpdump 捕获特定接口的标志是什么？

## Quiz Answer

-i
