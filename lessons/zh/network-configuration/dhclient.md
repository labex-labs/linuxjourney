---
lang: "zh"
title: "dhclient"
meta_title: "dhclient - 网络配置"
meta_description: "了解 dhclient，它如何使用 DHCP 获取 IP 地址，以及管理网络租约。理解 dhclient.conf 和 dhclient.leases 文件。Linux 初学者指南。"
meta_keywords: "dhclient, DHCP, Linux 网络，IP 地址，网络配置，Linux 教程，初学者指南"
---

## Lesson Content

我们之前讨论过 DHCP，通常你永远不需要静态设置你的 IP 地址、子网掩码等。相反，你会使用 DHCP！`dhclient` 在启动时启动，并从 `dhclient.conf` 文件获取网络接口列表。对于列出的每个接口，它尝试使用 DHCP 协议配置该接口。

在 `dhclient.leases` 文件中，`dhclient` 跟踪系统重启时的租约列表。在读取 `dhclient.conf` 后，会读取 `dhclient.leases` 文件，让它知道已经分配了哪些租约。

### To obtain a fresh IP

```bash
sudo dhclient
```

## Exercise

No exercises for this lesson.

## Quiz Question

什么尝试使用 DHCP 协议分配 IP 地址？

## Quiz Answer

dhclient
