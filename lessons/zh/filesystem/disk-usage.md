---
lesson_id: "disk-usage"
course_id: "filesystem"
lang: "zh"
order_index: 9
title: "磁盘用量"
description: "了解 `df` 和 `du` 如何从不同角度衡量文件系统数据块与 inode 消耗。"
meta_title: "磁盘用量 - 文件系统"
meta_description: "学习使用 df 和 du 命令检查 Linux 磁盘使用情况和可用空间。本指南涵盖如何分析磁盘空间，包括使用 df -i linux 检查 inode 使用情况，以及查找哪些文件占用了空间。"
meta_keywords: "df 命令，du 命令，Linux 磁盘使用情况，检查可用空间，df -i linux, 磁盘管理，Linux 教程，磁盘利用率，文件系统使用"
---

文件系统容量至少受到两类资源限制：数据块，以及 inode 等元数据对象。`df` 从文件系统角度报告分配情况，`du` 则遍历可达路径名并汇总归属于它们的用量。两者回答的问题不同，结果不必一致。

## 使用 `df` 查看文件系统容量

以下命令显示已挂载文件系统类型和便于阅读的数据块数值：

```bash
$ df -hT
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda1      ext4  6.2G  2.3G  3.6G  40% /
```

`Size`、`Used` 和 `Avail` 来自文件系统统计。由于保留块、元数据、分配策略、配额或舍入，可用空间可能小于总量减去已用量。对某个路径运行 `df`，可以报告包含该路径的文件系统：

```bash
$ df -hT /var/log
```

:::single-choice{#disk-usage-df-scope}
`df` 主要报告什么？

::option[一个目录中每个文件的字节内容。]{#disk-usage-df-file-content explanation="目录树统计属于 `du` 等工具的职责。"}
::option[文件系统级容量、已用空间和可用空间。]{#disk-usage-df-filesystem .correct explanation="Df 查询已挂载文件系统的分配统计，而不是遍历每个路径名。"}
::option[只报告磁盘标签上印刷的物理容量。]{#disk-usage-df-physical-label explanation="其数值描述文件系统统计，而不只是硬件宣传容量。"}
:::

## Inode 容量

采用 inode 类对象的文件系统即使仍有数据块，也可能耗尽 inode：

```bash
$ df -i /var
```

大量小文件可能耗尽可用 inode。删除一个大文件可以释放许多数据块，但通常只释放一个 inode；删除大量不再需要的小文件则有助于缓解 inode 压力。某些文件系统动态分配元数据，并以不同方式报告这些概念。

:::single-choice{#disk-usage-inode-exhaustion}
文件系统仍有可用数据块、但没有可用 inode 时，可能发生什么？

::option[所有现有文件都会自动变成原来的两倍大。]{#disk-usage-inode-double explanation="Inode 耗尽会阻止分配新元数据，不会扩大现有内容。"}
::option[创建新文件可能失败。]{#disk-usage-inode-create-fail .correct explanation="即使仍有空间保存文件数据，新的文件系统对象也需要元数据。"}
::option[文件系统会转换成交换空间。]{#disk-usage-inode-swap explanation="资源耗尽不会改变文件系统类型。"}
:::

## 使用 `du` 查看路径用量

汇总某个目录下可达内容分配的空间：

```bash
$ du -sh /var/log
```

在不跨越文件系统的情况下比较直接子项：

```bash
$ sudo du -xhd1 /var | sort -h
```

这里所示的 GNU 选项分别表示便于阅读的输出、最大深度一层，以及只遍历一个文件系统。权限可能隐藏子树，使总数不完整。默认情况下，`du` 也可能只统计一次硬链接文件；它还能区分表观大小与已分配数据块，并会根据选项以不同方式处理稀疏文件。

:::single-choice{#disk-usage-du-purpose}
哪个命令汇总 `/var/log` 下已分配的用量？

::option[`df -i /var/log`]{#disk-usage-df-inodes explanation="该命令报告路径所在文件系统的 inode 统计。"}
::option[`du -sh /var/log`]{#disk-usage-du-summary .correct explanation="Du 遍历指定目录树，`-s` 以便于阅读的单位输出一项汇总。"}
::option[`mount -a /var/log`]{#disk-usage-mount-a explanation="挂载与只读目录用量汇总无关。"}
:::

## `df` 与 `du` 不一致的原因

常见原因包括：

- 进程仍然打开已删除文件，因此数据块仍被分配，但 `du` 找不到对应路径名
- 文件系统元数据、保留空间、日志、reflink、快照或压缩影响统计
- 遍历的目录树中挂载了另一个文件系统
- 权限阻止 `du` 读取某些目录
- 稀疏文件的表观大小与已分配大小不同

对于已删除但仍打开的文件，可以使用 `lsof +L1` 等工具检查已获授权的进程。应通过常规流程重启相关服务或向其发送信号，而不要截断未知文件描述符。

:::single-choice{#disk-usage-deleted-open-file}
为什么 `df` 可能显示仍有空间被占用，而基于路径名的 `du` 找不到它？

::option[`df` 总会把每个文件大小乘以二。]{#disk-usage-df-doubles explanation="不存在这种通用倍增规则。"}
::option[已删除文件可能仍被运行中进程打开并占用空间。]{#disk-usage-open-deleted .correct explanation="目录条目已经消失，但在最后一个打开引用关闭前，文件系统仍会保留数据块。"}
::option[`du` 统计后会自动删除文件。]{#disk-usage-du-deletes explanation="Du 是统计工具，不会删除遍历的文件。"}
:::

## 避免让事故变得更严重

从 `df` 报告已满的文件系统开始，用 `findmnt` 确定挂载目标，再把 `du` 搜索限定在同一文件系统中逐步缩小范围。还应考虑快照、容器层、日志、软件包缓存和应用保留策略。不要只因为文件很大就删除它；应先确定其所有者、备份、合规要求和服务行为。

:::single-choice{#disk-usage-safe-investigation}
发现大文件后，最安全的处理方式是什么？

::option[在服务仍写入时立即删除。]{#disk-usage-delete-immediately explanation="这可能丢失必要数据；如果文件仍打开，也可能不会释放空间。"}
::option[对所在设备运行 `mkfs`。]{#disk-usage-mkfs-device explanation="格式化会摧毁文件系统，而不能解决单个文件增长问题。"}
::option[更改前先确认其所有者和保留用途。]{#disk-usage-review-large-file .correct explanation="仅凭大小不能证明文件可丢弃或可以安全截断。"}
:::

## 总结

现在，你可以协调文件系统统计与基于路径名的空间报告。

1. 使用 `df` 查看已挂载文件系统的数据块容量。
2. 在支持时使用 `df -i` 检查 inode 压力。
3. 使用限定范围的 `du` 遍历归属可达路径用量。
4. 调查已删除但仍打开的文件，以及文件系统特有的统计差异。
5. 删除数据前，遵循所有权和保留策略。
