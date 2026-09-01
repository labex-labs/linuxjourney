---
lesson_id: "change-directory-cd-command"
course_id: "command-line"
lang: "zh"
order_index: 3
title: "cd（切换目录）"
description: "学习使用 cd 配合路径和快捷方式在 Linux 文件系统中移动。"
meta_title: "cd（切换目录）- 命令行"
meta_description: "通过示例学习 Linux cd 命令，包括绝对路径、相对路径、主目录快捷方式、父目录和上一个目录的导航。"
meta_keywords: "cd 命令, linux cd 命令, 切换目录, cd 父目录, cd 主目录, cd 上一个目录, 绝对路径, 相对路径"
---

在 Linux 文件系统中移动时，你需要使用路径来指定目标位置。主要工具是 `cd` 命令，意为切换目录。它会更改 shell 当前的工作目录。

目标必须是目录而不是普通文件。如果目录不存在、名称输入错误，或你没有进入权限，`cd` 会报告错误，而不会改变位置。

基本语法是：

```bash
cd [DIRECTORY]
```

## 理解路径

指定路径有两种方式：绝对路径和相对路径。

- **绝对路径**：从根目录（`/`）开始的完整路径。例如：`/home/pete/Desktop`。

- **相对路径**：基于你当前所在位置的路径。如果你在 `/home/pete/Documents`，想访问名为 `taxes` 的子目录，可以使用 `taxes/`。

:::single-choice{#recognize-absolute-cd-path} 以下哪项正确描述了绝对路径？

::option[它从 shell 当前所在的目录开始]{#begins-at-current-directory explanation="依赖 shell 当前位置的路径是相对路径，不一定从根目录开始。"}
::option[它只包含最终目录名，不含父目录]{#contains-final-name-only explanation="单个目标名称通常会相对于当前目录解释；绝对路径包含从 `/` 开始的完整路线。"}
::option[它从以 `/` 表示的根目录开始]{#begins-at-root .correct explanation="绝对路径从文件系统根目录开始；开头的 `/` 使其起点不受当前目录影响。"}
:::

## 使用 cd 命令

要使用绝对路径切换到特定目录，输入：

```bash
$ cd /home/pete/Pictures
```

此命令会直接切换到 `Pictures` 目录。

你可以用 `pwd` 确认你的位置：

```bash
$ pwd
/home/pete/Pictures
```

:::single-choice{#verify-changed-directory} 执行 `cd` 后，哪个命令可以确认 shell 当前所在的位置？

::option[`cd`]{#cd-command explanation="`cd` 会改变当前目录，但通常不打印结果的完整路径；应使用 `pwd` 进行确认。"}
::option[`ls`]{#ls-command explanation="`ls` 显示目录内容，可以帮助查看当前位置，但报告位置本身的是 `pwd`。"}
::option[`pwd`]{#pwd-command .correct explanation="`pwd` 打印当前工作目录，可用于确认 `cd` 把 shell 移到了哪里。"}
:::

## 进入子目录

如果你已经在某个目录，想进入子目录，可以使用相对路径。例如，当前目录是 `/home/pete/Pictures`，其中有一个名为 `Hawaii` 的文件夹，你可以这样进入：

```bash
$ cd Hawaii
```

注意我们只用了文件夹名，因为我们已经在它的父目录 `/home/pete/Pictures` 中。

## 重要的导航快捷方式

使用完整路径导航可能很繁琐。幸运的是，shell 提供了几个快捷方式，让移动更快。

- `.`（当前目录）：表示你当前所在的目录。
- `..`（父目录）：向上一级，进入包含当前目录的目录。
- `~`（主目录）：指向你的个人主目录，比如 `/home/pete`。
- `-`（上一个目录）：返回你之前所在的目录。

你可以和 `cd` 一起使用这些快捷方式：

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

:::single-choice{#move-to-parent-directory} 从 `/home/pete/Pictures` 出发，哪个命令会移动到 `/home/pete`？

::option[`cd .`]{#cd-current explanation="`.` 表示当前目录，因此这个命令会让 shell 留在 `/home/pete/Pictures`。"}
::option[`cd -`]{#cd-previous explanation="`-` 返回上一个工作目录，而它不一定是父目录；目标在上一级时应使用 `..`。"}
::option[`cd ..`]{#cd-parent .correct explanation="`..` 表示当前目录的父目录；`Pictures` 的父目录是 `/home/pete`。"}
:::

:::single-choice{#return-to-previous-directory} 哪个命令会返回当前目录之前刚使用过的目录？

::option[`cd -`]{#previous-directory .correct explanation="`cd -` 会切换到上一个工作目录，而这个目录可以位于文件系统中的任何位置。"}
::option[`cd ..`]{#parent-directory explanation="`cd ..` 移动到父目录；父目录与上一个访问的目录不一定相同。"}
::option[`cd ~`]{#home-directory explanation="`cd ~` 移动到主目录，不会追踪此前刚访问的目录。"}
:::

多练习这些快捷方式，可以让你在命令行中更高效。

## 实用 cd 示例

进入你的主目录：

```bash
$ cd
```

不带目录参数运行 `cd` 也会进入主目录。

向上两级：

```bash
$ cd ../..
```

进入包含空格的目录名，使用引号：

```bash
$ cd "Vacation Photos"
```

:::single-choice{#enter-directory-with-spaces} 哪个命令会把 `Vacation Photos` 视为一个目录名？

::option[`cd Vacation Photos`]{#unquoted-directory-name explanation="没有引号时，shell 会把 `Vacation` 和 `Photos` 作为两个独立参数，而不是一个目录名。"}
::option[`"cd Vacation Photos"`]{#quote-entire-command explanation="给整行加引号会让 shell 把它视为一个命令名；命令本身必须放在路径引号外。"}
::option[`cd "Vacation Photos"`]{#quote-directory-name .correct explanation="引号把两个单词组合成传递给 `cd` 的一个路径参数。"}
:::

返回上一个目录：

```bash
$ cd -
/home/pete/Documents
```

要巩固对 Linux 目录导航的理解，可以尝试以下动手实验：

1. **[Linux cd 命令：切换目录](https://labex.io/zh/labs/linux-linux-cd-command-directory-changing-209733)** - 学习使用 `cd` 高效导航文件系统，包括切换目录、理解路径和探索文件结构的多种技巧。
2. **[Linux 目录导航](https://labex.io/zh/labs/linux-directory-navigation-387844)** - 使用基础命令在目录之间移动，检验你的 Linux 命令行技能。
3. **[搭建新项目结构](https://labex.io/zh/labs/linux-setting-up-a-new-project-structure-387859)** - 创建指定的项目结构，并使用 `mkdir`、`cd` 等命令在其中导航。

## 总结

现在，你可以使用 `cd` 配合完整路径和 shell 快捷方式在目录之间移动。

1. 区分绝对路径和相对路径。
2. 切换目录，并用 `pwd` 验证结果。
3. 移动到父目录、主目录和上一个目录。
4. 进入名称中包含空格的目录。
5. 识别常见的路径和权限错误。
