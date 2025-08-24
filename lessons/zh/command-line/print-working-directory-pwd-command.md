---
index: 2
lang: "zh"
title: "pwd (打印工作目录)"
meta_title: "pwd (打印工作目录) - 命令行"
meta_description: "了解如何在 Linux 中使用 'pwd' 命令打印当前工作目录。了解 Linux 文件系统路径和导航，适合初学者。"
meta_keywords: "pwd 命令，Linux 目录，当前目录，Linux 路径，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

Linux 中的一切都是文件。随着您深入了解 Linux，您会明白这一点，但目前，请记住这一点。每个文件都组织在一个分层的目录树中。文件系统中的第一个目录恰当地命名为根目录。根目录有许多文件夹和文件，可以存储更多文件夹和文件，等等。以下是目录树的示例：

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

这些文件和目录的位置被称为路径。如果您有一个名为 `home` 的文件夹，其中包含一个名为 `pete` 的文件夹，并且该文件夹中还有一个名为 `Movies` 的文件夹，那么该路径将如下所示：`/home/pete/Movies`。很简单，是吧？

文件系统的导航，就像现实生活一样，如果您知道自己身在何处以及要去往何处，就会很有帮助。要查看您身在何处，可以使用 `pwd` 命令。此命令表示“打印工作目录”，它只显示您所在的目录。请注意，路径源自根目录。

```bash
pwd
```

你在哪里？我在哪里？试一试。

## Exercise

要亲自动手练习 `pwd` 命令，请尝试此交互式实验：

- [Linux pwd Command: Directory Displaying](https://labex.io/zh/labs/linux-linux-pwd-command-directory-displaying-209734)

## Quiz Question

如何查找您当前所在的目录？

## Quiz Answer

pwd
