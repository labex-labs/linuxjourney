---
lesson_id: "memory-monitoring"
course_id: "process-utilization"
lang: "zh"
order_index: 6
title: "内存监控"
description: "学习如何解读 vmstat 的内存、分页、进程、I/O 和 CPU 样本。"
meta_title: "内存监控 - 进程资源利用"
meta_description: "使用 vmstat 命令掌握 Linux 内存监控。本指南解释了如何使用此强大的内存利用率监视器来分析系统性能指标。"
meta_keywords: "内存监控，内存利用率监视器，vmstat, linux 内存，系统性能，内存使用，linux 教程"
---

Linux 会有意使用原本空闲的内存作为缓存，因此 `free` 值较小本身并不能证明存在内存压力。`vmstat` 可以帮助你把内存与可运行任务、分页、I/O 和 CPU 活动联系起来。

## 使用 vmstat 采样

可以每秒收集一个样本：

```bash
$ vmstat 1
```

第一行数据通常报告系统启动以来的平均值，后续各行覆盖每个采样间隔。捕获到具有代表性的时段后，按 `Ctrl-C` 停止。单位和可用字段会有差异，因此应检查 `vmstat --unit` 和本机手册。

:::single-choice{#vmstat-interval-rows}
`vmstat 1` 的哪些行最适合观察逐秒变化？

::option[初始报告之后的各行。]{#vmstat-later-rows .correct explanation="后续各行描述指定的每个采样间隔，而不是累计时段。"}
::option[只有第一行数据上方的标题。]{#vmstat-headings explanation="标题定义字段，但不包含活动样本。"}
::option[只使用从另一台主机复制的一行。]{#vmstat-other-host explanation="不同系统不能代表当前工作负载。"}
:::

## 进程与内存

常见进程字段包括表示可运行任务的 `r`，以及表示在不可中断睡眠中阻塞任务的 `b`。内存字段包括已用交换空间（`swpd`）、空闲内存（`free`）、缓冲区（`buff`）和缓存（`cache`）。这些都是系统级数值，而不是单个进程的消耗量。

若要更直观地查看当前可用内存，可以与以下输出比较：

```bash
$ free -h
```

`available` 估算值通常比单独的 `free` 更有用，因为可回收缓存可以用于满足新的内存分配。

:::single-choice{#vmstat-free-memory}
为什么 Linux 上较低的 `free` 值可能是正常现象？

::option[该值总是排除全部物理 RAM。]{#vmstat-excludes-ram explanation="它是内存字段，不过应确认具体单位。"}
::option[内核可以把空闲内存用于可回收缓存。]{#vmstat-reclaimable-cache .correct explanation="应用需要内存时，缓存内存通常可以被回收。"}
::option[空闲内存少证明 CPU 已经关机。]{#vmstat-cpu-off explanation="内存分配和 CPU 电源状态之间不存在这种结论。"}
:::

## 分页与 I/O

`si` 和 `so` 显示换入和换出速率。持续分页若同时伴随延迟和内存回收活动，可能表示存在压力；但交换空间使用量（`swpd`）非零本身并不能证明当前有问题。`bi` 和 `bo` 报告块输入与输出速率，并不限于交换流量。

:::single-choice{#vmstat-swap-pressure}
哪项证据更能支持当前存在内存压力的诊断？

::option[`swpd` 非零，且没有其他观察结果。]{#vmstat-swpd-alone explanation="早期压力过后，内存页仍可能留在交换空间，因此单看使用量并不充分。"}
::option[持续分页，并且与内存回收活动和工作负载延迟相关。]{#vmstat-correlated-pressure .correct explanation="反复出现且相互关联的证据，能够把内存行为与当前影响联系起来。"}
::option[登录时打印的主机名。]{#vmstat-hostname explanation="主机名无法衡量内存回收或分页活动。"}
:::

## CPU 与系统活动

CPU 列通常包括用户（`us`）、系统（`sy`）、空闲（`id`）、I/O 等待（`wa`）和窃取（`st`）百分比。系统列包括每秒中断数（`in`）和上下文切换数（`cs`）。应依据基线解读尖峰；对于某些工作负载，较高的上下文切换率可能完全正常。

:::single-choice{#vmstat-r-column}
进程字段 `r` 表示什么？

::option[以只读方式挂载的文件系统。]{#vmstat-readonly explanation="进程字段不表示文件系统挂载标志。"}
::option[拥有活动 shell 的远程用户。]{#vmstat-remote-users explanation="登录会话由其他工具报告。"}
::option[可运行或正在等待 CPU 的任务。]{#vmstat-runnable .correct explanation="将此数量与 CPU 容量比较，有助于识别 CPU 需求。"}
:::

## 总结

现在，你可以把 `vmstat` 解读为按时间关联的系统视图。

1. 区分初始累计报告和后续间隔样本。
2. 将缓存视为可能可回收的内存。
3. 把分页与内存回收和应用影响相互关联。
4. 综合阅读进程、I/O、系统和 CPU 字段。
