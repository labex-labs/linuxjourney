---
index: 2
lang: "zh"
title: "pwd（显示当前工作目录）"
meta_title: "pwd（显示当前工作目录）- 命令行"
meta_description: "学习 Linux 中的 pwd 命令，了解显示当前工作目录的含义，以及绝对路径如何显示你在文件系统中的当前位置。"
meta_keywords: "pwd 命令, linux pwd, 显示当前工作目录, 当前目录 linux, 绝对路径, linux 文件系统, 目录树"
---

## Lesson Content

在 Linux 中，文件和目录以层级结构组织，称为文件系统。在你能够自如地移动之前，你需要知道自己所在的位置。`pwd` 命令通过打印你当前的工作目录来回答这个问题。

### The Directory Tree in Linux

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

### Understanding File Paths

任何文件或目录的位置都由其路径描述。路径是一系列目录，从起点到特定目标的顺序。

例如，如果你在 `/home` 目录下有一个名为 `pete` 的文件夹，`pete` 文件夹内有一个 `Movies` 文件夹，则完整路径是：

```plaintext
/home/pete/Movies
```

以 `/` 开头的路径是绝对路径，因为它从根目录开始。像 `Movies` 这样的路径是相对路径，因为它依赖于你当前的位置。

### What is the Full Form of PWD in Linux?

`pwd` 的完整形式是“print working directory”（打印当前工作目录）。你的工作目录是你的 shell 当前所在的目录。使用相对路径的命令都是从这个位置开始的。

### Using the pwd Command

要查找你当前的目录，输入 `pwd` 并按回车。

```bash
$ pwd
/home/pete
```

输出是一个绝对路径。在此示例中，shell 当前位于 `pete` 用户的主目录。

### Why pwd is Useful

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

### Common Questions

**pwd 会改变任何东西吗？** 不会。`pwd` 只打印信息。

**为什么我的系统上输出不同？** 你的用户名、主目录和当前位置可能不同。

**pwd 和 cd 有什么区别？** `pwd` 显示你所在的位置。`cd` 改变你所在的位置。

## Exercise

熟能生巧！这里有一些动手实验，帮助你巩固对 Linux 文件系统导航和定位当前所在位置的理解：

1. **[Linux pwd 命令：显示目录](https://labex.io/zh/labs/linux-linux-pwd-command-directory-displaying-209734)** - 本实验提供了对 `pwd` 命令的重点介绍和实际使用，直接对应本课关于查找当前目录的内容。
2. **[Linux 目录导航](https://labex.io/zh/labs/linux-directory-navigation-387844)** - 通过导航不同目录，测试你的基本 Linux 命令行技能，巩固对路径和文件系统结构的理解。
3. **[Linux cd 命令：切换目录](https://labex.io/zh/labs/linux-linux-cd-command-directory-changing-209733)** - 学习如何使用 `cd` 命令高效地导航文件系统，理解切换目录的不同技巧并探索文件结构。

这些实验将帮助你在实际场景中应用文件系统层级和导航的概念，并增强对基本 Linux 命令的信心。

## Quiz Question

哪个命令用于查找你当前所在的目录？（请用英文回答，仅使用小写命令名称。）

## Quiz Answer

pwd
