---
index: 2
lang: "zh"
title: "rsync"
meta_title: "rsync - 网络共享"
meta_description: "学习 rsync 以实现高效的 Linux 文件同步和备份。了解使用 rsync 命令和选项进行远程和本地数据传输。提高您的 Linux 技能！"
meta_keywords: "rsync, Linux 文件传输，数据备份，文件同步，Linux 教程，rsync 命令，初学者，指南"
---

## Lesson Content

另一个用于从不同主机复制数据的工具是 rsync（remote synchronization 的缩写）。Rsync 与 scp 非常相似，但它有一个主要区别。Rsync 使用一种特殊的算法，可以提前检查您要复制的数据是否已存在，并且只会复制差异部分。例如，假设您正在复制一个文件，但网络中断了；因此，您的复制中途停止了。Rsync 不会从头开始重新复制所有内容，而只会复制未复制的部分。

它还通过校验和验证您正在复制的文件的完整性。这些小的优化允许更大的文件传输灵活性，并使 rsync 成为远程和本地目录同步、数据备份、大数据传输等的理想选择。

一些常用的 rsync 选项：

- v - 详细输出
- r - 递归进入目录
- h - 人类可读输出
- z - 压缩以便于传输，非常适合慢速连接

### 在同一主机上复制/同步文件

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### 从远程主机复制/同步文件到本地主机

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### 从本地主机复制/同步文件到远程主机

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

虽然本主题没有具体的实验，但我们建议您探索全面的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

哪条命令对数据备份有用？

## Quiz Answer

rsync
