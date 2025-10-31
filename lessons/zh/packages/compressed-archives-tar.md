---
index: 3
lang: "zh"
title: "tar 和 gzip"
meta_title: "tar 和 gzip - 软件包"
meta_description: "关于在 Linux 中使用 tar 和 gzip 的综合指南。了解 tar 压缩、如何创建和提取归档文件，以及 gzip 和 tar 之间的区别。掌握压缩 tar gz 文件的命令，并有效管理您的软件包。"
meta_keywords: "tar 和 gzip, tar 压缩，gzip tar, 压缩 tar gz, gzip 和 tar, Linux 归档，文件压缩，tar 命令，gzip 命令，Linux 教程"
---

## Lesson Content

在深入研究包管理器之前，了解文件归档和压缩至关重要。当您从网上下载软件时，通常会发现它被打包在归档和压缩格式中。本课程重点介绍用于此目的的两个基本实用程序：`tar` 和 `gzip`。

### 理解归档与压缩

区分归档和压缩非常重要。**归档**是将多个文件和目录组合成一个文件的过程，称为归档文件。这使得管理和传输一组文件变得更加容易。另一方面，**压缩**是减小文件大小以节省磁盘空间和加快传输速度的过程。`tar` 实用程序用于归档，而 `gzip` 用于压缩。通常，您会看到 `gzip and tar` 一起使用。

### 使用 gzip 压缩单个文件

`gzip` 程序用于压缩 Linux 中的单个文件。当您使用 `gzip` 压缩文件时，它会被一个带有 `.gz` 扩展名的文件替换。

压缩文件：

```bash
gzip mycoolfile
```

这将创建 `mycoolfile.gz` 并删除原始文件。要解压缩文件，您可以使用 `gunzip`：

```bash
gunzip mycoolfile.gz
```

### 使用 tar 创建归档文件

虽然 `gzip` 非常适合压缩，但它不能将多个文件捆绑到一个归档文件中。为此，我们使用 `tar`（磁带归档）实用程序。使用 `tar` 创建的文件通常称为“tarball”，并具有 `.tar` 扩展名。

创建包含多个文件的新归档文件：

```bash
tar cvf myarchive.tar file1 file2 directory1
```

我们来分解一下选项：

- `c`: **c**reate（创建）一个新归档。
- `v`: **v**erbose（详细）模式，它会列出正在处理的文件。
- `f`: **f**ile（文件），指定下一个参数是归档文件的名称。

### tar 和 gzip 结合的威力

真正的威力来自于将 `tar and gzip` 一起使用。您可以先创建一个 `.tar` 归档文件，然后用 `gzip` 压缩它，从而得到一个 `.tar.gz` 文件。然而，`tar` 提供了一种方便的方式，使用 `z` 选项在单个步骤中处理 `tar compression`（tar 压缩）。这个过程有时被称为创建 `gzip tar` 归档文件。

创建压缩归档文件（这是 `compress tar gz` 文件的常见方法）：

```bash
tar czvf myarchive.tar.gz file1 file2 directory1
```

在这里，`z` 选项告诉 `tar` 使用 `gzip` 进行压缩。

### 提取 tar 和 gzip 归档文件

要从归档文件中提取文件，您需要使用 `x` 选项。

提取简单的 `.tar` 归档文件：

```bash
tar xvf myarchive.tar
```

要在一个命令中解压缩并提取 `.tar.gz` 归档文件，只需再次添加 `z` 选项即可：

```bash
tar xzvf myarchive.tar.gz
```

我们来回顾一下提取选项：

- `x`: **e**xtract（提取）归档中的文件。
- `z`: 使用 `g**z**ip` 解压缩归档文件。
- `v`: **v**erbose（详细）模式，列出正在提取的文件。
- `f`: **f**ile（文件），指定要提取的归档文件。

A helpful mnemonic for this is: e**X**tract **Z**ee **V**ery **F**ast!（一个有用的助记符是：快速提取！）

`tar` 是一个非常重要但又经常被遗忘的命令。相关 xkcd：`https://xkcd.com/1168`

### 其他实用程序

虽然 `tar` 和 `gzip` 非常常见，但在您的 Linux 之旅中还会遇到其他归档和压缩格式。这些包括 `bzip2`（创建 `.bz2` 文件并使用 `tar` 中的 `j` 标志）、`xz`（使用 `J` 标志创建 `.xz` 文件）以及熟悉的 `zip`/`unzip` 实用程序。每个都有自己的一套命令和压缩率，但基本概念保持不变。

## Exercise

实践造就完美！以下是一些实践操作实验，以加强您对文件归档和压缩的理解：

1. **[文件打包和压缩](https://labex.io/zh/labs/linux-file-packaging-and-compression-385413)** - 使用 tar、gzip 和 zip 等工具学习基本的 Linux 文件压缩和打包技术。
2. **[在 Linux 中使用 tar 创建和恢复备份](https://labex.io/zh/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - 获得使用 tar 命令创建和恢复文件系统备份的实践经验。
3. **[备份系统日志](https://labex.io/zh/labs/linux-backup-system-log-17989)** - 学习使用 tar 命令和日期格式备份系统日志文件的基本技能。

这些实验将帮助您在实际场景中应用归档和压缩的概念，并建立在 Linux 中管理文件的信心。

## Quiz Question

用于创建归档文件的 tar 标志是什么？请用单个小写英文字母回答。

## Quiz Answer

c
