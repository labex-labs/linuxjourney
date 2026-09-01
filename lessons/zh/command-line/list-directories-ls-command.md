---
lesson_id: "list-directories-ls-command"
course_id: "command-line"
lang: "zh"
order_index: 4
title: "ls（列出目录）"
description: "学习使用 ls 选项查看文件、隐藏条目、详细信息、大小和排序顺序。"
meta_title: "ls（列出目录）- 命令行"
meta_description: "通过示例学习 Linux ls 命令，包括列出文件、隐藏文件、长格式输出、人类可读大小、排序和组合选项。"
meta_keywords: "ls 命令, linux ls, 列出文件 linux, 列出目录, ls -a, ls -l, ls -lh, ls -r, 隐藏文件"
---

既然我们知道如何在文件系统中移动，如何确定有哪些内容可用呢？`ls` 命令列出文件和目录，让你检查当前所在位置或其他路径的内容。

## ls 命令的基本用法

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

:::single-choice{#list-another-directory} 哪个命令可以在不进入 `/home/pete` 的情况下列出其内容？

::option[`ls /home/pete`]{#ls-target-path .correct explanation="向 `ls` 传入目录路径会列出该目录的内容，而 shell 仍停留在当前工作目录。"}
::option[`cd /home/pete`]{#cd-target-path explanation="`cd` 会改变 shell 的工作目录，本身不会执行所需的内容列举。"}
::option[`pwd /home/pete`]{#pwd-target-path explanation="`pwd` 报告当前工作目录，不接受要列举的目标；应把路径传给 `ls`。"}
:::

## 查看隐藏文件

并非目录中的所有文件默认都可见。在 Linux 中，以点号（`.`）开头的文件名是隐藏的。你可以使用 `-a` 选项查看它们，`-a` 代表 all（全部）。

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

点文件默认隐藏，常用于保存 `.bashrc` 等配置。

:::single-choice{#show-hidden-files} 哪个命令会在列表中包含隐藏文件？

::option[`ls -l`]{#long-format explanation="`-l` 会添加详细信息列，但本身不会包含隐藏名称。"}
::option[`ls -r`]{#reverse-order explanation="`-r` 会反转排序顺序，并不改变是否包含隐藏文件。"}
::option[`ls -a`]{#all-files .correct explanation="`-a` 表示 all，因此 `ls` 会包含以点号开头的名称。"}
:::

## 获取详细信息

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

:::single-choice{#show-readable-file-details} 哪个命令会显示长格式详情和易读的大小？

::option[`ls -la`]{#long-all explanation="它组合了长格式和隐藏文件，但没有要求使用易读的大小单位。"}
::option[`ls -lh`]{#long-human-readable .correct explanation="`-l` 选择长格式，`-h` 让大小更易读；两个标志可以组合在一个命令中。"}
::option[`ls -ltr`]{#long-time-reverse explanation="它组合了长格式、按修改时间排序和反向顺序，但不包含 `-h` 大小选项。"}
:::

## 反向排序

有时你可能想改变排序顺序。`-r` 选项会以反向顺序列出文件和目录。

```bash
$ ls -r
```

你可以先用 `-t` 按修改时间排序，再用 `-r` 反转顺序：

```bash
$ ls -lt
$ ls -ltr
```

:::single-choice{#show-newest-files-last} 哪个命令按修改时间排序，并把最新条目放在最后？

::option[`ls -ltr`]{#time-reversed .correct explanation="`-t` 按修改时间排序，`-r` 再反转顺序；组合后旧条目会排在新条目前面。"}
::option[`ls -lt`]{#time-default explanation="它会按修改时间排序，但保留默认的最新优先顺序，不会把最新条目放在最后。"}
::option[`ls -lr`]{#reverse-name-order explanation="它使用长格式并反转默认的名称排序；没有 `-t` 时，修改时间不会决定顺序。"}
:::

## 组合命令选项

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

## 常用 ls 选项

- `-a`：显示所有文件，包括隐藏文件。
- `-l`：使用长格式。
- `-h`：配合 `-l` 显示人类可读大小。
- `-r`：反转排序顺序。
- `-t`：按修改时间排序。
- `-S`：按文件大小排序。
- `-d`：列出目录本身，而非其内容。

:::single-choice{#list-directory-entry-itself} 哪个命令会列出 `projects/` 目录条目本身，而不是其中的内容？

::option[`ls -d projects/`]{#directory-entry .correct explanation="`-d` 选项让 `ls` 显示目录条目本身，而不是打开目录列出内容。"}
::option[`ls projects/`]{#directory-contents explanation="不使用 `-d` 时，把目录路径传给 `ls` 会显示该目录中的条目。"}
::option[`cd projects/`]{#change-to-directory explanation="`cd` 会改变工作目录，并不会列出这里要求的目录条目。"}
:::

有些系统会针对不同文件类型用不同颜色显示 `ls` 输出。这通常来自别名或环境设置，因此系统之间的颜色可能不同。

要巩固对 `ls` 命令的理解，可以尝试这个动手实验：

- **[Linux ls Command: Content Listing](https://labex.io/zh/labs/linux-linux-ls-command-content-listing-219205)** - 练习使用 `ls` 命令高效列出和分析文件及目录内容。你将学习详细列表、隐藏文件显示、人类可读大小和排序技巧等多种选项，提升命令行技能。

## 总结

现在，你可以使用 `ls` 查看目录内容，并控制条目的显示方式。

1. 列出当前目录或其他路径。
2. 在列表中包含隐藏文件。
3. 显示带有易读大小的详细信息。
4. 按修改时间反向排列条目。
5. 只列出目录条目而不列出其内容。
