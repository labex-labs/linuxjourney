---
lesson_id: "touch-command"
course_id: "command-line"
lang: "zh"
order_index: 5
title: "touch 命令"
description: "学习使用 touch 命令创建空文件并管理文件时间戳。"
meta_title: "touch 命令 - 命令行教程"
meta_description: "通过示例学习 Linux touch 命令，包括创建空文件、更新时间戳、设置日期、使用参考文件以及避免覆盖等用法。"
meta_keywords: "linux touch 命令, touch 命令, linux 创建文件, 更新时间戳 linux, touch -d, touch -r, touch -c"
---

`touch` 命令用于更改文件时间戳，也常用于创建一个或多个空文件。

基本语法是：

```bash
touch [OPTIONS] FILE...
```

## 创建空文件

创建空文件最简单的方法是使用 `touch` 后跟文件名。如果文件不存在，`touch` 会创建它。

```bash
$ touch mysuperduperfile
```

你也可以通过列出每个文件名，一次创建多个文件：

```bash
$ touch file1.txt file2.txt file3.log
```

这适合创建占位文件，但 `touch` 不会向文件中添加文本。需要非空文件时，请使用文本编辑器或其他能够写入内容的命令。

:::single-choice{#create-several-empty-files}
如果 `one`、`two` 和 `three` 尚不存在，哪个命令会创建这三个空文件？

::option[`touch "one two three"`]{#touch-one-spaced explanation="引号会让它成为一个含空格的文件名，因此这个命令只处理一个文件，而不是三个。"}
::option[`mkdir one two three`]{#mkdir-three explanation="`mkdir` 创建的是目录，而不是空的普通文件；这里应使用 `touch`。"}
::option[`touch one two three`]{#touch-three .correct explanation="`touch` 接受多个文件操作数，会分别创建每个缺失的文件而不添加内容。"}
:::

## 更新文件时间戳

文件会记录多种时间戳。默认情况下，对现有文件运行 `touch` 会把访问时间和修改时间都改为当前时间，同时保持文件内容不变。

你可以通过使用 `ls -l` 查看文件时间戳，运行 `touch` 后再查看来验证这一点。

```bash
$ ls -l mysuperduperfile
$ touch mysuperduperfile
$ ls -l mysuperduperfile
```

`ls -l` 输出通常显示修改时间，而不是访问时间。

:::single-choice{#touch-existing-file}
如果 `report.txt` 已经存在，运行 `touch report.txt` 会发生什么？

::option[它的时间戳会更新，但内容不会被替换。]{#timestamps-only .correct explanation="默认情况下，`touch` 会更新现有文件的访问时间和修改时间，而不会覆盖文件数据。"}
::option[它的内容会被删除，文件变为空。]{#contents-deleted explanation="创建空文件是目标文件缺失时的行为；对现有文件更新时间戳时会保留内容。"}
::option[命令会因文件名已被使用而失败。]{#existing-error explanation="`touch` 本来就能处理现有文件和缺失文件；名称已存在本身并不是错误。"}
:::

## 控制更改哪个时间戳

使用 `-a` 只更改访问时间，使用 `-m` 只更改修改时间：

```bash
$ touch -a notes.txt
$ touch -m notes.txt
```

:::single-choice{#change-modification-time-only}
哪个命令只更新 `notes.txt` 的修改时间？

::option[`touch -a notes.txt`]{#access-only explanation="`-a` 只更改访问时间，并不选择这里要求的修改时间。"}
::option[`touch -m notes.txt`]{#modification-only .correct explanation="`-m` 把更改限制为修改时间，访问时间保持不变。"}
::option[`touch -c notes.txt`]{#no-create explanation="`-c` 控制是否创建缺失文件，并不把更新限制为某一种时间戳。"}
:::

## 设置或复制时间

`-d` 选项接受日期字符串，而不是使用当前时间：

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

要让一个文件拥有与参考文件相同的访问和修改时间，请使用 `-r`：

```bash
$ touch -r file1.txt file2.txt
```

这里 `file1.txt` 提供时间戳，`file2.txt` 是被更改的文件。`-t` 选项也可用紧凑的数字格式指定时间。

:::single-choice{#copy-reference-timestamps}
哪个命令会把 `source.txt` 的时间戳复制给 `target.txt`？

::option[`touch -r source.txt target.txt`]{#reference-source .correct explanation="使用 `-r` 时，其后的操作数是参考文件，最后一个操作数是时间戳被更新的文件。"}
::option[`touch -r target.txt source.txt`]{#reference-target explanation="这颠倒了两个文件的角色，会以 `target.txt` 为参考去更新 `source.txt`。"}
::option[`touch -d source.txt target.txt`]{#date-source explanation="`-d` 需要日期字符串，而不是参考文件名；复制其他文件的时间戳应使用 `-r`。"}
:::

## 避免创建文件

通常，当指定路径不存在时，`touch` 会创建文件。如果只想更新已经存在的文件，请加上 `-c`：

```bash
$ touch -c existing-file.txt
```

如果 `existing-file.txt` 不存在，该命令不会创建它。这适合用于只应更新时间戳、而不应引入新文件的脚本。

:::single-choice{#update-without-creating}
哪个命令会在 `status.log` 存在时更新它，但缺失时不创建它？

::option[`touch -a status.log`]{#touch-access explanation="`-a` 选择访问时间，但仍可能创建缺失文件，不能满足不创建的要求。"}
::option[`touch -m status.log`]{#touch-modification explanation="`-m` 选择修改时间，但不会阻止创建缺失文件；应使用 `-c`。"}
::option[`touch -c status.log`]{#touch-no-create .correct explanation="`-c` 会禁止创建缺失文件，同时仍可更新现有文件的时间戳。"}
:::

## 总结

现在，你可以使用 `touch` 创建空文件并控制文件时间戳。

1. 创建一个或多个空文件。
2. 在不改变文件内容的情况下更新时间戳。
3. 选择访问时间或修改时间。
4. 设置特定时间或复制参考文件的时间戳。
5. 防止创建缺失文件。
