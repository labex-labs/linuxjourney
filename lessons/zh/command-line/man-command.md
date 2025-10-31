---
index: 16
lang: "zh"
title: "手册"
meta_title: "man 命令 - 命令行"
meta_description: "学习如何在 Linux 中使用 'man' 命令来访问 'ls' 等命令的详细手册。理解 man ls 页面以掌握命令行。"
meta_keywords: "man, man ls, ls 手册，ls -l 手册，Linux 手册页，命令手册，Linux 文档，命令行帮助"
---

## Lesson Content

在 Linux 中，几乎每个命令都附带了自己的使用手册。这些被称为“man 页面”（manual pages 的缩写），是有效学习如何使用系统的基本资源。

### 理解 Man 页面

Man 页面是 Linux 命令、实用程序和系统调用的内置文档。它们提供了关于命令功能的详细描述、可用的选项（或标志）以及如何使用它。它们是你获取命令行帮助的首选和最佳来源。

### 使用 man 访问手册

要查看任何命令的手册，你需要使用 `man` 命令本身，后跟你想了解的命令名称。例如，要阅读 `ls` 命令的手册，你可以输入：

```bash
man ls
```

这将打开 `ls man` 页面，这是一个详细介绍其所有功能的综合文档。你可以使用箭头键滚动浏览手册，按 `q` 键退出并返回命令行。

### 查找命令选项的详细信息

Man 页面在理解命令选项方面特别有用。例如，如果你见过 `ls -l` 命令，并想知道 `-l` 标志的作用或输出中每列的含义，`man ls` 页面会提供完整的解释。它是任何命令变体的权威指南，使其成为不可或缺的工具。

## Exercise

实践是掌握命令行的关键。这些动手实验将帮助你巩固对基本命令的掌握。完成它们后，使用 `man` 命令来探索每种工具的全部潜力。

1.  **[Linux ls 命令：内容列表](https://labex.io/zh/labs/linux-linux-ls-command-content-listing-219205)** - 练习列出和分析文件和目录内容，然后使用 `man ls` 发现更多选项。
2.  **[Linux pwd 命令：目录显示](https://labex.io/zh/labs/linux-linux-pwd-command-directory-displaying-209734)** - 学习使用 `pwd` 命令显示当前目录，并探索其 man 页面以获取详细信息。
3.  **[Linux cd 命令：目录切换](https://labex.io/zh/labs/linux-linux-cd-command-directory-changing-209733)** - 通过 `cd` 掌握文件系统导航，并使用 `man cd` 来理解其各种技术。

这些实验将帮助你在实际场景中应用核心概念，并建立对基本 Linux 命令的信心，为你有效地使用 `man` 来加深知识做好准备。

## Quiz Question

如何查看命令的手册？（请仅用小写英文字母回答命令名称）。

## Quiz Answer

man
