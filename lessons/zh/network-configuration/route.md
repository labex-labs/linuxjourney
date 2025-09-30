---
index: 2
lang: "zh"
title: "route"
meta_title: "route - 网络配置"
meta_description: "学习如何使用 Linux 的 route 和 ip 命令添加和删除网络路由。了解面向初学者和中级用户的路由表管理。"
meta_keywords: "route 命令，ip route, 添加路由，删除路由，Linux 网络，路由表，Linux 教程，初学者指南"
---

## Lesson Content

我们已经讨论过使用 `route` 命令查看路由表。如果您想手动添加或删除路由，可以这样做。

### 添加新路由

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### 删除路由

```bash
sudo route del -net 192.168.2.1/23
```

您也可以使用 **ip** 命令执行这些更改：

### 添加路由

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### 删除路由

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

熟能生巧！这里有一些动手实验，以加强您对网络路由和 IP 地址的理解：

1. **[在 Linux 中管理 IP 地址](https://labex.io/zh/labs/comptia-manage-ip-addressing-in-linux-592736)** - 练习配置静态 IP、设置默认网关以及使用 `ip` 命令验证网络配置。
2. **[在 Linux 中使用 ping 和 arp 探索网络层交互](https://labex.io/zh/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - 了解默认网关如何处理远程流量并观察网络层交互。

这些实验将帮助您在实际场景中应用 IP 地址和路由的概念，并增强您对 Linux 网络的信心。

## Quiz Question

删除路由的命令标志是什么？

## Quiz Answer

del
