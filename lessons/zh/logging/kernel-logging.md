---
lesson_id: "kernel-logging"
course_id: "logging"
lang: "zh"
order_index: 4
title: "内核日志"
description: "学习如何使用 dmesg 和 journalctl 查询当前及已保留的 Linux 内核消息。"
meta_title: "内核日志 - 日志"
meta_description: "探索 Linux 内核日志，包括 /var/log/kern.log 和 dmesg。学习如何检查 kern 日志中的启动消息、硬件驱动信息并排查系统问题。"
meta_keywords: "内核日志, kern.log, /var/log/kern.log, Linux 内核日志, kern 日志, dmesg, Linux 日志, 启动消息, 内核事件"
---

内核会发出与启动、驱动程序、设备、文件系统、网络、内存和故障有关的消息。这些记录可以解释底层症状，但单独一条警告并不能证明硬件有缺陷。

## 读取内核环形缓冲区

`dmesg` 从内核环形缓冲区读取消息：

```bash
$ dmesg --human
```

该缓冲区容量有限，因此新消息可能覆盖旧消息。访问也可能仅限特权用户。支持 `dmesg --follow` 的实现可以用它跟踪新内核消息；完成有限时间的重现后应停止跟踪。

:::single-choice{#kernel-log-ring-buffer-limit}
为什么较早的内核事件可能没有出现在当前 `dmesg` 输出中？

::option[内核事件只能包含一个字符。]{#kernel-log-one-character explanation="内核消息可以包含普通诊断文本和元数据。"}
::option[`dmesg` 显示每一行后都会永久删除它。]{#kernel-log-display-deletes explanation="正常读取不会消耗所有已显示的内核消息。"}
::option[容量有限的环形缓冲区可能已经覆盖它。]{#kernel-log-overwritten .correct explanation="内存缓冲区只能保留有限数量的内核消息数据。"}
:::

## 使用易读时间戳

原始内核时间戳通常以启动时间为基准。`dmesg --ctime` 或 `--human` 可以渲染墙上时钟时间，但转换值取决于时钟历史；如果启动后时钟发生变化，结果可能不准确。在精确事件排序很重要时，应保留相对于启动的时间。

:::single-choice{#kernel-log-timestamp-caution}
为什么应谨慎看待转换后的 `dmesg` 墙上时钟时间戳？

::option[它们始终指向另一台计算机。]{#kernel-log-other-machine explanation="它们在本地派生，但时钟变化会影响转换。"}
::option[它们依赖于将启动相对时间映射到可能发生变化的时钟。]{#kernel-log-clock-change .correct explanation="时间同步或手动更改时钟可能使渲染的墙上时间产生误导。"}
::option[它们显示的是文件系统可用空间而不是时间。]{#kernel-log-free-space explanation="时间戳选项仍显示时间，而不是存储容量。"}
:::

## 查询持久内核记录

在 systemd 主机上，用以下命令查询当前启动的内核记录：

```bash
$ journalctl -k -b
```

如果持久 journal 存储保留了先前启动记录，可查看启动列表并选择其中一次：

```bash
$ journalctl --list-boots
$ journalctl -k -b -1
```

传统 syslog 路由可能创建 `/var/log/kern.log` 或其他文件，但这取决于配置。保存的 `/var/log/dmesg` 文件也并非普遍存在，而且可能只代表启动时的快照。

:::single-choice{#kernel-log-previous-boot}
哪个命令请求查看上一次已保留启动的内核消息？

::option[`journalctl -u kernel -f`]{#kernel-log-unit-follow explanation="内核消息使用 -k 选择，而跟踪操作不会选择上一次启动。"}
::option[`dmesg --clear`]{#kernel-log-clear explanation="清除会改变缓冲区状态，而不会取回早先启动记录。"}
::option[`journalctl -k -b -1`]{#kernel-log-previous .correct explanation="内核过滤器与负一启动偏移结合，会选择上一次已保留启动。"}
:::

## 调查内核事件

确定启动、时间戳、设备、子系统以及当时正在进行的操作。查询周围的内核和服务记录，再与硬件清单和当前状态进行比较：

```bash
$ journalctl -k -b --since '10 minutes ago'
$ lspci -k
$ lsblk
```

只使用与相关子系统有关的工具。重新加载驱动程序、解除设备绑定或重启前，应评估对存储、网络、控制台和服务的影响，并保留恢复通道。

:::single-choice{#kernel-log-warning-response}
面对一条内核警告，最佳响应是什么？

::option[立即卸载所有已加载的驱动程序。]{#kernel-log-unload-all explanation="这可能中断关键设备，也无法隔离警告原因。"}
::option[认定必须更换整台计算机。]{#kernel-log-replace-machine explanation="单条记录不足以支持这种结论。"}
::option[将其与周围事件和当前子系统状态关联。]{#kernel-log-correlate .correct explanation="选择纠正措施前，需要结合上下文并确认可重现的影响。"}
:::

## 总结

现在，你可以区分实时内核缓冲区消息与已保留的内核日志。

1. 使用 `dmesg` 读取容量有限的环形缓冲区。
2. 谨慎解读启动相对时间和转换后的时间戳。
3. 使用 `journalctl -k` 查询当前或先前启动。
4. 在进行破坏性更改前关联内核消息。
