---
index: 16
lang: "zh"
title: "man 命令"
meta_title: "man 命令 - 命令行手册"
meta_description: "通过示例学习 Linux man 命令，了解如何阅读手册页、在手册页中搜索、理解章节以及查找命令选项。"
meta_keywords: "man 命令, linux man 页, 命令手册, man ls, man 章节, 搜索 man 页, 命令行帮助"
---

## Lesson Content

在 Linux 中，几乎每个命令都有自己的使用说明手册。这些被称为“man 页”（manual pages 的缩写），是学习如何有效使用系统的重要资源。

### 理解 Man 页

Man 页是 Linux 命令、工具和系统调用的内置文档。它们详细描述了命令的功能、可用选项（或标志）以及如何使用。它们是你获取命令行帮助的首选且最佳来源。

### 使用 man 访问手册

要查看任何命令的手册，使用 `man` 后跟命令名称。例如，要阅读 `ls` 的手册，输入：

```bash
$ man ls
```

这会打开 `ls` 的 man 页。你可以用方向键滚动，用 `/` 搜索，按 `q` 退出。

### 查找命令选项的详细信息

Man 页对于理解命令选项特别有用。例如，如果你见过 `ls -l` 并想知道 `-l` 的含义，可以打开 `man ls` 并搜索 `-l`。

在 man 页内：

- 按 `/` 并输入搜索词向前搜索。
- 按 `n` 跳转到下一个匹配项。
- 按 `N` 跳转到上一个匹配项。
- 按 `q` 退出。

### 理解 Man 页章节

手册页按编号章节组织。常见章节包括：

- `1`：用户命令。
- `2`：系统调用。
- `3`：库函数。
- `5`：文件格式。
- `8`：系统管理命令。

有时同一名称会出现在多个章节中。你可以指定章节号：

```bash
$ man 5 passwd
$ man 1 passwd
```

### 常见问题

**为什么 man 输出这么长？** Man 页是参考文档。使用 man 内的搜索功能跳转到你需要的部分。

**如何退出 man？** 按 `q`。

**如果没有 man 页怎么办？** 尝试 `COMMAND --help`、`help COMMAND`，或安装你发行版的文档包。

## Exercise

实践是掌握命令行的关键。这些动手实验将帮助你巩固基础命令的技能。完成后，使用 `man` 命令探索每个工具的全部潜力。

1. **[Linux ls 命令：内容列表](https://labex.io/zh/labs/linux-linux-ls-command-content-listing-219205)** - 练习列出和分析文件及目录内容，然后使用 `man ls` 发现更多选项。
2. **[Linux pwd 命令：显示目录](https://labex.io/zh/labs/linux-linux-pwd-command-directory-displaying-209734)** - 学习 `pwd` 命令显示当前目录，并探索其 man 页了解详情。
3. **[Linux cd 命令：切换目录](https://labex.io/zh/labs/linux-linux-cd-command-directory-changing-209733)** - 掌握使用 `cd` 导航文件系统，并使用 `man cd` 理解其各种用法。

这些实验将帮助你在实际场景中应用核心概念，建立对基本 Linux 命令的信心，为你有效使用 `man` 深入学习打下基础。

## Quiz Question

如何查看某个命令的手册？（请仅用小写英文字母回答命令名称）

## Quiz Answer

man
