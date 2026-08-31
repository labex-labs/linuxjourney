---
lesson_id: "tr-translate-command"
course_id: "text-fu"
lang: "zh"
order_index: 13
title: "tr（转换）"
description: "学习如何转换、删除和压缩标准输入流中的字符集合。"
meta_title: "tr（翻译） - Text-Fu"
meta_description: "通过示例学习 Linux tr 命令，用于字符翻译、删除字符、压缩重复字符、使用字符类和清理文本。"
meta_keywords: "linux tr 命令, tr 命令, tr -d, tr -s, 字符翻译, 删除字符, 字符类, 文本处理 linux"
---

`tr` 是 translate 的缩写，它会转换、删除或压缩从 stdin 读取的字符。它不接受普通的输入文件操作数，因此应通过管道或输入重定向提供数据。

基本语法为：

```bash
tr [OPTIONS] SET1 [SET2]
```

`tr` 处理的是字符集合，而不是单词或通用正则表达式。如果转换取决于完整单词、行结构或周围上下文，请使用其他工具。

## 转换字符

提供两个集合时，`SET1` 中的字符会按位置映射到 `SET2` 中的字符：

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

这里，小写范围中的位置会映射到对应的大写位置。请为集合表达式加引号，确保 shell 原样传递它们。

也可以把一个字符转换为另一个字符：

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

不在 `SET1` 中的字符会原样通过。

:::single-choice{#tr-map-characters}
`printf '%s\n' 'abc123' | tr 'abc' 'ABC'` 会输出什么？

::option[`ABCABC`]{#tr-uppercase-digits explanation="数字不属于源集合，因此 `tr` 不会用字母替换它们。"}
::option[`ABC123`]{#tr-uppercase-abc .correct explanation="`a`、`b` 和 `c` 分别映射到 `ABC` 中相同位置的字符，数字保持不变。"}
::option[`abc123ABC`]{#tr-append-set explanation="`tr` 转换匹配的输入字符，不会把目标集合追加到流末尾。"}
:::

## 删除字符

使用 `-d` 和一个集合，可以删除每个匹配的字符：

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

每个数字都会单独删除；`tr` 并不是在识别完整的数字词元。

字符类可以描述由当前 locale 定义的字符组：

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

删除换行符会直接连接各输入行，不会插入替代分隔符：

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

:::single-choice{#tr-delete-digits}
哪个命令会从 stdin 中删除每个数字，同时让其他字符保持不变？

::option[`tr -d '[:digit:]'`]{#tr-delete-digit-class .correct explanation="`-d` 选项会从输入流中删除数字字符类里的所有字符。"}
::option[`tr -s '[:digit:]'`]{#tr-squeeze-digits explanation="`-s` 会压缩重复数字，但每一连续组仍会保留一个字符。"}
::option[`tr '[:digit:]'`]{#tr-one-set-no-delete explanation="转换通常需要第二个集合；单独提供一个集合并不表示删除。"}
:::

## 压缩重复字符

使用 `-s SET` 可把所列字符的每一连续重复组替换为该字符的一个实例：

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

该集合只包含一个普通空格，所以这个命令不会压缩制表符或换行符。

也可以压缩重复的换行符：

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

:::single-choice{#tr-squeeze-spaces}
哪个命令会把 stdin 中每一连续的普通空格压缩为一个空格？

::option[`tr -s ' '`]{#tr-squeeze-space .correct explanation="`-s` 选项压缩所给集合中的重复字符，这里的集合只包含一个普通空格。"}
::option[`tr -d ' '`]{#tr-delete-space explanation="`-d` 会删除所有普通空格，而不是每一连续组保留一个。"}
::option[`tr ' ' ''`]{#tr-empty-destination explanation="空的转换集合不是请求压缩的清晰可移植方式；处理重复字符应使用 `-s`。"}
:::

## 使用字符类和补集

在许多 locale 中，字符类比手写范围更能清楚表达意图。常见字符类包括：

- `[:lower:]`：小写字母。
- `[:upper:]`：大写字母。
- `[:digit:]`：数字。
- `[:alpha:]`：字母。
- `[:alnum:]`：字母和数字。
- `[:space:]`：空白字符。
- `[:punct:]`：标点字符。

例如，使用字符类把小写文本转换为大写：

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

`-c` 选项会对 `SET1` 取补集，也就是集合之外的所有字符。将它与 `-d` 结合，可以只保留选定种类的字符：

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

这也会删除换行符，因为换行符不是字母或数字。如果记录边界很重要，请有意添加或保留分隔符。

:::single-choice{#tr-keep-alphanumeric}
`tr -cd '[:alnum:]'` 会对 stdin 做什么？

::option[删除字母和数字，保留其他所有字符。]{#tr-delete-alnum explanation="补集会改变 `-d` 的目标；字母数字集合本身会被保留。"}
::option[删除所有非字母数字字符。]{#tr-delete-nonalnum .correct explanation="`-c` 对字母数字集合取补集，`-d` 再删除得到的非字母数字集合。"}
::option[把所有字母和数字转换为大写。]{#tr-uppercase-alnum explanation="命令没有目标转换集合，因此不会执行大小写转换。"}
:::

## 构建流转换

如果把不同转换作为独立阶段更清楚，可以连接多个 `tr` 进程：

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

对于简单的制表符分隔输入，可以把制表符转换为逗号：

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

由于 `tr` 读取 stdin，可以使用 `<` 提供文件内容：

```bash
$ tr '[:lower:]' '[:upper:]' < names.txt
```

需要保存结果时，请把 stdout 重定向到另一个文件。不要重定向回输入路径，因为 shell 会在 `tr` 读取之前将其截断。

:::single-choice{#tr-read-file-input}
哪个命令会让 `tr` 从 stdin 读取 `names.txt`，并把小写字符转换为大写？

::option[`tr names.txt '[:lower:]' '[:upper:]'`]{#tr-file-operand explanation="`tr` 不以这种方式接受普通输入文件名；多出的操作数会使语法无效。"}
::option[`tr -d '[:lower:]' < names.txt`]{#tr-delete-lowercase explanation="这会正确读取文件，但会删除小写字母而不是转换它们。"}
::option[`tr '[:lower:]' '[:upper:]' < names.txt`]{#tr-input-redirection .correct explanation="shell 会把 `names.txt` 打开为 stdin，`tr` 再把小写字符类映射到大写字符类。"}
:::

要练习字符级的流转换，可以尝试以下动手实验：

1. **[Linux tr 命令：字符转换](https://labex.io/zh/labs/linux-linux-tr-command-character-translating-219198)** - 学习使用 Linux `tr` 命令对文本流进行字符级转换。你将练习转换字符、删除特定字符、使用字符类和压缩重复字符。

## 总结

现在，你可以使用专门的 `tr` 操作转换字符流。

1. 在对应的集合之间映射字符。
2. 使用 `-d` 删除选定字符。
3. 使用 `-s` 压缩重复字符。
4. 有意识地使用 locale 相关字符类和补集。
5. 通过 stdin 而不是文件名操作数提供输入。
