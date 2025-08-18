---
lang: "zh"
title: "路由"
meta_title: "路由 - 网络配置"
meta_description: "学习如何使用 Linux 的 route 和 ip 命令添加和删除网络路由。了解初学者和中级用户的路由表管理。"
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

本课程没有练习，但您可以在手册页中阅读更多关于此处讨论的命令的信息。

```bash
man route
```

```bash
man ip-route
```

## Quiz Question

删除路由的命令标志是什么？

## Quiz Answer

del
