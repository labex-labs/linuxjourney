---
index: 5
lang: "zh"
title: "touch"
meta_title: "touch - 命令行"
meta_description: "学习如何使用 Linux touch 命令创建新文件和更新时间戳。这份适合初学者的指南帮助您理解文件管理。"
meta_keywords: "touch command, create files, Linux tutorial, file timestamps, Linux for beginners, Linux guide, basic commands"
---

## Lesson Content

让我们学习如何创建一些文件。一个非常简单的方法是使用 `touch` 命令。`touch` 允许您创建新的空文件。

```bash
touch mysuperduperfile
```

瞧，新文件就创建好了！

`touch` 也用于更改现有文件和目录的时间戳。试一试：对一个文件执行 `ls -l` 并记下时间戳，然后 `touch` 该文件，它将更新时间戳。

还有许多其他创建文件的方法，涉及重定向和文本编辑器等，但我们将在文本操作课程中介绍。

## Exercise

1. 创建一个新文件。
2. 记下时间戳。
3. 再次 `touch` 该文件并检查时间戳。

如需更多文件管理方面的实践，请探索这些交互式实验：

- [Linux Directory Navigation](https://labex.io/zh/labs/linux-directory-navigation-387844)
- [Setting Up a New Project Structure](https://labex.io/zh/labs/linux-setting-up-a-new-project-structure-387859)

## Quiz Question

如何创建一个名为 `myfile` 的文件？

## Quiz Answer

touch myfile
