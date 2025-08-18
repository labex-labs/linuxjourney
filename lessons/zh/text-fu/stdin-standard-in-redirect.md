---
index: 2
lang: "zh"
title: "stdin (标准输入)"
meta_title: "stdin (标准输入) - 文本操作"
meta_description: "了解 Linux 中 stdin（标准输入）重定向。理解如何将 '<' 运算符与文件和命令一起使用。探索实际示例并提高您的 Linux 命令行技能。"
meta_keywords: "stdin, 标准输入，Linux 重定向，< 运算符，Linux 教程，命令行，初学者，指南"
---

## Lesson Content

在上一课中，我们了解到可以使用不同的标准输出（stdout）流，例如文件或屏幕。同样，我们也可以使用不同的标准输入（stdin）流。我们知道可以通过键盘等设备进行 stdin 输入，但我们也可以使用文件、其他进程的输出以及终端。让我们看一个例子。

让我们使用上一课中的 `peanuts.txt` 文件作为此示例。请记住，它包含文本“Hello World”。

```bash
cat < peanuts.txt > banana.txt
```

就像我们使用 `>` 进行 stdout 重定向一样，我们可以使用 `<` 进行 stdin 重定向。

通常，在 `cat` 命令中，您将一个文件发送给它，该文件就成为 stdin。在这种情况下，我们将 `peanuts.txt` 重定向为我们的 stdin。然后 `cat peanuts.txt` 的输出（即“Hello World”）被重定向到另一个名为 `banana.txt` 的文件。

## Exercise

尝试几个命令：

```bash
echo < peanuts.txt > banana.txt
ls < peanuts.txt > banana.txt
pwd < peanuts.txt > banana.txt
```

## Quiz Question

您使用哪个重定向符来重定向 stdin？

## Quiz Answer

<
