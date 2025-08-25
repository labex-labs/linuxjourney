---
index: 7
lang: "zh"
title: "编译源代码"
meta_title: "编译源代码 - 软件包"
meta_description: "了解如何在 Linux 中使用 make、configure 和 checkinstall 编译源代码。了解初学者和中级用户的构建过程。"
meta_keywords: "编译源代码，make install, checkinstall, Linux 编译，build-essential, Linux 教程，初学者指南"
---

## Lesson Content

通常，您会遇到一个晦涩的软件包，它只以纯源代码的形式提供。您需要使用一些命令来编译并将该源代码包安装到您的系统上。

首先，您需要安装能够编译源代码的工具。

```bash
sudo apt install build-essential
```

完成此操作后，提取软件包文件的内容，最可能是 `.tar.gz` 文件。

```bash
tar -xzvf package.tar.gz
```

在执行任何操作之前，请查看软件包内的 `README` 或 `INSTALL` 文件。有时会有特定的安装说明。

根据开发人员使用的编译方法，您需要使用不同的命令，例如 `cmake` 或其他命令。

然而，最常见的是基本的 `make` 编译，所以我们将讨论它：

软件包内容中会有一个 `configure` 脚本。此脚本检查系统上的依赖项，如果您缺少任何内容，您将看到错误，并且需要修复这些依赖项。

```bash
./configure
```

`./` 允许您在当前目录中执行脚本。

```bash
make
```

软件包内容中有一个名为 `Makefile` 的文件，其中包含构建软件的规则。当您运行 `make` 命令时，它会查看此文件来构建软件。

```bash
sudo make install
```

此命令实际上安装了软件包；它会将正确的文件复制到您计算机上的正确位置。

如果要卸载软件包，请使用：

```bash
sudo make uninstall
```

使用 `make install` 时要小心；您可能没有意识到后台实际发生了多少事情。如果您决定删除此软件包，您可能无法实际删除所有内容，因为您没有意识到系统添加了什么。相反，忘记我刚刚向您解释的关于 `make install` 的所有内容，并使用 **checkinstall** 命令。此命令将为您创建一个 `.deb` 文件，您可以轻松安装和卸载它。

```bash
sudo checkinstall
```

此命令将实质上“make install”并构建一个 `.deb` 包并安装它。这使得以后更容易删除软件包。

## Exercise

熟能生巧！这是一个动手实验，旨在加强您对从源代码构建软件的理解：

1. **[在 Linux 中从源代码构建软件](https://labex.io/zh/labs/comptia-build-software-from-source-code-in-linux-590853)** - 练习从源代码构建和安装软件的基本过程，包括使用 `configure`、`make` 和 `make install`。

本实验将帮助您在实际场景中应用这些概念，并增强编译软件的信心。

## Quiz Question

您应该始终使用什么来代替 `make install`？

## Quiz Answer

checkinstall
