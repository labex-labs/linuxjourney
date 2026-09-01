---
lesson_id: "make-directory-mkdir-command"
course_id: "command-line"
lang: "zh"
order_index: 12
title: "mkdir（创建目录）"
description: "学习使用 mkdir 选项创建单个、多个和嵌套目录。"
meta_title: "mkdir（创建目录）- 命令行"
meta_description: "通过示例学习 Linux mkdir 命令，包括创建单个目录、多个目录、嵌套父目录以及设置权限。"
meta_keywords: "mkdir 命令, linux mkdir, 创建目录 linux, 创建文件夹 linux, mkdir -p, mkdir -m, 创建文件夹"
---

`mkdir` 是“make directory”的缩写，用于创建目录，以便组织文件和其他目录。

基本语法是：

```bash
mkdir [OPTIONS] DIRECTORY...
```

## 创建单个目录

`mkdir` 最基本的用法是创建一个新的目录。如果该目录尚不存在，此命令将在您当前的位置创建它。

```bash
$ mkdir documents
```

如果名为 `documents` 的条目已经存在，`mkdir` 会报告错误，而不会替换它。可以用 `ls -ld documents` 检查现有条目。

:::single-choice{#create-one-directory} 哪个命令会在当前工作目录中创建名为 `documents` 的目录？

::option[`mkdir documents`]{#mkdir-documents .correct explanation="`mkdir` 会在相对路径 `documents` 处创建所需目录。"}
::option[`touch documents`]{#touch-documents explanation="路径缺失时，`touch` 创建的是空的普通文件，而不是目录。"}
::option[`cd documents`]{#cd-documents explanation="`cd` 会尝试进入现有目录，并不会创建缺失目录。"}
:::

## 创建多个目录

您也可以一次创建多个目录，只需用空格分隔它们的名称。这是快速设置多个文件夹的高效方法。

```bash
$ mkdir books paintings
```

:::single-choice{#create-separate-directories} 哪个命令会创建两个同级目录 `books` 和 `paintings`？

::option[`mkdir books/paintings`]{#nested-paintings explanation="这个路径表示 `books` 中的 `paintings`，而不是两个同级目录；如果 `books` 不存在还会失败。"}
::option[`mkdir "books paintings"`]{#spaced-directory explanation="引号会把两个单词组合成一个路径，因此只会请求创建一个名称中含空格的目录。"}
::option[`mkdir books paintings`]{#two-directories .correct explanation="分别提供两个操作数，会让 `mkdir` 创建 `books` 和 `paintings` 两个目录。"}
:::

## 创建缺失的父目录

有时您需要同时创建一个目录及其父目录。`-p` 选项非常适合此用途。它可以防止当父目录不存在时出现错误。

```bash
$ mkdir -p books/hemingway/favorites
```

这会创建路径中所有缺失的部分。如果最终目录已经存在，它也不会仅因此报告错误；但权限不足等其他错误仍可能发生。

:::single-choice{#create-nested-path} `projects/app/src` 中的目录都还不存在。哪个命令会创建完整路径？

::option[`mkdir -p projects/app/src`]{#mkdir-parents .correct explanation="`-p` 会先创建每个缺失的父目录，再创建最终目录。"}
::option[`mkdir projects/app/src`]{#mkdir-no-parents explanation="不使用 `-p` 时，如果中间目录不存在，`mkdir` 就无法创建 `src`。"}
::option[`mkdir -m projects/app/src`]{#mkdir-mode-missing explanation="`-m` 需要一个模式参数，而且不会要求创建缺失的父目录。"}
:::

## 设置初始模式

使用 `-m` 选项可以在创建目录时设置权限。

```bash
$ mkdir -m 755 public
```

你将在后续课程中学习权限模式。本例中的 `755` 让所有者拥有读、写和搜索权限，让组和其他用户拥有读与搜索权限。

添加 `-v` 可以为每个新建目录打印一条消息：

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

:::single-choice{#set-directory-mode} 哪个命令会创建权限模式为 `755` 的 `public`？

::option[`mkdir -p 755 public`]{#parents-755 explanation="`-p` 会把剩余单词视为目录路径，因此不会把 `755` 设置为权限模式。"}
::option[`mkdir -v 755 public`]{#verbose-755 explanation="`-v` 会打印创建消息，并不会把 `755` 解释为权限模式。"}
::option[`mkdir -m 755 public`]{#mode-public .correct explanation="`-m` 接受所需模式，`public` 则是要创建的目录路径。"}
:::

要练习创建和组织目录，可以尝试以下动手实验：

1. **[Linux mkdir 命令：目录创建](https://labex.io/zh/labs/linux-linux-mkdir-command-directory-creating-209739)** - 学习如何在 Linux 中使用 `mkdir` 命令创建目录、设置权限并组织文件系统。本实验涵盖基础和高级用法，包括创建嵌套目录。
2. **[搭建新项目结构](https://labex.io/zh/labs/linux-setting-up-a-new-project-structure-387859)** - 通过创建特定项目结构并使用 `mkdir` 和 `cd` 等基本命令导航，练习您的 Linux 目录管理技能。

## 总结

现在，你可以使用明确的名称、父目录和模式创建目录结构。

1. 用一条命令创建一个或多个目录。
2. 识别由现有路径引起的错误。
3. 使用 `-p` 创建缺失的父目录。
4. 使用 `-m` 设置新目录的模式。
