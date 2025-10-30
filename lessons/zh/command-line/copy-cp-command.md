---
index: 10
lang: "zh"
title: "cp (复制)"
meta_title: "cp (复制) - 命令行"
meta_description: "掌握 Linux cp 命令来复制文件和目录。本指南涵盖了递归复制 (-r)、使用 cp -p 标志保留属性以及使用 cp -f 标志强制覆盖等基本选项。了解 Linux 中的 cp -p 如何帮助维护文件元数据。"
meta_keywords: "cp 命令，复制文件 linux, linux cp -p, cp -p 标志，linux 中的 cp -p, cp -f 标志，递归复制，cp -r, linux 通配符，linux 命令行"
---

## Lesson Content

cp 命令是 Linux 中用于复制文件和目录的标准工具。其基本语法是 `cp [SOURCE] [DESTINATION]`。

### 基本文件复制

要复制文件，您需要指定源文件和目标目录或路径。

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

在此示例中，`mycoolfile` 是源文件，而 `/home/pete/Documents/cooldocs` 是目标目录。您也可以复制文件并为其在目标位置指定一个新名称。

```bash
cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

### 使用通配符进行批量复制

通配符是特殊的字符，可帮助您根据模式选择多个文件，从而提供极大的灵活性。

- `*`: 匹配任何字符序列。
- `?`: 匹配任何单个字符。
- `[]`: 匹配方括号中包含的任何一个字符。

例如，要将当前位置的所有 JPEG 图像复制到 `Pictures` 目录中：

```bash
cp *.jpg /home/pete/Pictures
```

### 递归复制目录

如果尝试在不使用任何选项的情况下使用 `cp` 复制目录，您将收到错误。要复制目录及其所有内容（包括子目录），必须使用 `-r`（递归）标志。

```bash
cp -r Pumpkin/ /home/pete/Documents
```

此命令将 `Pumpkin` 目录及其内部的所有内容复制到您的 `Documents` 目录中。

### 处理文件覆盖

默认情况下，如果目标位置存在同名文件，`cp` 将覆盖它。为防止意外数据丢失，请使用 `-i`（交互式）标志，它会在覆盖前提示确认。

```bash
cp -i mycoolfile /home/pete/Pictures
```

相反，如果您想在不进行任何提示的情况下强制覆盖，可以使用 `cp -f 标志`。这在无法进行用户交互的脚本中非常有用。

```bash
cp -f mycoolfile /home/pete/Pictures
```

### 使用 cp -p 保留文件属性

当您复制文件时，其元数据（如修改时间和所有权）通常会被更新。要保留这些原始属性，`cp -p` 标志至关重要。在 Linux 中使用 `cp -p` 可确保复制品不仅内容相同，而且元数据也相同。

`cp -p 标志` 在备份或迁移文件时特别有用，因为保留时间戳至关重要。

```bash
cp -p mycoolfile /home/pete/backups/
```

此命令演示了如何使用 `linux cp -p` 复制 `mycoolfile`，同时保留其模式、所有权和时间戳。

## Exercise

熟能生巧！以下是一些实践练习，以加强您对在 Linux 中复制文件和目录的理解：

1.  **[Linux cp 命令：文件复制](https://labex.io/zh/labs/linux-linux-cp-command-file-copying-209744)** - 练习基本用法、递归复制、保留属性等高级选项，以及使用通配符高效地复制文件和目录。
2.  **[组织文件和目录](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 通过使用 `cp`、`mv` 和 `rm` 命令来组织项目结构、移动文件和清理不必要的目录，练习基本的 Linux 文件管理技能。

这些实验将帮助您在实际场景中应用这些概念，并增强您对 Linux 中文件复制和管理的信心。

## Quiz Question

您需要指定哪个标志才能复制一个目录？

## Quiz Answer

-r
