---
lang: "zh"
title: "udev"
description: "了解 udev，它如何动态管理 Linux 设备文件，并使用 udevadm。理解初学者的设备节点创建。"
keywords: "udev, udevadm, Linux 设备管理，设备文件，Linux 教程，Linux 初学者，udev 规则，Linux 指南"
---

## Lesson Content

在过去，如果你真的想，你可以使用以下命令创建设备节点：

```bash
mknod /dev/sdb1 b 8 3
```

此命令将创建一个设备节点 `/dev/sdb1`，并将其设为块设备 (b)，主设备号为 8，次设备号为 3。

要删除设备，你只需在 `/dev` 目录中 **rm** 该设备文件。

幸运的是，由于 udev，我们现在真的不需要再这样做。udev 系统会根据设备是否连接，为我们动态创建和删除设备文件。系统上运行着一个 `udevd` 守护进程，它监听来自内核的关于连接到系统的设备的消息。`Udevd` 将解析这些信息，并将数据与 `/etc/udev/rules.d` 中指定的规则进行匹配。根据这些规则，它很可能会为设备创建设备节点和符号链接。你可以编写自己的 udev 规则，但这超出了本课程的范围。幸运的是，你的系统已经附带了许多 udev 规则，所以你可能永远不需要编写自己的规则。

你还可以使用 **udevadm** 命令查看 udev 数据库和 sysfs。这个工具非常有用，但有时会变得非常复杂。一个查看设备信息的简单命令是：

```bash
udevadm info --query=all --name=/dev/sda
```

## Exercise

运行给定的 `udevadm` 命令并查看输出。

## Quiz Question

什么动态地添加和移除设备？

## Quiz Answer

udev
