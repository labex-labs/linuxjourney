---
lesson_id: "wireshark-display-filters"
course_id: "network-monitoring"
lang: "zh"
order_index: 4
title: "Wireshark 显示过滤器"
description: "用 Wireshark 显示过滤器缩小练习抓包的查看范围。"
meta_title: "Wireshark 显示过滤器 - 网络监测"
meta_description: "在 Wireshark 或 TShark 中按协议和 IP 地址筛选离线抓包，并解释空列表能说明什么。"
meta_keywords: "Wireshark, 显示过滤器, TShark, 抓包, 网络监测, Linux Journey"
---

一份抓包可以包含多种协议。**显示过滤器**告诉 Wireshark 要显示哪些已经保存的数据包。它只改变你看到的内容，抓包文件本身保持不变。

## 选择协议

把[练习抓包文件](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/examples/network-monitoring/sample.pcap)保存为 `sample.pcap`。用 Wireshark 打开，在显示过滤器输入框中键入 `dns`。如果 Linux 终端里装有 TShark，下面的命令会对同一个文件应用相同的过滤器。示例文件包含一次无害的查询，以及另一些用于练习的流量。

```bash
$ tshark -r sample.pcap -Y dns
```

`-r` 选项读取文件，`-Y` 应用显示过滤器。从结果里找出一条查询和对应的应答。

:::single-choice{#wireshark-display-filters-display-effect} 过滤后的列表比原来少了两行。其他数据包怎么了？

::option[已经从抓包文件中删除。]{#wireshark-display-filters-display-effect-a explanation="显示过滤器只改变可见结果。"}
::option[还保存在文件中，只是没有匹配这个过滤器。]{#wireshark-display-filters-display-effect-b .correct explanation="清除过滤器可以再次看到未筛选的列表。"}
::option[这些数据包被重新发到网络上了。]{#wireshark-display-filters-display-effect-c explanation="读取保存的抓包文件不会发送任何数据包。"}
:::

## 匹配地址

过滤器也可以引用数据包中的字段。`ip.addr` 可以匹配 IPv4 来源地址或目标地址。两个等号用来把该字段与示例值比较。

```bash
$ tshark -r sample.pcap -Y 'ip.addr == 192.0.2.10'
```

shell 中的引号会把整个表达式保留为一个参数。可以在显示的各行中识别端点。

:::single-choice{#wireshark-display-filters-address-scope} 某个数据包从另一个地址发往 192.0.2.10。它会匹配吗？

::option[会，因为条件会检查通信的两端。]{#wireshark-display-filters-address-scope-a .correct explanation="ip.addr 可以匹配来源地址或目标地址。"}
::option[不会，因为条件只检查来源地址。]{#wireshark-display-filters-address-scope-b explanation="这个字段可以匹配两个方向。"}
::option[只有数据包承载 DNS 时才会匹配。]{#wireshark-display-filters-address-scope-c explanation="这个表达式只检查 IPv4 地址。"}
:::

![记录的 TShark 输出对比了仅显示 DNS 的结果与练习抓包的两种协议](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/network-monitoring/wireshark-display-filters/saved-dns-exchange.png)

## 解释空列表

结果为空，说明过滤器在所查看的文件里没有找到匹配数据包。要得出更广的结论，先检查表达式、时段和抓包位置。可以先清除过滤器，确认文件里确实有流量。

:::single-choice{#wireshark-display-filters-empty-capture-view} 在离线抓包中应用 dns 过滤器，结果一行也没有。你可以怎么报告？

::option[网络上所有人都没有使用 DNS。]{#wireshark-display-filters-empty-capture-view-a explanation="文件只覆盖特定的抓包位置和时间。"}
::option[Wireshark 删掉了 DNS 证据。]{#wireshark-display-filters-empty-capture-view-b explanation="显示过滤器不会删除已经保存的数据包。"}
::option[这个过滤器没有从这份抓包中显示出 DNS 数据包。]{#wireshark-display-filters-empty-capture-view-c .correct explanation="这项说法没有超出你实际查看的证据范围。"}
:::

要在浏览器实验环境里查看另一份抓包，可以试试 [Wireshark 入门](https://labex.io/courses/quick-start-with-wireshark)里的显示过滤器练习。

## 总结

现在，你可以筛选保存的抓包文件，并说明结果的覆盖范围。

1. 用显示过滤器选中某种协议。
2. 用 ip.addr 匹配数据包地址。
3. 根据抓包文件的可见范围解释过滤结果。
