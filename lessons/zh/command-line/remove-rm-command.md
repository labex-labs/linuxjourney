---
index: 13
lang: "zh"
title: "rm (删除)"
meta_title: "rm (删除) - 命令行"
meta_description: "掌握 Linux 中的 `rm` 命令，安全地删除文件和目录。了解 `-f`、`-i`、`-r` 等选项以及 `rmdir` 命令。理解 `rm -rf linux` 的强大功能以及使用 Linux rm 命令时保持谨慎的重要性。"
meta_keywords: "rm 命令，Linux 删除文件，删除目录，Linux 教程，Linux 初学者，rmdir, linux rm 命令，rm -rf linux, rm linux, linux rm -rf, rm -rf linux 命令"
---

## Lesson Content

我们经常会积累过多的文件，有时需要删除一些。要删除文件，您可以使用 `rm` 命令。`rm`（remove，删除）命令是 Linux 中删除文件和目录的基础命令。

```bash
rm file1
```

### 使用 rm 命令的注意事项

使用 `rm` 命令时务必小心谨慎。与图形操作系统不同，Linux 中没有神奇的“回收站”或“垃圾箱”可以找回已删除的文件。一旦文件通过 `rm` 命令删除，它们就永远消失了。在使用像 `rm -rf linux` 这样强大的命令时尤其如此。

幸运的是，系统设置了一些安全措施。例如，受写保护的文件在删除前会提示您确认。同样，受写保护的目录也不会轻易被删除。

### 强制删除文件

如果您需要绕过这些安全提示并强制删除文件，可以使用强制选项。

```bash
rm -f file1
```

`-f` 或 force（强制）选项指示 `rm` 命令删除所有指定的文件，无论它们是否受写保护，并且不向用户发出提示（前提是您拥有必要的权限）。这通常是强大但危险的 `rm -rf linux command` 序列的一部分。

### 交互式删除

为了更安全的删除，您可以使用交互式标志。

```bash
rm -i file
```

添加 `-i` 标志（类似于许多其他 Linux 命令）会在实际删除文件或目录之前提示您确认。这是在使用 `linux rm command` 时避免意外删除的好习惯。

### 递归删除目录

默认情况下，您不能简单地使用 `rm` 来删除目录。您必须添加递归标志。

```bash
rm -r directory
```

您需要添加 `-r` 标志（recursive，递归）来删除目录，这也会删除该目录包含的所有文件和任何子目录。这就是臭名昭著的 `linux rm -rf` 组合中的“r”。

### 使用 rmdir 删除空目录

或者，您可以使用 `rmdir` 命令删除空目录。

```bash
rmdir directory
```

`rmdir` 命令比 `rm -r` 更安全，因为它仅在目录完全为空时才起作用。

## Exercise

熟能生巧！这里有一些动手实验，以巩固您对 Linux 中文件和目录删除的理解：

1. **[Linux rm 命令：文件删除](https://labex.io/zh/labs/linux-linux-rm-command-file-removing-209741)** - 学习如何使用 `rm` 命令删除文件和目录，包括 `-r` 和 `-i` 等各种选项，并练习安全有效的文件删除。
2. **[组织文件和目录](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 在实际挑战中，练习基本的 Linux 文件管理技能，包括使用 `rm` 命令清理不必要的目录。

这些实验将帮助您在实际场景中应用这些概念，并增强您管理 Linux 文件和目录的信心。

## Quiz Question

如何删除名为 `myfile` 的文件？（请使用完全准确的命令，区分大小写。）

## Quiz Answer

rm myfile
