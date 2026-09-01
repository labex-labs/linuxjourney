---
lesson_id: "continuous-monitoring"
course_id: "process-utilization"
lang: "zh"
order_index: 7
title: "持续监控"
description: "了解 sysstat 数据收集和 sar 报告如何支持 Linux 历史性能分析。"
meta_title: "持续监控 - 进程资源利用"
meta_description: "通过 sar 学习持续的 Linux 系统监控。了解安装、数据收集以及如何分析历史资源使用情况以提高性能。立即开始！"
meta_keywords: "sar, sysstat, Linux 监控，系统性能，持续监控，初学者，教程，指南"
---

交互式工具显示的是你观察时正在发生的情况。如果性能下降已经结束，就需要历史监控。`sysstat` 工具套件会定期收集系统计数器，而 `sar` 既可以读取当前计数器，也可以读取保存的活动文件。

## 启用数据收集

安装发行版提供的 `sysstat` 软件包后，还要确认其收集器和保留机制已经启用。具体服务、定时器和配置路径会随发行版而变化；安装软件包并不保证数据收集已经开始。

在 systemd 主机上，应检查软件包提供的单元，而不要猜测其名称：

```bash
$ systemctl list-unit-files | grep sysstat
$ systemctl list-timers --all | grep sysstat
```

确认发行版的 sysstat 数据目录中正在创建新的活动文件，并检查文件权限和保留策略。

:::single-choice{#sar-installation-verification} 安装 `sysstat` 后应该验证什么？

::option[数据收集已启用，并且活动文件正在更新。]{#sar-collector-updating .correct explanation="软件包已经安装和定期收集正在运行是两个不同条件。"}
::option[每个进程都已手动重启。]{#sar-restart-processes explanation="安装监控收集器并不要求重启所有工作负载。"}
::option[所有历史文件都允许任何人写入。]{#sar-world-writable explanation="监控数据应该保持适当的访问控制。"}
:::

## 读取当前样本

让 `sar` 每秒收集一次，共生成三份 CPU 报告：

```bash
$ sar -u 1 3
```

其他常见报告包括运行队列和负载（`-q`）、内存（`-r`）、分页（`-B`）、块设备（`-d`）以及各 CPU 活动（`-P ALL`）。选项和字段会随 sysstat 版本而变化，因此应查阅 `sar --help` 或本机手册。

:::single-choice{#sar-one-second-count} `sar -u 1 3` 请求什么？

::option[每秒一份，共三份 CPU 报告。]{#sar-three-cpu-samples .correct explanation="第一个数字是采样间隔秒数，第二个数字是报告数量。"}
::option[一份恰好覆盖三天的报告。]{#sar-three-days explanation="这些操作数指定采样间隔和次数，而不是日期范围。"}
::option[删除三个已保存的 CPU 文件。]{#sar-delete-files explanation="该命令读取计数器，并未请求删除文件。"}
:::

## 读取历史文件

保存文件的位置和名称会有差异，通常位于 `/var/log/sysstat` 或 `/var/log/sa` 下。使用 `-f` 传入选定的活动文件：

```bash
$ sar -q -f /var/log/sysstat/sa02
```

应从报告标题确认文件的完整日期；两位数字后缀通常表示某月中的日期，在跨越多个保留周期时可能有歧义。保存的二进制格式也可能要求兼容的 sysstat 版本。

:::single-choice{#sar-historical-file-option} 哪个选项让 `sar` 读取指定的活动文件？

::option[`-P`]{#sar-option-p explanation="该选项用于选择处理器报告，而不是输入文件。"}
::option[`-q`]{#sar-option-q explanation="该选项用于选择队列和负载报告。"}
::option[`-f`]{#sar-option-f .correct explanation="文件选项用于选择要读取的已保存活动数据。"}
:::

## 关联分析事故

先确定事故时间和时区，再比较同一时间段内的多个信号。检查负载、CPU、运行队列、分页、设备活动、网络流量和应用延迟的变化。计数器变化表示相关性，但不一定代表因果关系；部署记录和应用日志可能解释触发原因。

数据缺口可能表示主机停机、收集器失败，或数据已被保留策略删除。监控流程本身也要受到监控，以便在事故发生前就能发现证据缺失。

:::single-choice{#sar-incident-method} 事故复盘时应如何使用历史 `sar` 数据？

::option[把单个最高计数器视为已经证实的根本原因。]{#sar-single-root explanation="单一相关性无法证明因果关系。"}
::option[在同一个已核实时间窗口内比较多项指标。]{#sar-correlate-window .correct explanation="对齐的信号有助于区分假设，并把系统行为与事故联系起来。"}
::option[忽略数据缺口，因为安装后一定会持续收集。]{#sar-ignore-gaps explanation="数据收集可能失败或被禁用，缺口必须得到解释。"}
:::

## 总结

现在，你可以使用 `sar` 调查交互式会话之外发生的性能问题。

1. 验证数据收集和保留机制确实处于活动状态。
2. 使用采样间隔和次数获取有界的当前样本。
3. 明确选择历史活动文件。
4. 将多项指标与事故时间和工作负载证据对齐。
