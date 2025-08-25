---
index: 3
lang: "zh"
title: "dhclient"
meta_title: "dhclient - 网络配置"
meta_description: "了解 dhclient、它如何使用 DHCP 获取 IP 地址以及管理网络租约。理解 dhclient.conf 和 dhclient.leases 文件。Linux 初学者指南。"
meta_keywords: "dhclient, DHCP, Linux 网络，IP 地址，网络配置，Linux 教程，初学者指南"
---

## Lesson Content

我们之前讨论过 DHCP，大多数情况下你永远不需要静态设置你的 IP 地址、子网掩码等。相反，你将使用 DHCP！`dhclient` 在启动时启动，并从 `dhclient.conf` 文件中获取网络接口列表。对于列出的每个接口，它尝试使用 DHCP 协议配置该接口。

在 `dhclient.leases` 文件中，`dhclient` 跟踪系统重启时租约的列表。读取 `dhclient.conf` 后，会读取 `dhclient.leases` 文件，以便它知道已经分配了哪些租约。

### 获取新的 IP

```bash
sudo dhclient
```

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对动态 IP 寻址和网络配置的理解：

1. **[在 Linux 中管理 IP 寻址](https://labex.io/zh/labs/linux-manage-ip-addressing-in-linux-592736)** - 练习使用 `dhclient` 获取动态 IP 地址并在真实的 Linux 环境中验证网络配置。
2. **[在 Linux 中识别 MAC 和 IP 地址](https://labex.io/zh/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - 学习检查网络接口并识别 MAC 和 IP 地址，这对于理解 DHCP 如何分配地址至关重要。
3. **[在 Linux 中探索 IP 地址类型和可达性](https://labex.io/zh/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - 测试网络可达性并探索不同的 IP 地址类型，从而加深您对 IP 地址在网络中如何运作的理解。

这些实验将帮助您在实际场景中应用 DHCP 和 IP 寻址的概念，并增强您在 Linux 中进行网络配置的信心。

## Quiz Question

什么尝试使用 DHCP 协议分配 IP 地址？

## Quiz Answer

dhclient
