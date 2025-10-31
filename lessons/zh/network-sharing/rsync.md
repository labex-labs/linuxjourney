---
index: 2
lang: "zh"
title: "rsync"
meta_title: "rsync - 网络共享"
meta_description: "了解如何在 Linux 中使用强大的 rsync 命令进行高效的文件同步、远程数据传输和可靠的备份。本指南涵盖了主要的 rsync 命令和选项。"
meta_keywords: "rsync, linux rsync, 文件同步，数据备份，远程同步，rsync 命令，linux 文件传输，rsync 教程"
---

## Lesson Content

### 什么是 rsync？

在不同主机之间复制数据的另一个重要工具是 `rsync`，它是“远程同步”的缩写。虽然它与 `scp` 相似，但 `rsync` 有一个关键区别，使其效率极高。它使用一种增量传输算法，可以智能地检查目标位置上已存在的数据，并且只传输文件中发生变化的部分。

例如，如果一个大文件传输中断，`rsync` 可以恢复复制过程，只传输文件中剩余的部分，而不是从头开始。这使其成为不稳定网络连接的可靠选择。

### rsync 的主要特点

`rsync` 的效率来自于其智能优化。它使用校验和来验证文件完整性，确保复制的数据在传输过程中没有损坏。这些特性提供了极大的灵活性，使 `rsync` 成为以下场景的理想工具：

- 目录同步（远程和本地）
- 创建增量数据备份
- 高效处理大文件传输

### 常见的 rsync 选项

您可以使用多个选项来修改 `rsync` 命令的行为。一些最常用的选项包括：

- `-v`：详细输出，显示正在传输的文件。
- `-r`：递归，复制整个目录时必需。
- `-h`：人类可读输出，以更易于理解的格式显示数字（例如 KB、MB）。
- `-z`：在传输过程中压缩文件数据，这对于慢速连接非常有用。
- `-a`：归档模式，一个方便的快捷方式，它组合了多个选项（`-rlptgoD`），用于保留权限、所有权和时间戳。

### rsync 用法示例

#### 在同一主机上同步文件

您可以使用 `rsync` 来同步本地机器上的两个目录。这对于创建本地备份非常有用。

```bash
rsync -avh /my/local/directory/one/ /my/local/directory/two/
```

#### 从远程主机同步文件到本地主机

要将文件从远程服务器拉取到本地机器，请先指定远程源。

```bash
rsync -avh username@remotehost.com:/remote/directory/ /local/directory/
```

#### 从本地主机同步文件到远程主机

要将文件从本地机器推送到远程服务器，请先指定本地源。

```bash
rsync -avh /local/directory/ username@remotehost.com:/remote/directory/
```

## Exercise

虽然此主题没有特定的实验环节，但我们建议您探索全面的[Linux 学习路径](https://labex.io/zh/learn/linux)来练习相关的 Linux 技能和概念。

## Quiz Question

哪个以其增量传输算法而闻名的命令特别适用于创建高效的数据备份？请用英语回答，注意区分大小写。

## Quiz Answer

rsync
