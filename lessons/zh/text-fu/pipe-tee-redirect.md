---
index: 4
lang: "zh"
title: "管道和 tee"
meta_title: "管道和 tee - 文本操作"
meta_description: "学习 Linux 管道和 tee 命令，实现高效的命令行数据流。理解 stdout、stdin 和文件输出。提升你的 Linux 技能！"
meta_keywords: "Linux 管道，tee 命令，Linux 教程，stdout, stdin, Linux 初学者，命令行，Linux 指南"
---

## Lesson Content

现在我们来做一些“管道”工作，虽然不是真的管道，但有点类似。我们来尝试一个命令：

```bash
ls -la /etc
```

你应该会看到一个非常长的列表；实际上，这有点难以阅读。与其将这个输出重定向到一个文件，如果我们能直接在另一个命令（比如 `less`）中看到输出，那不是很好吗？嗯，我们可以做到！

```bash
ls -la /etc | less
```

管道操作符 `|`，由一个竖线表示，允许我们将一个命令的 `stdout` 作为另一个进程的 `stdin`。在这个例子中，我们获取了 `ls -la /etc` 的 `stdout`，然后将其“管道”传输给 `less` 命令。管道命令非常有用，我们将永远继续使用它。

那么，如果我想将命令的输出写入两个不同的流怎么办？这可以通过 `tee` 命令实现：

```bash
ls | tee peanuts.txt
```

你应该会在屏幕上看到 `ls` 的输出，如果你打开 `peanuts.txt` 文件，你应该会看到相同的信息！

## Exercise

尝试以下命令：

```bash
ls | tee peanuts.txt banan.txt
```

## Quiz Question

哪个键代表管道操作符？

## Quiz Answer

|
