---
lesson_id: "udev"
course_id: "devices"
lang: "zh"
order_index: 5
title: "udev"
description: "学习 udev 如何处理内核设备事件，以应用策略、权限和持久链接。"
meta_title: "udev - 设备"
meta_description: "了解 udev 如何动态管理 Linux 设备文件，以及如何使用 udevadm，帮助初学者理解设备节点创建。"
meta_keywords: "udev, udevadm, Linux 设备管理, 设备文件, Linux 教程, Linux 初学者, udev 规则, Linux 指南"
---

Linux 内核通过 uevent 向用户空间报告设备变化。在许多现代发行版上，`systemd-udevd` 使用 udev 规则和设备数据库处理这些事件。它与由内核填充的 `devtmpfs` 共同产生应用程序在 `/dev` 周围看到的所有权、权限、属性和符号链接。

## 从内核事件到设备策略

添加、更改、移动或移除设备时，udev 可以：

- 从 sysfs 和事件属性读取信息
- 将所有者、组和模式策略应用到设备节点
- 添加 `/dev/disk/by-id/...` 等稳定符号链接
- 为其他服务标记设备
- 运行范围有限的辅助处理

内核仍负责实际设备及其驱动程序。从 `/dev` 删除节点不会在物理上移除硬件，使用 `mknod` 手动创建设备节点也不会让不受支持的硬件凭空出现或绑定驱动程序。

:::single-choice{#udev-kernel-event-input}
什么通常会触发 udev 处理设备变化？

::option[APT 执行的软件包仓库刷新。]{#udev-apt-refresh explanation="软件包元数据更新与实时设备事件处理无关。"}
::option[用户手动重命名 `/dev` 下的每个文件。]{#udev-manual-renaming explanation="动态策略由内核事件和规则驱动，而不是由批量手动重命名驱动。"}
::option[描述设备操作的内核 uevent。]{#udev-kernel-uevent .correct explanation="udev 从内核接收设备事件，并应用匹配的用户空间规则。"}
:::

## 规则位置与优先级

规则通常位于：

- `/usr/lib/udev/rules.d/`：厂商或软件包提供的规则
- `/run/udev/rules.d/`：易失的运行时规则
- `/etc/udev/rules.d/`：本地管理员策略

文件按文件名的词法顺序处理；根据已安装 udev 实现的规则，高优先级目录中的同名文件会替换低优先级版本。本地规则应使用经过考虑的文件名，并匹配稳定属性，而不是枚举名称。

一条规则可能影响所有匹配设备，因此要仔细测试作用范围。当本地覆盖规则或补充规则足以满足需求时，不要直接编辑软件包提供的规则。

:::single-choice{#udev-local-rules-directory}
哪个目录用于存放持久的本地管理员 udev 规则？

::option[`/proc/udev/rules.d/`]{#udev-proc-rules explanation="procfs 不提供持久的本地规则目录。"}
::option[`/etc/udev/rules.d/`]{#udev-etc-rules .correct explanation="本地策略应位于 /etc 下，与软件包管理的厂商规则分开。"}
::option[`/dev/udev/rules.d/`]{#udev-dev-rules explanation="/dev 包含运行时面向设备的对象，而不是持久规则配置。"}
:::

## 使用 `udevadm` 检查设备

查询现有节点的 udev 属性：

```bash
$ udevadm info --query=all --name=/dev/sda
```

应使用当前系统上实际存在的节点。`udevadm info --attribute-walk --name=...` 可以显示 sysfs 父级链上的属性，有助于构造规则。`udevadm monitor --kernel --udev --property` 会观察内核事件和处理后的事件；输出可能暴露设备标识符，因此要妥善处理捕获内容。

:::single-choice{#udev-info-purpose}
`udevadm info --query=all --name=/dev/sda` 请求什么？

::option[以破坏性方式重写磁盘分区表。]{#udev-info-partition-write explanation="该查询属于检查操作，不会格式化存储或重新分区。"}
::option[从互联网安装缺失的内核驱动程序。]{#udev-info-install-driver explanation="udevadm 检查不会充当软件下载工具。"}
::option[查询指定设备节点的已知 udev 属性。]{#udev-info-properties .correct explanation="info 命令查询设备数据库及相关 sysfs 信息。"}
:::

## 谨慎应用规则变更

重新加载规则文件会影响未来的事件处理，但不会自动重建每个现有设备的状态。手动触发事件可能影响许多设备和服务，因此应缩小目标范围，并查阅已安装 `udevadm` 的文档。测试命令可以模拟规则评估，但可能无法重现真实事件的每项副作用。

更改权限或名称前，应备份本地规则、验证语法、观察一个已知测试设备，并保留恢复通道。不要直接在 udev 事件处理中运行耗时工作；应将其交给适当的服务。

:::single-choice{#udev-reload-effect}
重新加载 udev 规则主要会改变什么？

::option[后续匹配设备事件的处理方式。]{#udev-future-events .correct explanation="重新加载会更新内存中的规则；设备仍需发生事件或被有意触发，才会重新评估。"}
::option[每个已连接设备的物理接线。]{#udev-physical-wiring explanation="加载软件规则无法改变硬件连接。"}
::option[无论事件或匹配条件如何都改变每个现有设备节点。]{#udev-all-existing explanation="仅重新加载并不能保证立即重新评估所有当前设备。"}
:::

可通过[在 Linux 中探索硬件设备](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)，在受控环境中关联 `udevadm` 属性、sysfs 路径和 `/dev` 链接。

## 总结

现在，你可以把 udev 置于内核事件与用户空间设备策略之间来理解。

1. 理解 uevent 和 sysfs 属性与 udev 规则匹配的关系。
2. 区分厂商、运行时和本地规则位置。
3. 使用 `udevadm` 检查属性和事件流。
4. 仅在范围明确且经过测试时重新加载并触发规则。
