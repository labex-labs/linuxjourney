---
index: 14
lang: "zh"
title: "find"
meta_title: "find - 命令行"
meta_description: "了解如何使用 Linux 'find' 命令来定位文件和目录。发现基本搜索选项并提高您的 Linux 文件管理技能。"
meta_keywords: "Linux find 命令，find 文件 Linux, Linux 目录搜索，find 命令教程，Linux 文件管理，Linux 初学者，Linux 指南"
---

## Lesson Content

系统中有这么多文件，要找到一个特定的文件可能会有点麻烦。不过，我们可以使用一个命令来解决这个问题：`find`！

```bash
find /home -name puppies.jpg
```

使用 `find` 命令时，您必须指定要搜索的目录以及要查找的内容。在本例中，我们尝试按名称查找文件 `puppies.jpg`。

您可以指定要查找的文件类型。

```bash
find /home -type d -name MyFolder
```

您可以看到我将要查找的文件类型设置为 `d`，表示目录，并且我仍然按名称 `MyFolder` 进行搜索。

值得注意的一点是，`find` 不会停止在您正在搜索的目录；它还会查找该目录可能包含的任何子目录。

## Exercise

熟能生巧！以下是一些动手实验，旨在加强您对在 Linux 中查找文件和目录的理解：

1. **[Linux find 命令：文件搜索](https://labex.io/zh/labs/linux-linux-find-command-file-searching-219191)** - 本实验介绍了 `find` 命令，这是一个多功能的实用程序，用于根据各种条件搜索和定位文件和目录。您将练习使用 `find` 来定位特定文件。
2. **[发现关键系统资源](https://labex.io/zh/labs/linux-discover-critical-system-resources-388032)** - 学习用于定位文件和可执行文件的基本 Linux 命令，包括 `find`。您将练习有效地导航文件系统并发现关键系统资源。

这些实验将帮助您在实际场景中应用概念，并增强有效使用 `find` 命令的信心。

## Quiz Question

如果我想按名称搜索，我应该为 `find` 指定哪个选项？

## Quiz Answer

-name
