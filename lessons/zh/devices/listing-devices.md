---
index: 6
lang: "zh"
title: "lsusb, lspci, lssci"
meta_title: "lsusb, lspci, lssci - 设备列表"
meta_description: "了解如何在 Linux 系统上列出和检查 USB、PCI 和 SCSI 硬件。本指南涵盖 lsusb、lspci 和 lssci 命令，包括 lsusb -t 等查看设备树的选项。"
meta_keywords: "lsusb, lspci, lssci, lsusb -t, 列出 usb 设备，列出 pci 设备，列出 scsi 设备，linux 硬件，设备信息"
---

## Lesson Content

正如您使用 `ls` 命令列出文件一样，Linux 也提供了类似的工具来列出硬件设备。这些命令对于识别连接到系统的硬件至关重要。

### 使用 lsusb 列出 USB 设备

要查看连接到系统的所有 USB 设备，您可以使用 `lsusb` 命令。此命令会扫描 USB 集线器并报告它找到的设备信息，例如网络摄像头、键盘和外部驱动器。

```bash
lsusb
```

为了获得更有条理的视图，您可以使用 `lsusb -t` 命令。此选项以树状结构显示 USB 设备，有助于理解设备是如何物理连接到 USB 控制器和集线器的。

### 使用 lspci 列出 PCI 设备

`lspci` 命令用于列出所有 PCI（外设组件互连）设备。这些通常是连接到主板的内部组件，例如显卡、网络适配器和声卡。此命令可以快速了解您系统的核心硬件。

```bash
lspci
```

### 使用 lssci 列出 SCSI 和 SATA 设备

对于存储设备，`lssci` 命令特别有用。它列出了所有连接的 SCSI 和 SATA 设备，这些通常包括硬盘、固态硬盘和光盘驱动器（CD/DVD/蓝光）。虽然其他命令可能会显示存储控制器，但 `lssci` 提供了关于存储设备本身的直接信息，使其成为系统管理员和管理存储用户的宝贵工具。

```bash
lssci
```

## Exercise

为了加强您对在 Linux 中探索硬件设备的理解，请尝试以下实践实验：

1. **[在 Linux 中探索硬件设备](https://labex.io/zh/labs/comptia-explore-hardware-devices-in-linux-590861)** - 在此实验中，您将学习在 Linux 环境中探索、识别和检查硬件设备的基本技能。您将获得使用强大的命令行实用程序的实践经验，以了解操作系统如何与物理组件交互。

此实验将帮助您在现实场景中应用这些概念，并建立管理设备信息的信心。

## Quiz Question

查看已连接 USB 设备列表使用的命令是什么？（请仅用小写英文字符回答。）

## Quiz Answer

lsusb
