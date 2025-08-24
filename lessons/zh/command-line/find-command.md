---
index: 14
lang: "zh"
title: "find"
meta_title: "find - 命令行"
meta_description: "了解如何使用 Linux 'find' 命令来定位文件和目录。发现基本搜索选项并提高您的 Linux 文件管理技能。"
meta_keywords: "Linux find 命令，Linux 查找文件，Linux 目录搜索，find 命令教程，Linux 文件管理，Linux 初学者，Linux 指南"
---

## Lesson Content

系统中有这么多文件，要找到一个特定的文件可能会有点麻烦。不过，我们可以使用一个命令来解决这个问题：`find`！

```bash
find /home -name puppies.jpg
```

使用 `find` 命令时，您需要指定要搜索的目录以及要查找的内容。在本例中，我们正在尝试按名称查找文件 `puppies.jpg`。

您可以指定要查找的文件类型。

```bash
find /home -type d -name MyFolder
```

您可以看到我将要查找的文件类型设置为 `d`，表示目录，并且我仍然按名称 `MyFolder` 进行搜索。

值得注意的一点是，`find` 不会停止在您正在搜索的目录；它还会查找该目录可能包含的任何子目录。

## Exercise

1. 从根目录中查找包含“net”一词的文件。

如需使用 `find` 命令进行实践操作，请尝试此交互式实验：

- [Linux find Command: File Searching](https://labex.io/zh/labs/linux-linux-find-command-file-searching-219191)

## Quiz Question

如果我想按名称搜索，我应该为 `find` 指定哪个选项？

## Quiz Answer

-name
