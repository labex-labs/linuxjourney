---
lesson_id: "subnetting-cheats"
course_id: "subnetting"
lang: "zh"
order_index: 4
title: "子网划分速查"
description: "学习使用简洁的二进制和块大小方法检查 IPv4 子网计算。"
meta_title: "子网划分速查 - 子网划分"
meta_description: "通过二进制转换速查掌握子网划分。学习使用 128+64+32+16+8+4+2+1 表格，快速在 IP 地址的十进制与二进制表示之间转换，适用于网络面试和认证。"
meta_keywords: "子网划分, 二进制转换, IP 地址, 网络, Linux 网络, 128+64+32+16+8+4+2+1, 十进制转二进制, 子网计算, 教程, 指南"
---

子网计算器很有用，但掌握少量二进制模式可以更容易地验证其输出。这些方法用于检查，并不能取代对真实地址分配和路由策略的确认。

## 八位组的位值

一个 IPv4 八位组使用以下位权：

```text
bit:    1   1   1   1   1  1  1  1
value: 128  64  32  16   8  4  2  1
```

八个位值相加得到 255。十进制 192 等于 `128 + 64`，因此其二进制表示是 `11000000`。

:::single-choice{#subnet-cheats-binary-192} 十进制 192 的八位二进制表示是什么？

::option[`11000000`]{#subnet-cheats-192-correct .correct explanation="128 和 64 位置设为一，其余位置为零。"}
::option[`10101000`]{#subnet-cheats-168 explanation="该模式等于 168。"}
::option[`11111111`]{#subnet-cheats-255 explanation="八个位置全部设为一等于 255。"}
:::

## 常见的不完整八位组掩码

连续前缀位会产生一个简短的掩码序列：

```text
bits set: 0    1    2    3    4    5    6    7    8
decimal:  0  128  192  224  240  248  252  254  255
```

例如，`/19` 包含 16 个完整前缀位，以及第三个八位组中的三个位，因此其掩码是 `255.255.224.0`。

:::single-choice{#subnet-cheats-prefix-19} 哪个掩码对应 IPv4 `/19`？

::option[`255.255.224.0`]{#subnet-cheats-mask-19 .correct explanation="十六个完整位再加三个位，得到 255、255 和 224。"}
::option[`255.255.19.0`]{#subnet-cheats-literal-19 explanation="前缀长度是位数，而不是十进制掩码八位组。"}
::option[`255.255.255.19`]{#subnet-cheats-tail-19 explanation="这不是连续的 19 位掩码。"}
:::

## 块大小

在掩码中第一个不等于 255 的八位组内，用 256 减去掩码值即可得到子网增量。`/27` 掩码以 224 结尾，因此块大小为 `256 - 224 = 32`。最后一个八位组的边界依次是 0、32、64、96、128、160、192 和 224。

地址 `198.51.100.77/27` 位于 64 到 95 的块中。

:::single-choice{#subnet-cheats-77-network} `198.51.100.77/27` 的网络地址是什么？

::option[`198.51.100.32`]{#subnet-cheats-network-32 explanation="该块覆盖最后一个八位组的 32 到 63。"}
::option[`198.51.100.77`]{#subnet-cheats-network-77 explanation="该地址包含主机位，并不是块边界。"}
::option[`198.51.100.64`]{#subnet-cheats-network-64 .correct explanation="从 64 开始的 /27 块覆盖 64 到 95。"}
:::

## 转换任意八位组

要转换十进制 123，应依次选择不超过剩余值的最大位权：

```text
123 = 64 + 32 + 16 + 8 + 2 + 1
    = 01111011
```

反向转换时，只需把值为一的位置对应的位权相加。在 IPv4 八位组内进行计算时，始终保留全部八个位置。

:::single-choice{#subnet-cheats-binary-123} 哪个八位值等于十进制 123？

::option[`1111011`]{#subnet-cheats-123-seven-bit explanation="数值相同，但八位组表示必须保留八个位置。"}
::option[`01111011`]{#subnet-cheats-123-correct .correct explanation="设为一的位置相加为 64 + 32 + 16 + 8 + 2 + 1。"}
::option[`01111100`]{#subnet-cheats-124 explanation="该模式设置了 4 位，而不是 2 和 1 位，结果为 124。"}
:::

## 总结

现在，你可以使用简洁的二进制模式检查常见 IPv4 计算。

1. 使用从 128 到 1 的八个八位组位权。
2. 记住连续的不完整八位组掩码序列。
3. 用 256 减去不完整掩码来求块大小。
4. 转换单个八位组时保留八位。
