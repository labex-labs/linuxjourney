---
lang: "zh"
title: "内核位置"
meta_title: "内核位置 - 内核"
meta_description: "了解 Linux 内核在 /boot 目录中的位置，理解 vmlinuz、initrd 和 System.map。探索内核文件并有效管理空间。"
meta_keywords: "Linux 内核，/boot 目录，vmlinuz, initrd, System.map, Linux 初学者，内核教程，Linux 指南"
---

## Lesson Content

安装新内核时会发生什么？它实际上会向您的系统添加几个文件；这些文件通常会添加到 `/boot` 目录中。

您会看到不同内核版本的多个文件：

- `vmlinuz` - 这是实际的 Linux 内核
- `initrd` - 正如我们之前讨论的，`initrd` 用作临时文件系统，在加载内核之前使用
- `System.map` - 符号查找表
- `config` - 内核配置设置；如果您正在编译自己的内核，可以设置可以加载哪些模块

如果您的 `/boot` 目录空间不足，您始终可以删除这些文件的旧版本，或者只使用包管理器。但在该目录中进行维护时要小心，不要意外删除您当前正在使用的内核。

## Exercise

进入您的 boot 目录，查看其中有哪些文件。

## Quiz Question

`/boot` 中的内核镜像叫什么？

## Quiz Answer

vmlinuz
