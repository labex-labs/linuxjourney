---
lang: "zh"
title: "expand 和 unexpand"
description: "学习使用 `expand` 命令将制表符转换为空格，并使用 `unexpand` 命令将空格转换为制表符。通过本 Linux 教程改进文本文件格式。"
keywords: "expand 命令，unexpand 命令，Linux 制表符，Linux 空格，文本格式化，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

在我们关于 `cut` 命令的课程中，我们有一个包含制表符的 `sample.txt` 文件。通常，制表符会显示出明显的区别，但有些文本文件显示得不够好。文本文件中的制表符可能无法提供所需的间距。要将制表符更改为空格，请使用 `expand` 命令。

```bash
expand sample.txt
```

上面的命令将打印输出，其中每个制表符都转换为一组空格。要将此输出保存到文件中，请使用如下所示的输出重定向。

```bash
expand sample.txt > result.txt
```

与 `expand` 相反，我们可以使用 `unexpand` 命令将每组空格转换回制表符：

```bash
unexpand -a result.txt
```

## Exercise

如果您只输入 `expand` 而不带文件输入，会发生什么？

## Quiz Question

用于将制表符转换为空格的命令是什么？

## Quiz Answer

expand
