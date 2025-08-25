---
index: 8
lang: "zh"
title: "less"
meta_title: "less - 命令行"
meta_description: "学习如何使用 Linux 'less' 命令进行高效的文本文件查看和导航。通过这份适合初学者的指南，掌握分页、搜索和退出。"
meta_keywords: "less 命令, Linux less, 查看文本文件, 导航文件, Linux 教程, Linux 初学者, Linux 指南"
---

## Lesson Content

如果您正在查看比简单输出更大的文本文件，那么 `less` 命令会更有效。（实际上有一个名为 `more` 的命令，它做的事情类似，所以这很讽刺。）文本以分页方式显示，因此您可以逐页浏览文本文件。

继续使用 `less` 查看文件的内容。一旦进入 `less` 命令，您实际上可以使用其他键盘命令在文件中导航。

```bash
less /home/pete/Documents/text1
```

使用以下命令在 `less` 中导航：

- `q` - 用于退出 `less` 并返回到您的 shell。
- `Page up`、`Page down`、`Up` 和 `Down` - 使用箭头键和翻页键导航。
- `g` - 移动到文本文件的开头。
- `G` - 移动到文本文件的末尾。
- `/search` - 您可以在文本文档中搜索特定文本。在您要搜索的单词前加上 `/`。
- `h` - 如果您在使用 `less` 时需要一些关于如何使用 `less` 的帮助，请使用帮助。

## Exercise

熟能生巧！以下是一些动手实验，以加强您对在 Linux 中查看和导航文本文件的理解：

1. **[Linux less 命令：文件分页](https://labex.io/zh/labs/linux-linux-less-command-file-paging-214301)** - 学习 Linux 的 'less' 命令，用于高效的文本文件查看和导航，包括搜索、行号和模式匹配。
2. **[Linux more 命令：文件滚动](https://labex.io/zh/labs/linux-linux-more-command-file-scrolling-214299)** - 学习 Linux 的 'more' 命令，用于高效的文本文件查看，包括基本用法、从特定行开始以及自定义显示。
3. **[在 Linux 中查看日志和配置文件](https://labex.io/zh/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 学习基本的 Linux 命令行技能，使用 `cat`、`more` 和 `less` 等命令高效地查看和导航文本文件，包括系统日志和配置文件。

这些实验将帮助您在实际场景中应用概念，并增强您对文本文件操作和导航的信心。

## Quiz Question

如何退出 `less` 命令？

## Quiz Answer

q