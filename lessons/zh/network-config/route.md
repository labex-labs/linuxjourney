---
index: 2
lang: "zh"
title: "路由"
meta_title: "路由 - 网络配置"
meta_description: "学习管理您的 Linux 路由表。本指南涵盖使用现代的 'ip route 命令' 和传统的 'route 命令' 添加和删除网络路由。"
meta_keywords: "linux ip route 命令，linux ip 路由命令，添加路由，删除路由，路由表，网络路由，linux 网络，ip route"
---

## Lesson Content

在 Linux 中，路由表负责将网络流量导向正确的目的地。虽然我们之前讨论过查看此表，但您也可以手动添加或删除路由来控制数据包的转发方式。这对于配置复杂的网络设置或排除连接问题至关重要。

### 使用传统的 route 命令

`route` 命令是管理路由表的传统工具。虽然它仍然可用，但它被认为是遗留的，现在更推荐使用 `ip` 命令。

要添加新的网络路由，您需要指定网络地址、子网掩码和网关 (`gw`):

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

要删除路由，请使用 `del` 标志和网络地址：

```bash
sudo route del -net 192.168.2.1/23
```

### 使用 ip route 进行现代路由管理

`ip route` 命令是 Linux 中现代且功能更强大的网络配置工具。它提供了更一致和更广泛的选项集来管理网络接口和路由。使用 **linux ip route command** 是当前系统的推荐做法。

要使用 **ip route command in linux** 添加路由，您使用 `add` 操作，指定目标网络和通过网关的下一跳：

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

要删除路由，您可以使用 `delete` 操作。您可以完整指定路由，或者如果目标网络是唯一的，只需指定目标网络即可：

```bash
# 通过指定完整路由删除
ip route delete 192.168.2.1/23 via 10.11.12.3

# 或者，仅通过指定目标删除
ip route delete 192.168.2.1/23
```

掌握 `ip route` 命令是任何负责网络管理的 Linux 管理员的一项关键技能。

## Exercise

熟能生巧！以下是一些实践操作实验，以加强您对网络路由和 IP 地址的理解：

1. **[在 Linux 中管理 IP 地址](https://labex.io/zh/labs/comptia-manage-ip-addressing-in-linux-592736)** - 练习使用 `ip` 命令配置静态 IP、设置默认网关和验证网络配置。
2. **[在 Linux 中使用 ping 和 arp 探索网络层交互](https://labex.io/zh/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - 了解默认网关如何处理远程流量并观察网络层交互。

这些实验将帮助您在实际场景中应用 IP 寻址和路由的概念，并增强您对 Linux 网络操作的信心。

## Quiz Question

When using the legacy `route` command, what is the flag used to delete a route? Please answer in English, paying attention to case.

## Quiz Answer

del
