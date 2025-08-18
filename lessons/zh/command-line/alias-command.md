---
lang: "zh"
title: "别名"
meta_description: "学习如何为常用命令创建和管理 Linux 别名。了解如何在 .bashrc 中设置临时和永久别名。提高您的命令行效率！"
meta_keywords: "Linux 别名，bash 别名，unalias 命令，.bashrc, Linux 教程，命令行，Linux 初学者，Linux 指南"
---

## Lesson Content

有时输入命令会非常重复，或者如果您需要多次输入一个长命令，最好为此使用一个别名。要为命令创建别名，您只需指定一个别名名称并将其设置为该命令。

```bash
alias foobar='ls -la'
```

现在，您无需输入 `ls -la`，而是可以输入 `foobar`，它将执行该命令——非常棒。请记住，此命令在重启后不会保存您的别名，因此如果您希望它在重启后仍然存在，则需要将永久别名添加到：

```plaintext
~/.bashrc
```

或类似文件中。

您可以使用 `unalias` 命令删除别名：

```bash
unalias foobar
```

## Exercise

创建几个别名，然后删除它们。

## Quiz Question

用于创建别名的命令是什么？

## Quiz Answer

alias
