---
index: 3
lang: "zh"
title: "stderr (标准错误)"
meta_title: "stderr (标准错误) - 文本操作"
meta_description: "了解 Linux stderr（标准错误）重定向。理解 2>、2>&1、&> 和 /dev/null 用于 Bash 中的错误处理。提高您的 Linux 命令行技能！"
meta_keywords: "Linux stderr, 标准错误，2> 重定向，2>&1, &> 重定向，/dev/null, Bash 错误处理，Linux 教程，Linux 初学者"
---

## Lesson Content

现在我们来尝试一些不同的东西。让我们尝试列出系统中不存在的目录的内容，并将输出再次重定向到 `peanuts.txt` 文件。

```bash
ls /fake/directory > peanuts.txt
```

你应该看到的是：

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

现在你可能会想，这条消息不应该发送到文件吗？实际上，这里还有另一个 I/O 流，称为标准错误 (stderr)。默认情况下，stderr 也会将其输出发送到屏幕；它与 stdout 是一个完全不同的流。因此，你需要以不同的方式重定向其输出。

不幸的是，重定向器不像使用 `<` 或 `>` 那么方便，但它非常接近。我们将不得不使用文件描述符。文件描述符是一个非负数，用于访问文件或流。我们稍后会深入探讨这一点，但现在要知道 stdin、stdout 和 stderr 的文件描述符分别为 0、1 和 2。

所以现在如果我们要将 stderr 重定向到文件，我们可以这样做：

```bash
ls /fake/directory 2> peanuts.txt
```

你应该只在 `peanuts.txt` 中看到 stderr 消息。

那么如果我想在 `peanuts.txt` 文件中同时看到 stderr 和 stdout 呢？也可以使用文件描述符来实现这一点：

```bash
ls /fake/directory > peanuts.txt 2>&1
```

这会将 `ls /fake/directory` 的结果发送到 `peanuts.txt` 文件，然后通过 `2>&1` 将 stderr 重定向到 stdout。这里的操作顺序很重要；`2>&1` 将 stderr 发送到 stdout 指向的任何地方。在这种情况下，stdout 指向一个文件，所以 `2>&1` 也将 stderr 发送到一个文件。所以如果你打开 `peanuts.txt` 文件，你应该会看到 stderr 和 stdout。在我们的例子中，上面的命令只输出 stderr。

有一种更短的方法可以将 stdout 和 stderr 都重定向到文件：

```bash
ls /fake/directory &> peanuts.txt
```

那么如果我不想看到任何这些冗余信息，并想完全摆脱 stderr 消息呢？嗯，你也可以将输出重定向到一个名为 `/dev/null` 的特殊文件，它会丢弃任何输入。

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

以下命令在做什么？

```bash
ls /fake/directory >> /dev/null 2>&1
```

## Quiz Question

stderr 的重定向符是什么？

## Quiz Answer

2>
