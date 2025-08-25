---
index: 2
lang: "zh"
title: "pwd (打印工作目录)"
meta_title: "pwd (打印工作目录) - 命令行"
meta_description: "学习如何在 Linux 中使用 'pwd' 命令来打印当前工作目录。了解 Linux 文件系统路径和导航，适合初学者。"
meta_keywords: "pwd 命令，Linux 目录，当前目录，Linux 路径，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

Linux 中的一切都是文件。随着你深入了解 Linux，你会明白这一点，但现在，请记住这一点。每个文件都组织在一个分层的目录树中。文件系统中的第一个目录恰当地命名为根目录。根目录有许多文件夹和文件，这些文件夹和文件可以存储更多的文件夹和文件，等等。以下是目录树的示例：

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

这些文件和目录的位置被称为路径。如果你有一个名为 `home` 的文件夹，其中包含一个名为 `pete` 的文件夹，而该文件夹中又有一个名为 `Movies` 的文件夹，那么该路径将如下所示：`/home/pete/Movies`。很简单，对吧？

文件系统的导航，就像现实生活一样，如果你知道你在哪里以及要去哪里，就会很有帮助。要查看你在哪里，你可以使用 `pwd` 命令。这个命令的意思是“打印工作目录”，它只是显示你当前所在的目录。请注意，路径源自根目录。

```bash
pwd
```

你在哪里？我在哪里？试一试。

## Exercise

熟能生巧！这里有一些动手实验，可以帮助你巩固对 Linux 文件系统导航和识别当前位置的理解：

1. **[Linux pwd 命令：目录显示](https://labex.io/zh/labs/linux-linux-pwd-command-directory-displaying-209734)** - 本实验提供了 `pwd` 命令的重点概述和实际用法，直接与课程中查找当前目录的介绍相符。
2. **[Linux 目录导航](https://labex.io/zh/labs/linux-directory-navigation-387844)** - 通过导航各种目录来测试你的基本 Linux 命令行技能，巩固你对路径和文件系统结构的理解。
3. **[Linux cd 命令：目录更改](https://labex.io/zh/labs/linux-linux-cd-command-directory-changing-209733)** - 学习使用 `cd` 命令高效地导航文件系统，了解更改目录和探索文件结构的不同技术。

这些实验将帮助你在实际场景中应用文件系统层次结构和导航的概念，并增强对基本 Linux 命令的信心。

## Quiz Question

如何查找你当前所在的目录？

## Quiz Answer

pwd
