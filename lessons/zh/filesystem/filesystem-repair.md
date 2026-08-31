---
lesson_id: "filesystem-repair"
course_id: "filesystem"
lang: "zh"
order_index: 10
title: "文件系统修复"
description: "学习如何诊断文件系统损坏，并在有备份的前提下选择特定类型的离线修复流程。"
meta_title: "文件系统修复 - 文件系统"
meta_description: "学习使用 fsck 进行 Linux 文件系统修复和数据恢复。了解如何使用此基本命令检查和修复磁盘错误。开始您的 Linux 之旅！"
meta_keywords: "fsck, 文件系统修复，Linux 命令，磁盘错误，数据恢复，Linux 教程，初学者指南"
---

文件系统修复会重写元数据，以恢复内部一致性。它可能丢弃损坏的引用或数据；存储硬件正在故障时，修复还可能加剧损失。应把修复视为恢复操作：先保留证据和可恢复数据，再使用针对准确文件系统类型编写的工具。

## 修复前先诊断

I/O 错误、重新挂载为只读、文件丢失或挂载失败等症状，并不都能证明文件系统已经损坏。先收集只读证据：

```bash
$ findmnt --target /affected/path
$ lsblk -f
$ journalctl -k -b
```

检查存储栈、设备健康状况、线缆或网络路径、RAID 状态、加密和近期事件。如果设备正在故障，反复扫描可能耗尽它剩余的寿命。可行时，应使用面向恢复的工具创建映像或克隆件，并在副本上操作。

:::single-choice{#filesystem-repair-first-response}
可能存在硬件故障时，在执行可写文件系统修复前应该做什么？

::option[反复运行每一种修复工具，直到某个工具返回零。]{#filesystem-repair-repeat-tools explanation="使用不匹配的工具并反复写入可能让损坏进一步恶化。"}
::option[立即在设备上创建新分区表。]{#filesystem-repair-new-table explanation="覆盖布局元数据会破坏证据，使恢复更加困难。"}
::option[保留可恢复数据或设备映像，并调查设备健康状况。]{#filesystem-repair-preserve-first .correct explanation="修复会改变元数据，而故障介质可能在反复访问时继续恶化。"}
:::

## 识别准确的文件系统与设备

确定文件系统是位于分区、逻辑卷、RAID 设备、加密映射还是整个磁盘上。不能仅仅因为 `/dev/sda1` 子分区受到影响，就对 `/dev/sda` 运行检查器。

使用 `lsblk -f`、`blkid`、`findmnt` 和各存储层工具映射目标。检测到的签名可能过时，因此要与已知配置和备份相互核对。

:::single-choice{#filesystem-repair-target-layer}
如果 ext4 位于 `/dev/sda1`，它的 ext4 检查器通常应该接收哪一层？

::option[无论分区表如何，都使用 `/dev/sda`。]{#filesystem-repair-whole-disk explanation="整个磁盘包含分区表和可能存在的多个子区域，并不直接包含该 ext4 实例。"}
::option[安全离线后的 `/dev/sda1`。]{#filesystem-repair-partition-target .correct explanation="检查器作用于直接包含该文件系统的块设备。"}
::option[应用仍在写入时的 `/mnt/data`。]{#filesystem-repair-live-mount explanation="挂载点路径不是检查器期望的离线块设备目标。"}
:::

## 让文件系统离线

大多数传统一致性检查器都要求文件系统已经卸载。挂载的文件系统会在检查器读取时持续变化，而修复写入可能与内核缓存状态冲突，造成损坏。

停止依赖服务、卸载嵌套文件系统、让进程工作目录离开目标，并按需停用上层结构。对于根文件系统，应启动到救援环境，或使用发行版提供的离线检查机制。通过 `findmnt` 确认目标在相关命名空间中没有挂载。

:::single-choice{#filesystem-repair-mounted-risk}
为什么通常应该先卸载文件系统，再让修复检查器写入？

::option[内核和检查器并发更新可能冲突并损坏元数据。]{#filesystem-repair-concurrent-writes .correct explanation="离线视图可以防止文件系统在修复过程中继续变化。"}
::option[卸载会自动从备份恢复每个损坏文件。]{#filesystem-repair-unmount-restores explanation="分离能为检查提供一致状态，但不是数据恢复。"}
::option[文件系统工具只能读取目录，不能读取块设备。]{#filesystem-repair-tools-directories explanation="修复工具通常直接作用于离线块设备。"}
:::

## 使用文件系统专用工具

`fsck` 是一个可以调用文件系统专用辅助程序的前端，而不是通用修复引擎。不同流程包括：ext 文件系统使用 `e2fsck`，XFS 使用 `xfs_repair`，Btrfs 则使用其专用诊断和恢复工具。

名称相似的选项可能具有不同语义，尤其不能照搬另一种文件系统指南中的 `--repair` 或强制选项。应阅读已安装工具的手册，以及当前项目或发行版恢复文档。如果实现提供可靠的无修改或诊断模式，应从该模式开始，保存输出并理解建议的修复内容。

:::single-choice{#filesystem-repair-fsck-role}
Linux 上的 `fsck` 通常负责什么？

::option[把检查工作分派给适合文件系统类型的辅助程序。]{#filesystem-repair-fsck-dispatch .correct explanation="实际验证和修复逻辑属于特定格式的工具与流程。"}
::option[检查前把所有文件系统转换为 ext4。]{#filesystem-repair-fsck-convert explanation="检查器必须保留并理解现有格式。"}
::option[修复故障硬件扇区并保证不丢失数据。]{#filesystem-repair-fsck-hardware explanation="文件系统一致性工具无法修复物理硬件，也不能保证恢复数据。"}
:::

## 验证并恢复服务

记录修复工具、版本、选项、输出和退出状态。修复后，再次检查设备健康状况；适当时先以只读方式挂载，检查关键数据并与已知备份比较。随后逐步恢复普通挂载和服务，同时监控内核与应用日志。

文件系统能够挂载，并不能证明每个文件都正确。应从备份恢复丢失或损坏的应用数据，并在应用层进行验证。

:::single-choice{#filesystem-repair-mountable-proof}
修复后成功挂载能证明所有应用数据都正确吗？

::option[不能；一致性修复与应用层数据验证是两回事。]{#filesystem-repair-not-data-proof .correct explanation="文件系统结构可能已经可以挂载，但文件或事务仍可能丢失或损坏。"}
::option[能；挂载会对照备份以加密方式验证每个文件。]{#filesystem-repair-mount-verifies explanation="普通挂载不会执行完整备份比较。"}
::option[能；修复工具会自动重建所有未知内容。]{#filesystem-repair-recreates-data explanation="元数据修复无法推断任意丢失的用户数据。"}
:::

## 总结

现在，你可以把文件系统修复规划为分阶段恢复流程。

1. 写入前诊断硬件，并保留可恢复数据。
2. 映射直接包含该文件系统的准确块设备层。
3. 让文件系统在相关命名空间中离线。
4. 使用文档规定的文件系统专用诊断和修复工具。
5. 分别验证设备健康、文件系统状态和应用数据。
