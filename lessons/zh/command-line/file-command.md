---
lesson_id: "file-command"
course_id: "command-line"
lang: "zh"
order_index: 6
title: "file 命令"
description: "学习在不依赖文件名或扩展名的情况下识别文件可能包含的内容类型。"
meta_title: "file 命令 - 命令行"
meta_description: "通过示例学习 Linux 中的 file 命令，用于识别文本文件、图片、脚本、压缩档案、二进制文件和 MIME 类型。"
meta_keywords: "linux file 命令, file 命令, 识别文件类型 linux, mime 类型 linux, 文本文件, 二进制文件, 压缩文件"
---

在上一课中，你使用 `touch` 创建了一个没有扩展名的文件。Linux 文件名不必说明文件中有什么：名为 `funny.gif` 的文件未必真是 GIF 图片。

要了解一个文件的类型，可以使用 `file` 命令。它会显示文件内容的描述。

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

## 为什么文件扩展名不够用

Linux 工具通常不要求用扩展名判断文件类型。一个 shell 脚本可以命名为 `backup`，文本文件可以叫 `README`，图片也可能带有误导性的扩展名。`file` 会检查文件系统元数据和内容中可识别的模式等属性。

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

它给出的是分类结果，而非绝对保证。少见、不完整或已损坏的文件可能只得到 `data` 这样的宽泛描述。

:::single-choice{#identify-misleading-extension} 名为 `report.jpg` 的文件未必包含图片。哪个命令可以检查它可能的内容类型？

::option[`ls report.jpg`]{#list-report explanation="`ls` 可以确认名称存在并显示元数据，但不会对文件内容进行分类。"}
::option[`file report.jpg`]{#inspect-report .correct explanation="`file` 会检查文件并报告其可能的类型，而不是只依赖 `.jpg` 后缀。"}
::option[`touch report.jpg`]{#touch-report explanation="`touch` 会更新时间戳或创建缺失文件，并不识别内容类型。"}
:::

## 检查多个文件

你可以一次检查多个文件：

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

也可以传入 shell 通配符。shell 会先把 `*` 展开为匹配的名称，再由 `file` 逐个检查：

```bash
$ file *
```

:::single-choice{#inspect-multiple-files} 哪个命令会让 `file` 检查当前目录中 `*` 匹配到的每个非隐藏名称？

::option[`file *`]{#file-wildcard .correct explanation="shell 会把 `*` 展开为匹配的非隐藏名称，`file` 再检查得到的每个操作数。"}
::option[`file .`]{#file-current-directory explanation="单个点号表示当前目录本身；这个命令只会对该目录分类，而不是检查其中每个条目。"}
::option[`file -b`]{#file-brief-no-operand explanation="`-b` 会改变输出格式，但这个命令没有提供要检查的文件。"}
:::

## 显示 MIME 信息

`-i` 选项会打印 MIME 风格的信息，包括媒体类型，并在可用时给出字符集。当其他程序需要 `text/html` 之类的值时，这种形式很有用。

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

:::single-choice{#show-mime-information} 哪个命令会报告 `index.html` 的 MIME 风格信息？

::option[`file -b index.html`]{#brief-index explanation="`-b` 会在普通描述中省略文件名，并不专门请求 MIME 风格输出。"}
::option[`file -i index.html`]{#mime-index .correct explanation="`-i` 会请求 MIME 风格输出，例如 `text/html` 以及字符集信息。"}
::option[`file -L index.html`]{#follow-index explanation="`-L` 控制符号链接处理方式，并不选择 MIME 输出格式。"}
:::

## 实用的 file 选项

- `-i`：显示 MIME 类型信息。
- `-b`：简洁模式，输出时省略文件名。
- `-L`：跟随符号链接。
- `-z`：尝试检查压缩文件。

例如：

```bash
$ file -b notes.txt
ASCII text
```

:::single-choice{#omit-filename-from-output} 哪个命令会对 `notes.txt` 分类，但在输出中省略文件名？

::option[`file -i notes.txt`]{#mime-notes explanation="`-i` 会请求 MIME 风格信息，输出通常仍包含文件名。"}
::option[`file -z notes.txt`]{#compressed-notes explanation="`-z` 会尽可能检查压缩数据内部，并不会启用简洁输出。"}
::option[`file -b notes.txt`]{#brief-notes .correct explanation="使用 `-b` 选择简洁模式后，只打印分类结果，不添加文件名前缀。"}
:::

## 总结

现在，你可以使用 `file` 调查文件可能包含的内容。

1. 不依赖扩展名对文件分类。
2. 用一个命令检查多个路径名。
3. 请求 MIME 风格信息。
4. 调整链接、压缩数据和输出标签的处理方式。
