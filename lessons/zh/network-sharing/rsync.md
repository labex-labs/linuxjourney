---
lang: "zh"
title: "rsync"
meta_description: "学习 rsync 以实现高效的 Linux 文件同步和备份。了解使用 rsync 命令和选项进行远程和本地数据传输。提升您的 Linux 技能！"
meta_keywords: "rsync, Linux 文件传输，数据备份，文件同步，Linux 教程，rsync 命令，初学者，指南"
---

## Lesson Content

另一个用于从不同主机复制数据的工具是 rsync（remote synchronization 的缩写）。Rsync 与 scp 非常相似，但它有一个主要区别。Rsync 使用一种特殊的算法，可以提前检查您要复制的数据是否已存在，并且只会复制差异部分。例如，假设您正在复制一个文件，但网络中断了，导致复制中途停止。Rsync 不会从头开始重新复制所有内容，而只会复制未复制的部分。

它还通过校验和验证您正在复制的文件的完整性。这些小的优化提供了更大的文件传输灵活性，使 rsync 成为远程和本地目录同步、数据备份、大数据传输等的理想选择。

一些常用的 rsync 选项：

- v - 详细输出
- r - 递归进入目录
- h - 人类可读输出
- z - 压缩以便于传输，非常适合慢速连接

### Copy/sync files on the same host

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copy/sync files to local host from a remote host

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copy/sync files to a remote host from a local host

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

使用 rsync 将一个目录同步到另一个目录。请务必不要覆盖重要目录！

## Quiz Question

哪个命令对数据备份有用？

## Quiz Answer

rsync
