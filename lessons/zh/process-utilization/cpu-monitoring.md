---
lesson_id: "cpu-monitoring"
course_id: "process-utilization"
lang: "zh"
order_index: 4
title: "CPU 监控"
description: "学习如何结合 CPU 数量、利用率和任务状态来解读 Linux 平均负载。"
meta_title: "CPU 监控 - 进程资源利用"
meta_description: "学习使用 uptime 命令进行 Linux CPU 监控的基础知识。本初学者指南解释了如何解释负载平均值、理解进程利用率以及评估系统性能。"
meta_keywords: "uptime 命令，Linux CPU 监控，负载平均值，系统性能，进程利用率，Linux 教程，初学者指南"
---

排查 CPU 问题的第一步，是区分负载、利用率和响应能力。没有任何一个数字能单独证明存在瓶颈，因此应比较多个时间窗口，并把主机指标与用户实际感受到的工作负载表现联系起来。

## 阅读 uptime 输出

`uptime` 可以作为简洁的起点：

```text
$ uptime
 17:23:35 up 1 day, 5:59, 2 users, load average: 0.00, 0.02, 0.05
```

最后三个值分别是大约过去 1、5、15 分钟的平均负载。比较它们可以看出趋势：1 分钟值明显更大，可能表示负载正在上升；15 分钟值更大，则可能表示负载正在下降。

:::single-choice{#cpu-uptime-windows} `uptime` 按什么顺序显示平均负载的时间窗口？

::option[15、5、1 秒。]{#cpu-windows-seconds explanation="这些值是分钟级平均值，而且不会按最长窗口优先显示。"}
::option[1、5、15 分钟。]{#cpu-windows-one-five-fifteen .correct explanation="最短的近期窗口最先显示，最长窗口最后显示。"}
::option[当前、最低和最高 CPU 百分比。]{#cpu-windows-percentages explanation="平均负载不是最低或最高 CPU 百分比。"}
:::

## 理解 Linux 负载

Linux 平均负载统计可运行任务，包括正在使用 CPU 或等待 CPU 的任务，还包括处于不可中断睡眠的任务，后者通常与 I/O 有关。因此，平均负载并不等同于 CPU 利用率。

负载 `4.0` 在只有一个逻辑 CPU 和拥有十六个逻辑 CPU 的系统上含义截然不同。可以用以下命令查看系统可用的处理单元数量：

```bash
$ nproc
```

CPU 配额、亲和性、虚拟化和容器限制都可能减少特定工作负载实际可见的容量，所以主机 CPU 数量只能作为分析起点。

:::single-choice{#cpu-load-not-percentage} 为什么平均负载不是 CPU 利用率百分比？

::option[它只报告 CPU 时钟频率。]{#cpu-load-clock explanation="时钟速度是另一项硬件或频率调节指标。"}
::option[它只衡量可用物理内存。]{#cpu-load-memory explanation="内存可用量由其他指标报告。"}
::option[它包括可运行任务和处于不可中断睡眠的任务。]{#cpu-load-task-count .correct explanation="负载基于任务需求和等待状态，而不是已用 CPU 时间所占的百分比。"}
:::

## 比较负载与 CPU 活动

应收集多个样本，而不是只依赖一次输出。常用的配套命令包括：

```bash
$ top
$ vmstat 1
$ mpstat -P ALL 1
```

`top` 结合主机和进程视图；`vmstat` 显示可运行和阻塞任务数以及 CPU 类别；许多发行版由 `sysstat` 提供的 `mpstat` 会显示各 CPU 的活动情况。工具是否可用以及具体字段都可能不同，因此应查阅本机手册。

高负载同时伴随 CPU 繁忙，可能表明 CPU 需求较高。高负载若伴随大量阻塞任务、I/O 延迟或 I/O 等待现象，则指向其他受限资源。较低的平均利用率也可能掩盖单个 CPU 已饱和或短暂的延迟尖峰。

:::single-choice{#cpu-high-load-next-step} 观察到较高平均负载后，最佳的下一步是什么？

::option[比较多次采集的 CPU、任务状态、I/O 和工作负载指标。]{#cpu-load-correlate .correct explanation="相互关联的样本可以区分造成负载的不同原因。"}
::option[不收集其他数据，立即重启。]{#cpu-load-reboot explanation="重启会消除证据并可能中断服务，却无法确定原因。"}
::option[假定所有 CPU 都已经满负荷运行。]{#cpu-load-assume explanation="负载可能包含不可中断任务，而且也可能在各 CPU 之间分布不均。"}
:::

## 评估容量与影响

没有通用规则要求负载始终低于 CPU 数量。批处理系统或许可以接受任务排队，而交互式服务可能在达到这一点之前就已经违反延迟目标。应为相同主机和工作负载建立基线，再比较响应时间、吞吐量、错误率、饱和度和资源使用情况。

:::single-choice{#cpu-capacity-threshold} 应该依据什么判断观察到的负载是否可以接受？

::option[负载值必须始终低于一。]{#cpu-below-one explanation="多核容量和工作负载目标使这个固定阈值并不可靠。"}
::option[仅依据 `uptime` 列出的用户数量。]{#cpu-user-count explanation="已登录的 shell 用户并不能代表全部工作负载需求。"}
::option[工作负载基线和服务目标。]{#cpu-baseline-objectives .correct explanation="可接受程度取决于预期行为和用户可见的性能，而不是通用阈值。"}
:::

## 总结

现在，你可以把平均负载作为 CPU 调查的一部分来解读。

1. 阅读 1、5、15 分钟三个负载窗口。
2. 区分任务负载与 CPU 时间百分比。
3. 把负载与可用处理能力进行比较。
4. 将反复采集的主机指标与服务结果相互关联。
