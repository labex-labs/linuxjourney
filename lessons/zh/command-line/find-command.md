---
lang: "zh"
title: "find"
description: "学习如何使用 Linux 的 'find' 命令来定位文件和目录。探索基本的搜索选项并提高您的 Linux 文件管理技能。"
keywords: "Linux find 命令，Linux 查找文件，Linux 目录搜索，find 命令教程，Linux 文件管理，Linux 初学者，Linux 指南"
---

## Lesson Content

系统中有这么多文件，要找到一个特定的文件可能会有点混乱。不过，我们可以使用一个命令来解决这个问题：`find`！

```bash
find /home -name puppies.jpg
```

使用 `find` 命令时，您需要指定要搜索的目录以及要查找的内容。在本例中，我们正在尝试查找名为 `puppies.jpg` 的文件。

您可以指定要查找的文件类型。

```bash
find /home -type d -name MyFolder
```

您可以看到我将要查找的文件类型设置为 `d`，表示目录，并且我仍然通过名称 `MyFolder` 进行搜索。

值得注意的一点是，`find` 不会停止在您正在搜索的目录；它还会查找该目录可能拥有的任何子目录。

## Exercise

1. 从根目录中查找包含“net”一词的文件。

## Quiz Question

如果我想按名称搜索，我应该为 `find` 指定哪个选项？

## Quiz Answer

-name
