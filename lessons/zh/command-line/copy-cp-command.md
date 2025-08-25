---
index: 10
lang: "zh"
title: "cp (复制)"
meta_title: "cp (复制) - 命令行"
meta_description: "了解如何使用 Linux cp 命令复制文件和目录。理解 -r 和通配符等选项。立即开始您的 Linux 之旅！"
meta_keywords: "cp 命令, 复制文件 Linux, Linux 教程, Linux 初学者, cp -r, Linux 通配符, Linux 指南"
---

## Lesson Content

让我们开始复制这些文件。就像在其他操作系统中复制和粘贴文件一样，shell 为我们提供了一种更简单的方法。

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile` 是您要复制的文件，而 `/home/pete/Documents/cooldocs` 是您将文件复制到的位置。

您可以复制多个文件和目录，也可以使用通配符。通配符是一个字符，可以替换为基于模式的选择，从而为您提供更大的搜索灵活性。您可以在每个命令中使用通配符以获得更大的灵活性。

- `*` 通配符中的通配符，用于表示所有单个字符或任何字符串。
- `?` 用于表示一个字符
- `[]` 用于表示方括号内的任何字符

```bash
cp *.jpg /home/pete/Pictures
```

这会将当前目录中所有扩展名为 `.jpg` 的文件复制到 `Pictures` 目录。

一个有用的命令是使用 `-r` 标志；这将递归复制目录中的文件和目录。

尝试对包含几个文件的目录执行 `cp` 命令到您的 `Documents` 目录。没有成功，对吗？那是因为您需要使用 `-r` 命令同时复制其中的文件和目录。

```bash
cp -r Pumpkin/ /home/pete/Documents
```

需要注意的一点是，如果您将文件复制到具有相同文件名的目录中，则该文件将被您复制过去的内容覆盖。如果您有一个不想被意外覆盖的文件，这可不是什么好事。您可以使用 `-i` 标志（交互式）在覆盖文件之前提示您。

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

熟能生巧！这里有一些动手实验来巩固您对 Linux 中复制文件和目录的理解：

1. **[Linux cp 命令：文件复制](https://labex.io/zh/labs/linux-linux-cp-command-file-copying-209744)** - 练习基本用法、递归复制、保留属性和使用通配符等高级选项，以高效复制文件和目录。
2. **[组织文件和目录](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 通过使用 `cp`、`mv` 和 `rm` 命令来组织项目结构、移动文件和清理不必要的目录，练习基本的 Linux 文件管理技能。

这些实验将帮助您在实际场景中应用概念，并增强您在 Linux 中进行文件复制和管理的信心。

## Quiz Question

复制目录需要指定哪个标志？

## Quiz Answer

-r