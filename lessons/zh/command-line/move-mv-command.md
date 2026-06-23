---
index: 11
lang: "zh"
title: "mv（移动）"
meta_title: "mv（移动）- 命令行"
meta_description: "通过示例学习 Linux mv 命令，用于移动文件、重命名文件和目录、移动多个文件以及避免覆盖。"
meta_keywords: "linux mv 命令, mv 命令, 移动文件 linux, 重命名文件 linux, 重命名目录 linux, mv -i, mv -n, mv -t"
---

## Lesson Content

`mv` 命令，意为“移动”，是任何 Linux 环境中的基础工具。它有两个主要用途：重命名文件或目录，以及将它们移动到不同的位置。

基本语法是：

```bash
mv [OPTIONS] SOURCE DESTINATION
```

与创建副本的 `cp` 不同，`mv` 改变了原始项目的位置或名称。

### 重命名文件和目录

`mv` 最常见的用途之一是重命名。语法很简单：指定旧名称和新名称。

重命名文件：

```bash
$ mv oldfile newfile
```

同样的逻辑适用于重命名目录：

```bash
$ mv old_directory_name new_directory_name
```

### 移动文件和目录

`mv` 命令的另一个核心功能是将项目从一个位置移动到另一个位置。

将单个文件移动到不同目录：

```bash
$ mv file2 /home/pete/Documents
```

你也可以一次移动多个文件。只需列出所有源文件，后跟目标目录：

```bash
$ mv file_1 file_2 somedirectory/
```

在 GNU/Linux 系统上，一个有用的选项是 `-t`，它允许你先指定目标目录。当移动许多文件时，这样更清晰。

```bash
$ mv -t somedirectory/ file_1 file_2
```

与 `cp` 命令不同，移动目录不需要递归选项。`mv` 默认支持目录。

### mv 命令的重要选项

默认情况下，如果你将文件移动到一个已存在同名文件的目标位置，`mv` 会直接覆盖而不提示。为了防止意外数据丢失，你可以使用以下选项：

- **-i（交互式）**：这是一个重要的安全功能。它会在覆盖任何已有文件前提示你确认。

  ```bash
  $ mv -i source_file destination_directory
  ```

- **-b（备份）**：如果你打算覆盖文件但想保留旧版本，此选项会创建目标文件的备份。备份文件通常会加上波浪号（`~`）后缀。

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- **-v（详细）**：此选项使 `mv` 命令打印出正在执行的操作，显示每个被移动或重命名的文件。

  ```bash
  $ mv -v file1 file2 somedirectory/
  ```

另一个有用的选项是 `-n`，表示不覆盖。它防止覆盖已存在的目标文件。

```bash
$ mv -n source_file destination_directory
```

### 常见 mv 示例

重命名文件：

```bash
$ mv draft.txt final.txt
```

移动目录：

```bash
$ mv project /home/pete/Documents/
```

将所有文本文件移动到一个文件夹：

```bash
$ mv *.txt notes/
```

在移动大量文件前，可以用 `ls` 预览通配符匹配的文件。

### 常见问题

**mv 会复制文件吗？** 不会。`mv` 是移动或重命名原始项目。

**mv 会覆盖文件吗？** 会。使用 `mv -i` 先询问，或用 `mv -n` 避免覆盖。

**移动目录需要 mv -r 吗？** 不需要。`mv` 默认支持移动目录，无需 `-r`。

## Exercise

熟能生巧！动手实践对于掌握像 `mv` 这样的 Linux 命令至关重要。这些实验将帮助你在真实环境中巩固移动和重命名文件及目录的理解：

1. **[Linux mv 命令：文件移动与重命名](https://labex.io/zh/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - 练习使用 `mv` 命令移动和重命名文件及目录，理解其各种选项和行为。
2. **[组织文件和目录](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 在实际挑战中应用 `mv`（以及 `cp` 和 `rm`）知识，整理项目结构，移动文件并清理目录。

这些实验将帮助你在真实场景中应用概念，增强使用 `mv` 命令管理文件和目录的信心。

## Quiz Question

使用 `mv` 命令，如何将名为 `cat` 的文件重命名为 `dog`？请提供完整命令。注意：答案区分大小写，应以小写英文输入。

## Quiz Answer

mv cat dog
