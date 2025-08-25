---
index: 5
lang: "zh"
title: "rpm 和 dpkg"
meta_title: "rpm 和 dpkg - 包"
meta_description: "学习使用 rpm 和 dpkg 命令安装、移除和列出包。了解 .deb 和 .rpm 文件的直接包管理。开始您的 Linux 之旅！"
meta_keywords: "rpm, dpkg, Linux 包管理，.deb, .rpm, Linux 教程，初学者指南，安装包"
---

## Lesson Content

尽管本课程的大部分内容是关于包管理系统（包管理中的蝙蝠侠），但我们不能忘记罗宾。虽然它们非常有用和可靠，但它们没有附带那辆酷炫的蝙蝠车和多功能腰带。

就像 `.exe` 是一个单独的可执行文件一样，`.deb` 和 `.rpm` 也是如此。如果您使用包仓库，通常不会看到这些文件，但如果您直接下载包，您很可能会得到这些流行的格式。显然，它们是各自发行版独有的：`.deb` 用于基于 Debian 的发行版，`.rpm` 用于基于 Red Hat 的发行版。

要安装这些直接的包，您可以使用包管理命令：`rpm` 和 `dpkg`。这些工具用于安装包文件；但是，它们不会安装包的依赖项。因此，如果您的包有 10 个依赖项，您将不得不单独安装这些包，然后安装它们的依赖项，依此类推。正如您所看到的，这就是后来我们讨论的成熟管理系统出现的原因之一。

请记住，您将无数次需要使用这些工具之一来安装、查询或验证包，因此请记住这些命令。

### 安装包

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

`i` 代表安装（install）。您也可以使用更长的格式 `--install`。

### 移除包

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r` 代表移除（remove）
RPM: `e` 代表擦除（erase）

### 列出已安装的包

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l` 代表列表（list）
RPM: `q` 代表查询（query），`a` 代表所有（all）

## Exercise

熟能生巧！这是一个动手实验，旨在巩固您对直接包管理的理解：

1. **[在 Linux 中使用 RPM 管理包](https://labex.io/zh/labs/rhel-managing-packages-with-rpm-in-linux-590868)** - 获得使用 `rpm` 及相关工具查询包信息、验证完整性、列出依赖项、模拟移除和检查 RPM 包内容的实践经验。

本实验将帮助您在实际场景中应用管理单个包文件的概念，并增强您对这些基本 Linux 工具的信心。

## Quiz Question

用于 `.deb` 文件的包管理工具是什么？

## Quiz Answer

dpkg
