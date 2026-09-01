---
lesson_id: "boot-process-bios"
course_id: "boot-system"
lang: "zh"
order_index: 2
title: "启动过程：BIOS"
description: "了解传统 BIOS 与现代 UEFI 固件如何定位并授权下一个启动阶段。"
meta_title: "启动过程：BIOS - 系统启动"
meta_description: "探索 Linux 启动过程的第一步：BIOS。了解它如何通过 MBR 或 GPT 查找引导加载程序，并理解 UEFI 的作用。本指南解释系统启动，并涉及如何进入 BIOS 进行配置。"
meta_keywords: "Linux 启动过程，BIOS, MBR, UEFI, Linux 中的 bios, bios linux, 如何进入 bios, 引导加载程序，系统启动"
---

固件在 Linux 内核运行前执行。PC 类硬件上的两种主要接口是传统 BIOS 和 UEFI。它们采用不同的启动发现模型，因此“BIOS 读取引导加载程序”只能描述其中一条路径。

## 传统 BIOS 启动

完成早期平台初始化和启动设备选择后，传统 BIOS 通常读取选定磁盘的第一个 512 字节扇区；如果该扇区具有预期签名，就把控制权交给其中的启动代码。

在 MBR 布局中，该扇区包含一小段启动代码、四个分区条目和一个签名。其代码空间不足以容纳功能丰富的加载程序，因此通常会在磁盘其他位置或文件系统中寻找后续阶段。

BIOS 可以从 GPT 磁盘启动，但保护性 MBR 本身并不提供加载程序的后续阶段。GRUB 通常在 GPT 上使用一个较小的 BIOS 启动分区来嵌入核心代码。具体布局由已安装加载程序决定。

:::single-choice{#boot-bios-legacy-first-sector} 传统 BIOS 通常首先从选定启动磁盘加载什么？

::option[包含少量启动代码的初始启动扇区。]{#boot-bios-boot-sector .correct explanation="固件的传统磁盘路径会把控制权交给选定磁盘第一个扇区中的代码。"}
::option[把整个 Linux 根文件系统载入固件内存。]{#boot-bios-entire-root explanation="第一阶段扇区很小，后续软件才会定位内核和根存储。"}
::option[`/etc` 下的每个用户服务配置。]{#boot-bios-etc-config explanation="固件不会解析已安装系统的完整服务配置。"}
:::

## UEFI 启动

UEFI 固件能够理解 EFI 系统分区（ESP）上规定的文件系统，并加载 EFI 可执行文件。存储在非易失性变量中的固件启动条目通常会标识磁盘、分区和可执行文件路径。可移动介质或恢复场景还可以使用标准化后备路径。

ESP 包含启动应用及其辅助文件，而不是“所有启动信息”。内核映像、initramfs 文件和加载程序配置可以位于其中，也可以根据启动设计放在其他位置。UEFI 系统通常使用 GPT，但固件接口与分区表方案仍是不同层次。

:::single-choice{#boot-bios-uefi-esp} UEFI 通常从 EFI 系统分区加载什么？

::option[由固件启动条目选中的 EFI 可执行文件。]{#boot-bios-efi-executable .correct explanation="UEFI 启动管理让固件指向受支持系统分区上的可执行文件。"}
::option[任意 ext4 家目录中的 POSIX shell 脚本。]{#boot-bios-shell-script explanation="固件从受支持启动路径加载规定的可执行格式，而不会运行普通用户 shell。"}
::option[包含用户账户的 MBR 扩展分区。]{#boot-bios-extended-users explanation="账户数据与 UEFI 可执行文件发现无关。"}
:::

## 安全启动与信任

启用安全启动后，UEFI 会根据已登记的平台密钥和策略验证启动链中的签名。Linux 发行版可以使用已签名的 shim、引导加载程序、内核和内核模块策略来延伸这条信任链。

安全启动不会加密磁盘，也不能证明每个用户空间程序都安全。它有助于阻止配置的信任策略接受未经授权的预启动代码。

:::single-choice{#boot-bios-secure-boot-purpose} UEFI 安全启动主要实施什么？

::option[自动加密每块磁盘上的每个文件。]{#boot-bios-secure-encryption explanation="磁盘保密性需要独立的加密系统。"}
::option[根据签名授权启动链可执行文件。]{#boot-bios-secure-signatures .correct explanation="固件和后续已验证组件根据已登记密钥与策略接受代码。"}
::option[保证已签名软件完全没有漏洞。]{#boot-bios-secure-no-vulnerabilities explanation="有效签名证明授权和完整性，而不是代码毫无缺陷。"}
:::

## 进入固件设置

进入固件设置的按键因制造商和型号而异，常见按键包括启动早期使用 Delete、Escape 或某个功能键。应查阅设备文档，不要随机尝试更改。某些 UEFI 系统也提供由操作系统请求重启到固件设置的功能。

更改安全启动、存储控制器模式、TPM、虚拟化或启动顺序前，应记录现有值和恢复密钥。固件变更可能让加密卷或已安装操作系统暂时无法访问。

:::single-choice{#boot-bios-setup-key} 为什么不存在进入固件设置的通用按键？

::option[Linux 每次启动后都会随机分配新按键。]{#boot-bios-random-key explanation="操作系统不会随机定义固件早期启动按键。"}
::option[按键和触发时机由系统制造商决定。]{#boot-bios-vendor-key .correct explanation="不同型号的固件接口各不相同，因此需要权威设备文档。"}
::option[只有删除引导加载程序才能进入设置。]{#boot-bios-delete-loader explanation="固件设置与破坏已安装启动文件无关。"}
:::

## 总结

现在，你可以区分传统 BIOS 与 UEFI 的启动发现模型。

1. 把传统 BIOS 与首扇区启动代码及后续加载阶段联系起来。
2. 把 UEFI 启动条目与 ESP 上的 EFI 可执行文件联系起来。
3. 将 GPT、固件接口和引导加载程序布局视为不同选择。
4. 只有保留恢复路径时，才能更改固件信任和存储设置。
