---
lang: "zh"
title: "内核安装"
description: "学习如何安装和管理 Linux 内核。了解内核版本，使用 `uname -r` 和 apt 命令。开始你的 Linux 内核之旅！"
keywords: "Linux 内核，安装内核，uname -r, apt dist-upgrade, 内核管理，Linux 教程，Linux 入门，Linux 指南"
---

## Lesson Content

好了，现在我们已经把那些无聊的东西都讲完了，接下来我们来谈谈如何实际安装和修改内核。你可以在你的系统上安装多个内核；还记得我们关于启动过程的课程吗？在我们的 GRUB 菜单中，我们可以选择启动哪个内核。

要查看你的系统上有什么内核版本，请使用以下命令：

```bash
$ uname -r
3.19.0-43-generic
```

`uname` 命令打印系统信息；`-r` 选项将打印内核发布版本。

你可以通过不同的方式安装 Linux 内核：你可以下载源代码包并从源代码编译，或者你可以使用包管理工具安装它。

```bash
sudo apt install linux-generic-lts-vivid
```

然后只需重启到你安装的内核。很简单，对吧？有点。你还需要安装其他 Linux 软件包，例如 `linux-headers`、`linux-image-generic` 等。你也可以指定版本号，所以上面的命令可以看起来像：**`sudo apt install 3.19.0-43-generic`**

或者，如果你只是想要更新的内核版本，只需使用 `dist-upgrade`；它会升级你系统上的所有软件包：

```bash
sudo apt dist-upgrade
```

有许多不同的内核版本。有些用作 LTS（长期支持），有些是最新最好的。不同内核版本之间的兼容性可能差异很大，所以你可能需要尝试不同的内核。

## Exercise

1. Find out what kernel version you have.
2. Research the different versions of kernels available.

## Quiz Question

你如何查看你系统的内核版本？

## Quiz Answer

uname -r
