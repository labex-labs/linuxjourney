---
lang: "zh"
title: "cut"
description: "学习如何使用 Linux `cut` 命令从文件中提取文本。这个初学者友好的教程涵盖了字符和字段剪切。提高您的 Linux 文本处理技能！"
keywords: "cut 命令，Linux 文本处理，提取文本，Linux 教程，Linux 初学者，cut 示例，Linux 指南"
---

## Lesson Content

我们将学习几个可以用来处理文本的有用命令。在开始之前，让我们创建一个将要使用的文件。复制并粘贴以下命令；完成后，在“lazy”和“dog”之间添加一个 TAB 键（按住 Ctrl-v + TAB）。

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

我们将学习的第一个命令是 `cut` 命令。它从文件中提取文本的某些部分。

按字符列表提取内容：

```bash
cut -c 5 sample.txt
```

这将输出文件中每一行的第 5 个字符。在这种情况下，它是“q”；请注意，空格也算作一个字符。

要按字段提取内容，我们需要做一些修改：

```bash
cut -f 2 sample.txt
```

`-f` 或字段标志根据字段剪切文本。默认情况下，它使用 TAB 作为分隔符，因此由 TAB 分隔的所有内容都被视为一个字段。您应该会看到“dog”作为输出。

您可以将字段标志与分隔符标志结合使用，以通过自定义分隔符提取内容：

```bash
cut -f 1 -d ";" sample.txt
```

这将把 TAB 分隔符更改为“;”分隔符，并且由于我们正在剪切第一个字段，结果应该是“The quick brown”。

## Exercise

以下命令的作用是什么？为什么？

```bash
cut -c 5-10 sample.txt
cut -c 5- sample.txt
cut -c -5 sample.txt
```

## Quiz Question

您将使用什么命令来获取文件中每一行的第一个字符？

## Quiz Answer

cut -c 1
