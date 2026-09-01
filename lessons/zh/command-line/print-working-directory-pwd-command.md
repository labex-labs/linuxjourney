---
lesson_id: "print-working-directory-pwd-command"
course_id: "command-line"
lang: "zh"
order_index: 2
title: "pwd（显示当前工作目录）"
description: "学习使用 pwd 确认自己在 Linux 文件系统中的当前位置。"
meta_title: "pwd（显示当前工作目录）- 命令行"
meta_description: "学习 Linux 中的 pwd 命令，了解显示当前工作目录的含义，以及绝对路径如何显示你在文件系统中的当前位置。"
meta_keywords: "pwd 命令, linux pwd, 显示当前工作目录, 当前目录 linux, 绝对路径, linux 文件系统, 目录树"
---

在 Linux 中，文件和目录以层级结构组织，称为文件系统。在你能够自如地移动之前，你需要知道自己所在的位置。`pwd` 命令通过打印你当前的工作目录来回答这个问题。

## Linux 中的目录树

整个文件系统从一个顶层目录开始，称为根目录，用斜杠（`/`）表示。从根目录开始，目录树分支出子目录，子目录中可以包含文件和更多子目录。

下面是该结构的简化示例：

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

:::single-choice{#identify-root-subdirectories} 在上面的目录树中，`home` 和 `etc` 与 `/` 是什么关系？

::option[它们是从 `/` 分支出来的子目录。]{#root-subdirectories .correct explanation="这两个目录都直接出现在 `/` 下方；文件系统从根目录向下分支形成子目录。"}
::option[它们是存放在 `bin` 目录中的文件。]{#files-inside-bin explanation="目录树把 `home` 和 `etc` 放在与 `bin` 同一层，而不是其内部；在本例中它们是目录而非文件。"}
::option[它们是根目录的其他名称。]{#alternate-root-names explanation="Linux 只有一个以 `/` 表示的文件系统根；`home` 和 `etc` 是它下面的目录。"}
:::

## 理解文件路径

任何文件或目录的位置都由其路径描述。路径是一系列目录，从起点到特定目标的顺序。

例如，如果你在 `/home` 目录下有一个名为 `pete` 的文件夹，`pete` 文件夹内有一个 `Movies` 文件夹，则完整路径是：

```plaintext
/home/pete/Movies
```

以 `/` 开头的路径是绝对路径，因为它从根目录开始。像 `Movies` 这样的路径是相对路径，因为它依赖于你当前的位置。

:::single-choice{#recognize-absolute-path} 为什么 `/home/pete/Movies` 是绝对路径？

::option[它包含多个以 `/` 分隔的目录名。]{#contains-directories explanation="绝对路径和相对路径都可以包含多个目录名；决定路径类型的是起点，而不是名称数量。"}
::option[它以名为 `Movies` 的目录结尾。]{#ends-with-movies explanation="目标名称并不决定路径是否绝对；绝对路径由其根目录起点来识别。"}
::option[它以 `/` 开头，从根目录出发。]{#starts-at-root .correct explanation="绝对路径从根目录开始，开头的 `/` 就表明了这一点。"}
:::

## PWD 在 Linux 中的全称是什么？

`pwd` 的完整形式是“print working directory”（打印当前工作目录）。你的工作目录是你的 shell 当前所在的目录。使用相对路径的命令都是从这个位置开始的。

:::single-choice{#expand-pwd-name} `pwd` 代表什么？

::option[Print working directory]{#print-working-directory .correct explanation="这个名称准确描述了命令的作用：打印 shell 的当前工作目录。"}
::option[Present working directory]{#present-working-directory explanation="日常表达中可以把当前位置称为 present directory，但这不是 `pwd` 的完整名称。"}
::option[Print whole directory]{#print-whole-directory explanation="`pwd` 报告当前目录的路径，并不会打印目录中的全部内容。"}
:::

## 使用 pwd 命令

要查找你当前的目录，输入 `pwd` 并按回车。

```bash
$ pwd
/home/pete
```

输出是一个绝对路径。在此示例中，shell 当前位于 `pete` 用户的主目录。

具体输出可能因用户名、主目录和当前位置不同而有所差异。`pwd` 只打印信息，不会改变工作目录；相比之下，`cd` 会改变 shell 所在的目录。

:::single-choice{#check-location-without-changing-it} 哪项操作可以在不改变当前位置的情况下检查当前目录？

::option[运行 `cd`，再查看它切换到的目录。]{#run-cd explanation="`cd` 会改变工作目录，因此不满足在不改变位置的情况下进行检查这一要求。"}
::option[输入 `/home/pete`，把这个路径当成命令。]{#run-path explanation="绝对路径可以标识位置，但路径本身并不是报告当前目录的命令。"}
::option[运行 `pwd`，读取它打印的绝对路径。]{#run-pwd .correct explanation="`pwd` 会报告 shell 的当前位置而不移动它，因此需要确认自己所在位置时可以放心使用。"}
:::

## pwd 的用途

使用 `pwd` 的场景包括：

- 你正在按照指示操作，需要确认你的位置。
- 命令失败了，因为文件路径错误。
- 你穿越了多个目录，忘记了自己所在的位置。
- 你想将当前目录路径复制到另一个命令中。

例如：

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

这告诉你 `app.py` 和 `README.md` 位于 `/home/pete/projects` 目录下。

熟能生巧！这里有一些动手实验，帮助你巩固对 Linux 文件系统导航和定位当前所在位置的理解：

1. **[Linux pwd 命令：显示目录](https://labex.io/zh/labs/linux-linux-pwd-command-directory-displaying-209734)** - 本实验提供了对 `pwd` 命令的重点介绍和实际使用，直接对应本课关于查找当前目录的内容。
2. **[Linux 目录导航](https://labex.io/zh/labs/linux-directory-navigation-387844)** - 通过导航不同目录，测试你的基本 Linux 命令行技能，巩固对路径和文件系统结构的理解。
3. **[Linux cd 命令：切换目录](https://labex.io/zh/labs/linux-linux-cd-command-directory-changing-209733)** - 学习如何使用 `cd` 命令高效地导航文件系统，理解切换目录的不同技巧并探索文件结构。

## 总结

现在，你可以使用 `pwd` 确认自己在 Linux 文件系统中的当前位置。

1. 识别目录树的根。
2. 区分绝对路径和相对路径。
3. 说明 `pwd` 的含义及其报告的信息。
4. 在不改变位置的情况下检查工作目录。
