---
index: 13
lang: "zh"
title: "rm (删除)"
meta_title: "rm (删除) - 命令行"
meta_description: "学习如何在 Linux 中使用 `rm` 命令安全地删除文件和目录。了解 -f、-i、-r 和 rmdir 等选项。开始您的 Linux 之旅！"
meta_keywords: "rm 命令, 删除文件 Linux, 删除目录, Linux 教程, Linux 初学者, rmdir, Linux 指南"
---

## Lesson Content

现在，我觉得文件太多了；让我们删除一些。要删除文件，可以使用 `rm` 命令。`rm` (remove) 命令用于删除文件和目录。

```bash
rm file1
```

使用 `rm` 时要小心；没有神奇的回收站可以从中找回已删除的文件。一旦它们消失了，就永远消失了，所以要小心。

幸运的是，有一些安全措施，所以普通用户不能随意删除一堆重要文件。受写保护的文件在删除前会提示您确认。如果目录受写保护，它也不会轻易被删除。

现在，如果您不关心这些，您绝对可以删除一堆文件。

```bash
rm -f file1
```

`-f` 或 force 选项告诉 `rm` 删除所有文件，无论它们是否受写保护，而无需提示用户（只要您有适当的权限）。

```bash
rm -i file
```

添加 `-i` 标志，就像许多其他命令一样，会提示您是否确实要删除文件或目录。

```bash
rm -r directory
```

默认情况下，您不能直接 `rm` 一个目录；您需要添加 `-r` 标志（recursive）来删除其中的所有文件和任何子目录。

您可以使用 `rmdir` 命令删除目录。

```bash
rmdir directory
```

## Exercise

熟能生巧！以下是一些动手实验，以加深您对 Linux 中文件和目录删除的理解：

1. **[Linux rm 命令：文件删除](https://labex.io/zh/labs/linux-linux-rm-command-file-removing-209741)** - 学习如何使用 `rm` 命令删除文件和目录，包括 `-r` 和 `-i` 等各种选项，并练习安全有效的文件删除。
2. **[组织文件和目录](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 在实际挑战中，练习基本的 Linux 文件管理技能，包括使用 `rm` 清理不必要的目录。

这些实验将帮助您在实际场景中应用概念，并增强在 Linux 中管理文件和目录的信心。

## Quiz Question

如何删除名为 `myfile` 的文件？

## Quiz Answer

rm myfile