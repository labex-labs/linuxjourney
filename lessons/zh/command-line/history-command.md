---
index: 9
lang: "zh"
title: "history"
meta_title: "history - 命令行"
meta_description: "学习如何使用 Linux history 命令、!! 快捷方式和 Ctrl-R 来高效地召回命令。通过这些基本技巧提高您的终端生产力！"
meta_keywords: "Linux history, bash history, Ctrl-R, clear command, Linux 教程, 命令行, 初学者指南"
---

## Lesson Content

您的 shell 中有您之前输入的命令历史记录。您可以查看这些命令。当您想查找并运行以前使用过的命令而无需再次输入时，这非常有用。

```bash
history
```

想运行之前执行过的相同命令吗？只需按向上箭头键。

想不重新输入就运行上一个命令吗？使用 `!!`。如果您输入了 `cat file1` 并想再次运行它，您实际上只需输入 `!!`，它就会运行您上次运行的命令。

另一个历史记录快捷方式是 `Ctrl-R`。这是反向搜索命令。如果您按下 `Ctrl-R` 并开始输入您想要的命令的一部分，它将显示匹配项。您可以通过再次按下 `Ctrl-R` 键来浏览它们。一旦找到您想再次使用的命令，只需按 Enter 键。

我们的终端有点杂乱了，不是吗？让我们清理一下。使用 `clear` 命令来清除您的显示。

```bash
clear
```

看，这样好多了，不是吗？

当我们谈论有用的东西时，任何命令行环境中最有用的功能之一就是 Tab 补全。如果您开始输入命令、文件、目录等的开头，然后按下 Tab 键，它将根据在您搜索的目录中找到的内容自动补全，只要您没有其他以这些字母开头的文件。例如，如果您尝试运行 `chrome` 命令，您可以输入 `chr` 并按下 Tab 键，它将自动补全为 `chrome`。

## Exercise

虽然本主题没有特定的实验，但我们建议探索全面的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

清除终端的命令是什么？

## Quiz Answer

clear