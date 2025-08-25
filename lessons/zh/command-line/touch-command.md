---
index: 5
lang: "zh"
title: "touch"
meta_title: "touch - 命令行"
meta_description: "学习如何使用 Linux touch 命令创建新文件和更新时间戳。这个适合初学者的指南帮助您理解文件管理。"
meta_keywords: "touch 命令，创建文件，Linux 教程，文件时间戳，Linux 初学者，Linux 指南，基本命令"
---

## Lesson Content

让我们学习如何创建一些文件。一个非常简单的方法是使用 `touch` 命令。`touch` 允许您创建新的空文件。

```bash
touch mysuperduperfile
```

瞧，新文件就创建好了！

`touch` 也用于更改现有文件和目录的时间戳。试一试：对一个文件执行 `ls -l` 并记下时间戳，然后 `touch` 该文件，它将更新时间戳。

还有许多其他创建文件的方法，涉及重定向和文本编辑器等，但我们将在文本操作课程中学习这些。

## Exercise

熟能生巧！以下是一些动手实验，以巩固您对创建和管理文件系统对象的理解：

1. **[Linux mkdir 命令：目录创建](https://labex.io/zh/labs/linux-linux-mkdir-command-directory-creating-209739)** - 学习如何在 Linux 中使用 `mkdir` 命令创建目录、设置权限并组织文件系统。这将帮助您理解在文件系统中创建新项目的更广泛概念。
2. **[设置新项目结构](https://labex.io/zh/labs/linux-setting-up-a-new-project-structure-387859)** - 通过创建特定的项目结构并使用 `mkdir` 和 `cd` 等基本命令进行导航，练习您的 Linux 目录管理技能。

这些实验将帮助您在实际场景中应用文件系统创建和组织的概念，并增强您使用 Linux 命令的信心。

## Quiz Question

如何创建一个名为 `myfile` 的文件？

## Quiz Answer

touch myfile
