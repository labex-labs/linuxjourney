---
lesson_id: "stderr-standard-error-redirect"
course_id: "text-fu"
lang: "zh"
order_index: 3
title: "stderr (标准错误)"
description: "学习在 Bash 中单独重定向标准错误，或将其与标准输出合并。"
meta_title: "stderr (标准错误) - Text-Fu"
meta_description: "了解如何在 Linux 中管理标准错误。本指南涵盖 stderr 重定向、stderr 文件描述符 (2) 以及如何使用 2>、2>&1 和 &> 将 stderr 重定向到文件或 /dev/null。"
meta_keywords: "stderr, 标准错误 linux, stderr 文件描述符，stderr 文件，linux 标准错误，重定向 stderr, 2>, 2>&1, &>, /dev/null, bash 错误处理"
---

程序通常把正常结果写入标准输出，把诊断信息写入另一条名为标准错误（**stderr**）的数据流。保持两条流分离，就能保存有用数据，而不会混入错误消息。

## 分离正常输出与错误

```bash
$ ls /fake/directory > peanuts.txt
ls: cannot access '/fake/directory': No such file or directory
```

`>` 只重定向 stdout。诊断信息写到仍连接终端的 stderr。同时，shell 会为 stdout 创建或清空 `peanuts.txt`，即使 `ls` 没有产生正常结果。

标准流按约定使用以下文件描述符：

- `0`: stdin (标准输入)
- `1`: stdout (标准输出)
- `2`：stderr（标准错误）

:::single-choice{#stderr-not-in-stdout-file}
为什么 `ls /missing > results.txt` 的错误通常仍显示在终端？

::option[`>` 重定向 stdout，而诊断信息写入 stderr。]{#stderr-separate-stream .correct explanation="普通 `>` 只改变文件描述符 1，文件描述符 2 仍保持原来的终端目标。"}
::option[`ls` 会等待文件关闭后才打印错误。]{#stderr-waits-for-close explanation="问题与时机无关；正常消息和诊断消息使用不同输出流。"}
::option[`results.txt` 只能保存正常文字，无法保存诊断信息。]{#stderr-file-capability explanation="普通文件可以保存任意一条流；这条命令行只是没有把 stderr 重定向到文件。"}
:::

## 使用 2> 重定向 stderr

要将 `stderr` 重定向到文件，你需要使用文件描述符 `2` 后面跟上 `>` 运算符。此命令会将任何错误消息发送到指定的 `stderr 文件`。

```bash
$ ls /fake/directory 2> errors.txt
```

shell 会创建或清空 `errors.txt`，并把它连接到描述符 2。stdout 保持原目标。需要追加错误输出时，请改用 `2>> errors.txt`。

:::single-choice{#stderr-to-error-file}
哪个命令会用 `find /restricted` 的诊断信息替换 `errors.log`，同时让 stdout 保持原目标？

::option[`find /restricted > errors.log`]{#stdout-errors-log explanation="普通 `>` 重定向描述符 1，因此捕获的是正常结果，而不是专门重定向诊断信息。"}
::option[`find /restricted < errors.log`]{#stdin-errors-log explanation="小于号会把文件作为 stdin 提供，并不会捕获任何输出流。"}
::option[`find /restricted 2> errors.log`]{#stderr-errors-log .correct explanation="开头的 `2` 选择 stderr，`>` 为这条流创建或清空目标。"}
:::

## 合并 stdout 与 stderr

如果想将正常输出和错误消息都捕获到同一个文件中，该怎么办？你可以通过重定向两个流来实现这一点。

```bash
$ ls /fake/directory /etc/passwd > combined.txt 2>&1
```

我们来分解一下：

1. `> combined.txt` 把 stdout 连接到文件。
2. `2>&1` 把 stderr 连接到 stdout 此刻所指向的位置。

重定向从左到右处理，因此颠倒顺序会改变结果：

```bash
$ ls /fake/directory /etc/passwd 2>&1 > regular.txt
```

这里 stderr 先复制 stdout 原来的终端目标，随后只有 stdout 移动到 `regular.txt`，两条流最终位于不同位置。

:::single-choice{#stderr-combine-order}
哪个 Bash 重定向会把 `command` 的 stdout 和 stderr 都发送到 `all.log`？

::option[`command 2>&1 > all.log`]{#stderr-before-stdout explanation="它先把 stderr 连接到 stdout 的旧目标，再只把 stdout 重定向到文件；两条流最终会分开。"}
::option[`command 2> all.log > /dev/null`]{#stderr-file-stdout-null explanation="它把 stderr 发往 `all.log`，却丢弃 stdout，并没有把两条流合并到文件。"}
::option[`command > all.log 2>&1`]{#stdout-then-stderr .correct explanation="stdout 先进入文件，stderr 随后复制 stdout 此刻的目标。"}
:::

Bash 还提供 `&>` 作为用两条流替换文件的简写：

```bash
$ ls /fake/directory /etc/passwd &> combined.txt
```

在 Bash 中使用 `&>>` 可以追加两条流。显式的 `> file 2>&1` 形式也很重要，因为 shell 脚本和文档中经常使用它。

:::single-choice{#stderr-bash-short-form}
哪个 Bash 命令会把 `build` 的 stdout 和 stderr 都追加到 `build.log`？

::option[`build &> build.log`]{#replace-both-build explanation="Bash 的 `&>` 会重定向两条流，但会替换现有文件，而不是追加。"}
::option[`build 2>> build.log`]{#append-errors-build explanation="它只追加 stderr，stdout 仍保留原目标。"}
::option[`build &>> build.log`]{#append-both-build .correct explanation="在 Bash 中，`&>>` 会把文件描述符 1 和 2 一起追加到同一目标。"}
:::

## 有意识地丢弃数据流

有时，你可能希望运行一个命令并完全忽略任何潜在的错误消息。要做到这一点，你可以将 `stderr` 重定向到一个名为 `/dev/null` 的特殊文件，该文件会丢弃写入其中的任何数据。

```bash
$ ls /fake/directory 2> /dev/null
```

这不会让命令成功，也不会改变退出状态，只会隐藏诊断流。排障期间应保留或显示 stderr，而不是丢弃所需信息。

:::single-choice{#stderr-dev-null-effect}
`check-data 2> /dev/null` 改变了什么？

::option[它会丢弃 stdout，并把所有错误转为成功。]{#discard-stdout-success explanation="描述符 2 是 stderr 而非 stdout，重定向也不会改写程序的退出状态。"}
::option[它会丢弃 stderr，但不会强制返回成功状态。]{#discard-stderr-only .correct explanation="重定向改变的是诊断信息的去向；程序仍自行决定成功或失败状态。"}
::option[它会把 stderr 保存到名为 `/dev/null` 的隐藏文件。]{#save-dev-null explanation="`/dev/null` 会丢弃写入的数据，并不是供日后恢复的存储文件。"}
:::

要练习管理三条标准流，可以尝试这个动手实验：

1. **[在 Linux 中重定向输入和输出](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 在此实验中，你将学习如何在 Linux shell 中重定向输入和输出。你将通过操纵标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin) 以及使用 `>`、`>>`、`2>` 和 `tee` 命令等运算符来练习控制命令的数据流。

## 总结

现在，你可以让诊断信息保持独立，也可以把它与正常命令输出合并。

1. 知道 stderr 是文件描述符 2。
2. 使用 `2>` 或 `2>>` 替换或追加错误日志。
3. 从左到右应用多个重定向。
4. 使用明确的语法合并两条输出流。
5. 只在可以接受信息丢失时丢弃诊断。
