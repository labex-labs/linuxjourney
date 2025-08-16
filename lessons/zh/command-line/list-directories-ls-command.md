---
lang: "zh"
title: "ls (列出目录)"
description: "学习如何在 Linux 中使用 'ls' 命令来列出目录内容、查看隐藏文件并理解文件详细信息。提高您的 Linux 命令行技能！"
keywords: "ls 命令，列出目录，Linux 教程，隐藏文件，Linux 命令，Linux 初学者，Linux 指南"
---

## Lesson Content

既然我们知道如何在系统中移动，那么我们如何知道有哪些可用的内容呢？现在，我们就像在黑暗中摸索。嗯，我们可以使用出色的 `ls` 命令来列出目录内容。`ls` 命令默认会列出当前目录中的目录和文件；但是，您可以指定要列出其目录的路径。

```bash
ls
ls /home/pete
```

`ls` 是一个非常有用的工具；它还会向您显示有关您正在查看的文件和目录的详细信息。

另外，请注意，并非目录中的所有文件都可见。以 `.` 开头的文件名是隐藏的。但是，您可以使用 `ls` 命令并向其传递 `-a` 标志（`a` 代表 all）来查看它们。

```bash
ls -a
```

还有一个有用的 `ls` 标志，`-l` 代表 long。这会以长格式显示文件的详细列表。这将向您显示详细信息，从左到右依次是：文件权限、链接数、所有者名称、所有者组、文件大小、上次修改的时间戳以及文件/目录名称。

```bash
ls -l
```

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

命令有称为标志（或参数或选项，随你怎么称呼）的东西，以增加更多功能。看看我们是如何添加 `-a` 和 `-l` 的；嗯，你可以将它们一起添加为 `-la`。标志的顺序决定了它的执行顺序。大多数时候，这并不重要，所以你也可以使用 `ls -al`，它仍然会起作用。

```bash
ls -la
```

## Exercise

运行 `ls` 并使用不同的标志，查看您收到的输出。

## Quiz Question

您会使用什么命令来查看隐藏文件？

## Quiz Answer

ls -a
