---
index: 11
lang: "zh"
title: "mv (移动)"
meta_title: "mv (移动) - 命令行"
meta_description: "学习如何使用 Linux mv 命令移动和重命名文件/目录。了解其选项并防止覆盖。开始你的 Linux 之旅！"
meta_keywords: "mv 命令，Linux mv, 移动文件 Linux, 重命名文件 Linux, Linux 教程，初学者，Linux 指南"
---

## Lesson Content

用于移动文件和重命名文件。在标志和功能方面与 `cp` 命令非常相似。

你可以像这样重命名文件：

```bash
mv oldfile newfile
```

或者你可以将文件移动到不同的目录：

```bash
mv file2 /home/pete/Documents
```

并移动多个文件：

```bash
mv file_1 file_2 /somedirectory
```

你也可以重命名目录：

```bash
mv directory1 directory2
```

像 `cp` 一样，如果你 `mv` 一个文件或目录，它会覆盖同一目录中的任何内容。因此，你可以使用 `-i` 标志在覆盖任何内容之前提示你。

```bash
mv -i directory1 directory2
```

假设你确实想 `mv` 一个文件来覆盖之前的文件。你也可以备份该文件，它只会将旧版本重命名为 `~`。

```bash
mv -b directory1 directory2
```

## Exercise

重命名一个文件，然后将该文件移动到不同的目录。

## Quiz Question

如何将名为 `cat` 的文件重命名为 `dog`？

## Quiz Answer

mv cat dog
