---
index: 13
lang: "zh"
title: "tr（翻译）"
meta_title: "tr（翻译） - Text-Fu"
meta_description: "通过示例学习 Linux tr 命令，用于字符翻译、删除字符、压缩重复字符、使用字符类和清理文本。"
meta_keywords: "linux tr 命令, tr 命令, tr -d, tr -s, 字符翻译, 删除字符, 字符类, 文本处理 linux"
---

## Lesson Content

`tr` 命令，全称为 translate，是一个命令行工具，用于从标准输入中翻译、删除或压缩字符。它适用于简单的文本操作，常与管道结合使用以处理其他命令的输出。

基本语法是：

```bash
tr [OPTIONS] SET1 [SET2]
```

与 `sed` 或 `awk` 等工具不同，`tr` 是逐字符处理的。它不理解单词、列或正则表达式的方式不同。这使得它在大小写转换、删除数字和规范化重复空格等任务中快速且简单。

### 基本字符翻译

`tr` 最常见的用途是将一组字符替换为另一组字符。例如，你可以轻松地将所有小写字符转换为大写。

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

在这个例子中，我们将 `echo` 的输出通过管道传递给 `tr` 命令。`tr` 命令将字符范围 `a-z` 翻译为对应的 `A-Z` 范围内的字符。

你也可以将一个字符翻译为另一个字符：

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

`SET1` 中的每个字符映射到 `SET2` 中相同位置的字符。

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

这里，`a` 变成 `A`，`b` 变成 `B`，`c` 变成 `C`。

### 使用 -d 删除字符

另一个强大的功能是使用 `-d` 选项删除特定字符。这对于清理文本特别有用。例如，如果你想从字符串中删除所有数字，可以使用：

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

这里，`tr -d` 删除了指定集合中所有字符，从 `0` 到 `9`。

你也可以使用字符类删除字符串中的标点符号：

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

你还可以删除换行符以将多行合并为一行：

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

### 压缩重复字符

`tr` 命令还可以使用 `-s` 选项将重复的字符“压缩”为单个字符。这对于规范化多余的空白非常有用。

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

在这个例子中，`tr -s ' '` 将多个连续空格替换为单个空格，使输出更整洁。

你也可以压缩重复的换行符：

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

### 使用字符类

字符类使 `tr` 命令更易读且更具可移植性。常见的字符类包括：

- `[:lower:]`：小写字母。
- `[:upper:]`：大写字母。
- `[:digit:]`：数字。
- `[:alpha:]`：字母。
- `[:alnum:]`：字母和数字。
- `[:space:]`：空白字符。
- `[:punct:]`：标点符号。

例如，使用字符类将小写文本转换为大写：

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

使用 `-c` 和 `-d` 删除除字母和数字之外的所有字符。`-c` 选项表示补集，即“集合之外的所有字符”。

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

### 结合删除和压缩

你可以在清理文本时结合使用选项。这个例子先删除标点符号，然后压缩重复的空格：

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

对于制表符分隔的输入，你可以将制表符转换为逗号：

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

### 常用 tr 选项

以下是你最常用的选项：

- `-d`：删除 `SET1` 中的字符。
- `-s`：压缩 `SET1` 中重复的字符。
- `-c`：使用 `SET1` 的补集。
- `-t`：在翻译前将 `SET1` 截断为与 `SET2` 相同长度。

### 常见问题

**为什么 tr 从管道读取？** `tr` 从标准输入读取，因此通常用在 `echo`、`cat`、`printf` 或其他产生文本的命令之后。

**tr 会替换单词吗？** 不会。`tr` 是逐字符翻译，不处理单词。需要替换整个单词或模式时，请使用 `sed`。

**为什么我的 tr 命令是逐字符替换？** 这就是 `tr` 的工作方式。它将 `SET1` 中的每个字符映射到 `SET2` 中对应位置的字符。

**为什么要给字符集加引号，如 'a-z'？** 引号防止 shell 在 `tr` 接收之前解释特殊字符。

## Exercise

为了实践你的知识，尝试以下动手实验。它将帮助你巩固字符翻译和文本处理的理解。

1. **[Linux tr 命令：字符翻译](https://labex.io/zh/labs/linux-linux-tr-command-character-translating-219198)** - 学习 Linux `tr` 命令在文本流中进行字符级转换。你将练习字符翻译、删除特定字符、使用字符类和压缩重复字符。

这个实验将帮助你在实际场景中应用文本处理概念，增强对 `tr` 命令的信心。

## Quiz Question

用于翻译字符的命令是什么？（请仅用小写英文字母回答）

## Quiz Answer

tr
