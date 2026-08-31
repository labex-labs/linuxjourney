---
lesson_id: "swap-space"
course_id: "filesystem"
lang: "zh"
order_index: 8
title: "交换空间"
description: "了解 Linux 如何使用、初始化、激活、规划大小并安全停用交换空间。"
meta_title: "交换空间 - 文件系统"
meta_description: "了解 Linux 交换空间的工作原理，以及如何创建和管理交换分区。通过本指南优化系统的内存使用！"
meta_keywords: "Linux 交换，mkswap, swapon, swapoff, /etc/fstab, 虚拟内存，Linux 入门，Linux 教程"
---

Linux 可以在 RAM 与交换后端存储之间移动选定的匿名内存页。这样既能保留不活跃内存，又能释放 RAM 供活跃工作负载和文件系统缓存使用，但存储速度远慢于 RAM。交换空间是容量和内存管理工具，不能替代充足内存，也不能充当应用程序内存限制。

## 交换空间如何参与内存管理

根据工作负载、内存压力、cgroup 和 swappiness 等可调参数，内核可能会在 RAM 尚未完全耗尽前使用交换空间。文件后端的干净内存页通常可以丢弃，之后再从文件读取；匿名页则需要交换空间，或必须留在 RAM 中。

长期大量交换可能造成严重延迟或颠簸。应诊断内存需求、工作集、压力和应用程序限制，而不要把扩大交换区域视为通用性能修复方法。

:::single-choice{#swap-space-anonymous-pages}
哪种内存是存入交换空间的主要候选？

::option[安装在 `/usr` 下的所有可执行文件。]{#swap-space-installed-files explanation="已安装文件仍位于文件系统中；干净的映射页可以从那里重新读取。"}
::option[不活跃的匿名内存页。]{#swap-space-anonymous-memory .correct explanation="匿名页没有可供直接重新读取的普通后端文件。"}
::option[磁盘的分区表条目。]{#swap-space-partition-table explanation="分区元数据保留在块设备上，并不是从 RAM 换出的进程内存。"}
:::

## 检查活动交换空间

先使用只读命令：

```bash
$ swapon --show
$ cat /proc/swaps
$ free -h
```

这些命令显示已配置的活动交换区域和汇总内存数字。“已用”值非零并不自动表示存在问题；应把它与换入和换出速率、内存压力、延迟及工作负载行为联系起来。

:::single-choice{#swap-space-show-active}
哪个命令以结构化视图列出活动交换区域？

::option[`swapon --show`]{#swap-space-swapon-show .correct explanation="显示模式会报告活动交换文件或设备，并在可用时显示容量、用量和优先级。"}
::option[`mkswap --all`]{#swap-space-mkswap-all explanation="Mkswap 用于初始化交换签名，不是只读的活动状态列表命令。"}
::option[`mkfs -t swap`]{#swap-space-mkfs-swap explanation="标准初始化工具是 `mkswap`，而格式化操作也不是状态查询。"}
:::

## 初始化并激活交换设备

`mkswap` 会写入交换签名，并破坏目标原有的可用元数据。练习时只能使用经过核实的可丢弃目标：

```bash
$ sudo mkswap /dev/VERIFIED-SWAP-TARGET
$ sudo swapon /dev/VERIFIED-SWAP-TARGET
```

运行 `mkswap` 前，应像运行 `mkfs` 前一样，核实型号、序列号、容量、持久身份、现有签名、挂载、RAID、LVM、加密和备份。激活后，用 `swapon --show` 确认准确来源。

若要持久启用，可在 `/etc/fstab` 中使用交换空间 UUID，并根据本地策略填写类型和选项：

```text
UUID=VERIFIED-SWAP-UUID none swap sw 0 0
```

:::single-choice{#swap-space-enable-command}
哪个命令会激活已经初始化的交换区域？

::option[`swapon`]{#swap-space-command-swapon .correct explanation="Swapon 会把有效的交换设备或文件加入内核的活动交换集合。"}
::option[`mkswap`]{#swap-space-command-mkswap explanation="Mkswap 初始化签名，但不会自行激活该区域。"}
::option[`mount`]{#swap-space-command-mount explanation="交换空间通过交换子系统激活，不会像目录文件系统那样挂载。"}
:::

## 交换文件与其他后端

交换文件无需重新分区即可灵活增加容量，但创建要求取决于文件系统。文件必须具备严格权限、合适的实际分配，不能存在不受支持的空洞或写时复制行为，还要写入交换签名并激活。应遵循文件系统和发行版文档，不要把某个通用 `fallocate` 流程原样套用到所有环境。

zram 等压缩 RAM 设备可以提供另一层交换空间，但会产生不同的 CPU 和容量取舍。加密交换空间可以保护静态页面；休眠则需要恢复配置以及容量足够且合适的存储。这些目标都会影响容量规划和设计。

不存在“交换空间必须等于 RAM 两倍”的通用规则。应根据工作负载峰值、期望的故障行为、休眠需求、存储延迟与耐久性、崩溃转储设计和运维监控来规划大小。

:::single-choice{#swap-space-sizing-rule}
规划交换空间大小的最佳依据是什么？

::option[始终严格等于已安装 RAM 的两倍。]{#swap-space-twice-ram explanation="这一历史经验法则并不适用于所有工作负载或现代内存容量。"}
::option[测得的工作负载需求、休眠目标和故障策略。]{#swap-space-sizing-requirements .correct explanation="系统用途和观察到的内存行为比固定 RAM 倍数更重要。"}
::option[只要系统使用 SSD，就始终设为零。]{#swap-space-zero-ssd explanation="存储类型本身无法决定内存压力或休眠需求。"}
:::

## 安全停用交换空间

使用以下命令停用一个经过核实的特定区域：

```bash
$ sudo swapoff /dev/VERIFIED-SWAP-TARGET
```

内核必须把其中驻留的交换页移到其他位置。如果 RAM 和剩余交换空间无法容纳它们，操作可能失败或造成危险的内存压力。应先停止或限制工作负载并监控内存；只有核实目标正确后才移除持久 fstab 条目；重新利用存储前，再用 `swapon --show` 确认已经停用。

:::single-choice{#swap-space-swapoff-capacity}
为什么 `swapoff` 可能在高负载系统上失败或造成危险？

::option[Swapoff 总会重新格式化每个 RAM 模块。]{#swap-space-formats-ram explanation="它改变活动交换配置，不会格式化物理内存硬件。"}
::option[该区域中的内存页需要 RAM 或其他交换空间来容纳。]{#swap-space-pages-need-capacity .correct explanation="系统继续运行时，停用操作必须重新安置仍然有效的交换页。"}
::option[非活动交换区域必须继续挂载到 `/swap`。]{#swap-space-mounted-path explanation="交换区域不是挂载到目录的文件系统。"}
:::

可以在受控环境中通过[在 Linux 中创建和激活交换文件](https://labex.io/zh/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)练习文件权限、激活和持久配置。

## 总结

现在，你可以把交换空间视为明确的内存管理资源。

1. 理解交换空间主要用于内存压力下的匿名内存。
2. 更改容量前，检查活动交换空间和工作负载行为。
3. 只初始化经过核实的可丢弃目标，再用 `swapon` 激活。
4. 根据工作负载和休眠要求规划并保护交换空间。
5. 使用 `swapoff` 前确保具备重新安置内存页的容量。
