---
lesson_id: "io-monitoring"
course_id: "process-utilization"
lang: "zh"
order_index: 5
title: "I/O 监控"
description: "学习如何使用 iostat 样本调查 CPU 和块设备活动。"
meta_title: "I/O 监控 - 进程资源利用"
meta_description: "使用 iostat 命令掌握 Linux I/O 监控。本指南解释了如何分析 CPU 和磁盘使用率指标以优化系统性能。"
meta_keywords: "i/o 监控，iostat, linux i/o 监控，cpu 使用率，磁盘使用率，系统性能，iowait, linux 命令"
---

`iostat` 通常由 `sysstat` 软件包提供，用于报告 CPU 和块设备活动。应结合重复采样和应用延迟进行分析：吞吐量或利用率本身并不能证明存储正在造成用户可见的问题。

## 收集有效样本

可以每秒收集一次扩展设备统计信息：

```bash
$ iostat -xz 1
```

在常见实现中，第一份报告包含系统启动以来的平均值，后续报告则覆盖各自的采样间隔。`-x` 选项增加扩展字段，`-z` 则隐藏无活动设备。应等待多个间隔，以捕获正常和异常时段。

:::single-choice{#iostat-first-report} 第一份 `iostat` 报告通常表示什么？

::option[仅表示命令执行最后一秒内的操作。]{#iostat-final-second explanation="这并不是初始累计报告的含义。"}
::option[系统启动以来的活动平均值。]{#iostat-since-boot .correct explanation="后续报告通常针对各个采样间隔，因此第一份报告需要单独解读。"}
::option[对明天设备利用率的预测。]{#iostat-forecast explanation="该工具报告已观察到的统计信息，而不是未来需求。"}
:::

## 阅读 CPU 字段

CPU 部分通常包括用户时间（`%user`）、系统时间（`%system`）、空闲时间（`%idle`）、I/O 等待时间（`%iowait`）和虚拟机窃取时间（`%steal`）。I/O 等待是系统存在尚未完成的 I/O 请求时 CPU 的空闲时间，并不是磁盘繁忙程度的百分比。

:::single-choice{#iostat-iowait-meaning} `%iowait` 描述什么？

::option[磁盘容量已经占用的百分比。]{#iostat-capacity explanation="文件系统容量和 CPU 时间是两种不同指标。"}
::option[存在未完成 I/O 请求时 CPU 的空闲时间。]{#iostat-iowait-cpu .correct explanation="它是 CPU 时间类别，无法单独指出具体设备。"}
::option[等待删除的文件数量。]{#iostat-delete-queue explanation="该字段不表示文件删除次数。"}
:::

## 阅读设备字段

字段名称会随 sysstat 版本而变化，但常用概念包括：

- 每秒读写操作数或数据量表示工作负载速率。
- `await` 表示平均请求延迟，其中包括排队时间和服务时间。
- 平均队列大小字段表示正在等待或处理的请求。
- `%util` 表示设备存在 I/O 活动的时间占总时间的百分比。

对于简单的串行设备，较高的 `%util` 可能表示已经饱和；但对于并行存储、阵列或虚拟设备，它不能直接换算为性能容量。应把延迟与设备设计、工作负载模式和服务目标进行比较。

:::single-choice{#iostat-await-purpose} 哪个字段与平均 I/O 请求延迟最直接相关？

::option[设备名称。]{#iostat-device-name explanation="名称用于标识设备，并不衡量请求持续时间。"}
::option[`await`]{#iostat-await .correct explanation="`await` 反映请求的平均耗时，其中包括排队和服务时间。"}
::option[`%idle`]{#iostat-idle explanation="这是 CPU 字段，而不是设备请求延迟。"}
:::

## 关联分析证据

下结论前，应先把设备名称对应到挂载点和底层设备：

```bash
$ lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
$ findmnt
```

然后将 `iostat` 的各个间隔与应用响应时间、数据库或文件系统指标以及进程级 I/O 相互关联。设备映射器、RAID、容器和网络后端存储都可能增加额外层次，需要使用各自对应的工具检查。

:::single-choice{#iostat-high-util-conclusion} 看到设备的 `%util` 较高后，应该怎么做？

::option[假定所有文件系统都没有可用空间。]{#iostat-assume-full explanation="繁忙时间并不表示文件系统容量。"}
::option[在识别挂载的工作负载前就删除文件。]{#iostat-delete-first explanation="删除是会改变状态的操作，与证明 I/O 瓶颈无关。"}
::option[结合存储设计，关联分析延迟和工作负载行为。]{#iostat-correlate .correct explanation="设备并行能力和工作负载目标决定观察到的现象是否有害。"}
:::

## 总结

现在，你可以把 `iostat` 用作 I/O 调查中的证据。

1. 收集多个扩展统计采样间隔。
2. 区分 CPU 的 I/O 等待时间与设备繁忙时间。
3. 综合解读延迟、排队、吞吐量和利用率。
4. 将设备映射到工作负载，并验证对应用的影响。
