---
lesson_id: "boot-process-bootloader"
course_id: "boot-system"
lang: "zh"
order_index: 3
title: "启动过程：引导加载程序"
description: "了解引导加载程序如何选择 Linux 启动内容、构造内核命令行并移交控制权。"
meta_title: "启动过程：引导加载程序 - 系统启动"
meta_description: "关于 Linux 引导加载程序的指南。了解什么是 Linux 引导加载程序、其主要功能，以及 GRUB 如何使用 initrd 和 root 等内核参数启动系统。"
meta_keywords: "linux 引导加载程序，linux 中的引导加载程序，linux 引导加载程序，grub, 什么是 linux 引导加载程序，内核参数，initrd, root 文件系统，linux 启动过程"
---

引导加载程序连接固件发现与内核执行。GRUB 常用于 Linux PC，但 systemd-boot、U-Boot、固件直接加载 EFI stub 内核等设计会实现这一角色的不同部分。

## 选择启动内容

加载程序条目可以标识：

- Linux 内核映像
- 可选的 initramfs 或传统 initrd 映像
- 内核命令行
- 平台特有元数据或另一个操作系统的加载程序

GRUB 可以显示多个内核和恢复条目。只有匹配的模块与 initramfs 仍然可用且经过测试时，后备内核才真正有用。加载程序通过自身支持的存储和文件系统模块读取文件，并不依赖尚未运行的 Linux VFS。

:::single-choice{#bootloader-primary-handoff}
Linux 引导加载程序通常把控制权交给什么？

::option[所有服务都已运行的交互式用户 shell。]{#bootloader-user-shell explanation="只有内核和 init 系统启动后，用户空间 shell 才会出现。"}
::option[加载所需启动内容后的选定内核映像。]{#bootloader-selected-kernel .correct explanation="加载程序会在执行内核入口点前准备内核、参数，通常还有 initramfs。"}
::option[用于依赖解析的文件系统包管理器。]{#bootloader-package-manager explanation="包管理并不是启动过程中下一个获得处理器控制权的阶段。"}
:::

## 内核命令行参数

加载程序传递一段文本命令行，由内核和早期用户空间解析。常见示例包括：

- `root=...`：标识预期根文件系统或早期用户空间的来源说明
- `ro` 或 `rw`：请求初始根目录挂载模式
- `quiet`：减少内核控制台消息
- `init=...`：为专门恢复请求另一个第一个用户空间程序
- 由 initramfs 工具解释的发行版特有 `rd.*` 参数

`initrd` 通常是指定映像的加载程序指令，而不是通用内核参数。`BOOT_IMAGE=` 可能出现在某些 GRUB 配置生成的命令行中，但它并不是加载内核的机制。

使用以下命令检查当前启动所用命令行：

```bash
$ cat /proc/cmdline
```

:::single-choice{#bootloader-root-parameter}
`root=` 内核命令行参数有什么用途？

::option[标识启动最终应使用的根文件系统。]{#bootloader-root-filesystem .correct explanation="内核或 initramfs 把该值作为定位和组装真实根目录的一部分来解释。"}
::option[设置 root 账户的登录密码。]{#bootloader-root-password explanation="绝不能把身份验证密钥作为普通内核命令行文本传递。"}
::option[把 PID 1 重命名为 `root`。]{#bootloader-root-pid explanation="进程命名与这个存储参数无关。"}
:::

:::single-choice{#bootloader-quiet-parameter}
`quiet` 参数通常请求什么？

::option[以只读方式访问每个已挂载文件系统。]{#bootloader-quiet-readonly explanation="初始根目录写入策略使用 `ro` 等参数，而不是 `quiet`。"}
::option[减少启动期间打印的内核消息。]{#bootloader-quiet-console .correct explanation="它会抑制许多信息性消息，但不能保证所有启动组件都完全静默。"}
::option[禁用所有硬件散热风扇。]{#bootloader-quiet-fans explanation="该参数涉及消息详细程度，而不是硬件噪声控制。"}
:::

## 临时编辑与恢复

GRUB 通常允许获授权的控制台用户编辑一个只用于本次启动的条目，常通过菜单显示的编辑按键进入。这可用于移除 `quiet`、选择恢复参数或纠正错误的根目录标识符。具体界面和授权方式有所不同，尤其是在启用安全启动或 GRUB 密码保护时。

命令行参数可能通过 `/proc/cmdline`、启动日志和崩溃报告暴露敏感文本，也可能削弱安全性或使系统无法启动。绝不能把密钥放在其中，并应保留已知可用条目和控制台恢复路径。

:::single-choice{#bootloader-temporary-edit}
在 GRUB 菜单中交互编辑条目以启动一次，通常具有什么特性？

::option[它会自动重写每个已安装内核映像。]{#bootloader-rewrites-kernels explanation="更改命令文本不会修改内核二进制文件。"}
::option[它会永久禁用所有磁盘上的固件验证。]{#bootloader-disables-firmware explanation="固件策略是独立的，并不会普遍受到单条目编辑影响。"}
::option[除非另行保存到配置，否则变更只适用于本次启动。]{#bootloader-one-boot-change .correct explanation="菜单编辑通常改变内存中的条目，而不是持久配置源。"}
:::

## 持久 GRUB 配置

发行版通常会根据模板、默认值、脚本和发现的内核生成最终 GRUB 配置。除非发行版明确规定此流程，否则不要直接编辑生成的 `grub.cfg`；重新生成可能覆盖它。

应对配置源进行一项限定范围的更改，运行发行版文档规定的重新生成命令，检查输出并测试，同时保留较旧的已知可用条目和可启动恢复介质。Debian、Fedora、UEFI 和 BIOS 安装所用命令和输出路径会有所不同。

:::single-choice{#bootloader-generated-config}
为什么直接编辑生成的 `grub.cfg` 通常不可靠？

::option[该文件绝不可能包含可读文本。]{#bootloader-config-binary explanation="GRUB 配置是文本，但仍要考虑生成文件的所有权。"}
::option[GRUB 只读取每个用户家目录中的文件。]{#bootloader-grub-home explanation="启动配置属于系统级内容，必须在用户家目录会话之前可用。"}
::option[之后重新生成配置时可能覆盖手动变更。]{#bootloader-regeneration-overwrites .correct explanation="持久设置通常应写入发行版配置源，并通过其生成流程应用。"}
:::

只能在具备恢复能力的实验环境中使用[自定义 GRUB2 引导菜单](https://labex.io/zh/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)。

## 总结

现在，你可以区分加载程序指令与内核命令行参数。

1. 识别内核、initramfs、命令行和备选条目。
2. 根据实际用途使用 `root=`、`ro` 和 `quiet`。
3. 通过 `/proc/cmdline` 检查当前启动参数。
4. 把交互编辑视为临时且涉及安全的操作。
5. 通过发行版工作流程更改持久的生成配置。
