---
index: 2
lang: "zh"
title: "pwd (打印工作目录)"
meta_title: "pwd (打印工作目录) - 命令行"
meta_description: "掌握 Linux pwd 命令以显示您在 Linux 中的当前目录。本课程解释了 pwd 在 Linux 中的完整形式以及如何在 Linux 中导航目录树。"
meta_keywords: "linux pwd, linux 当前目录，linux 目录树，pwd 在 linux 中的完整形式，打印工作目录，linux 路径，linux 导航，命令行基础"
---

## Lesson Content

在 Linux 中，一个核心概念是所有内容都被视为文件。这些文件组织在一个被称为文件系统的分层结构中。理解这种结构是有效导航系统的关键。

### Linux 中的目录树

整个文件系统从一个名为根目录的顶级目录开始，用正斜杠（`/`）表示。从根目录开始，**linux 中的目录树** 分支成各种子目录，这些子目录可以包含文件和更多的子目录。

以下是这种结构的一个简化示例：

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

### 理解文件路径

任何文件或目录的位置都由其路径描述。路径是从一个起点到特定目的地的目录序列。例如，如果 `/home` 目录下有一个名为 `pete` 的文件夹，而 `pete` 内部有一个 `Movies` 文件夹，那么完整路径将是 `/home/pete/Movies`。

### Linux 中 PWD 的完整形式是什么？

在文件系统导航时，了解您当前的位置至关重要。用于此目的的命令是 `pwd`。**linux 中 pwd 的完整形式** 是 "print working directory"（打印工作目录）。它的唯一目的是显示您当前所在目录的完整路径，从根目录（`/`）开始。

### 使用 linux pwd 命令

要查找您的 **current directory linux**（当前目录），只需键入 **linux pwd** 命令并按 Enter 键。它会在命令行上打印出您当前位置的绝对路径。

```bash
pwd
```

你在哪里？我在哪里？尝试一下以查看您自己的当前工作目录。

## Exercise

实践造就完美！以下是一些实践操作实验，以加强您对 Linux 文件系统导航和识别当前位置的理解：

1. **[Linux pwd 命令：目录显示](https://labex.io/zh/labs/linux-linux-pwd-command-directory-displaying-209734)** - 此实验提供了对 `pwd` 命令的集中概述和实际用法，直接与课程中介绍的查找当前目录的内容相符。
2. **[Linux 目录导航](https://labex.io/zh/labs/linux-directory-navigation-387844)** - 通过在各种目录中导航来测试您的基本 Linux 命令行技能，巩固您对路径和文件系统结构的理解。
3. **[Linux cd 命令：目录更改](https://labex.io/zh/labs/linux-linux-cd-command-directory-changing-209733)** - 学习如何使用 `cd` 命令高效地导航文件系统，理解更改目录和探索文件结构的不同技术。

这些实验将帮助您在实际场景中应用文件系统层次结构和导航的概念，并增强对基本 Linux 命令的信心。

## Quiz Question

用于查找您当前所在目录的命令是什么？（请用英文回答，只使用小写的命令名称。）

## Quiz Answer

pwd
