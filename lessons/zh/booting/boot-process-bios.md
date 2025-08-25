---
index: 2
lang: "zh"
title: "启动过程：BIOS"
meta_title: "启动过程：BIOS - 启动系统"
meta_description: "了解 Linux 启动过程、BIOS 和 MBR。通过这份适合初学者的指南，了解您的系统如何启动。探索 UEFI 概念！"
meta_keywords: "Linux 启动过程，BIOS, MBR, UEFI, Linux 教程，引导加载程序，Linux 初学者，系统启动"
---

## Lesson Content

### BIOS

Linux 启动过程的第一步是 BIOS，它执行系统完整性检查。BIOS 是一种固件，在当今主流的 IBM PC 兼容计算机中最为常见。您可能使用过 BIOS 固件来更改硬盘的启动顺序、检查系统时间、机器的 MAC 地址等。BIOS 的主要目标是找到系统引导加载程序。

因此，一旦 BIOS 启动硬盘，它就会搜索启动块以确定如何启动系统。根据您如何分区磁盘，它会查找主引导记录 (MBR) 或 GPT。MBR 位于硬盘的第一个扇区，即前 512 字节。MBR 包含加载磁盘上另一个程序的代码；该程序反过来实际加载我们的引导加载程序。

现在，如果您使用 GPT 对磁盘进行了分区，引导加载程序的位置会略有变化。

### UEFI

除了使用 BIOS 之外，还有另一种启动系统的方法，那就是使用 UEFI（“统一可扩展固件接口”）。UEFI 旨在成为 BIOS 的继任者；当今大多数硬件都内置了 UEFI 固件。Macintosh 机器多年来一直使用 EFI 启动，Windows 也已将其大部分内容转移到 UEFI 启动。GPT 格式旨在与 EFI 配合使用。如果您正在启动 GPT 磁盘，则不一定需要 EFI。GPT 磁盘的第一个扇区保留用于“保护性 MBR”，以便可以启动基于 BIOS 的机器。

UEFI 将所有启动信息存储在 `.efi` 文件中。此文件存储在硬件上一个名为 EFI 系统分区的特殊分区中。在此分区内，它将包含引导加载程序。UEFI 比传统的 BIOS 固件有许多改进。然而，由于我们使用的是 Linux，我们大多数人都在使用 BIOS。因此，所有这些课程都将以此为前提。

## Exercise

熟能生巧！以下是一些动手实验，可帮助您加深对 Linux 用户和组管理的理解：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户帐户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新帐户到修改和删除它们。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 获得使用命令行实用程序进行组管理的实践经验，包括创建新组、修改用户成员资格和删除组。
3. **[在 Linux 中配置用户帐户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户帐户和 sudo 权限的基本技术，以增强 Linux 系统的安全性。

这些实验将帮助您在实际场景中应用概念，并增强您在 Linux 中进行用户和组管理的信心。

## Quiz Question

BIOS 加载什么？

## Quiz Answer

bootloader
