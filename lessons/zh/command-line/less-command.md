---
index: 8
lang: "zh"
title: "less"
meta_title: "less - 命令行"
meta_description: "学习如何使用 Linux 'less' 命令进行高效的文本文件查看和导航。通过这份适合初学者的指南，掌握分页、搜索和退出。"
meta_keywords: "less 命令，Linux less, 查看文本文件，导航文件，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

如果你正在查看比简单输出更大的文本文件，那么 `less` 命令会更有效。（实际上有一个名为 `more` 的命令，它做的事情类似，所以这有点讽刺。）文本以分页方式显示，因此你可以逐页浏览文本文件。

继续使用 `less` 查看文件的内容。一旦进入 `less` 命令，你实际上可以使用其他键盘命令在文件中导航。

```bash
less /home/pete/Documents/text1
```

使用以下命令在 `less` 中导航：

- `q` - 用于退出 `less` 并返回到你的 shell。
- `Page up`, `Page down`, `Up` 和 `Down` - 使用箭头键和翻页键导航。
- `g` - 移动到文本文件的开头。
- `G` - 移动到文本文件的末尾。
- `/search` - 你可以在文本文档中搜索特定文本。在你想要搜索的单词前加上 `/`。
- `h` - 如果你在 `less` 中需要关于如何使用 `less` 的一点帮助，请使用 help。

## Exercise

在一个文件上运行 `less`，然后向上和向下翻页。尝试搜索一个特定的单词。快速导航到文件的开头或结尾。

如需 `less` 命令的动手实践，请尝试此交互式实验：

- [Linux less Command: File Paging](https://labex.io/zh/labs/linux-linux-less-command-file-paging-214301)

## Quiz Question

如何退出 `less` 命令？

## Quiz Answer

q
