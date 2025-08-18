---
index: 6
lang: "zh"
title: "文件"
meta_title: "文件 - 命令行"
meta_description: "学习如何使用 Linux 的 'file' 命令来识别文件类型和内容。通过这份适合初学者的指南，了解 Linux 文件命名约定。"
meta_keywords: "Linux file 命令，识别文件类型，Linux 教程，文件命名，Linux 初学者，Linux 指南"
---

## Lesson Content

在上一课中，我们学习了 `touch`。让我们回顾一下。你有没有注意到文件名不符合标准的命名约定，就像你可能在其他操作系统（如 Windows）中看到的那样？通常，你会期望一个名为 `banana.jpeg` 的文件是一个 JPEG 图片文件。

在 Linux 中，文件名不要求代表文件的内容。你可以创建一个名为 `funny.gif` 的文件，但它实际上不是 GIF。

要找出文件是什么类型，你可以使用 `file` 命令。它会显示文件内容的描述。

```bash
file banana.jpg
```

## Exercise

对几个不同的目录和文件运行 `file` 命令，并记下输出。

## Quiz Question

你可以使用什么命令来查找文件的文件类型？

## Quiz Answer

file
