---
index: 6
lang: "zh"
title: "Vim 插入和追加文本"
meta_title: "Vim 插入和追加文本 - 高级文本技巧"
meta_description: "学习 Vim 插入和追加模式。了解 'i'、'a'、'I'、'A'、'o'、'O' 命令以高效编辑文本。立即提升你的 Vim 技能！"
meta_keywords: "Vim 插入模式，Vim 追加，Vim 命令，Vim 教程，Linux 文本编辑器，Vim 初学者，Vim 指南，Vim 'i' 'a"
---

## Lesson Content

Vim 有两种你经常会用到的主要模式：普通模式（用于命令）和插入模式（用于输入文本）。

- 随时按 `Esc` 返回普通模式。

根据你想要输入的位置，可以通过不同的方式进入插入模式：

- `i` – 在光标前插入
- `a` – 在光标后追加
- `I` – 在当前行开头插入
- `A` – 在当前行末尾追加
- `o` – 在当前行下方打开新行并开始插入
- `O` – 在当前行上方打开新行并开始插入

提示：你可以在这些命令前加上一个计数。例如，`3o` 会在下方打开三行新行。

完成文本插入后，按 `Esc` 返回普通模式。

## Exercise

熟能生巧！这里有一些动手实验来巩固你对 Vim 文本编辑功能的理解：

1. **[使用 Vim 和 Nano 在 Linux 中编辑文本文件](https://labex.io/zh/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 练习使用 vi/vim 和 nano 创建文件、编辑文本、保存文件和导航。本实验将帮助你掌握使用 Vim 普通模式和插入模式的基本技能。

本实验将帮助你在实际场景中应用这些概念，并增强使用 Vim 在 Linux 中编辑文本的信心。

## Quiz Question

哪个键可以在光标前进入插入模式？

## Quiz Answer

i
