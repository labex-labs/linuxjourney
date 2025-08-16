---
lang: "zh"
title: "less"
description: "学习如何使用 Linux 的 'less' 命令高效地查看和导航文本文件。通过这份适合初学者的指南，掌握分页、搜索和退出。"
keywords: "less 命令，Linux less, 查看文本文件，导航文件，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

如果你正在查看比简单输出更大的文本文件，`less` 命令会更高效。（实际上有一个名为 `more` 的命令功能类似，所以这有点讽刺。）文本以分页方式显示，因此你可以逐页浏览文本文件。

继续使用 `less` 查看文件的内容。一旦进入 `less` 命令，你实际上可以使用其他键盘命令在文件中导航。

```bash
less /home/pete/Documents/text1
```

使用以下命令在 `less` 中导航：

- `q` - 用于退出 `less` 并返回到你的 shell。
- `Page up`, `Page down`, `Up` 和 `Down` - 使用方向键和翻页键导航。
- `g` - 移动到文本文件的开头。
- `G` - 移动到文本文件的末尾。
- `/search` - 你可以在文本文档中搜索特定文本。在你想要搜索的单词前加上 `/`。
- `h` - 如果你在 `less` 中需要关于如何使用 `less` 的帮助，请使用帮助。

## Exercise

对一个文件运行 `less`，然后向上和向下翻页。尝试搜索一个特定的单词。快速导航到文件的开头或结尾。

## Quiz Question

How do you quit out of a `less` command?

## Quiz Answer

q
