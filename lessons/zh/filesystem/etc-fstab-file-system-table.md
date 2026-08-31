---
lesson_id: "etc-fstab-file-system-table"
course_id: "filesystem"
lang: "zh"
order_index: 7
title: "/etc/fstab"
description: "学习如何在 `/etc/fstab` 中定义持久的文件系统和交换空间附加关系，并安全验证配置。"
meta_title: "/etc/fstab - 文件系统"
meta_description: "了解如何在 Linux 中使用 /etc/fstab 文件在启动时自动挂载文件系统。本指南涵盖 fstab 语法、如何安全编辑 etc fstab 文件及其在系统启动中的作用。"
meta_keywords: "fstab, fstab linux, etc fstab, /etc/fstab, fstab 文件，挂载文件系统，Linux 启动，fstab 教程"
---

`/etc/fstab` 即文件系统表，用于声明文件系统、交换区域、绑定挂载、网络来源和其他可由系统工具挂载或激活的附加关系。条目可以参与启动流程，但 `noauto` 等选项、自动挂载集成和服务管理器策略会影响它们何时或是否生效。

## 六个字段

传统条目包含六个由空白分隔的字段：

```text
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /data ext4 defaults,nosuid,nodev 0 2
```

1. **来源**：设备路径、`UUID=`、`LABEL=`、网络来源或其他受支持的说明。
2. **目标**：挂载点；对于交换空间等合适用途，可以是 `none`。
3. **类型**：文件系统类型、`swap`、`none` 或受支持的自动类型。
4. **选项**：由挂载辅助程序和集成层解释的逗号分隔列表。
5. **Dump 字段**：历史上用于控制 `dump` 备份工具；`0` 通常表示不参与。
6. **Pass 字段**：在适用时控制启动期间的 `fsck` 顺序；`0` 表示不通过此机制自动检查。

字段内部的空白必须使用 fstab 语法转义，例如用 `\040` 表示空格。字段外的 `#` 表示注释开始。

