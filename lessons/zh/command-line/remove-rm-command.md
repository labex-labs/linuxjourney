---
index: 13
lang: "zh"
title: "rm (删除)"
meta_title: "rm (删除) - 命令行"
meta_description: "学习如何在 Linux 中使用 `rm` 命令安全地删除文件和目录。了解 -f、-i、-r 和 rmdir 等选项。开始你的 Linux 之旅！"
meta_keywords: "rm command, delete files Linux, remove directories, Linux tutorial, beginner Linux, rmdir, Linux guide"
---

## Lesson Content

现在，我觉得文件太多了；我们来删除一些。要删除文件，可以使用 `rm` 命令。`rm` (remove) 命令用于删除文件和目录。

```bash
rm file1
```

使用 `rm` 时要小心；没有神奇的回收站可以让你找回已删除的文件。一旦它们消失了，就永远消失了，所以要小心。

幸运的是，有一些安全措施，所以普通用户不能轻易删除一堆重要文件。受写保护的文件在删除前会提示你确认。如果一个目录受写保护，它也不会轻易被删除。

现在，如果你不关心这些，你绝对可以删除一堆文件。

```bash
rm -f file1
```

`-f` 或 force 选项告诉 `rm` 删除所有文件，无论它们是否受写保护，而无需提示用户（只要你拥有适当的权限）。

```bash
rm -i file
```

添加 `-i` 标志，就像许多其他命令一样，会提示你是否真的要删除文件或目录。

```bash
rm -r directory
```

默认情况下，你不能直接 `rm` 一个目录；你需要添加 `-r` 标志（recursive）来删除其中的所有文件和任何子目录。

你可以使用 `rmdir` 命令删除目录。

```bash
rmdir directory
```

## Exercise

要亲自动手练习 `rm` 命令，请尝试这个交互式实验：

- [Linux rm Command: File Removing](https://labex.io/zh/labs/linux-linux-rm-command-file-removing-209741)

## Quiz Question

如何删除一个名为 `myfile` 的文件？

## Quiz Answer

rm myfile
