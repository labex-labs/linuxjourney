---
index: 8
lang: "zh"
title: "niceness"
meta_title: "niceness - 进程"
meta_description: "了解 Linux niceness 和进程优先级。理解 nice 和 renice 命令以管理进程的 CPU 时间。提高系统性能！"
meta_keywords: "Linux niceness, 进程优先级，nice 命令，renice 命令，Linux 教程，CPU 调度，Linux 初学者，Linux 指南"
---

## Lesson Content

当您在计算机上同时运行多个程序时，例如 Chrome、Microsoft Word 或 Photoshop，这些进程可能看起来是同时运行的，但这并不完全正确。

进程使用 CPU 一小段时间，这被称为时间片。然后它们暂停几毫秒，另一个进程获得一小段时间片。默认情况下，进程调度以这种循环方式进行。每个进程都会获得足够的时间片，直到它完成处理。内核处理所有这些进程切换，并且大多数时候它都做得很好。

进程无法决定何时以及获得多长时间的 CPU 时间。如果所有进程都正常运行，它们将（大致）获得相同数量的 CPU 时间。但是，有一种方法可以通过 nice 值来影响内核的进程调度算法。Niceness 是一个相当奇怪的名称，但它的意思是进程有一个数字来确定它们对 CPU 的优先级。高数字意味着该进程是“nice”的，并且对 CPU 的优先级较低，而低或负数意味着该进程不是很“nice”，并且它希望尽可能多地获得 CPU 时间。

```bash
top
```

您现在可以看到一个 `NI` 列；那是进程的 niceness 级别。

要更改 niceness 级别，您可以使用 `nice` 和 `renice` 命令：

```bash
nice -n 5 apt upgrade
```

`nice` 命令用于为新进程设置优先级。`renice` 命令用于为现有进程设置优先级。

```bash
renice 10 -p 3245
```

## Exercise

哪些进程不是很“nice”，为什么？

## Quiz Question

如果我希望一个进程获得更高的 CPU 优先级，我应该使用更低还是更高的 nice 值？

## Quiz Answer

lower
