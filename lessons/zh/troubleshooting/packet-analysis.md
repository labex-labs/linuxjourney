---
lesson_id: "packet-analysis"
course_id: "troubleshooting"
lang: "zh"
order_index: 5
title: "数据包分析"
description: "了解如何捕获范围有界、经过过滤的数据包轨迹，并使用 tcpdump 安全分析。"
meta_title: "数据包分析 - 故障排除"
meta_description: "学习 Linux 网络数据包分析基础。本指南介绍强大的数据包分析工具 tcpdump，用它捕获并解读网络流量。"
meta_keywords: "tcpdump, 数据包分析, 网络数据包分析, 网络数据包分析器, 网络分析, 网络数据包分析工具, Linux 网络, Wireshark, Linux 命令, 网络流量"
---

数据包捕获会记录在所选观察点可见的流量。它可以揭示协议交换和时序，也可能收集凭据、个人数据以及无关用户的流量。应先获得授权、尽量缩小范围、保护文件并遵守保留策略。

## 选择观察点

在受影响流实际经过的接口和网络命名空间中抓包。网桥、容器、VPN、链路聚合、VLAN 和卸载功能都会改变某个接口能看到的内容。抓包前使用 `ip route get` 和 `ip link` 确定候选位置。

:::single-choice{#packet-analysis-interface-choice} 为什么抓包接口的选择很重要？

::option[每个接口都会自动镜像整个互联网。]{#packet-analysis-mirrors-internet explanation="主机通常只能看到经其接口传递或镜像到接口的流量。"}
::option[只能记录该观察点可见的流量。]{#packet-analysis-visible-point .correct explanation="命名空间、隧道、网桥和路由可能让相关流出现在别处。"}
::option[接口名称可以解密 TLS 载荷。]{#packet-analysis-name-decrypts explanation="名称不具备解密能力。"}
:::

## 捕获有界的数据流

禁用名称解析，将范围限制到某台主机和一个 TCP 端口，并最多捕获 100 个数据包：

```bash
$ sudo tcpdump -i enp1s0 -n -c 100 -w incident.pcap \
    'host 192.0.2.25 and tcp port 443'
```

`-i` 选择接口，`-n` 保持数字形式，`-c` 限制数据包数量，`-w` 写入 pcap 数据，最后的表达式是捕获过滤器。如果流量可能一直不出现，还应在外部设置时间限制。

:::single-choice{#packet-analysis-count-bound} `-c 100` 有什么作用？

::option[只捕获 TCP 端口 100。]{#packet-analysis-port-hundred explanation="端口选择应写在过滤表达式中。"}
::option[把文件压缩到 100 字节。]{#packet-analysis-compress-hundred explanation="该选项限制的是数据包数量，而不是文件大小。"}
::option[捕获 100 个数据包后停止。]{#packet-analysis-hundred .correct explanation="该计数可以避免无人看管的捕获按数据包数量无限增长。"}
:::

## 读取已捕获的数据包

分析已保存的文件而不修改它：

```bash
$ tcpdump -n -tttt -r incident.pcap
```

根据具体协议解读时间戳、协议、源、目的地、标志、序列或确认数据以及长度。捕获时间戳表示在本主机观察到数据包的时刻，不一定是它在别处发出的准确时间。关联多个系统的抓包时，时钟同步非常重要。

:::single-choice{#packet-analysis-read-file} 哪个选项从已保存的 pcap 文件读取数据包？

::option[`-r`]{#packet-analysis-option-read .correct explanation="读取选项会处理现有捕获文件。"}
::option[`-i`]{#packet-analysis-option-interface explanation="该选项选择实时捕获接口。"}
::option[`-w`]{#packet-analysis-option-write explanation="该选项把原始数据包写入文件。"}
:::

## 解读缺失与加密

没有捕获到数据包，可能是接口或命名空间错误、抓包丢失、过滤器过窄、卸载功能影响、流量经别处路由，或确实没有流量。检查 tcpdump 的已接收和已丢弃计数器，并重现一个已知事件。

TLS 和其他加密通常会隐藏应用程序载荷，但仍会留下端点、时序、大小、TCP 行为和部分握手等有用元数据。不要尝试未经授权的解密，也不要随意收集私钥。

:::single-choice{#packet-analysis-no-packets} 一次空的过滤抓包能证明什么？

::option[远程应用程序已被永久删除。]{#packet-analysis-empty-deleted explanation="观察点或过滤器错误也能产生相同结果。"}
::option[整个网络的流量为零。]{#packet-analysis-empty-network explanation="狭窄的过滤器可以排除无关流量。"}
::option[只能证明该捕获点没有记录到匹配的数据包。]{#packet-analysis-empty-limited .correct explanation="得出结论前，应验证接口、命名空间、过滤器、捕获丢包和测试流量生成。"}
:::

## 保护与共享证据

使用严格权限存储 pcap，记录命令、主机、接口、时区、过滤器和事件时间窗口；完整性很重要时，还要对证据计算哈希。共享前，应使用能够保留所需字段的工具和流程尽量减少或清理数据；数据包载荷乃至元数据都可能识别用户与系统。

:::single-choice{#packet-analysis-pcap-safety} 应该如何处理事件 pcap？

::option[将其视为敏感证据，限制访问并记录来源。]{#packet-analysis-sensitive-evidence .correct explanation="捕获可能含有机密内容，同时需要完整性与机密性控制。"}
::option[将其视为无害文本，无需审查即可公开上传。]{#packet-analysis-public explanation="二进制捕获可能暴露载荷、身份和基础设施。"}
::option[直接修改原文件中的字节，不保留原件。]{#packet-analysis-edit-original explanation="这会破坏来源记录，并可能使后续分析失效。"}
:::

## 总结

现在，你可以创建有用的数据包捕获，同时避免范围不必要地扩大或处理方式不安全。

1. 选择正确的接口和网络命名空间。
2. 用过滤器、数据包数量和时间限制捕获范围。
3. 保存原始数据包，并以只读方式分析文件。
4. 在正确认识局限的前提下看待数据缺失与加密载荷。
5. 保护捕获数据的机密性、完整性与来源信息。
