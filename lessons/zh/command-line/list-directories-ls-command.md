---
index: 4
lang: "zh"
title: "ls（列出目录）"
meta_title: "ls（列出目录）- 命令行"
meta_description: "通过示例学习 Linux ls 命令，包括列出文件、隐藏文件、长格式输出、人类可读大小、排序和组合选项。"
meta_keywords: "ls 命令, linux ls, 列出文件 linux, 列出目录, ls -a, ls -l, ls -lh, ls -r, 隐藏文件"
---

## Lesson Content

既然我们知道如何在文件系统中移动，如何确定有哪些内容可用呢？`ls` 命令列出文件和目录，让你检查当前所在位置或其他路径的内容。

### ls 命令的基本用法

默认情况下，`ls` 命令会列出当前目录中的目录和文件。不过，你也可以指定路径来列出其他目录的内容。

```bash
$ ls
$ ls /home/pete
```

你也可以列出一个特定的文件：

```bash
$ ls /etc/hosts
/etc/hosts
```

### 查看隐藏文件

并非目录中的所有文件默认都可见。在 Linux 中，以点号（`.`）开头的文件名是隐藏的。你可以使用 `-a` 选项查看它们，`-a` 代表 all（全部）。

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

### 获取详细信息

另一个重要的 `ls` 选项是 `-l`，表示长格式。它显示文件权限、链接数、所有者、组、大小、修改时间和名称。

```bash
$ ls -l
```

下面是输出示例：

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

为了更易读的文件大小，可以加上 `-h`，表示人类可读格式：

```bash
$ ls -lh
```

### 反向排序

有时你可能想改变排序顺序。`-r` 选项会以反向顺序列出文件和目录。

```bash
$ ls -r
```

你可以先用 `-t` 按修改时间排序，再用 `-r` 反转顺序：

```bash
$ ls -lt
$ ls -ltr
```

### 组合命令选项

命令有标志，也叫选项，用来增加功能。正如我们看到的 `-a` 和 `-l`，你可以将它们组合成一个命令，比如 `ls -la`。选项的顺序通常无关紧要，所以 `ls -al` 也一样。

```bash
$ ls -la
```

常用组合包括：

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

### 常用 ls 选项

- `-a`：显示所有文件，包括隐藏文件。
- `-l`：使用长格式。
- `-h`：配合 `-l` 显示人类可读大小。
- `-r`：反转排序顺序。
- `-t`：按修改时间排序。
- `-S`：按文件大小排序。
- `-d`：列出目录本身，而非其内容。

### 常见问题

**为什么有些文件名以点号开头？** 点文件默认是隐藏的，通常存储配置，如 `.bashrc`。

**如何只列出目录本身？** 使用 `ls -d directory/`。

**如何让最新的文件显示在最后？** 使用 `ls -ltr`。

**为什么 ls 会显示颜色？** 许多系统通过别名或环境设置配置了 `ls` 以颜色区分文件类型。

## Exercise

熟能生巧！这里有一个动手实验，帮助你巩固对 `ls` 命令的理解：

- **[Linux ls Command: Content Listing](https://labex.io/zh/labs/linux-linux-ls-command-content-listing-219205)** - 练习使用 `ls` 命令高效列出和分析文件及目录内容。你将学习详细列表、隐藏文件显示、人类可读大小和排序技巧等多种选项，提升命令行技能。

此实验将帮助你在真实场景中应用概念，增强 Linux 目录列表操作的信心。

## Quiz Question

你会使用什么命令查看隐藏文件？请用英文回答，注意大小写。

## Quiz Answer

ls -a
