---
index: 13
lang: "zh"
title: "tr (转换)"
meta_title: "tr (转换) - Text-Fu"
meta_description: "掌握 Linux tr 命令进行字符转换和删除。本指南涵盖如何使用 tr 进行字符转换、使用 linux tr -d 等选项删除字符，并提供实用的文本处理示例。"
meta_keywords: "tr, tr 命令，字符转换，linux tr -d, tr -d linux, 转换字符，删除字符，文本处理，Linux 命令"
---

## Lesson Content

`tr` 命令，是 translate（翻译）的缩写，是一个 Linux 命令行实用程序，用于从标准输入翻译或删除字符。它是简单文本处理的有用工具，通常与管道一起使用来处理其他命令的输出。`trtranslate` 功能是文本处理的核心部分。

### 基本字符翻译

`tr` 最常见的用法是将一组字符替换为另一组字符。例如，您可以轻松地将所有小写字符翻译成大写。

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

在这个例子中，我们将 `echo` 的输出通过管道传递给 `tr` 命令。然后 `tr` 命令将字符范围 `a-z` 翻译成范围 `A-Z` 中对应的字符。

### 使用 -d 删除字符

另一个强大的功能是使用 `-d`（delete，删除）选项删除特定字符的能力。这在清理文本时特别有用。例如，如果您想从字符串中删除所有数字，您可以使用 `linux tr -d`。

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

在这里，`tr -d` 命令从输入流中删除了指定集合（'0' 到 '9'）中的所有字符。这是 `tr -d linux` 用户常见的用法。

### 挤压重复字符

`tr` 命令还可以使用 `-s`（squeeze，挤压）选项将重复的字符“挤压”成单个实例。这非常适合用单个空格规范化包含多余空格的文本。

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

在这种情况下，`tr -s ' '` 将多个空格序列替换为单个空格，使输出更加整洁。

## Exercise

为了将您的知识付诸实践，请尝试以下动手实验。它将帮助您巩固对字符翻译和文本处理的理解。

1.  **[Linux tr 命令：字符翻译](https://labex.io/zh/labs/linux-linux-tr-command-character-translating-219198)** - 学习 Linux `tr` 命令，用于文本流中的字符级转换。您将练习翻译字符、删除特定字符、使用字符类以及挤压重复字符。

此实验将帮助您在实际场景中应用文本操作概念，并增强对 `tr` 命令的信心。

## Quiz Question

什么命令用于翻译字符？（请仅用小写英文字母回答）

## Quiz Answer

tr