:::single-choice{#fstab-field-count}
普通 `/etc/fstab` 条目包含多少个字段？

::option[四个。]{#fstab-four-fields explanation="来源、目标、类型和选项后面还有 dump 与 pass 字段。"}
::option[八个。]{#fstab-eight-fields explanation="八个并不是单条 fstab 记录的标准字段数。"}
::option[六个。]{#fstab-six-fields .correct explanation="传统格式包含来源、目标、类型、选项、dump 和 pass 字段。"}
:::

## 稳定的来源标识符

对于本地文件系统，文件系统 UUID 通常比 `/dev/sdX` 枚举更稳定：

```bash
$ lsblk -f
$ sudo blkid
```

只有确认标识符属于预期文件系统后，才能使用 `UUID=...`。重新格式化会创建新 UUID，块级克隆则可能复制原有 UUID。`PARTUUID=` 标识的是分区表条目，语义与之不同。

:::single-choice{#fstab-uuid-source}
来源字段中的 `UUID=...` 通常标识什么？

::option[拥有挂载点的用户账户。]{#fstab-user-uuid explanation="账户身份不是通过文件系统 UUID 来源语法选择的。"}
::option[携带该 UUID 的文件系统元数据。]{#fstab-filesystem-uuid .correct explanation="Mount 会把文件系统标识符解析到可用块设备，而不依赖枚举名称。"}
::option[最后卸载该文件系统的进程。]{#fstab-process-uuid explanation="此来源字段不会编码进程历史。"}
:::

## 挂载选项与检查字段

`defaults` 会展开为实现定义的一组传统选项，并不一定是每个挂载最安全的策略。应根据信任程度和工作负载添加选项，例如只读访问，或限制设备节点和 setuid 行为。网络及可移动文件系统可能需要超时、依赖或容错策略，以免启动意外停滞。

对于 `fsck` 支持的文件系统，根文件系统传统上使用 pass `1`，其他受检查的本地文件系统使用 `2`。不同文件系统的惯例可能不同，例如某些类型不使用通用的启动期 fsck，因此应遵循已安装文件系统和发行版的文档，而不要机械地填写 `2`。

:::single-choice{#fstab-pass-zero}
第六个字段为 `0` 时请求什么？

::option[该条目不参与 fstab 控制的自动 fsck 顺序。]{#fstab-pass-zero-skip .correct explanation="Pass 为零会把条目排除在此字段控制的启动检查序列之外。"}
::option[在任何情况下都以只读方式挂载文件系统。]{#fstab-pass-zero-readonly explanation="只读行为属于挂载选项字段。"}
::option[每次启动前擦除文件系统。]{#fstab-pass-zero-erase explanation="Pass 字段不会格式化或擦除文件系统。"}
:::

## 在保留恢复路径的前提下编辑

无效的根目录、启动目录或必要网络条目可能中断启动。编辑前：

1. 确认已有当前备份，并具备控制台或救援访问方式。
2. 在保留权限的情况下复制现有文件。
3. 核实来源身份，并创建预期挂载点。
4. 每次只进行一项限定范围的更改。
5. 重启前先验证和测试。

不要把凭据直接写进所有用户可读的 fstab 条目。应使用相关挂载辅助程序提供的受保护凭据机制。

:::single-choice{#fstab-editing-recovery}
为什么更改关键 fstab 条目前应确认救援访问方式？

::option[编辑 fstab 总会立即擦除分区表。]{#fstab-no-partition-erase explanation="编辑文本本身不会重写磁盘分区，不过之后的挂载可能产生实际影响。"}
::option[此文件只能从另一个操作系统编辑。]{#fstab-other-os-only explanation="具备适当权限和保护措施时，可以在 Linux 上编辑它。"}
::option[错误条目可能使正常启动无法进入可用系统。]{#fstab-boot-failure .correct explanation="关键挂载失败可能进入紧急模式，或阻止依赖服务启动。"}
:::

## 验证但不预设成功

在支持的系统上，先进行静态检查：

```bash
$ sudo findmnt --verify --verbose
```

然后在受控条件下测试特定新条目，用 `findmnt` 确认；如果只是临时测试，再卸载它。`mount -a` 会尝试许多符合条件的条目，可能连接网络或附加非预期来源；它也会跳过已挂载和 `noauto` 条目，因此既不是无害的语法检查器，也不是完整证明。

在基于 systemd 的系统上，编辑 fstab 后应重新加载管理器配置，使生成的挂载单元得到刷新，再按照本地文档验证依赖和启动行为。

:::single-choice{#fstab-mount-a-limit}
为什么单独使用 `mount -a` 不能完整验证 fstab？

::option[它总会在挂载前重新格式化所有列出的设备。]{#fstab-mount-a-formats explanation="Mount 通常不会创建文件系统。"}
::option[它可能跳过条目，并执行范围广泛的真实挂载，而不只是检查语法。]{#fstab-mount-a-incomplete .correct explanation="已挂载或 `noauto` 记录可能不会被测试，而其他符合条件的来源会产生实际影响。"}
::option[它只读取 shell 历史，完全忽略 fstab。]{#fstab-mount-a-history explanation="该命令确实会读取 fstab 中符合条件的条目。"}
:::

请在[管理 Linux 分区和文件系统](https://labex.io/zh/labs/comptia-manage-linux-partitions-and-filesystems-590845)实验具备安全恢复条件的辅助存储上练习。

## 总结

现在，你可以阅读并验证持久的文件系统表条目。

1. 解析来源、目标、类型、选项、dump 和 pass 字段。
2. 选择经过核实且身份语义符合预期的标识符。
3. 根据实际文件系统选择挂载和检查策略。
4. 保留救援访问方式，并进行单项限定更改。
5. 结合静态验证、定向挂载和启动策略检查。
