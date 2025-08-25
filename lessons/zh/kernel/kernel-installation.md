---
index: 4
lang: "zh"
title: "内核安装"
meta_title: "内核安装 - 内核"
meta_description: "了解如何安装和管理 Linux 内核。探索内核版本，使用 `uname -r` 和 apt 命令。开始你的 Linux 内核之旅！"
meta_keywords: "Linux 内核，安装内核，uname -r, apt dist-upgrade, 内核管理，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

好了，现在我们已经把那些无聊的东西都讲完了，接下来我们来谈谈如何实际安装和修改内核。你可以在系统上安装多个内核；还记得我们在引导过程那一课中讲过吗？在我们的 GRUB 菜单中，我们可以选择引导哪个内核。

要查看系统上的内核版本，请使用以下命令：

```bash
$ uname -r
3.19.0-43-generic
```

`uname` 命令打印系统信息；`-r` 选项将打印内核发布版本。

你可以通过不同的方式安装 Linux 内核：你可以下载源代码包并从源代码编译，或者你可以使用包管理工具安装它。

```bash
sudo apt install linux-generic-lts-vivid
```

然后只需重启到你安装的内核。很简单，对吧？有点。你还需要安装其他 Linux 包，例如 `linux-headers`、`linux-image-generic` 等。你还可以指定版本号，所以上面的命令可以看起来像：**`sudo apt install 3.19.0-43-generic`**

或者，如果你只是想要更新的内核版本，只需使用 `dist-upgrade`；它会升级系统上的所有包：

```bash
sudo apt dist-upgrade
```

有许多不同的内核版本。有些用作 LTS（长期支持），有些是最新最好的。不同内核版本之间的兼容性可能差异很大，因此你可能需要尝试不同的内核。

## Exercise

熟能生巧！这里有一些动手实验，可以帮助你巩固对 Linux 内核管理和相关系统管理任务的理解：

1. **[在 Linux 中自定义 GRUB2 引导菜单](https://labex.io/zh/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - 练习修改 GRUB2 引导菜单，这在管理多个内核版本和选择引导哪个内核时至关重要。
2. **[在 Linux 中管理内核模块](https://labex.io/zh/labs/comptia-manage-kernel-modules-in-linux-590865)** - 学习列出、检查、加载和卸载内核模块，这是内核管理和理解硬件如何与系统交互的基本方面。
3. **[Linux 上的软件安装](https://labex.io/zh/labs/linux-software-installation-on-linux-18005)** - 获得使用各种方法安装和管理软件的实践经验，包括使用包管理器，这是安装和更新内核的常用方法。

这些实验将帮助你在实际场景中应用内核管理、引导过程和包管理的概念，从而增强系统管理的信心。

## Quiz Question

如何查看系统的内核版本？

## Quiz Answer

uname -r
