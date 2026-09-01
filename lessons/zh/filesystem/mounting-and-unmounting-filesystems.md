---
lesson_id: "mounting-and-unmounting-filesystems"
course_id: "filesystem"
lang: "zh"
order_index: 6
title: "mount 与 umount"
description: "学习如何使用核实过的来源和挂载点附加、检查并安全分离文件系统。"
meta_title: "mount 与 umount - 文件系统"
meta_description: "学习如何在 Linux 中使用 mount 和 umount 命令来挂载和分离文件系统。本指南涵盖设备挂载、安全的 sudo umount 过程以及使用 UUID。"
meta_keywords: "挂载，卸载，sudo 卸载，umount linux, linux 卸载，debian 卸载，挂载文件系统，卸载设备，Linux UUID, 挂载点"
---

挂载会把文件系统附加到可见命名空间中的一个目录。来源可以是块设备、网络导出、虚拟文件系统、绑定挂载来源或其他实现特有的对象。目标目录称为挂载点。

## 准备并检查挂载点

本地策略要求时，创建一个用途明确的目录：

```bash
$ sudo mkdir -p /mnt/mydrive
```

挂载前先检查它：

```bash
$ findmnt --target /mnt/mydrive
$ sudo ls -la /mnt/mydrive
```

在非空目录上挂载文件系统，会把原有条目隐藏在新文件系统之后，直到卸载为止；原有条目不会被删除。这可能使应用程序困惑，并在不可见处占用磁盘空间，因此应使用空的专用挂载点。

:::single-choice{#mount-umount-nonempty-target} 在一个目录上挂载另一个文件系统后，其中已有的文件会怎样？

::option[它们会自动复制到新文件系统。]{#mount-umount-copied-files explanation="挂载改变命名空间中的附加关系，不会迁移目录内容。"}
::option[内核会永久删除它们。]{#mount-umount-erased-files explanation="这些文件只是被遮挡，卸载后通常会重新出现。"}
::option[在该挂载被分离之前，它们会被隐藏。]{#mount-umount-hidden-files .correct explanation="底层目录仍然存在，但路径查找会进入已挂载文件系统。"}
:::

## 挂载核实过的文件系统

确认来源身份、检测到的类型和预期内容后，明确执行挂载：

```bash
$ sudo mount -t ext4 /dev/VERIFIED-PARTITION /mnt/mydrive
```

`-t` 选项指定文件系统实现。Mount 通常能够检测类型，但显式指定类型并审查选项可以让意图更清楚。对于不受信任或可移动的内容，可在符合工作负载需要时考虑 `ro`、`nosuid`、`nodev` 和 `noexec` 等限制性选项；每项选项都有局限，不能当作完整沙箱。

验证实际挂载的内容：

```bash
$ findmnt --target /mnt/mydrive -o TARGET,SOURCE,FSTYPE,OPTIONS
```

挂载受命名空间限制。在容器或私有服务命名空间中创建的挂载，可能不会出现在另一个进程的视图中。

:::single-choice{#mount-umount-mount-role} 在所示工作流程中，`mount` 命令会做什么？

::option[创建新文件系统并擦除来源。]{#mount-umount-format-source explanation="创建文件系统是独立且具有破坏性的 `mkfs` 操作。"}
::option[把文件系统来源附加到挂载命名空间中的目录。]{#mount-umount-attach-filesystem .correct explanation="之后在目标下进行路径查找时，会进入附加的文件系统。"}
::option[更改磁盘的分区边界。]{#mount-umount-change-partitions explanation="编辑分区表与命名空间挂载是不同操作。"}
:::

## 使用文件系统 UUID

`/dev/sdb2` 这样的枚举名称可能变化。可以用以下命令发现文件系统标识符：

```bash
$ lsblk -f
$ sudo blkid
```

然后按 UUID 挂载已经核实的文件系统：

```bash
$ sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mnt/mydrive
```

UUID 标识文件系统，而不一定标识物理磁盘。重新格式化会改变它，克隆则可能复制它。把原始文件系统和克隆件同时附加到一个系统前，应确认 UUID 唯一。

:::single-choice{#mount-umount-uuid-benefit} 为什么在持久配置中，文件系统 UUID 通常优于 `/dev/sdX`？

::option[它能防止所有存储设备发生故障。]{#mount-umount-uuid-no-failure explanation="标识符不提供冗余、完整性修复或备份。"}
::option[它能保证克隆的文件系统具有不同标识符。]{#mount-umount-uuid-clone-unique explanation="块级克隆会复制 UUID，从而造成冲突。"}
::option[它绑定文件系统身份，而不是当前枚举顺序。]{#mount-umount-uuid-identity .correct explanation="块设备路径可能改变，而文件系统元数据仍保留其 UUID。"}
:::

## 安全卸载

使用准确的挂载点进行分离：

```bash
$ sudo umount /mnt/mydrive
```

命令拼写为 `umount`，开头没有第一个 `n`。成功卸载表示内核完成了必要的回写，并在引用允许时分离文件系统。拔出存储设备前，应使用 `findmnt` 再次确认。

对于可移动介质，成功卸载不一定就是安全移除的最后一步。桌面存储栈可能提供弹出或断电操作，用于刷新设备缓存并禁用 USB 设备。应遵循平台和硬件的工作流程。

:::single-choice{#mount-umount-command-name} 哪个命令会分离 `/mnt/mydrive`？

::option[`umount /mnt/mydrive`]{#mount-umount-umount-correct .correct explanation="`umount` 会分离挂载到指定目标的文件系统。"}
::option[`unmount /mnt/mydrive`]{#mount-umount-unmount-spelling explanation="标准命令名称省略了第一个 `n`。"}
::option[`mkfs /mnt/mydrive`]{#mount-umount-mkfs-target explanation="Mkfs 用于创建文件系统结构，绝不能用来分离挂载。"}
:::

## 诊断繁忙的文件系统

如果命名空间中仍有活动引用，卸载会失败，例如打开的文件、进程工作目录、嵌套挂载、交换空间或其他存储层。应调查原因，而不是立即强制卸载：

```bash
$ findmnt --submounts /mnt/mydrive
$ sudo fuser -vm /mnt/mydrive
```

让 shell 离开该目录树，干净地停止相关应用程序，并先卸载子挂载再卸载父挂载。延迟卸载和强制选项有专门语义，可能留下活动引用或造成数据丢失；只有在具备文档支持的恢复理由时才能使用。

:::single-choice{#mount-umount-busy-cause} 哪种情况会让 `umount` 报告文件系统繁忙？

::option[挂载点目录名包含小写字母。]{#mount-umount-lowercase explanation="路径大小写本身不会创建活动文件系统引用。"}
::option[某个进程的当前工作目录位于该挂载中。]{#mount-umount-cwd-busy .correct explanation="该进程保留了指向已挂载文件系统的引用，从而阻止普通分离。"}
::option[文件系统 UUID 比设备名更长。]{#mount-umount-uuid-length explanation="标识符字符串长度与繁忙状态检查无关。"}
:::

可以在[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)实验指定的可丢弃存储上练习。

## 总结

现在，你可以在可验证的范围内附加和分离文件系统。

1. 使用空的专用挂载点。
2. 核实来源、类型、选项和最终挂载结果。
3. 在持久引用中优先使用唯一的文件系统标识符。
4. 按目标卸载，并在移除设备前确认已经分离。
5. 诊断活动引用，而不是强制卸载繁忙的文件系统。
