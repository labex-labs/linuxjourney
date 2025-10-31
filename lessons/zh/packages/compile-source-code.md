---
index: 7
lang: "zh"
title: "编译源代码"
meta_title: "编译源代码 - 软件包"
meta_description: "了解如何在 Linux 中从源代码编译。本指南涵盖了使用 configure、make 和推荐的 checkinstall 命令构建源代码以进行干净软件包管理的基本步骤。"
meta_keywords: "如何从源代码编译，如何构建源代码，编译源代码，make install, checkinstall, Linux 编译，build-essential, configure 脚本，makefile, Linux 教程"
---

## Lesson Content

有时，您可能会发现某个软件包仅以源代码的形式提供。要使用它，您需要在系统上编译和安装它。本课程将指导您完成如何从源代码编译的常见过程。

### 准备您的系统

在编译任何内容之前，您需要必要的工具。在基于 Debian 的系统（如 Ubuntu）上，您可以使用一个命令安装它们。

```bash
sudo apt install build-essential
```

`build-essential` 包安装了一套软件开发工具，包括 GCC 编译器和 `make` 实用程序，它们对编译至关重要。

安装工具后，解压源代码包的内容，这通常是一个 `.tar.gz` 文件。

```bash
tar -xzvf package.tar.gz
```

在继续之前，请务必检查解压后的目录中是否存在 `README` 或 `INSTALL` 文件。这些文件通常包含该特定软件包所需的具体说明或依赖项。

### 标准构建过程

虽然不同的开发人员可能会使用各种构建系统（如 `cmake`），但最传统的方法涉及一个三步过程。理解这一点是学习如何构建源代码的基础。

首先，运行 `configure` 脚本。此脚本会检查您的系统是否具有软件构建和正确运行所需的所有必要依赖项和库。

```bash
./configure
```

`./` 前缀告诉 shell 从当前目录执行脚本。如果脚本报告任何缺少依赖项，您必须在继续之前安装它们。

接下来，运行 `make` 命令。此命令会读取目录中名为 `Makefile` 的文件，其中包含一组关于如何将源代码编译成可执行程序的规则。

```bash
make
```

最后，要将软件安装到您的系统上，您通常会运行：

```bash
sudo make install
```

此命令会将编译后的文件复制到适当的系统目录中，使软件可供使用。

### 更好的安装方式

虽然 `sudo make install` 有效，但它有一个明显的缺点：它不会将软件注册到您系统的包管理器中。这使得将来难以跟踪、更新或干净地卸载该软件包。

一个更好的方法是使用 `checkinstall`。此工具会运行安装过程，但它不会直接复制文件，而是创建一个原生的系统包（如 Debian/Ubuntu 上的 `.deb` 文件）并安装它。

```bash
sudo checkinstall
```

使用 `checkinstall` 将编译后的软件集成到您的包管理系统中。这意味着您以后可以使用 `apt` 或 `dpkg` 轻松将其删除，就像您从官方存储库安装的任何其他软件包一样。因此，您应该始终优先使用 `checkinstall` 而不是 `make install`。

要卸载使用 `make install` 安装的软件包，您需要返回到源目录并运行 `sudo make uninstall`，但这并不总是可靠的。

## Exercise

实践造就完美！这是一个实践实验，用于巩固您对从源构建软件的理解：

1. **[在 Linux 中从源代码构建软件](https://labex.io/zh/labs/comptia-build-software-from-source-code-in-linux-590853)** - 练习从源代码构建和安装软件的基本过程，包括使用 `configure`、`make` 和 `make install`。

此实验将帮助您在真实场景中应用这些概念，并建立编译软件的信心。

## Quiz Question

您应该始终使用什么来代替 `make install`？（请用英语回答，注意区分大小写）

## Quiz Answer

checkinstall
