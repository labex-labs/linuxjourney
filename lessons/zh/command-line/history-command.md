---
index: 9
lang: "zh"
title: "历史记录"
meta_title: "历史记录 - 命令行"
meta_description: "掌握 Linux 中的 history 命令，高效地回顾和管理您的命令行活动。了解如何查看历史记录、使用 Ctrl-R 等快捷键，以及使用 history -c 和 history -d 等选项管理历史记录。"
meta_keywords: "linux 历史记录，history -c linux, history -d linux, history -w linux, unix 历史命令，bash 历史记录，命令行，Ctrl-R, 清除命令"
---

## Lesson Content

您的 shell 会记录您之前输入过的命令。您可以访问此列表，当您想查找并重用命令而无需重新输入时，此列表非常有用。`history` 命令是大多数 Unix 和 Linux 环境中的基本工具。

### 查看命令历史记录

要查看您使用过的命令列表，只需输入 `history` 命令即可。此功能提供了详细的活动日志，便于跟踪您的 `history in linux`。

```bash
history
```

### 重新运行之前的命令

shell 提供了一些快捷方式，使重新运行命令更加容易。

- **向上箭头**：想再次运行刚刚执行的命令吗？只需按下向上箭头键即可向后循环浏览您的历史记录。
- **`!!` 快捷方式**：要再次执行最近的命令，您可以使用 `!!`。例如，如果您刚刚运行了 `cat file1`，输入 `!!` 然后按 Enter 将再次运行 `cat file1`。

### 搜索历史记录

最强大的历史记录快捷方式之一是 `Ctrl-R`。这会启动反向搜索。按下 `Ctrl-R` 后，开始输入您要查找的命令的任何部分，shell 将显示最近的匹配项。您可以重复按 `Ctrl-R` 来循环查看更早的匹配项。找到所需的命令后，只需按 Enter 即可执行它。

### 管理历史记录列表

除了查看历史记录之外，您还可以直接管理它。

- **清除历史记录**：如果您想清除当前会话的命令历史记录，可以使用 `history -c linux` 命令。这将从内存中的历史记录列表中删除所有条目。
- **写入文件**：要将当前会话的历史记录保存到您的历史文件（通常是 `~/.bash_history`），您可以使用 `history -w linux`。这在关闭会话之前保存命令时很有用。
- **删除特定条目**：您可以使用 `history -d <offset>` 从历史记录中删除单个命令。Offset 是 `history` 输出中命令旁显示的数字。例如，`history -d 101` 将删除第 101 个条目。这是 `history -d linux` 的一个关键功能。

### 其他有用的终端工具

随着终端窗口的填满，您可能希望清理它。使用 `clear` 命令可以擦除显示内容，开始一个干净的屏幕。

```bash
clear
```

另一个不可或缺的功能是标签补全。如果您开始输入命令、文件名或目录的开头并按下 Tab 键，shell 将尝试自动完成它。如果有多个可能性，它可能会向您显示选项或不执行任何操作。再次按 Tab 键通常会列出所有可能的补全项。

## Exercise

虽然此主题没有特定的实验，但我们建议您探索全面的[Linux 学习路径](https://labex.io/zh/learn/linux)来练习相关的 Linux 技能和概念。

## Quiz Question

清除终端的命令是什么？（请仅用小写英文字母回答）

## Quiz Answer

clear
