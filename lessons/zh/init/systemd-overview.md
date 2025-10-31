---
index: 5
lang: "zh"
title: "Systemd 概述"
meta_title: "Systemd 概述 - 初始化系统"
meta_description: "了解 systemd 初始化系统的基础知识。本指南涵盖 systemd 如何使用单元（units）和目标（targets）来管理 Linux 启动过程和系统服务。理解现代 Linux 初始化标准的**核心概念**。"
meta_keywords: "systemd, system d, 初始化系统，systemd 单元，systemd 目标，linux 启动过程，linux 服务，系统管理，初学者，教程"
---

## Lesson Content

### 什么是 Systemd?

Systemd 是大多数现代 Linux 发行版的默认初始化系统和服务管理器。它负责在内核加载后以正确的顺序初始化系统。检查您的系统是否使用它的简单方法是查看 `/usr/lib/systemd` 目录是否存在。如果存在，则您的系统很可能由 **systemd** 管理。

### Systemd 启动过程

**systemd** 不使用僵化的顺序脚本，而是使用“目标”（goals）的概念将您的系统带入功能状态。它识别一个主要目标或 `target`，并努力满足其依赖项。这种方法在启动期间提供了更大的灵活性和并行性。由 **systemd** 管理的典型启动过程遵循以下步骤：

1. **systemd** 首先从 `/etc/systemd/system` 和 `/usr/lib/systemd/system` 等目录加载其配置文件。
2. 然后它识别默认启动目标，这通常是一个名为 `default.target` 的符号链接。
3. 最后，**systemd** 解析此目标的所有依赖项，并激活必要的单元以实现所需的系统状态。

### 理解 Systemd 目标 (Targets)

**systemd** 中的目标类似于旧的 SysV init 系统中的运行级别 (runlevels)。它们代表系统可以处于的不同状态。常见的目标包括：

- `poweroff.target`: 关闭系统。
- `rescue.target`: 引导到单用户 shell 进行维护。
- `multi-user.target`: 具有网络连接但没有图形界面的标准多用户环境。
- `graphical.target`: 具有网络连接和图形用户界面 (GUI) 的完整多用户环境。
- `reboot.target`: 重新启动系统。

`default.target` 是一个符号链接，指向系统默认启动到的目标，在桌面系统上通常是 `graphical.target`。

### 核心概念：Systemd 单元 (Units)

**systemd** 管理的基本对象称为“单元”（units）。单元是描述资源或服务的配置文件。**system d** 架构的强大之处在于它能够管理各种类型的资源，而不仅仅是服务。每个单元类型由其文件扩展名标识。最常见的类型是：

- **服务单元 (`.service`)**: 这些管理系统守护进程或服务，例如 Web 服务器或数据库。
- **挂载单元 (`.mount`)**: 这些控制文件系统挂载点。
- **目标单元 (`.target`)**: 这些用于将其他单元分组在一起，在启动过程中创建同步点。

例如，当系统启动到 `graphical.target` 时，该目标单元确保其所有依赖项（如 `multi-user.target` 和 `network.service` 等各种服务单元）首先启动。

## Exercise

虽然此主题没有特定的实验，但我们建议探索综合性的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

哪个单元用于将其他单元组合在一起？请用一个单独的小写英文字词回答。

## Quiz Answer

target
