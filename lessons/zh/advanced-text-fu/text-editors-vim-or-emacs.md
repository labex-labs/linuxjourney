---
lesson_id: "text-editors-vim-or-emacs"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 2
title: "文本编辑器"
description: "学习如何为 Linux 管理和开发选择及配置终端文本编辑器。"
meta_title: "文本编辑器 - 高级文本技巧"
meta_description: "了解 Linux 文本编辑器，如 Vim 和 Emacs。探索它们的用途以及对系统导航的重要性。开始你的 Linux 文本编辑器之旅！"
meta_keywords: "Linux 文本编辑器，Vim, Emacs, Linux 命令，Linux 教程，Linux 初学者，Linux 指南"
---

Linux 配置、脚本、源代码和日志通常以纯文本形式存储。终端编辑器让你可以在本地终端、远程 SSH 会话或没有图形桌面的环境中处理这些文件。

## 根据环境选择编辑器

没有哪一种编辑器适合所有人和所有任务。图形编辑器、终端编辑器和集成开发环境都可能是合适的选择。进行命令行工作时，应选择已经安装、能够安全退出，而且你理解其基本编辑模式的编辑器。

不要假设 Vim 或 Emacs 已经安装。请检查当前 shell 中的命令解析结果：

```bash
$ command -v vim
/usr/bin/vim
$ command -v emacs
/usr/bin/emacs
```

如果结果为空且状态非零，表示当前命令搜索路径中没有找到该名称。精简系统可能只提供 `vi`，其他系统可能包含 Nano，也可能完全没有交互式编辑器。

:::single-choice{#editors-check-availability}
哪个命令会检查当前 shell 能否解析名为 `vim` 的可执行程序？

::option[`vim --install`]{#editors-vim-install explanation="Vim 不使用该命令作为可移植的安装检查，软件包安装方式也因发行版而异。"}
::option[`file ~/.vimrc`]{#editors-file-vimrc explanation="如果该配置路径存在，此命令只会判断它的文件类型，不能确定 `vim` 是否可解析。"}
::option[`command -v vim`]{#editors-command-v-vim .correct explanation="这个 shell 内建命令会检查命令解析，并在可用时输出解析结果。"}
:::

## 理解 Vim 的模型

Vim 是模态编辑器。同一个按键会根据当前模式产生不同含义：

- 普通模式把按键解释为导航和编辑命令。
- 插入模式会插入输入的文本。
- 命令行模式接受写入或退出等命令。

经过练习后，这种模型可以提高重复键盘编辑的效率，但新用户必须留意当前模式。后续课程会逐项介绍 Vim 操作。

:::single-choice{#editors-vim-modal-meaning}
Vim 是模态编辑器意味着什么？

::option[每个文件都会在独立的图形窗口中打开。]{#editors-vim-windows explanation="窗口和缓冲区是不同概念；模态指的是按键行为会随编辑器状态改变。"}
::option[Vim 一次只能编辑一种文本文件。]{#editors-vim-file-type explanation="Vim 支持许多文件类型；模态描述的是交互模型，而不是文件限制。"}
::option[按键会根据当前模式执行不同操作。]{#editors-vim-modes .correct explanation="例如，同一按键在普通模式中可能执行命令，在插入模式中则会插入文本。"}
:::

## 理解 Emacs 的模型

Emacs 通常在可扩展环境中使用组合键和具名命令。文件会在缓冲区中访问，主模式和次模式可以为不同内容和任务自定义行为。Emacs 既能在终端中运行，也能在图形窗口中运行。

Vim 和 Emacs 都可以通过配置和扩展实现远超基础编辑的功能。添加自定义设置前，请先学会打开、更改、保存和关闭纯文本文件。

:::single-choice{#editors-emacs-buffer}
在 Emacs 术语中，所访问文件的可编辑文本通常保存在哪里？

::option[缓冲区中。]{#editors-emacs-buffer-answer .correct explanation="Emacs 会在缓冲区中访问文件，缓冲区保存正在查看或编辑的文本。"}
::option[shell 的别名表中。]{#editors-emacs-alias-table explanation="别名属于 shell 命令解析，不会存储编辑器文本。"}
::option[只保存在终端回滚区中。]{#editors-emacs-scrollback explanation="终端回滚区记录已显示的输出，而 Emacs 在缓冲区中管理可编辑文本。"}
:::

## 设置首选编辑器

许多命令行程序需要启动编辑器时会查询 `VISUAL` 或 `EDITOR`。例如，在当前 Bash 会话及其子进程中为命令选择 Vim：

```bash
$ export VISUAL=vim
$ export EDITOR="$VISUAL"
```

这些变量表达的是偏好，不会安装程序。请使用实际存在的命令，并在测试完成后再把这些 export 放入合适的 shell 启动文件。

:::single-choice{#editors-editor-variable}
`export EDITOR=vim` 会做什么？

::option[告诉之后的子进程，首选编辑器的值是 `vim`。]{#editors-export-preference .correct explanation="export 会把该偏好放入当前 shell 启动的命令所继承的环境中。"}
::option[为系统上的每个用户安装 Vim。]{#editors-install-vim explanation="环境变量赋值不会安装软件包，也不会改变其他用户的系统。"}
::option[让每个程序都采用 Vim 的按键绑定。]{#editors-global-bindings explanation="程序可能查询该变量来启动编辑器，但它不会替换程序自身的交互模型。"}
:::

## 在不危及重要文件的情况下练习

请在自己拥有的目录中使用可丢弃文件学习：

```bash
$ printf 'first line\nsecond line\n' > editor-practice.txt
$ vim editor-practice.txt
```

不要从系统配置或其他用户的数据开始练习。更改重要文件前应先制作备份，理解如何保存和退出，并使用 `cat` 或 `diff` 等只读命令检查结果。

:::single-choice{#editors-first-practice-file}
第一次练习不熟悉的编辑器时，哪种文件最安全？

::option[以 root 身份打开的关键启动配置文件。]{#editors-boot-file explanation="意外更改可能导致系统无法正常启动，而提升的访问权限会放大错误影响。"}
::option[自己拥有的目录中的可丢弃文本文件。]{#editors-disposable-file .correct explanation="练习文件可以在学习导航、保存和退出时限制意外编辑带来的后果。"}
::option[没有备份的共享生产文件。]{#editors-production-file explanation="在共享数据上进行未经检查的练习可能影响他人，也没有简单的恢复途径。"}
:::

要练习在终端中打开、编辑和保存文本文件，可以尝试以下动手实验：

1. **[使用 Vim 和 Nano 在 Linux 中编辑文本文件](https://labex.io/zh/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 练习使用 vi/vim 和 nano 创建文件、编辑文本、保存文件及导航，这些都是 Linux 用户的重要技能。

## 总结

现在，你可以选择终端编辑器，并准备安全的练习流程。

1. 检查编辑器命令是否可用。
2. 认识 Vim 的模态交互模型。
3. 认识 Emacs 的缓冲区和可扩展模式。
4. 设置编辑器偏好，同时不要把它误认为安装操作。
5. 编辑重要文件前，先使用可丢弃文本练习。
