---
index: 11
lang: "zh"
title: "mv (移动)"
meta_title: "mv (移动) - 命令行"
meta_description: "关于 Linux 中 mv 命令的综合指南。学习如何使用 bash mv 命令来移动和重命名文件和目录，使用 linux mv -t 等选项，以及防止意外覆盖。"
meta_keywords: "mv 命令，linux 中的 mv 命令，linux mv, bash mv, mv -r linux, linux mv -t, 移动文件，重命名文件，linux 命令行"
---

## Lesson Content

`mv` 命令是 "move" 的缩写，是任何 Linux 环境中的基本实用程序。它主要有两个目的：重命名文件或目录，以及将它们移动到不同的位置。它的功能在很多方面与 `cp` 命令相似。

### 重命名文件和目录

`mv command in linux` 最常见的用途之一就是重命名。语法很简单：指定旧名称和新名称。

重命名文件：

```bash
mv oldfile newfile
```

同样的逻辑也适用于重命名目录：

```bash
mv old_directory_name new_directory_name
```

### 移动文件和目录

`mv` 命令的另一个核心功能是将项目从一个位置移动到另一个位置。

将单个文件移动到另一个目录：

```bash
mv file2 /home/pete/Documents
```

您也可以一次移动多个文件。只需列出所有源文件，然后是目标目录：

```bash
mv file_1 file_2 /somedirectory
```

一个有用的选项是 `linux mv -t`，它允许您首先指定目标目录。在移动许多文件时，这可能更清晰。

```bash
mv -t /somedirectory file_1 file_2
```

与 `cp` 命令不同，您不需要 `-r` 标志来移动目录。`bash mv` 命令默认处理目录。虽然有些用户搜索 `mv -r linux`，但在使用 `mv` 移动目录时，此选项不是必需的。

### mv 命令的重要选项

默认情况下，如果您将文件移动到已存在同名文件的目标位置，`mv` 会在没有警告的情况下覆盖它。为防止意外数据丢失，您可以使用以下选项：

- **-i (interactive)**：这是一个关键的安全功能。它会在覆盖任何现有文件之前提示您确认。

  ```bash
  mv -i source_file destination_directory
  ```

- **-b (backup)**：如果您打算覆盖文件但想保留旧版本，此选项会创建目标文件的备份。备份通常以波浪号（`~`）后缀重命名。

  ```bash
  mv -b file1 directory_with_file1
  ```

- **-v (verbose)**：此选项使 `mv` 命令打印它正在执行的操作，显示正在移动或重命名的每个文件。

  ```bash
  mv -v file1 file2 /somedirectory
  ```

掌握 `mv command` 对于在命令行上高效管理文件至关重要。

## Exercise

实践造就完美！动手实践对于掌握 `mv` 等 Linux 命令至关重要。这些实验将帮助您在真实环境中巩固对移动和重命名文件和目录的理解：

1.  **[Linux mv 命令：文件移动和重命名](https://labex.io/zh/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - 练习使用 `mv` 命令移动和重命名文件和目录，包括了解其各种选项和行为。
2.  **[组织文件和目录](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 在实际挑战中应用您对 `mv`（以及 `cp` 和 `rm`）的知识，以组织项目结构、移动文件和清理目录。

这些实验将帮助您在真实场景中应用概念，并增强使用 `mv` 命令进行文件和目录管理的信心。

## Quiz Question

使用 `mv` 命令，如何将名为 `cat` 的文件重命名为 `dog`？请提供完整的命令。注意：答案区分大小写，应以小写英文输入。

## Quiz Answer

mv cat dog
