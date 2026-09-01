---
lesson_id: "emacs-text-editor"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 9
title: "Emacs"
description: "学习如何启动 Emacs、理解其按键记法，以及区分缓冲区、窗口和框架。"
meta_title: "Emacs - 高级文本技巧"
meta_description: "学习 Emacs，一个功能强大且可扩展的 Linux 文本编辑器。了解 Emacs 缓冲区和基本用法。立即开始你的 Emacs 之旅！"
meta_keywords: "Emacs, Linux 文本编辑器，Emacs 教程，Emacs 缓冲区，Linux 命令，初学者，指南"
---

GNU Emacs 是一款可扩展的文本编辑器，可以使用 Emacs Lisp 自定义其行为。它支持纯文本编辑、编程模式、文件与缓冲区管理，以及许多可选软件包。你可以学习其核心编辑命令，而不必采用所有扩展。

## 检查并启动 Emacs

不要假设 Emacs 已经安装。请检查 shell 如何解析它：

```bash
$ command -v emacs
/usr/bin/emacs
```

以正常的显示选择方式启动 Emacs：

```bash
$ emacs
```

在图形会话中，这可能创建图形框架。如果 Emacs 应留在当前终端中，请使用 `-nw`，即不使用窗口系统：

```bash
$ emacs -nw
```

:::single-choice{#emacs-terminal-start} 哪个命令会在当前终端中启动 Emacs，而不使用图形窗口系统？

::option[`emacs -w`]{#emacs-window-option explanation="这不是本课介绍的无窗口系统形式。"}
::option[`emacs -nw`]{#emacs-no-window .correct explanation="`-nw` 选项告诉 Emacs 不使用图形窗口系统，而是在终端上运行。"}
::option[`command -v emacs`]{#emacs-check-only explanation="这只会检查命令解析，并不会启动编辑器。"}
:::

## 打开文件

启动 Emacs 时传入路径名即可访问文件：

```bash
$ emacs notes.txt
```

如果文件存在，Emacs 会把它读入缓冲区。如果文件不存在，Emacs 会创建与该路径关联的新缓冲区；只有成功保存后才会创建文件。文件系统权限仍决定写入能否成功。

:::single-choice{#emacs-open-file-buffer} 当 `notes.txt` 尚不存在时，`emacs notes.txt` 通常会做什么？

::option[打开与该路径关联的新缓冲区。]{#emacs-new-file-buffer .correct explanation="缓冲区可以保存 `notes.txt` 的新文本，实际文件则延迟到保存时才创建。"}
::option[在编辑器启动前先在磁盘上创建文件。]{#emacs-immediate-file explanation="Emacs 可以把新缓冲区与路径关联，而无需在成功保存前创建磁盘文件。"}
::option[拒绝启动，因为每个访问的文件都必须存在。]{#emacs-refuse-new-file explanation="Emacs 支持通过与缺失路径关联的缓冲区编写新文件。"}
:::

## 理解缓冲区、窗口和框架

Emacs 使用相互关联但彼此不同的对象：

- **缓冲区**保存文本或其他编辑器状态。所访问文件的内容位于缓冲区中。
- **窗口**是 Emacs 框架内显示缓冲区的区域。
- **框架**是 Emacs 的顶层显示，例如图形框架或终端框架。

多个缓冲区可以存在而不显示，两个窗口也可以显示同一个缓冲区。关闭窗口不一定会终止其缓冲区或删除文件。

:::single-choice{#emacs-buffer-definition} Emacs 缓冲区是什么？

::option[顶层图形应用框架。]{#emacs-buffer-frame explanation="框架是顶层显示对象；缓冲区保存编辑器内容或状态。"}
::option[保存可编辑文本或其他编辑器状态的对象。]{#emacs-buffer-content .correct explanation="所访问文件的内容和许多非文件视图都位于 Emacs 缓冲区中。"}
::option[包含之前命令的 shell 历史文件。]{#emacs-buffer-history explanation="shell 历史与 Emacs 缓冲区存储是彼此独立的。"}
:::

## 阅读 Emacs 按键记法

Emacs 文档使用简洁记法：

- `C-x` 表示按住 Control 再按 `x`。
- `M-x` 表示按住 Meta 再按 `x`；在现代终端和桌面中，Alt 通常充当 Meta。
- `C-x C-f` 是一个按键序列：先按 Control+x，再按 Control+f。

具体终端可能会拦截或重映射某些按键。先按 `Esc` 再按另一个键，通常可以替代 Meta 组合键。

:::single-choice{#emacs-key-sequence-notation} 如何输入写作 `C-x C-f` 的 Emacs 按键序列？

::option[按住 Control 按 `x`，再按住 Control 按 `f`。]{#emacs-control-x-f .correct explanation="每个 `C-` 前缀作用于紧随其后的按键，两个组合键按顺序输入。"}
::option[在缓冲区中输入字面字符 `C-x C-f`。]{#emacs-literal-key-text explanation="该记法描述的是控制键事件，而不是要插入的文本。"}
::option[把 Control、`x` 和 `f` 同时作为一个组合键按下。]{#emacs-simultaneous-x-f explanation="该记法包含两个连续组合键，而不是一个三键组合。"}
:::

## 启动内置教程

在 Emacs 中输入 `C-h t` 可打开交互式教程。它会在安全的练习缓冲区中教授移动、插入、保存和退出。`C-h` 是帮助前缀；`C-h C-h` 会显示如何使用帮助的说明。

如果 Emacs 显示菜单或欢迎缓冲区，教程仍比直接在重要文件上试验更适合作为结构化起点。

:::single-choice{#emacs-open-tutorial} 哪个 Emacs 按键序列会打开内置教程？

::option[`C-x C-s`]{#emacs-save-buffer explanation="该序列会保存当前缓冲区，不会打开教程。"}
::option[`C-x C-c`]{#emacs-exit-sequence explanation="该序列会开始退出 Emacs，而不是启动课程。"}
::option[`C-h t`]{#emacs-help-tutorial .correct explanation="帮助前缀 `C-h` 后跟 `t` 会启动 Emacs 教程。"}
:::

## 总结

现在，你可以启动 Emacs，并理解其基础界面概念。

1. 检查 `emacs` 命令是否可用。
2. 使用 `-nw` 选择图形或终端运行方式。
3. 在缓冲区中访问已有或新的路径。
4. 区分缓冲区、窗口和框架。
5. 阅读按键记法并打开内置教程。
