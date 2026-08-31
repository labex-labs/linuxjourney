---
lesson_id: "vim-text-editor"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 3
title: "Vim（Vi Improved）"
description: "了解 Vim 是什么、它与 vi 的关系，以及如何打开文件、帮助和引导式练习。"
meta_title: "Vim (Vi 改进版) - 高级文本编辑术"
meta_description: "探索 Vim，这款强大的轻量级文本编辑器，又称 vi improved。本教程将介绍 Vim vi improved 的基础知识，它是大多数 Linux 系统预装的工具。"
meta_keywords: "Vim, vi improved, vim vi improved, Linux 文本编辑器，Vim 教程，Vi 编辑器，vim 改进版，Linux 命令"
---

Vim 是一款可配置的文本编辑器，其名称意为 **Vi Improved**。它保留了与原始 `vi` 编辑器相关的模态编辑模型，并增加了多级撤销、语法支持、脚本和丰富的帮助系统等功能。

## Vim 与 vi 的关系

`vi` 既指一款历史悠久的编辑器，也指一种常见的命令界面。在某个 Linux 系统上，`vi` 可能会以偏兼容模式启动 Vim；在另一个系统上，它可能启动不同的 vi 实现。不要假设每个 `vi` 命令都提供全部 Vim 功能。

检查当前 shell 的解析结果：

```bash
$ command -v vim
/usr/bin/vim
$ command -v vi
/usr/bin/vi
```

仅凭解析出的路径，无法判断 `vi` 和 `vim` 是否是同一实现。`type -a vi vim` 和编辑器的版本输出可以提供更多细节。

:::single-choice{#vim-name-origin}
Vim 这个名称是什么意思？

::option[Visual Input Manager]{#vim-visual-input explanation="这不是该编辑器名称的来源。"}
::option[Virtual Interface Mode]{#vim-virtual-interface explanation="Vim 确实使用模式，但这个短语并不是其名称的含义。"}
::option[Vi Improved]{#vim-vi-improved .correct explanation="Vim 最初是一款改进的 vi 兼容编辑器，其名称体现了这一点。"}
:::

:::single-choice{#vim-check-command}
哪个命令会检查 Bash 当前能否解析名称 `vim`？

::option[`vim --create`]{#vim-create-option explanation="这不是 shell 解析检查，也不是安装或发现 Vim 的方式。"}
::option[`command -v vim`]{#vim-command-resolution .correct explanation="如果该名称可用，这个 shell 内建命令会报告将要使用的命令。"}
::option[`file ~/.vimrc`]{#vim-file-vimrc explanation="这只会检查一个可能存在的配置文件，不能确定 Vim 可执行程序是否可用。"}
:::

## 打开 Vim 和文件

使用未命名缓冲区启动 Vim：

```bash
$ vim
```

传入路径名以编辑该文件：

```bash
$ vim filename.txt
```

如果 `filename.txt` 已存在且可读，Vim 会把内容加载到缓冲区中。如果路径不存在，Vim 会打开一个与该名称关联的新缓冲区；只有成功写入缓冲区时才会创建文件。

Vim 不会绕过文件系统权限。能够打开文件并不保证当前账户可以把更改保存到该路径。

:::single-choice{#vim-open-missing-path}
当 `vim draft.txt` 指定的路径还不存在时，通常会发生什么？

::option[Vim 打开一个新缓冲区，只有写入时才创建文件。]{#vim-new-buffer .correct explanation="缓冲区会记住路径名，但磁盘文件会延迟到成功保存时才创建。"}
::option[Vim 在打开界面前立即在磁盘上创建空文件。]{#vim-immediate-create explanation="新缓冲区会与路径名关联，但只有成功写入后才创建文件。"}
::option[Vim 拒绝启动，因为每个路径名都必须已经存在。]{#vim-refuse-missing explanation="Vim 可以为不存在的路径打开新缓冲区，让你编写新文件。"}
:::

## 使用内置学习资源

如果 Vim 安装包含 `vimtutor`，可从 shell 运行它来开始交互式练习课程：

```bash
$ vimtutor
```

在 Vim 中，按 `Esc` 进入普通模式，输入 `:help` 并按 Enter 打开帮助系统。命令后还可以跟特定主题：

```vim
:help user-manual
:help :write
```

帮助标签非常精确，所以标点符号可能很重要。在帮助链接上使用 `Ctrl+]` 可跟随链接，使用 `Ctrl+T` 返回。

:::single-choice{#vim-guided-tutorial}
安装了 Vim 引导教程时，哪个 shell 命令会启动它？

::option[`vim --quiz`]{#vim-quiz-option explanation="Vim 不使用该选项作为其标准引导教程界面。"}
::option[`vimtutor`]{#vim-tutor-command .correct explanation="`vimtutor` 会打开交互式教程的副本，以便安全地动手练习。"}
::option[`help vim`]{#vim-shell-help explanation="Bash 的 `help` 记录 shell 内建命令，不会启动 Vim 交互式教程。"}
:::

## 使用可丢弃文件练习

请从自己拥有的目录中的文件开始：

```bash
$ printf 'alpha\nbeta\n' > vim-practice.txt
$ vim vim-practice.txt
```

后续课程会介绍搜索、导航、插入、编辑和保存。在你学会安全离开之前，请记住 `Esc` 会返回普通模式，而输入 `:q!` 后按 Enter 会放弃当前窗口中未保存的更改。只有确实想丢弃这些更改时才使用该命令。

:::single-choice{#vim-abandon-practice-changes}
在可丢弃的练习文件中，哪个 Vim 命令会退出当前窗口并丢弃未保存的更改？

::option[`:w`]{#vim-write-only explanation="`:w` 会写入缓冲区，但不会退出当前窗口。"}
::option[`:wq`]{#vim-write-quit explanation="`:wq` 会先保存更改再退出，因此不会丢弃它们。"}
::option[`:q!`]{#vim-quit-force .correct explanation="`!` 会让 Vim 忽略缓冲区已修改的警告，退出且不写入这些更改。"}
:::

要练习使用 Vim 打开、编辑和保存文件，可以尝试以下动手实验：

1. **[在 Linux 中使用 Vim 和 Nano 编辑文本文件](https://labex.io/zh/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 在真实 Linux 环境中使用 Vim 和 Nano 练习创建文件、编辑文本、保存文件和导航。

## 总结

现在，你可以识别 Vim、打开缓冲区并找到安全的学习资源。

1. 说明 Vim 与 vi 的关系，同时不假定具体实现。
2. 检查 `vim` 命令是否可用。
3. 打开已有文件或新的具名缓冲区。
4. 启动 `vimtutor` 或打开 Vim 内置帮助。
5. 只在确实需要时放弃未保存的练习更改。
