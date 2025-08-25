---
index: 5
lang: "zh"
title: "内核位置"
meta_title: "内核位置 - 内核"
meta_description: "了解 /boot 目录中的 Linux 内核位置，理解 vmlinuz、initrd 和 System.map。探索内核文件并有效管理空间。"
meta_keywords: "Linux 内核，/boot 目录，vmlinuz, initrd, System.map, Linux 初学者，内核教程，Linux 指南"
---

## Lesson Content

安装新内核时会发生什么？它实际上会向您的系统添加几个文件；这些文件通常添加到 `/boot` 目录中。

您会看到不同内核版本的多个文件：

- `vmlinuz` - 这是实际的 Linux 内核
- `initrd` - 如前所述，`initrd` 用作临时文件系统，在加载内核之前使用
- `System.map` - 符号查找表
- `config` - 内核配置设置；如果您正在编译自己的内核，可以设置可以加载哪些模块

如果您的 `/boot` 目录空间不足，您可以随时删除这些文件的旧版本或只使用包管理器。但在该目录中进行维护时要小心，不要意外删除您当前正在使用的内核。

## Exercise

熟能生巧！以下是一些动手实验，以加强您对 Linux 引导过程和内核管理的理解：

1. **[在 Linux 中自定义 GRUB2 引导菜单](https://labex.io/zh/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - 练习修改 GRUB2 配置，这直接影响您的 Linux 系统如何引导和选择内核版本。本实验将帮助您理解 `/boot` 目录中讨论的文件的实际含义。

本实验将帮助您在实际场景中应用这些概念，并增强您对 Linux 内核和引导管理的信心。

## Quiz Question

`/boot` 中内核映像的名称是什么？

## Quiz Answer

vmlinuz
