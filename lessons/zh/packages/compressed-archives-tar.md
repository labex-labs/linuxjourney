---
index: 3
lang: "zh"
title: "tar 和 gzip"
meta_title: "tar 和 gzip - 软件包"
meta_description: "学习在 Linux 中使用 tar 和 gzip 进行文件归档和压缩。了解创建、提取和压缩文件的命令。通过这份初学者指南开始吧！"
meta_keywords: "tar, gzip, Linux 归档，文件压缩，tar 命令，gzip 命令，Linux 教程，Linux 初学者"
---

## Lesson Content

在我们深入了解软件包安装和各种管理器之前，我们需要讨论文件归档和压缩，因为您在网上寻找软件时很可能会遇到这些。

您可能已经知道什么是文件归档；您很可能遇到过 .rar 和 .zip 等文件类型。这些都是文件的归档；它们内部包含许多文件，但它们以这种非常整洁的单个文件形式出现，称为归档。

### Compressing files with gzip

gzip 是一个用于在 Linux 中压缩文件的程序；它们以 .gz 扩展名结尾。

要压缩文件：

```bash
gzip mycoolfile
```

要解压缩文件：

```bash
gunzip mycoolfile.gz
```

### Creating archives with tar

不幸的是，gzip 无法为我们添加多个文件到一个归档中。幸运的是，我们有 tar 程序可以做到这一点。当您使用 tar 创建归档时，它将具有 .tar 扩展名。

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - 创建
- `v` - 告诉程序详细输出，让我们看到它正在做什么
- `f` - tar 文件的文件名必须在此选项之后；如果您正在创建一个 tar 文件，您必须想一个名字

### Unpacking archives with tar

要提取 tar 文件的内容，请使用：

```bash
tar xvf mytarfile.tar
```

- `x` - 提取
- `v` - 告诉程序详细输出，让我们看到它正在做什么
- `f` - 您要提取的文件

### Compressing/uncompressing archives with tar and gzip

很多时候您会看到一个已压缩的 tar 文件，例如：`mycompressedarchive.tar.gz`。您所需要做的就是由外而内操作，所以首先使用 `gunzip` 解除压缩，然后您可以解包 tar 文件。或者您可以选择使用 tar 的 **z** 选项，它只是告诉它使用 gzip 或 gunzip 工具。

创建一个压缩的 tar 文件：

```bash
tar czf myfile.tar.gz
```

解压缩和解包：

```bash
tar xzf file.tar
```

如果您需要帮助记忆这个：e**X**tract all **Z**ee **F**iles！

tar 是那些非常重要但您却从不真正记住的命令之一。相关 xkcd：`https://xkcd.com/1168`

### Other Utilities

在您的 Linux 之旅中，您会遇到其他归档和压缩类型，例如：bzip2、compress、zip、unzip 等。它们不那么常见，但请记住，不同的工具需要不同的命令。

## Exercise

熟悉 tar 文档并查看手册页中可用的其他选项。

## Quiz Question

What tar flag is used to create archives?

## Quiz Answer

c
