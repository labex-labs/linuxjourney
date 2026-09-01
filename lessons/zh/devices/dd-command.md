---
lesson_id: "dd-command"
course_id: "devices"
lang: "zh"
order_index: 7
title: "dd"
description: "学习 `dd` 如何复制块数据流，以及如何避免输入、输出和大小错误造成破坏。"
meta_title: "dd - 设备"
meta_description: "探索 Linux 中强大的 dd 工具。本指南介绍如何使用 dd Linux 命令高效复制数据、创建磁盘映像和备份，并讲解 if、of 和 bs 等关键选项。"
meta_keywords: "dd 命令, Linux dd, dd 工具, 复制数据, 磁盘映像, Linux 教程, 初学者, 指南, 数据备份"
---

`dd` 将数据从输入流复制到输出流，同时应用所请求的块大小和转换。它不了解文件系统、分区边界，也不知道输出目标是否包含宝贵数据。因此，它既适用于映像和原始设备，也会在目标选错时立即造成破坏。

## 输入、输出与块大小

命令的一般形式如下：

```bash
$ dd if=input.img of=output.img bs=4M status=progress
```

- `if=` 选择输入；省略时，`dd` 从标准输入读取。
- `of=` 选择输出；省略时，`dd` 写入标准输出。
- `bs=` 设置普通复制时的输入和输出块大小。
- `status=progress` 要求 GNU `dd` 定期报告传输进度。

`dd` 复制的是块，并非固有地一次只复制一个字节。较大的 `bs` 可以减少系统调用开销，但最佳值取决于设备、对齐、缓存和工作负载。它不会改变所复制的逻辑数据。

:::single-choice{#dd-command-output-operand} 哪个操作数选择 `dd` 写入的目标？

::option[`if=`]{#dd-command-input-file explanation="if 标识输入来源。"}
::option[`of=`]{#dd-command-output-file .correct explanation="of 指定接收复制数据的输出流或文件。"}
::option[`bs=`]{#dd-command-block-size explanation="bs 选择传输块大小，而不是路径。"}
:::

## 限制复制量

`count=` 限制处理的输入块数量。对于普通输入文件：

```bash
$ dd if=source.img of=prefix.img bs=1M count=2 status=progress
```

该命令请求两个输入块，每块最大 1 MiB，因此最多复制 2 MiB。对于管道等数据流，短读可能使简单乘法不再成立；需要完整输入块时，GNU `dd` 提供 `iflag=fullblock`。应根据本地实现区分二进制单位和后缀语法。

:::single-choice{#dd-command-count-result} 对于普通文件，`bs=1M count=2` 请求的最大数据量是多少？

::option[1 MiB。]{#dd-command-one-mib explanation="这相当于所选大小的一个块。"}
::option[2 MiB。]{#dd-command-two-mib .correct explanation="两个输入块乘以每块 1 MiB，最大为 2 MiB。"}
::option[2 GiB。]{#dd-command-two-gib explanation="在 GNU dd 中，M 后缀表示 MiB 大小的块，而不是 GiB。"}
:::

## 将映像写入块设备

原始还原命令可能如下：

```bash
$ sudo dd if=backup.img of=/dev/sdX bs=4M status=progress conv=fsync
```

`/dev/sdX` 是特意使用的占位符，不是可以原样复制执行的命令。替换它之前：

1. 为所有宝贵数据保留经过测试的备份。
2. 使用 `lsblk`、`udevadm` 或等效工具，根据型号、序列号、大小、传输方式和持久链接识别目标。
3. 确认目标分区均未挂载、未用作交换空间、未加入 RAID 或 LVM，也未被其他服务打开。
4. 每次拔插、重启或拓扑变化后，重新检查设备。
5. 确保映像能够容纳，并确认确实打算写入整个设备。

输出设备会从开头起被覆盖。颠倒 `if` 和 `of`、选中系统磁盘，或在本应选择分区时选择整盘，都可能在没有确认提示的情况下摧毁数据。

:::single-choice{#dd-command-target-verification} 原始设备写入前，验证型号、序列号、大小和活动使用情况的最重要原因是什么？

::option[设备字母可能改变，而且 `dd` 会在不了解内容的情况下覆盖所选目标。]{#dd-command-target-can-change .correct explanation="身份和使用情况检查可以降低摧毁其他磁盘或活动存储堆栈的风险。"}
::option[除非文件系统标签与映像匹配，否则 `dd` 会拒绝写入。]{#dd-command-label-check explanation="该工具不会执行这种了解文件系统的安全检查。"}
::option[只要存在任何备份，块设备就无法打开。]{#dd-command-backup-prevents-open explanation="备份不会从技术上阻止写入；经过维护和测试的备份只能提供恢复手段。"}
:::

## 创建一致的映像

在文件系统不断变化时读取实时块设备，可能产生内部不一致的映像。应优先使用未挂载的文件系统、应用程序一致性快照，或文档规定的冻结/快照流程。数据库和虚拟机可能需要各自的静默操作。

原始设备映像会复制所有块，包括文件系统元数据和未使用区域，因此它可能比文件级备份大得多，也可能复制一些标识符；将克隆与原件同时挂载前，必须更改这些标识符。

:::single-choice{#dd-command-live-filesystem-image} 为什么对已挂载且不断变化的文件系统创建映像可能不可靠？

::option[已挂载文件系统绝不允许读取块设备。]{#dd-command-mounted-no-read explanation="原始读取可能可行，因此一致性需要规划，而不能想当然。"}
::option[不同块可能读取自文件系统状态的不同时间点。]{#dd-command-inconsistent-moments .correct explanation="并发修改可能使收集到的块映像无法表示某个一致时间点。"}
::option[`dd` 会自动将文件系统转换成 tar 归档。]{#dd-command-converts-tar explanation="该工具复制原始数据，不会创建了解文件系统的归档。"}
:::

## 完成与验证

命令完成且未出现 I/O 错误，并不能证明选择了预期的来源和目标，也不能证明映像可用。应记录确切身份和大小，确保缓冲输出已经到达存储，比较范围适当的回读数据或加密哈希，并按照备份计划测试恢复。

不要宣称使用 `dd` 覆盖就能保证安全擦除 SSD、闪存转换层、精简配置存储、快照或重映射扇区。应使用设备和平台支持的清理功能，并遵循明确的数据销毁策略。

:::single-choice{#dd-command-success-meaning} `dd` 返回零退出状态，本身不能证明什么？

::option[命令解析了所有提供的操作数。]{#dd-command-parsed-operands explanation="无效操作数通常会导致错误，而不是成功完成。"}
::option[操作者选择了预期的来源和目标。]{#dd-command-does-not-prove-intent .correct explanation="该工具无法推断操作者意图，因此也可能成功复制到错误目标。"}
::option[进程到达正常终止路径。]{#dd-command-normal-exit explanation="零状态确实表示命令层面正常成功，但不能证明所选目标在语义上正确。"}
:::

接触原始硬件前，只能使用普通文件或可丢弃的虚拟磁盘练习。[管理 Linux 分区和文件系统](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845)中的分区与文件系统概念提供了必要背景。

## 总结

现在，你可以将 `dd` 理解为不了解操作者意图的原始块复制工具。

1. 区分 `if`、`of`、`bs` 和 `count`。
2. 验证持久目标身份及每个活动使用者。
3. 从一致的存储状态创建映像。
4. 复制后刷新、验证并测试恢复。
5. 将每次原始设备输出都视为可能具有破坏性的操作。
