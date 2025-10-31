---
index: 2
lang: "zh"
title: "启动过程：BIOS"
meta_title: "启动过程：BIOS - 启动系统"
meta_description: "探索 Linux 启动过程的第一步：BIOS。了解它如何通过 MBR 或 GPT 查找引导加载程序，并理解 UEFI 的作用。本指南解释了系统启动，并涉及如何进入 BIOS 进行配置。"
meta_keywords: "Linux 启动过程，BIOS, MBR, UEFI, Linux 中的 bios, bios linux, 如何进入 bios, 引导加载程序，系统启动"
---

## Lesson Content

Linux 启动过程的第一步是 BIOS（基本输入/输出系统），它在启动时执行关键的系统完整性检查。BIOS 是常见于 IBM PC 兼容计算机中的固件，这类计算机占当今使用中计算机的大多数。

### BIOS 在 Linux 中的作用

当您开启计算机电源时，**BIOS in Linux**系统是第一个运行的软件。它的主要功能是初始化和测试系统硬件，例如 CPU、内存和硬盘。您很可能以前与 BIOS 固件打过交道，用于更改启动顺序、检查系统时间或查看机器的 MAC 地址。硬件检查完成后，**bios linux**过程的主要目标是定位并把控制权移交给系统引导加载程序（bootloader）。

### BIOS 如何找到引导加载程序

BIOS 初始化硬盘后，会搜索引导块以确定如何启动操作系统。它检查的位置取决于磁盘的分区方案：主引导记录（MBR）还是 GUID 分区表（GPT）。

MBR 位于硬盘的前 512 字节。这个很小的部分包含初始引导代码和分区表。MBR 中的代码负责加载另一个程序，该程序再加载我们实际的引导加载程序。如果您使用的是 GPT 分区的磁盘，过程会略有不同。

### 如何进入 BIOS

许多用户需要知道**如何进入 BIOS**来配置硬件设置。通常，进入 BIOS 的方法是在计算机开机后立即按下特定的键（例如 F2、F10、DEL 或 ESC）。学习**如何启动到 bios**对于更改启动设备优先级或启用虚拟化技术等任务至关重要。确切的按键因制造商而异，因此您可能需要查阅计算机的文档。

### UEFI 的兴起

传统 BIOS 的替代品是 UEFI（统一可扩展固件接口）。UEFI 被设计为 BIOS 的继任者，现在是大多数现代硬件的标准配置。它将所有启动信息存储在一个位于专用 EFI 系统分区（ESP）中的`.efi`文件中。该分区包含已安装操作系统的引导加载程序。

UEFI 在许多方面优于 BIOS，包括更快的启动时间和对更大硬盘的支持。虽然 GPT 格式是为 UEFI 设计的，但 GPT 磁盘上的“保护性 MBR”确保了向后兼容性，使得在旧的基于 BIOS 的机器上也可以从它们启动。尽管许多 Linux 系统现在使用 UEFI，但本指南将侧重于传统的 BIOS 启动过程，以建立基础理解。

## Exercise

实践造就完美！以下是一些实践实验，以加强您对 Linux 用户和组管理的理解：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从创建和保护新账户到修改和删除它们。
2. **[使用 groupadd、usermod 和 groupdel 管理 Linux 组](https://labex.io/zh/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 获得有关组管理命令行实用程序的实践经验，包括创建新组、修改用户组成员身份和删除组。
3. **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户账户和 sudo 权限的基本技术，以增强 Linux 系统的安全性。

这些实验将帮助您在实际场景中应用概念，并建立对 Linux 中用户和组管理的信心。

## Quiz Question

BIOS 加载什么？请用一个英文单词，小写回答。

## Quiz Answer

bootloader
