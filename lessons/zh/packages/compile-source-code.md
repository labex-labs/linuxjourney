---
lang: "zh"
title: "编译源代码"
meta_description: "学习如何在 Linux 中使用 make、configure 和 checkinstall 编译源代码。了解初学者和中级用户的构建过程。"
meta_keywords: "编译源代码，make install, checkinstall, Linux 编译，build-essential, Linux 教程，初学者指南"
---

## Lesson Content

你经常会遇到一个只以纯源代码形式存在的冷门软件包。你需要使用一些命令来编译并将该源代码包安装到你的系统上。

首先，你需要安装允许你编译源代码的工具软件。

```bash
sudo apt install build-essential
```

完成此操作后，解压软件包文件内容，很可能是一个 `.tar.gz` 文件。

```bash
tar -xzvf package.tar.gz
```

在做任何事情之前，请查看软件包内的 `README` 或 `INSTALL` 文件。有时会有特定的安装说明。

根据开发者使用的编译方法，你可能需要使用不同的命令，例如 `cmake` 或其他。

然而，最常见的是基本的 `make` 编译，所以我们将讨论它：

软件包内容中会有一个 `configure` 脚本。这个脚本会检查你系统上的依赖项，如果你缺少任何东西，你会看到一个错误，你需要修复这些依赖项。

```bash
./configure
```

`./` 允许你在当前目录中执行脚本。

```bash
make
```

软件包内容中有一个名为 `Makefile` 的文件，其中包含构建软件的规则。当你运行 `make` 命令时，它会查看此文件来构建软件。

```bash
sudo make install
```

此命令实际上会安装软件包；它会将正确的文件复制到你计算机上的正确位置。

如果你想卸载软件包，请使用：

```bash
sudo make uninstall
```

使用 `make install` 时要小心；你可能没有意识到后台实际发生了多少事情。如果你决定删除此软件包，你可能无法完全删除所有内容，因为你没有意识到系统添加了什么。相反，忘记我刚才向你解释的关于 `make install` 的所有内容，并使用 **checkinstall** 命令。此命令将为你创建一个 `.deb` 文件，你可以轻松安装和卸载它。

```bash
sudo checkinstall
```

此命令本质上会“make install”并构建一个 `.deb` 包并安装它。这使得以后更容易删除软件包。

## Exercise

Find a source code program (from a trusted site) and install from source.

## Quiz Question

你应该始终用什么来替代 `make install`？

## Quiz Answer

checkinstall
