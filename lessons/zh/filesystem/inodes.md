---
lesson_id: "inodes"
course_id: "filesystem"
lang: "zh"
order_index: 11
title: "Inode"
description: "了解 inode 编号如何把目录名称与文件系统对象的元数据和数据联系起来。"
meta_title: "Inode - 文件系统"
meta_description: "探索 Linux inode 的概念。了解 i-node 是什么、Linux 中的 inode 如何管理文件元数据，以及如何使用 `df -i` 和 `ls -li` 检查 inode 使用情况。"
meta_keywords: "linux inode, linux 索引节点，i 节点，inode, inode linux, inode 编号，文件系统，df -i, ls -li, stat"
---

在基于 inode 的 Unix 文件系统中，目录会把每个条目名称映射到一个 inode 编号。Inode 表示文件系统对象，并记录定位和解释其数据所需的元数据。因此，路径名并不作为对象自身的主要身份存储。

## Inode 存储的元数据

通常与 inode 关联的元数据包括：

- 对象类型和权限模式
- 用户和组所有权
- 逻辑大小与已分配数据块统计
- 硬链接数
- 访问、修改和状态变更时间戳
- 指向文件数据或文件系统特定区段结构的引用

Inode 通常不存储目录条目名称。文件系统还可能通过特定格式的结构保存扩展属性、访问控制列表、创建时间、内联数据或其他信息。

`ctime` 是 inode 状态变更时间，不一定是文件创建时间。单独的出生或创建时间戳是可选的，可能并不存在。

:::single-choice{#inodes-name-location} 普通文件的路径名组成部分通常在哪里与其 inode 编号关联？

::option[在进程调度器中。]{#inodes-scheduler-name explanation="CPU 调度状态并不实现文件系统路径名查找。"}
::option[在目录条目中。]{#inodes-directory-entry .correct explanation="目录会把名称映射到同一文件系统中的 inode 编号。"}
::option[在磁盘分区表中。]{#inodes-partition-name explanation="分区表映射存储区域，而不是单个文件名。"}
:::

## Inode 编号与文件系统范围

使用以下命令显示 inode 编号：

```bash
$ ls -li
```

第一个字段就是 inode 编号。可以用以下命令更详细地检查一个对象：

```bash
$ stat path
```

Inode 编号只在某个文件系统的特定时刻内唯一。另一个文件系统可以使用相同编号，inode 释放后也可能复用该编号。要稳健地标识对象，应同时使用文件系统身份和 inode 编号，而不能只看 inode 编号。

:::single-choice{#inodes-number-scope} Inode 编号在哪个范围内可以作为对象标识符？

::option[永久适用于世界上的每一台 Linux 系统。]{#inodes-global-forever explanation="Inode 分配局限于单个文件系统，而且标识符可以复用。"}
::option[某个文件系统的某个特定时刻。]{#inodes-one-filesystem .correct explanation="其他文件系统可以使用相同编号，释放后的 inode 编号也可能再次使用。"}
::option[只适用于创建文件的 shell 进程。]{#inodes-shell-scope explanation="Inode 身份由文件系统维护，而不是由某个 shell 维护。"}
:::

## 硬链接与打开引用

多个目录条目可以指向同一个 inode，这些条目称为硬链接。创建另一个硬链接会增加对象的链接数。只要仍有其他链接存在，移除一个名称只会减少链接数，不会删除数据。

即使最后一个目录条目已经删除，只要文件仍处于打开状态，它就会继续占用空间，直到最后一个进程引用关闭。其链接数可以为零，但文件描述符仍能访问它。这解释了为什么删除仍处于打开状态的大型日志后，`df` 用量可能不会立即下降。

:::single-choice{#inodes-unlinked-open-file} 已取消链接文件的资源通常在何时释放？

::option[任意一个硬链接名称被移除后立即释放。]{#inodes-one-link-removed explanation="其他硬链接或打开引用仍可能让对象保持有效。"}
::option[只有重新格式化整个文件系统后才释放。]{#inodes-reformat-only explanation="正常的取消链接和关闭操作会回收不再使用的 inode 与数据块。"}
::option[链接数归零且最后一个打开引用关闭后。]{#inodes-zero-links-no-opens .correct explanation="目录名称和进程文件描述符是彼此独立的 inode 引用。"}
:::

## Inode 容量

对于 inode 池有限或能够报告 inode 容量的文件系统，数百万个小文件可能在数据块填满前耗尽元数据容量。使用以下命令检查已挂载文件系统的 inode 统计：

```bash
$ df -i
```

如果没有可用 inode，即使 `df -h` 显示还有可用数据块，创建文件也可能失败。分配策略有所不同：某些文件系统在创建时预分配 inode 结构，另一些动态管理元数据，并可能以不同方式报告 inode 容量。

:::single-choice{#inodes-df-i-purpose} 对于提供 inode 统计的文件系统，`df -i` 报告什么？

::option[按 inode 顺序显示每个文件的内容。]{#inodes-df-i-content explanation="Df 报告文件系统汇总统计，不会读取文件内容。"}
::option[已用和可用的 inode 容量。]{#inodes-df-i-capacity .correct explanation="Inode 视图有助于独立于数据块诊断元数据对象耗尽。"}
::option[磁盘固件版本。]{#inodes-df-i-firmware explanation="固件清单与 inode 用量无关。"}
:::

## 文件系统特有的数据映射

不要假设每个 inode 都严格包含 12 个直接指针和 3 个间接指针。这可以描述某些经典文件系统布局，但现代 ext4 可以使用区段，XFS、Btrfs 和其他文件系统也采用不同结构。内联数据、压缩区段或写时复制区段会进一步改变这种关系。

需要研究内部映射时，只能以只读模式或文档规定的模式使用文件系统专用诊断工具。对于普通管理，`stat`、`find -inum`、`df -i` 和能够识别链接的工具提供了更安全的抽象。

:::single-choice{#inodes-layout-portability} 为什么不能假设每个 inode 都采用同一种固定指针布局？

::option[Inode 从不以任何方式引用文件数据。]{#inodes-no-data-reference explanation="文件系统必须把对象与其内容关联，只是机制有所不同。"}
::option[不同文件系统实现使用不同的区段、树和内联数据结构。]{#inodes-format-specific-layout .correct explanation="从 inode 到内容的磁盘映射属于各文件系统格式的一部分。"}
::option[每个 inode 的布局都由文件所有者单独选择。]{#inodes-owner-layout explanation="元数据结构由文件系统实现和格式决定。"}
:::

可以在[在 Linux 中管理文件和目录](https://labex.io/zh/labs/comptia-manage-files-and-directories-in-linux-590835)实验中，使用可丢弃文件比较 inode 编号和链接数。

## 总结

现在，你可以理解路径名、inode、链接与文件系统容量之间的关系。

1. 将目录条目视为从名称到 inode 编号的映射。
2. 阅读元数据和时间戳时，不要把 ctime 误认为创建时间。
3. 把 inode 编号限定在一个文件系统和某个时刻内。
4. 同时考虑硬链接和打开的文件描述符。
5. 使用文件系统特有模型，而不是套用一种通用指针布局。
