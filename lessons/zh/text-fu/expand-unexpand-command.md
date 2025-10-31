---
index: 10
lang: "zh"
title: "展开和取消展开"
meta_title: "展开和取消展开 - Text-Fu"
meta_description: "使用我们的 expand 和 unexpand 命令指南，掌握 Linux 中的文本格式设置。了解如何将制表符转换为空格，以及将空格转换回制表符，以实现一致的文件布局。"
meta_keywords: "expand 命令，unexpand 命令，Linux 制表符，Linux 空格，文本格式化，Linux 教程，Linux 入门，Linux 指南"
---

## Lesson Content

不一致的间距会使文本文件难以阅读。虽然制表符旨在创建统一的缩进，但它们在不同编辑器和系统上的显示宽度可能会有所不同。这会破坏文本格式和对齐。幸运的是，Linux 提供了通过在制表符和空格之间转换来管理此问题的简单工具。本初学者 Linux 指南将引导您完成此过程。

### 使用 expand 命令将制表符转换为空格

当您需要确保间距一致时，可以使用 `expand` 命令将制表符转换为标准数量的空格。此命令读取文件，将每个制表符替换为一组空格字符，并将结果打印到标准输出。

```bash
expand sample.txt
```

默认情况下，`expand command` 将每个制表符转换为 8 个空格。这个简单的实用程序是改善文本格式的强大工具。

### 保存转换后的输出

`expand` 命令仅将转换后的文本打印到终端。要保存更改，您必须将输出重定向到新文件。

```bash
expand sample.txt > result.txt
```

此命令获取 `expand sample.txt` 的输出并将其写入 `result.txt`，为您提供一个不含制表符而只含空格的新文件。

### 使用 unexpand 命令将空格转换回制表符

反向操作，即将空格转换回制表符，由 `unexpand` 命令处理。这对于减小文件大小或遵守要求使用制表符的编码标准非常有用。

```bash
unexpand -a result.txt
```

默认情况下，`unexpand` 只转换每行开头的空格。`-a` 选项告诉 `unexpand command` 将所有 8 个空格的实例转换为制表符，而不仅仅是行首的空格，从而对您的 Linux 空格和制表符提供更全面的控制。

## Exercise

为了掌握 Linux 中的文本操作和重定向，实践是关键。以下动手实验将帮助您巩固理解：

1. **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 练习使用 `>` 和 `>>` 等运算符来操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin)，从而控制命令的数据流。
2. **[简单的文本处理](https://labex.io/zh/labs/linux-simple-text-processing-18004)** - 学习使用 `tr`、`col`、`join` 和 `paste` 等强大命令来有效地操作和分析文本数据，增强您在数据处理方面的命令行技能。
3. **[文本处理和正则表达式](https://labex.io/zh/labs/linux-text-processing-and-regular-expressions-18003)** - 学习强大的文本处理工具 `grep`、`sed` 和 `awk`，并使用正则表达式在 Linux 中进行高效的文本操作和模式匹配。

完成这些实验将帮助您在实际场景中应用文本转换和文件操作的概念，增强您对基本 Linux 命令行工具的信心。

## Quiz Question

用于将制表符转换为空格的命令是什么？（请使用小写的英文命令名称回答。）

## Quiz Answer

expand
