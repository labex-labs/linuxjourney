---
lesson_id: "kernel-modules"
course_id: "kernel"
lang: "zh"
order_index: 6
title: "内核模块"
description: "学习如何检查、加载、配置并安全移除特定 Linux 内核版本的模块。"
meta_title: "内核模块 - 内核"
meta_description: "了解 Linux 内核模块是什么以及它们如何扩展内核功能。本课介绍如何使用 lsmod 和 modprobe 按需列出、加载和卸载模块。"
meta_keywords: "什么是内核模块, Linux 内核模块, modprobe, lsmod, 内核管理, Linux 教程, Linux 入门, Linux 指南"
---

可加载内核模块是能够用驱动程序、文件系统、网络功能或其他子系统扩展正在运行内核的特权代码。模块可以避免将每个可选功能都内置到同一个内核映像中，但加载模块也会扩大可信内核的攻击面。

## 列出和检查模块

列出当前已加载的模块：

```bash
$ lsmod
```

输出来自 `/proc/modules` 等内核状态，包含模块名称、大小以及使用计数或依赖关系。看似为零的计数并不能充分证明可以安全移除；驱动程序仍可能拥有活动设备或参与子系统状态。

检查当前内核可用的某个模块：

```bash
$ modinfo MODULE_NAME
```

`modinfo` 可以显示文件名、别名、参数、许可证、描述和签名信息。应把元数据视为描述，而不是模块可信或适合当前工作负载的证明。

:::single-choice{#kernel-modules-lsmod-purpose}
`lsmod` 显示什么？

::option[远程仓库中可用的每个模块软件包。]{#kernel-modules-repository-list explanation="查询仓库清单需要使用软件包管理器。"}
::option[只显示直接编译进内核映像的驱动程序。]{#kernel-modules-builtins explanation="内置功能不是可加载模块，通常不会出现在 lsmod 中。"}
::option[当前加载到运行中内核的模块。]{#kernel-modules-loaded-list .correct explanation="该列表反映实时模块状态以及依赖关系或使用信息。"}
:::

## 使用 `modprobe` 加载

按名称加载模块：

```bash
$ sudo modprobe MODULE_NAME
```

`modprobe` 会查询 `/lib/modules/$(uname -r)/` 下当前内核的依赖索引、别名和配置。它会加载所需依赖项，并传递已配置的参数。`insmod` 则直接插入一个指定模块文件，不提供同样的依赖解析流程。

加载前，应确认模块来源、签名策略、内核版本兼容性、参数、预期硬件绑定和回滚方案。安全启动或内核锁定可能拒绝未签名模块；强行加载不兼容代码可能导致崩溃或系统失陷。

:::single-choice{#kernel-modules-modprobe-dependencies}
为什么通常优先使用 `modprobe` 而不是直接使用 `insmod`？

::option[它会让模块完全在非特权用户空间中运行。]{#kernel-modules-modprobe-userspace explanation="插入的模块会作为特权内核代码执行。"}
::option[它保证每个第三方模块都经过签名且安全。]{#kernel-modules-modprobe-guarantee explanation="是否强制签名取决于策略，而且有效签名也不能证明不存在缺陷。"}
::option[它会解析模块别名、依赖关系和配置。]{#kernel-modules-modprobe-resolves .correct explanation="modprobe 使用与当前确切内核版本对应的索引模块树。"}
:::

## 模块参数与启动时加载

持久的参数和别名策略应写入 `/etc/modprobe.d/` 下的 `.conf` 文件：

```text
options example_module mode=careful
```

该行会影响 modprobe 加载模块的方式，但本身不会请求在启动时加载模块。简单的启动时加载列表通常放在 `/etc/modules-load.d/` 下：

```text
example_module
```

硬件别名通常会触发自动加载，无需显式列表。对于早期启动阶段所需的模块，修改配置后应按照发行版规定的流程更新 initramfs。

:::single-choice{#kernel-modules-options-versus-load}
`/etc/modprobe.d/` 中的 `options` 行会做什么？

::option[仅凭该行就保证每次启动都加载模块。]{#kernel-modules-options-autoload explanation="启动时加载请求使用 modules-load 配置或设备别名等其他机制。"}
::option[设置加载指定模块时使用的参数。]{#kernel-modules-options-parameters .correct explanation="modprobe 会在插入模块时应用配置的键值参数。"}
::option[为每个已安装内核版本编译该模块。]{#kernel-modules-options-compiles explanation="配置不会构建二进制模块。"}
:::

## 黑名单及其局限

modprobe 配置可以包含：

```text
blacklist example_module
```

黑名单通常会阻止通过模块别名自动加载。它不会卸载已加载模块，不会将模块从 initramfs 中移除，也不一定能阻止按确切名称显式加载或作为依赖项加载。安全加固需要结合具体威胁，从模块可用性、签名强制、initramfs 内容、启动参数和策略等方面采取措施。

:::single-choice{#kernel-modules-blacklist-effect}
基本的 modprobe `blacklist` 行主要阻止什么？

::option[通过模块别名自动加载。]{#kernel-modules-blacklist-aliases .correct explanation="该指令并不能普遍禁止代码已经加载或可能加载的所有途径。"}
::option[执行所有名称相似的用户空间程序。]{#kernel-modules-blacklist-user-programs explanation="modprobe 配置仅用于内核模块解析。"}
::option[内置到映像中的所有内核代码。]{#kernel-modules-blacklist-builtins explanation="内置功能无法像模块一样卸载或屏蔽。"}
:::

## 安全移除模块

请求移除模块：

```bash
$ sudo modprobe -r MODULE_NAME
```

modprobe 可以根据情况移除不再使用的依赖项。当普通引用跟踪显示模块正忙时，内核会拒绝移除，但不能只依赖这一项安全检查。移除支持活动硬件的代码前，应停止服务、卸载文件系统、分离设备、让网络停止活动，并确认已有其他驱动程序或恢复通道。

绝不要在需要保持稳定的系统上强制卸载模块。移除缺陷或未完成的活动可能导致内核崩溃或数据损坏。

:::single-choice{#kernel-modules-remove-command}
哪个命令会按名称请求以依赖感知方式移除模块？

::option[`lsmod -r MODULE_NAME`]{#kernel-modules-lsmod-remove explanation="lsmod 是只读列表工具，不负责移除模块。"}
::option[`uname -r MODULE_NAME`]{#kernel-modules-uname-remove explanation="uname 报告内核信息，不管理模块。"}
::option[`modprobe -r MODULE_NAME`]{#kernel-modules-modprobe-remove .correct explanation="移除模式会考虑请求模块周围已建立索引的依赖关系。"}
:::

可通过[在 Linux 中管理内核模块](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865)，练习操作实验指定的安全模块。

## 总结

现在，你可以在充分考虑内核级风险的前提下管理模块。

1. 使用 `lsmod` 查看实时状态，使用 `modinfo` 查看可用元数据。
2. 使用 `modprobe` 按别名和依赖关系加载模块。
3. 区分 modprobe 参数与启动时加载请求。
4. 将黑名单视为有限策略，而不是绝对禁止。
5. 执行 `modprobe -r` 前，让每个使用者停止活动。
