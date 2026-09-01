---
lesson_id: "kernel-location"
course_id: "kernel"
lang: "zh"
order_index: 5
title: "内核的位置"
description: "了解发行版将内核映像、initramfs 文件、配置、符号和按版本划分的模块放在哪里。"
meta_title: "内核的位置 - 内核"
meta_description: "了解 Linux 内核存储在哪里。本指南介绍 Linux 内核在 /boot 目录中的位置，并说明 vmlinuz 和 initrd 等关键文件。"
meta_keywords: "Linux 内核位置, 内核在哪里, 内核位置, Linux 内核存储位置, vmlinuz, /boot 目录"
---

Linux 发行版通常将可启动的内核构件存放在 `/boot` 下，但 UEFI 和引导加载程序规范布局也可能把构件放在 EFI 系统分区或扩展启动分区中，并挂载到 `/boot`、`/boot/efi` 或 `/efi` 等路径。应检查挂载点和加载程序配置，而不是假定所有系统都使用同一路径。

## `/boot` 下按版本划分的文件

传统的发行版布局可能包含：

- `vmlinuz-KERNEL_RELEASE`：可启动的 Linux 内核映像
- `initrd.img-KERNEL_RELEASE` 或 `initramfs-KERNEL_RELEASE.img`：早期用户空间映像
- `config-KERNEL_RELEASE`：构建该发行版内核时使用的配置
- `System.map-KERNEL_RELEASE`：内核构建生成的符号地址映射

具体名称各不相同。现代发行版中，名称带 `initrd` 的文件通常包含 initramfs 归档。`vmlinuz` 这一命名惯例并不能说明确切的内部压缩方式或平台启动格式；应使用发行版工具检查。

:::single-choice{#kernel-location-vmlinuz} 带版本号的 `vmlinuz-*` 文件通常包含什么？

::option[可启动的 Linux 内核映像。]{#kernel-location-kernel-image .correct explanation="引导加载程序或固件会加载这一与架构相关的内核构件。"}
::option[所有已安装内核的全部可加载模块。]{#kernel-location-all-modules explanation="模块单独存放在特定内核版本的模块树中。"}
::option[上次启动期间的用户 shell 历史记录。]{#kernel-location-shell-history explanation="启动内核映像不包含个人命令历史。"}
:::

## 初始 RAM 文件系统与构建元数据

initramfs 必须包含与其匹配的内核和根存储设计在早期启动阶段所需的模块与工具。文件名匹配并不足够；过期或生成失败的文件仍可能造成无法使用的启动项。

`config-*` 有助于了解哪些功能被内置、编译为模块或省略。`System.map-*` 可辅助符号解析和调试，但地址随机化、拆分的调试信息以及发行版工具都会影响其用法。这些是辅助构件，并非替代内核。

:::single-choice{#kernel-location-initramfs-match} 为什么 initramfs 与特定内核版本和系统配置相关联？

::option[它永久保存每个已挂载文件系统的全部内容。]{#kernel-location-all-filesystems explanation="initramfs 是一个小型早期启动环境，不是完整系统备份。"}
::option[它在每次启动时为用户分配新 UID。]{#kernel-location-user-ids explanation="账户身份管理不属于它的正常职责。"}
::option[它包含该启动路径所需的早期模块和工具。]{#kernel-location-early-modules .correct explanation="模块 ABI 以及所需的存储组装组件必须与选定内核一致。"}
:::

## 按版本划分的内核模块

当前运行版本的可加载模块通常位于：

```bash
$ printf '/lib/modules/%s\n' "$(uname -r)"
```

在合并文件系统布局中，该路径可能解析到 `/usr/lib/modules/KERNEL_RELEASE`。每个已安装内核都需要兼容的模块树和依赖索引。`modprobe` 使用特定版本的元数据，而不会在整个磁盘上任意搜索 `.ko` 文件。

:::single-choice{#kernel-location-module-tree} 按照惯例，哪个目录存放当前运行内核版本的模块？

::option[`/home/modules/current/`]{#kernel-location-home-modules explanation="用户主目录不是标准的系统模块树。"}
::option[`/lib/modules/$(uname -r)/`]{#kernel-location-lib-modules .correct explanation="版本部分将各个已安装内核的模块 ABI 和依赖数据分隔开。"}
::option[`/proc/modules/files/`]{#kernel-location-proc-files explanation="/proc/modules 报告已加载模块，并不是存放模块二进制文件的目录。"}
:::

## 统一内核映像与固件路径

统一内核映像（Unified Kernel Image，UKI）是一个经过签名的 EFI 可执行文件，可以捆绑内核、initrd、命令行和元数据。UKI 通常存放在 EFI 可访问的启动位置，而不是表示为独立的 `vmlinuz` 和 initramfs 文件。

因此，传统 `/boot` 布局看起来为空，并不能证明系统未安装内核。应使用 `findmnt`、软件包数据库、启动管理器工具和加载程序配置来确定实际使用的构件。

:::single-choice{#kernel-location-uki} 统一内核映像可以组合哪些内容？

::option[GPT 标头中的所有用户主目录。]{#kernel-location-uki-homes explanation="UKI 是启动可执行文件，不是用户数据容器或分区表。"}
::option[将所有已安装软件包放进一个 shell 脚本。]{#kernel-location-uki-packages explanation="它打包的是启动组件，而不是完整的操作系统软件仓库。"}
::option[在一个 EFI 可执行文件中组合内核、initrd、命令行和元数据。]{#kernel-location-uki-components .correct explanation="这一组合构件可以参与经过签名的 UEFI 启动流程。"}
:::

## 安全管理空间

如果启动文件系统已满，应先确定已挂载的启动路径，并查询每个构件归哪个软件包所有。使用软件包管理器提供的内核清理流程，保留当前运行的内核和一个确认可用的备用内核，重新生成或检查启动项，最后验证可用空间。

不要仅根据文件年龄手动删除 `vmlinuz`、initramfs、UKI 或模块树。即使某个文件当前没有运行，它也可能是唯一可启动的恢复项。

## 总结

现在，你可以将一个内核软件包对应到它的启动构件和模块构件。

1. 检查实际的 `/boot` 和 EFI 相关挂载点。
2. 区分内核映像、initramfs、配置文件和符号映射。
3. 将模块树与确切的内核版本相匹配。
4. 考虑统一内核映像和发行版特有的布局。
5. 只有制定经过验证的软件包与备用启动方案后，才释放启动空间。
