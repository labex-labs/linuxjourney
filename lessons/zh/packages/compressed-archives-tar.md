---
index: 3
lang: "zh"
title: "tar 和 gzip"
meta_title: "tar 和 gzip - 软件包"
meta_description: "学习在 Linux 中使用 tar 和 gzip 进行文件归档和压缩。了解创建、提取和压缩文件的命令。通过此初学者指南开始学习！"
meta_keywords: "tar, gzip, Linux 归档，文件压缩，tar 命令，gzip 命令，Linux 教程，Linux 初学者"
---

## Lesson Content

在深入了解软件包安装和不同的管理器之前，我们需要讨论文件归档和压缩，因为您在网上寻找软件时很可能会遇到这些。

您可能已经知道什么是文件归档；您很可能遇到过 .rar 和 .zip 等文件类型。这些都是文件归档；它们内部包含许多文件，但它们以这种非常整洁的单个文件形式出现，称为归档。

### 使用 gzip 压缩文件

gzip 是一个用于在 Linux 中压缩文件的程序；它们以 .gz 扩展名结尾。

压缩文件：

```bash
gzip mycoolfile
```

解压缩文件：

```bash
gunzip mycoolfile.gz
```

### 使用 tar 创建归档

遗憾的是，gzip 无法为我们添加多个文件到一个归档中。幸运的是，我们有 tar 程序可以做到这一点。当您使用 tar 创建归档时，它将具有 .tar 扩展名。

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - 创建
- `v` - 告诉程序详细输出，让我们看到它正在做什么
- `f` - tar 文件的文件名必须在此选项之后；如果您正在创建 tar 文件，则必须想一个名称

### 使用 tar 解包归档

要提取 tar 文件的内容，请使用：

```bash
tar xvf mytarfile.tar
```

- `x` - 提取
- `v` - 告诉程序详细输出，让我们看到它正在做什么
- `f` - 您要提取的文件

### 使用 tar 和 gzip 压缩/解压缩归档

很多时候，您会看到一个已压缩的 tar 文件，例如：`mycompressedarchive.tar.gz`。您所需要做的就是由外而内操作，所以首先使用 `gunzip` 解除压缩，然后您可以解包 tar 文件。或者，您可以选择使用 tar 的 **z** 选项，它只是告诉它使用 gzip 或 gunzip 工具。

创建压缩的 tar 文件：

```bash
tar czf myfile.tar.gz
```

解压缩和解包：

```bash
tar xzf file.tar
```

如果您需要帮助记忆：e**X**tract all **Z**ee **F**iles! (提取所有 Z 文件！)

tar 是那些非常重要但您却从不真正记住的命令之一。相关 xkcd：`https://xkcd.com/1168`

### 其他实用程序

在您的 Linux 之旅中，您会遇到其他归档和压缩类型，例如：bzip2、compress、zip、unzip 等。它们不太常见，但请记住，不同的实用程序需要不同的命令。

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对文件归档和压缩的理解：

1. **[文件打包和压缩](https://labex.io/zh/labs/linux-file-packaging-and-compression-385413)** - 学习使用 tar、gzip 和 zip 等工具进行基本的 Linux 文件压缩和打包技术。
2. **[在 Linux 中使用 tar 创建和恢复备份](https://labex.io/zh/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - 获得使用 tar 命令创建和恢复文件系统备份的实践经验。
3. **[备份系统日志](https://labex.io/zh/labs/linux-backup-system-log-17989)** - 学习使用 tar 命令和日期格式化备份系统日志文件的基本技能。

这些实验将帮助您在实际场景中应用归档和压缩的概念，并增强您在 Linux 中管理文件的信心。

## Quiz Question

What tar flag is used to create archives?

## Quiz Answer

c
