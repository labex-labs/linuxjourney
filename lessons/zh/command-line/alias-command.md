---
index: 18
lang: "zh"
title: "别名"
meta_title: "别名 - 命令行"
meta_description: "了解如何在 Linux 中创建和管理命令行别名，以简化您的工作流程。本指南涵盖使用 alias 命令和 .bashrc 文件创建临时和永久别名。"
meta_keywords: "linux 别名，linux alias 命令，linux 命令行别名，linux 命令别名，bash 别名，unalias 命令，.bashrc, 命令行，Linux 教程"
---

## Lesson Content

输入冗长或重复的命令可能会很乏味。幸运的是，您可以创建一个快捷方式，即**Linux 别名 (alias)**，以使您的命令行体验更高效。`alias` 命令允许您为任何命令或命令序列定义一个自定义名称。

### 创建临时别名

要创建一个仅在当前终端会话中有效的临时别名，您只需指定一个名称并将其设置为等于命令字符串。

例如，要为 `ls -la` 命令创建一个名为 `ll` 的别名，您将使用 `alias command linux` 语法，如下所示：

```bash
alias ll='ls -la'
```

现在，您无需输入 `ls -la`，只需输入 `ll` 即可执行相同的命令。这是自定义 shell 的一种简单而强大的方法。

### 使别名永久化

临时别名在您关闭终端或重新启动系统后就会消失。要使 **command alias in linux** 永久化，您需要将其添加到 shell 的配置文件中。对于 Bash shell，该文件通常是 `~/.bashrc`。

1. 在文本编辑器中打开文件：`nano ~/.bashrc`
2. 将您的别名定义添加到文件中，就像您在命令行中输入的那样：

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. 保存文件并退出编辑器。

为了使更改生效，您必须关闭并重新打开终端，或者使用 `source` 命令告诉 shell 重新加载配置文件：

```bash
source ~/.bashrc
```

您的 **Linux command alias** 现在每次启动新的终端会话时都将可用。

### 移除别名

如果您不再需要别名，可以使用 `unalias` 命令将其删除。这将从当前会话中删除它。

```bash
unalias ll
```

要删除永久别名，您还必须从 `~/.bashrc` 文件中删除其定义。

## Exercise

虽然此主题没有特定的实验环节，但我们建议探索全面的[Linux 学习路径](https://labex.io/zh/learn/linux)来练习相关的 Linux 技能和概念。

## Quiz Question

用于创建别名的命令是什么？请用小写英文回答。

## Quiz Answer

alias
