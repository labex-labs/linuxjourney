---
index: 7
lang: "zh"
title: "dd"
meta_title: "dd - 设备"
meta_description: "学习 Linux dd 命令，用于数据复制和磁盘映像。了解其选项，如 if、of 和 bs。开始您的 Linux 数据管理之旅！"
meta_keywords: "dd 命令，Linux dd, 复制数据，磁盘映像，Linux 教程，初学者，指南，数据备份"
---

## Lesson Content

`dd` 工具对于数据转换和复制非常有用。它从文件或数据流读取输入，并将其写入文件或数据流。

考虑以下命令：

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1024
```

此命令正在将 `backup.img` 的内容复制到 `/dev/sdb`。它将以 1024 字节的块复制数据，直到没有更多数据可复制。

- `if=file` - 输入文件；从文件而不是标准输入读取。
- `of=file` - 输出文件；写入文件而不是标准输出。
- `bs=bytes` - 块大小；它一次读取和写入这么多字节的数据。您可以使用不同的度量单位，例如用 `k` 表示千字节，`m` 表示兆字节等，因此 1024 字节是 1k。
- `count=number` - 要复制的块数。

您会看到一些使用 `count` 选项的 `dd` 命令。通常，使用 `dd` 时，如果您想复制一个 1 兆字节的文件，您通常会希望该文件在复制完成后也是 1 兆字节。假设您运行以下命令：

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
```

我们的 `backup.img` 文件是 10M；但是，我们在此命令中表示要复制 1M 2 次，因此只复制了 2M，导致复制的数据不完整。`count` 在许多情况下都很有用，但如果您只是复制数据，您可以省略 `count`，甚至 `bs`。如果您真的想优化数据传输，那么您会希望开始使用这些选项。

`dd` 功能极其强大；您可以使用它来备份任何内容，包括整个磁盘驱动器、恢复磁盘映像等等。请注意，如果您不确定自己在做什么，这个强大的工具可能会付出代价。

## Exercise

使用 `dd` 命令备份您的驱动器，并将输出设置为 `.img` 文件。

## Quiz Question

`dd` 中用于块大小的选项是什么？

## Quiz Answer

bs
