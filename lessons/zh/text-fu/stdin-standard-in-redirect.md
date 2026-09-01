---
lesson_id: "stdin-standard-in-redirect"
course_id: "text-fu"
lang: "zh"
order_index: 2
title: "标准输入 (stdin)"
description: "了解程序如何读取标准输入，以及 Bash 如何把这条流连接到文件。"
meta_title: "标准输入 (stdin) - Text-Fu"
meta_description: "通过学习如何重定向标准输入 (stdin)，掌握 Linux 命令行操作。本指南涵盖 stdin 与 stdout 的关系、使用 '<' 运算符，以及如 'cat stdin' 等实用示例，以有效管理数据流。"
meta_keywords: "stdin, 标准输入，重定向 stdin, cat stdin, stdin 和 stdout, Linux 重定向，命令行，输入流"
---

标准输入简称 **stdin**，是程序通常读取传入数据的数据流。在交互式终端中，shell 一般会把 stdin 连接到终端输入，因此程序可以读取你键入的内容。

## 标准输入与文件描述符 0

按约定，三条标准流使用以下文件描述符编号：

- `0`：标准输入（`stdin`）
- `1`：标准输出（`stdout`）
- `2`：标准错误（`stderr`）

程序可以自行决定是否以及如何使用这些流。当没有提供文件操作数或其他输入源时，设计为读取 stdin 的命令通常会等待终端输入。

:::single-choice{#stdin-descriptor-number} 按约定，哪个文件描述符表示标准输入？

::option[`0`]{#stdin-fd-zero .correct explanation="标准输入按约定使用文件描述符 0。"}
::option[`1`]{#stdin-fd-one explanation="文件描述符 1 按约定表示标准输出，即承载正常结果的数据流。"}
::option[`2`]{#stdin-fd-two explanation="文件描述符 2 按约定表示标准错误，而不是标准输入。"}
:::

## 把文件重定向到 stdin

`<` 运算符让 Bash 打开文件进行读取，并把它连接到命令的 stdin：

```bash
$ cat < peanuts.txt
Hello World
```

shell 负责处理 `< peanuts.txt`；`cat` 只会读取文件描述符 0。该路径不会作为普通文件操作数传给 `cat`。

如果输入文件不存在或无法打开，shell 会报告重定向错误，也不会以这份输入启动命令。

:::single-choice{#stdin-from-file} 哪个命令会让 `sort` 从 `names.txt` 读取标准输入？

::option[`sort < names.txt`]{#sort-stdin-file .correct explanation="Bash 会打开 `names.txt` 进行读取，并在文件描述符 0 上把它连接到 `sort`。"}
::option[`sort > names.txt`]{#stdout-to-names explanation="大于号会把 stdout 重定向到文件，并可能清空文件；它不会把文件作为输入。"}
::option[`sort names.txt >`]{#incomplete-sort-output explanation="这里包含不完整的输出重定向，并没有表达所需的 stdin 连接。"}
:::

## 文件操作数与输入重定向

有些命令既能接受文件名操作数，也能读取 stdin，但结果可能略有不同。例如：

```bash
$ wc -l peanuts.txt
1 peanuts.txt
$ wc -l < peanuts.txt
1
```

两种形式都统计相同数据中的行数。第一种形式中，`wc` 收到文件名参数，所以知道文件名；第二种形式中，它只从 stdin 收到数据流，没有可打印的文件名。

:::single-choice{#stdin-not-command-argument} 为什么 `wc -l < peanuts.txt` 的输出通常不包含 `peanuts.txt`？

::option[`wc` 会在统计完成后删除文件名。]{#stdin-delete-name explanation="命令不会重命名或删除源文件，变化的只是输入连接方式。"}
::option[`<` 运算符会隐藏命令打印的所有单词。]{#stdin-hide-words explanation="输入重定向不会过滤 stdout；没有文件名是因为 `wc` 从未收到它作为参数。"}
::option[Bash 把文件作为 stdin 提供，而不是文件名参数。]{#stdin-no-filename .correct explanation="shell 会消化重定向，并把文件连接到描述符 0，因此不会把路径作为操作数交给 `wc`。"}
:::

## 组合输入和输出重定向

一条命令行可以重定向多条流：

```bash
$ cat < peanuts.txt > banana.txt
```

shell 会建立两条互相独立的连接：

1. `< peanuts.txt` 打开 `peanuts.txt` 作为 `cat` 的 stdin。
2. `> banana.txt` 创建或清空 `banana.txt`，并把它连接到 `cat` 的 stdout。

`cat` 从 stdin 读取字节并写入 stdout，因此 `banana.txt` 会收到源内容。普通文件复制用 `cp peanuts.txt banana.txt` 能更直接地表达意图；本例用于说明数据流连接。

:::single-choice{#stdin-and-stdout-files} 在 `cat < input.txt > output.txt` 中，哪个文件提供 stdin，哪个文件接收 stdout？

::option[`output.txt` 提供 stdin，`input.txt` 接收 stdout。]{#stdin-output-stdout-input explanation="这颠倒了重定向运算符的含义；输入箭头指向命令，输出箭头指向文件。"}
::option[`input.txt` 提供 stdin，`output.txt` 接收 stdout。]{#stdin-input-stdout-output .correct explanation="`<` 会为描述符 0 打开 `input.txt`，`>` 会为描述符 1 打开 `output.txt`。"}
::option[两个文件都提供 stdin，stdout 仍留在终端。]{#both-stdin explanation="两个运算符影响不同的标准流；`>` 会把 stdout 从终端重定向出去。"}
:::

要练习输入和输出重定向，可以尝试以下动手实验：

1. **[Linux 中的输入和输出重定向](https://labex.io/zh/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 通过使用 `>`、`>>`、`2>` 等运算符以及 `tee` 命令来操作标准输出 (stdout)、标准错误 (stderr) 和标准输入 (stdin)，练习控制命令的数据流。
2. **[数据流重定向](https://labex.io/zh/labs/linux-data-stream-redirection-17995)** - 学习 Linux 流重定向的艺术。操作标准输入、输出和错误流，组合输出，并利用 `/dev/null` 进行高级文件操作。

## 总结

现在，你可以通过 shell 把命令的标准输入连接到文件。

1. 知道 stdin 是文件描述符 0。
2. 使用 `<` 重定向可读文件。
3. 区分文件名操作数与重定向输入。
4. 有意识地组合 stdin 和 stdout 重定向。
