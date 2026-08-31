---
lesson_id: "subnet-math"
course_id: "subnetting"
lang: "zh"
order_index: 3
title: "子网计算"
description: "学习如何根据前缀计算 IPv4 网络地址、广播地址、范围和地址数量。"
meta_title: "子网计算 - 子网划分"
meta_description: "掌握子网计算基础。本指南介绍如何通过子网掩码计算网络中的可用主机数量，并讲解 Linux 网络所需的 IP 寻址和二进制概念。"
meta_keywords: "子网计算, 子网掩码计算, IP 地址, 子网掩码, 网络主机, 二进制, Linux 网络, 主机数量计算, 初学者教程"
---

子网计算会将前缀长度应用到 IPv4 地址的 32 位。使用二进制推理，可以避免在不与十进制八位组对齐的前缀边界上出错。

## 查找网络地址

以地址 `192.168.1.165/24` 为例：

```text
address  11000000.10101000.00000001.10100101
mask     11111111.11111111.11111111.00000000
network  11000000.10101000.00000001.00000000
```

按位与会保留掩码为一处的地址位，并清除主机位。结果为 `192.168.1.0/24`。

:::single-choice{#subnet-math-network-operation}
使用地址和掩码计算 IPv4 网络地址时应采用哪种运算？

::option[十进制字符串拼接。]{#subnet-math-concatenation explanation="连接打印出的八位组不会应用前缀位。"}
::option[传输端口减法。]{#subnet-math-port-subtraction explanation="端口与网络前缀无关。"}
::option[按位与。]{#subnet-math-bitwise-and .correct explanation="网络位会保留，而掩码中零所对应的主机位置会被清除。"}
:::

## 计算地址数量

对于前缀 `/p`，主机部分包含 `32 - p` 位。总地址数量为：

```text
2^(32 - p)
```

因此，`/24` 包含 `2^8 = 256` 个地址。在传统广播子网中，全零主机值是网络地址，全一主机值是定向广播地址，剩下 254 个普通单播主机地址。

:::single-choice{#subnet-math-24-total}
IPv4 `/24` 中共有多少个地址？

::option[24]{#subnet-math-total-24 explanation="前缀长度统计的是网络位，而不是地址数。"}
::option[256]{#subnet-math-total-256 .correct explanation="八个主机位产生 2^8 个不同地址值。"}
::option[254]{#subnet-math-total-254 explanation="这是减去两个特殊地址后的传统可用主机数，而不是总数。"}
:::

## 查找块边界

对于 `/26`，掩码为 `255.255.255.192`。最后一个八位组的块大小为 `256 - 192 = 64`，因此子网边界是 0、64、128 和 192。地址 `192.168.1.165/26` 位于：

```text
network:   192.168.1.128
broadcast: 192.168.1.191
range:     192.168.1.129 through 192.168.1.190
```

:::single-choice{#subnet-math-165-network}
`192.168.1.165/26` 的网络地址是什么？

::option[`192.168.1.0`]{#subnet-math-network-zero explanation="这是第一个 /26 块，覆盖 0 到 63。"}
::option[`192.168.1.165`]{#subnet-math-network-self explanation="给定地址在 /26 内包含非零主机位。"}
::option[`192.168.1.128`]{#subnet-math-network-128 .correct explanation="165 位于 128 到 191 的地址块中。"}
:::

## 考虑前缀例外

`2^host_bits - 2` 这一快捷公式并非普遍适用。IPv4 `/31` 前缀专门用于点对点链路，两个地址都可作为端点，不需要定向广播。`/32` 标识一条主机路由或一个接口地址。哪些地址可分配取决于网络技术和协议用途。

:::single-choice{#subnet-math-31-exception}
为什么不能从每个 IPv4 前缀的地址数中都减去两个？

::option[任何前缀下的 IPv4 地址都没有主机位。]{#subnet-math-no-host-bits explanation="大多数前缀会留出一个或多个主机位。"}
::option[`/31` 点对点链路可以将两个地址都用作端点。]{#subnet-math-31-both .correct explanation="点对点模型不需要传统网络地址和定向广播地址保留。"}
::option[所有 IPv4 网络都使用多播而不是单播。]{#subnet-math-all-multicast explanation="普通单播寻址仍然是基础。"}
:::

## 验证计算

使用独立工具或库检查手工计算，再与真实接口和路由配置比较。数学上有效的前缀仍可能与另一个子网冲突，或违反地址分配计划。

:::single-choice{#subnet-math-valid-not-safe}
正确的子网计算无法证明什么？

::option[地址计划不存在重叠或策略冲突。]{#subnet-math-no-conflict .correct explanation="仍需运维分配和路由证据。"}
::option[IPv4 地址包含 32 位。]{#subnet-math-proves-size explanation="该计算正是以这个固定大小为基础。"}
::option[二的幂决定地址块数量。]{#subnet-math-powers explanation="二进制地址组合天然使用二的幂。"}
:::

## 总结

现在，你可以计算 IPv4 子网边界并识别常见例外。

1. 使用按位与求出网络地址。
2. 根据主机位数量计算总地址数。
3. 使用块大小确定网络和广播边界。
4. 根据预期用途处理 `/31` 和 `/32`。
5. 将数学结果与实际地址计划进行核对。
