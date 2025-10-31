---
index: 6
lang: "zh"
title: "内核模块"
meta_title: "内核模块 - Linux 内核"
meta_description: "了解 Linux 中的内核模块是什么，以及它们如何扩展内核功能。本课程涵盖使用 lsmod 和 modprobe 按需列出、加载和卸载模块。"
meta_keywords: "什么是内核模块，Linux 内核模块，modprobe, lsmod, 内核管理，Linux 教程，Linux 入门，Linux 指南"
---

## Lesson Content

将 Linux 内核想象成一辆汽车的核心引擎。您可以添加配件，如车顶行李架或新的音响系统，而无需更改引擎本身。这些配件可以根据需要添加或移除。Linux 内核使用类似的概念，即内核模块。

### 什么是内核模块

那么，**什么是内核模块**？它们是可以在需要时加载到内核中和从内核中卸载的代码片段。它们在不要求您重新编译核心内核或重新启动系统的情况下扩展了内核的功能。这种模块化方法允许动态添加对新硬件（如新的 Wi-Fi 卡）或新软件功能（如新的文件系统）的支持。这使得核心内核保持精简，同时提供了巨大的灵活性。

### 列出已加载的模块

要查看当前加载到内存中的所有内核模块的列表，您可以使用 `lsmod` 命令。这会为您提供活动模块及其依赖关系的快照。

```bash
lsmod
```

### 加载内核模块

要加载内核模块，我们使用 `modprobe` 命令。例如，要加载 `bluetooth` 模块，您将运行：

```bash
sudo modprobe bluetooth
```

`modprobe` 命令很智能；它会在标准目录（`/lib/modules/$(uname -r)/`）中搜索模块，并且还会加载目标模块所依赖的任何其他模块。

### 卸载内核模块

如果不再需要某个模块，您可以将其卸载以释放系统资源。使用 `modprobe` 配合 `-r` 标志来移除模块：

```bash
sudo modprobe -r bluetooth
```

### 在启动时管理模块

使用 `modprobe` 加载的模块是临时的，在重新启动后会消失。要使模块配置永久化，您可以在 `/etc/modprobe.d/` 目录中创建配置文件。

要自动加载带有特定选项的模块并在启动时加载，请创建一个 `.conf` 文件。例如，如果您有一个名为 `peanut_butter` 的假设模块，并希望将其 `type` 参数设置为 `almond`，您的文件将如下所示：

```plaintext
# /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

相反，要阻止模块在启动时加载（此过程称为黑名单化），您可以在配置文件中使用 `blacklist` 关键字：

```plaintext
# /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

这些配置文件允许您对系统启动时可用的模块进行精细控制。

## Exercise

实践造就完美！这是一个强化您对 Linux 内核模块理解的动手实验：

1. **[在 Linux 中管理内核模块](https://labex.io/zh/labs/comptia-manage-kernel-modules-in-linux-590865)** - 练习列出、检查、加载和卸载内核模块，并配置它们在启动时自动加载。此实验将帮助您在真实场景中应用这些概念，并建立对内核模块管理的信心。

## Quiz Question

用于卸载模块的命令是什么？

## Quiz Answer

modprobe -r
