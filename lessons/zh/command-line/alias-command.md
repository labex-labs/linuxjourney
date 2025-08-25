---
index: 18
lang: "zh"
title: "alias"
meta_title: "alias - 命令行"
meta_description: "了解如何为常用命令创建和管理 Linux 别名。探索 .bashrc 中临时和永久别名的设置。提高您的命令行效率！"
meta_keywords: "Linux 别名，bash 别名，unalias 命令，.bashrc, Linux 教程，命令行，Linux 初学者，Linux 指南"
---

## Lesson Content

有时输入命令会变得非常重复，或者如果您需要多次输入一个长命令，最好为此使用别名。要为命令创建别名，您只需指定一个别名名称并将其设置为该命令。

```bash
alias foobar='ls -la'
```

现在，您无需输入 `ls -la`，而是可以输入 `foobar`，它将执行该命令——非常棒。请记住，此命令在重启后不会保存您的别名，因此您需要将永久别名添加到：

```plaintext
~/.bashrc
```

或类似文件中，如果您希望它在重启后仍然存在。

您可以使用 `unalias` 命令删除别名：

```bash
unalias foobar
```

## Exercise

虽然此主题没有特定的实验，但我们建议探索全面的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

用于创建别名的命令是什么？

## Quiz Answer

alias
