---
index: 2
lang: "zh"
title: "pwd (打印工作目录)"
meta_title: "pwd (打印工作目录) - 命令行"
meta_description: "学习如何在 Linux 中使用 'pwd' 命令来打印当前工作目录。了解 Linux 文件系统路径和导航，适合初学者。"
meta_keywords: "pwd 命令，Linux 目录，当前目录，Linux 路径，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

在 Linux 中，一切皆文件。随着你深入学习 Linux，你会理解这一点，但目前只需记住这一点即可。每个文件都组织在一个分层的目录树中。文件系统中的第一个目录恰当地命名为根目录。根目录有许多文件夹和文件，它们可以存储更多的文件夹和文件，等等。以下是目录树的示例：

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

这些文件和目录的位置被称为路径。如果你有一个名为 `home` 的文件夹，其中包含一个名为 `pete` 的文件夹，而该文件夹中又有一个名为 `Movies` 的文件夹，那么该路径将是这样的：`/home/pete/Movies`。很简单，对吧？

文件系统的导航，就像现实生活一样，如果你知道你在哪里以及要去哪里，就会很有帮助。要查看你在哪里，你可以使用 `pwd` 命令。这个命令的意思是“print working directory”（打印工作目录），它只是显示你当前所在的目录。请注意，路径源自根目录。

```bash
pwd
```

你在哪里？我在哪里？试一试。

## Exercise

No exercises for this lesson.

## Quiz Question

如何查找您当前所在的目录？

## Quiz Answer

pwd
