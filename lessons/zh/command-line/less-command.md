---
index: 8
lang: "zh"
title: "less"
meta_title: "less 命令 - 命令行"
meta_description: "掌握 Linux less 命令以高效查看文本文件。本指南涵盖如何使用 less 命令、导航、执行 unix less 搜索以及如何退出 less。"
meta_keywords: "less 命令，command less, 退出 less, unix less 搜索，linux less, 查看文本文件，文件导航，linux 命令行"
---

## Lesson Content

当查看的文本文件太大而无法适应单个屏幕时，`less 命令`是一个非常有价值的工具。正如一句古老的 Unix 谚语所说：“less is more”（少即是多）。（这是对具有类似功能的 `more` 命令的一种文字游戏）。`less` 实用程序以分页格式显示文本，允许您逐页浏览文件，而无需将整个文件加载到内存中。

### less 命令入门

要开始查看文件，只需使用 `命令 less` 后面跟文件名即可。这将会在 `less` 界面中打开文件。

```bash
less /home/pete/Documents/text1
```

进入 `less` 查看器后，您标准的 shell 命令将无法工作。相反，您需要使用一组特定的按键来导航和与文本交互。

### 导航和控制

您可以使用几个按键在文档中移动：

- **箭头键和翻页键**：使用 `Page Up`（上一页）、`Page Down`（下一页）、`Up`（上箭头）和 `Down`（下箭头）逐行或逐页导航。
- **转到开头**：按 `g` 直接移动到文本文件的开头。
- **转到末尾**：按 `G` (Shift + g) 跳转到文本文件的末尾。
- **帮助菜单**：如果您在 `less` 内部忘记了命令，只需按 `h` 即可显示有用的摘要。

### Unix less 搜索

`less` 的一个强大功能是它搜索文本的能力。要执行 `unix less search`（Unix less 搜索），输入 `/` 后面跟您要查找的文本，然后按 Enter 键。这将高亮显示搜索词的所有出现位置。

- `/search_term`：向前搜索 "search_term"。
- `?search_term`：向后搜索 "search_term"。
- `n`：跳转到搜索词的下一次出现。
- `N`：跳转到上一次出现。

### 如何退出 less

完成文件查看后，您需要知道如何 `exit less`（退出 less）并返回到命令提示符。

- **退出**：只需按 `q` 即可退出 `less` 查看器并返回到 shell。

掌握 `less 命令` 是任何在 Linux 命令行上工作的人的一项基本技能，它使文件检查效率更高。

## Exercise

实践造就完美！以下是一些实践操作实验，以加强您对在 Linux 中查看和导航文本文件的理解：

1. **[Linux less 命令：文件分页](https://labex.io/zh/labs/linux-linux-less-command-file-paging-214301)** - 学习 Linux 'less' 命令，以实现高效的文本文件查看和导航，包括搜索、行号和模式匹配。
2. **[Linux more 命令：文件滚动](https://labex.io/zh/labs/linux-linux-more-command-file-scrolling-214299)** - 学习 Linux 'more' 命令，以实现高效的文本文件查看，涵盖基本用法、从特定行开始以及自定义显示。
3. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 学习使用 `cat`、`more` 和 `less` 等命令，在命令行中高效查看和导航文本文件（包括系统日志和配置文件）的基本 Linux 技能。

这些实验将帮助您在实际场景中应用这些概念，并建立对文本文件操作和导航的信心。

## Quiz Question

如何退出 `less` 命令？请提供单个字符键作为您的答案。注意：答案是区分大小写的英文字母。

## Quiz Answer

q
