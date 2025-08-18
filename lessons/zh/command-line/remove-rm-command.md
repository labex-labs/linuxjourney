---
lang: "zh"
title: "rm (删除)"
meta_description: "学习如何在 Linux 中使用 `rm` 命令安全地删除文件和目录。了解 -f、-i、-r 和 rmdir 等选项。开始你的 Linux 之旅！"
meta_keywords: "rm 命令，删除文件 Linux, 删除目录，Linux 教程，Linux 初学者，rmdir, Linux 指南"
---

## Lesson Content

现在，我想我们文件太多了；让我们删除一些。要删除文件，可以使用 `rm` 命令。`rm` (remove) 命令用于删除文件和目录。

```bash
rm file1
```

使用 `rm` 时要小心；没有神奇的回收站可以让你找回删除的文件。一旦它们消失了，就永远消失了，所以请务必小心。

幸运的是，有一些安全措施，所以普通用户不能轻易删除一堆重要文件。受写保护的文件在删除前会提示你确认。如果一个目录是受写保护的，它也不会轻易被删除。

现在，如果你不关心这些，你绝对可以删除一堆文件。

```bash
rm -f file1
```

`-f` 或 force 选项告诉 `rm` 删除所有文件，无论它们是否受写保护，且不提示用户（只要你拥有适当的权限）。

```bash
rm -i file
```

添加 `-i` 标志，就像许多其他命令一样，会提示你是否真的要删除文件或目录。

```bash
rm -r directory
```

你不能默认直接 `rm` 一个目录；你需要添加 `-r` 标志 (recursive) 来删除该目录中的所有文件和任何子目录。

你可以使用 `rmdir` 命令删除一个目录。

```bash
rmdir directory
```

## Exercise

1. 创建一个名为 `-file` 的文件（不要忘记破折号！）。
2. 删除该文件。

## Quiz Question

如何删除一个名为 `myfile` 的文件？

## Quiz Answer
