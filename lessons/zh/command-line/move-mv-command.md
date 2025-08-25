---
index: 11
lang: "zh"
title: "mv (移动)"
meta_title: "mv (移动) - 命令行"
meta_description: "学习如何使用 Linux mv 命令移动和重命名文件/目录。了解其选项并防止覆盖。开始您的 Linux 之旅！"
meta_keywords: "mv 命令, Linux mv, 移动文件 Linux, 重命名文件 Linux, Linux 教程, 初学者, Linux 指南"
---

## Lesson Content

用于移动文件和重命名文件。在标志和功能方面与 `cp` 命令非常相似。

您可以像这样重命名文件：

```bash
mv oldfile newfile
```

或者您可以将文件移动到不同的目录：

```bash
mv file2 /home/pete/Documents
```

并移动多个文件：

```bash
mv file_1 file_2 /somedirectory
```

您也可以重命名目录：

```bash
mv directory1 directory2
```

像 `cp` 一样，如果您 `mv` 一个文件或目录，它将覆盖同一目录中的任何内容。因此，您可以使用 `-i` 标志在覆盖任何内容之前提示您。

```bash
mv -i directory1 directory2
```

假设您确实想 `mv` 一个文件来覆盖前一个文件。您也可以备份该文件，它只会将旧版本重命名为 `~`。

```bash
mv -b directory1 directory2
```

## Exercise

熟能生巧！动手实践对于掌握像 `mv` 这样的 Linux 命令至关重要。这些实验将帮助您在真实环境中巩固对移动和重命名文件及目录的理解：

1. **[Linux mv 命令：文件移动和重命名](https://labex.io/zh/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - 练习使用 `mv` 命令移动和重命名文件和目录，包括理解其各种选项和行为。
2. **[组织文件和目录](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 在实际挑战中应用您对 `mv`（以及 `cp` 和 `rm`）的知识，以组织项目结构、移动文件和清理目录。

这些实验将帮助您在实际场景中应用概念，并使用 `mv` 命令建立文件和目录管理的信心。

## Quiz Question

如何将名为 `cat` 的文件重命名为 `dog`？

## Quiz Answer

mv cat dog