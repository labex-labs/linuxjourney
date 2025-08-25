---
index: 10
lang: "zh"
title: "expand 和 unexpand"
meta_title: "expand 和 unexpand - Text-Fu"
meta_description: "学习使用 `expand` 命令将制表符转换为空格，并使用 `unexpand` 将空格转换回制表符。通过本 Linux 教程改进文本文件格式。"
meta_keywords: "expand 命令，unexpand 命令，Linux 制表符，Linux 空格，文本格式化，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

在关于 `cut` 命令的课程中，我们的 `sample.txt` 文件包含一个制表符。通常，制表符会显示出明显的差异，但有些文本文件显示得不够好。文本文件中的制表符可能无法提供所需的间距。要将制表符更改为空格，请使用 `expand` 命令。

```bash
expand sample.txt
```

上述命令将打印输出，其中每个制表符都转换为一组空格。要将此输出保存到文件中，请使用如下所示的输出重定向。

```bash
expand sample.txt > result.txt
```

与 `expand` 相反，我们可以使用 `unexpand` 命令将每组空格转换回制表符：

```bash
unexpand -a result.txt
```

## Exercise

熟能生巧！以下是一些动手实验，以加强您对 Linux 中文本操作和重定向的理解：

1. **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 练习通过使用 `>` 和 `>>` 等运算符操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin) 来控制命令的数据流。
2. **[简单文本处理](https://labex.io/zh/labs/linux-simple-text-processing-18004)** - 学习使用 `tr`、`col`、`join` 和 `paste` 等强大命令来高效地操作和分析文本数据，从而提高您的命令行数据处理技能。
3. **[文本处理和正则表达式](https://labex.io/zh/labs/linux-text-processing-and-regular-expressions-18003)** - 学习强大的文本处理工具 `grep`、`sed` 和 `awk`，并使用正则表达式在 Linux 中进行高效的文本操作和模式匹配。

这些实验将帮助您在实际场景中应用文本转换和文件操作的概念，并增强您使用 Linux 命令行工具的信心。

## Quiz Question

用于将制表符转换为空格的命令是什么？

## Quiz Answer

expand
