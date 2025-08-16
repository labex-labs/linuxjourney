---
lang: "zh"
title: "启动过程：BIOS"
description: "了解 Linux 启动过程、BIOS 和 MBR。通过这份适合初学者的指南，了解您的系统如何启动。探索 UEFI 概念！"
keywords: "Linux 启动过程，BIOS, MBR, UEFI, Linux 教程，引导加载程序，Linux 初学者，系统启动"
---

## Lesson Content

### BIOS

Linux 启动过程的第一步是 BIOS，它执行系统完整性检查。BIOS 是一种固件，在 IBM PC 兼容计算机中最为常见，而 IBM PC 兼容计算机是当今主流的计算机类型。您可能使用过 BIOS 固件来更改硬盘的启动顺序、检查系统时间、机器的 MAC 地址等。BIOS 的主要目标是找到系统引导加载程序。

因此，一旦 BIOS 启动硬盘，它就会搜索启动块以确定如何启动系统。根据您如何分区磁盘，它会查找主引导记录 (MBR) 或 GPT。MBR 位于硬盘的第一个扇区，即前 512 字节。MBR 包含加载磁盘上某个位置的另一个程序的代码；该程序反过来实际加载我们的引导加载程序。

现在，如果您使用 GPT 分区磁盘，引导加载程序的位置会略有变化。

### UEFI

除了使用 BIOS 之外，还有另一种启动系统的方法，那就是使用 UEFI（“统一可扩展固件接口”）。UEFI 旨在成为 BIOS 的继任者；当今大多数硬件都内置了 UEFI 固件。Macintosh 机器多年来一直使用 EFI 启动，Windows 也已将其大部分内容转移到 UEFI 启动。GPT 格式旨在与 EFI 配合使用。如果您要启动 GPT 磁盘，不一定需要 EFI。GPT 磁盘的第一个扇区保留用于“保护性 MBR”，以便可以启动基于 BIOS 的机器。

UEFI 将所有启动信息存储在 `.efi` 文件中。此文件存储在硬件上一个名为 EFI 系统分区的特殊分区中。在该分区内部，它将包含引导加载程序。UEFI 比传统的 BIOS 固件有许多改进。但是，由于我们使用的是 Linux，我们大多数人都在使用 BIOS。因此，所有这些课程都将以此为前提。

## Exercise

Go into your BIOS menu and see if you have UEFI booting enabled.

## Quiz Question

BIOS 加载什么？

## Quiz Answer

bootloader
