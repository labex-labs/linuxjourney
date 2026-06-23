---
index: 10
lang: "zh"
title: "cp（复制）"
meta_title: "cp（复制）- 命令行"
meta_description: "通过示例学习 Linux cp 命令，了解如何复制文件、目录、多文件、通配符、备份以及 cp -r、cp -i 和 cp -p 等选项。"
meta_keywords: "linux cp 命令, cp 命令, 复制文件 linux, cp -r, cp -i, cp -p, cp -a, cp -u, 递归复制, linux 通配符"
---

## Lesson Content

`cp` 命令是 Linux 中复制文件和目录的标准工具。它创建一个新的副本，同时保留原始文件。其基本语法是：

```bash
cp [OPTIONS] SOURCE DESTINATION
```

你可以将一个文件复制到另一个文件，将一个或多个文件复制到目录，或者使用正确的选项复制整个目录树。

### 基本文件复制

要复制文件，你需要指定源文件和目标目录或路径。

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

在此示例中，`mycoolfile` 是源文件，`/home/pete/Documents/cooldocs` 是目标目录。你也可以复制文件并在目标中给它一个新名字。

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

如果目标是一个已存在的目录，复制的文件将保留其原始名称。如果目标是一个文件名，`cp` 会创建一个具有该新名称的副本。

### 将多个文件复制到目录

要将多个文件复制到同一目录，先列出所有源文件，最后写目标目录。

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

当你提供多个源文件时，最后一个参数必须是目录。

### 使用通配符批量复制

通配符是特殊字符，帮助你基于模式选择多个文件，提供极大的灵活性。

- `*`：匹配任意字符序列。
- `?`：匹配任意单个字符。
- `[]`：匹配括号内的任意一个字符。

例如，要将当前目录下所有 JPEG 图片复制到 `Pictures` 目录：

```bash
$ cp *.jpg /home/pete/Pictures
```

你可以先预览匹配的文件：

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

### 递归复制目录

如果你尝试使用 `cp` 复制目录而不加任何选项，会收到错误。要复制目录及其所有内容（包括子目录），必须使用 `-r`（递归）标志。

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

此命令将 `Pumpkin` 目录及其所有内容复制到你的 `Documents` 目录。

你也可能看到 `-R`，在典型 Linux 系统中它具有相同的递归作用：

```bash
$ cp -R website /home/pete/backups/
```

### 处理文件覆盖

默认情况下，如果目标位置有同名文件，`cp` 会覆盖它。为了防止意外数据丢失，可以使用 `-i`（交互式）标志，覆盖前会提示确认。

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

相反，如果你想强制覆盖且不提示，可以使用 `-f` 选项。这在脚本中非常有用，因为无法进行用户交互。

```bash
$ cp -f mycoolfile /home/pete/Pictures
```

另一个有用的安全选项是 `-n`，表示“不覆盖”。它防止覆盖已存在的目标文件。

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

### 使用 -p 保留文件属性

复制文件时，其元数据（如修改时间和所有权）通常会被更新。要保留这些原始属性，请使用 `-p` 选项。

`cp -p` 选项在备份或迁移文件时特别有用，因为保留时间戳很重要。

```bash
$ cp -p mycoolfile /home/pete/backups/
```

这会复制 `mycoolfile`，同时保留其权限、所有权（在允许的情况下）和时间戳。

### 使用 -a 归档复制

`-a` 选项表示归档。它常用于备份式目录复制，因为它保留许多属性并递归复制。

```bash
$ cp -a project/ project-backup/
```

对于日常备份，`cp -a` 比手动组合多个选项更方便。

### 使用 -u 仅复制较新的文件

`-u` 选项仅在源文件比目标文件新，或者目标文件不存在时才复制。

```bash
$ cp -u *.txt /home/pete/Documents/
```

这在刷新文件夹时非常有用，可以避免重写已经是最新的文件。

### 常用 cp 选项

以下是你最常用的选项：

- `-r` 或 `-R`：递归复制目录。
- `-i`：覆盖文件前询问确认。
- `-f`：强制覆盖，必要时先删除目标文件。
- `-n`：不覆盖已存在的文件。
- `-p`：保留权限、所有权（如果可能）和时间戳。
- `-a`：归档模式，适合保留目录树。
- `-u`：仅当源文件比目标文件新时复制。
- `-v`：显示复制的每个文件。

### 常见问题

**为什么 cp 会覆盖我的文件？** 默认情况下，`cp` 会替换同名的目标文件。使用 `cp -i` 先询问，或使用 `cp -n` 避免覆盖。

**为什么 cp 不能复制目录？** 目录需要递归复制。使用 `cp -r source-dir destination-dir`。

**cp 和 mv 有什么区别？** `cp` 创建副本并保留原文件。`mv` 移动或重命名原文件。

**备份时应该用 cp -r 还是 cp -a？** 简单递归复制用 `cp -r`。需要保留更多文件属性的备份用 `cp -a`。

## Exercise

熟能生巧！以下是一些动手实验，帮助你巩固在 Linux 中复制文件和目录的理解：

1. **[Linux cp 命令：文件复制](https://labex.io/zh/labs/linux-linux-cp-command-file-copying-209744)** - 练习基本用法、高级选项如递归复制、保留属性以及使用通配符高效复制文件和目录。
2. **[文件和目录的组织](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 通过使用 `cp`、`mv` 和 `rm` 命令，练习 Linux 文件管理技能，组织项目结构，移动文件，清理不必要的目录。

这些实验将帮助你在实际场景中应用概念，增强对 Linux 文件复制和管理的信心。

## Quiz Question

复制目录时需要指定哪个标志？

## Quiz Answer

-r
