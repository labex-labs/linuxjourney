---
lesson_id: "emacs-manipulate-files"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 10
title: "Emacs 文件操作"
description: "学习如何在 Emacs 中访问、保存、重命名、重新载入和审查由文件支持的缓冲区。"
meta_title: "Emacs 文件操作 - 高级文本技巧"
meta_description: "学习 Emacs 文件操作：使用 C-x C-s、C-x C-w 和 C-x C-f 命令保存、另存为和打开文件。掌握基本的 Emacs 文件操作！"
meta_keywords: "Emacs, Emacs 保存文件，Emacs 打开文件，Emacs 教程，Linux 命令，Emacs 初学者，Emacs 指南"
---

Emacs 在缓冲区中访问文件。编辑会先改变缓冲区，保存则把当前内容写入关联路径。请阅读迷你缓冲区消息，因为权限、磁盘上的冲突更改或其他错误都可能阻止写入。

## 访问文件

使用运行 `find-file` 的 `C-x C-f`，然后在迷你缓冲区中输入路径并按 Enter：

```text
C-x C-f
```

Emacs 会在缓冲区中打开已有的可读文件；如果路径不存在，则准备一个访问新文件的缓冲区。对于后一种情况，只有成功保存后磁盘文件才会存在。

输入路径时可以使用 Tab 补全。访问目录通常会打开 Emacs 的目录编辑器 Dired，而不会把目录当作文本文件。

:::single-choice{#emacs-find-file-key}
哪个 Emacs 按键序列会提示输入路径并访问它？

::option[`C-x C-s`]{#emacs-file-save explanation="这会保存当前访问文件的缓冲区，不会提示访问另一个路径。"}
::option[`C-x C-c`]{#emacs-file-exit explanation="这会开始退出 Emacs，而不是打开文件。"}
::option[`C-x C-f`]{#emacs-find-file .correct explanation="它运行 `find-file`，在迷你缓冲区中提示输入要访问的路径。"}
:::

:::single-choice{#emacs-find-missing-file}
使用 `C-x C-f` 访问不存在的路径时，通常何时创建磁盘文件？

::option[只有成功保存新缓冲区后。]{#emacs-file-created-on-save .correct explanation="在任何文件存在之前，缓冲区就可以保存编辑内容，保存操作才会执行创建。"}
::option[输入路径后立即创建。]{#emacs-file-created-immediately explanation="Emacs 会先创建与新路径关联的缓冲区，磁盘文件的创建会延后。"}
::option[只有 Emacs 本身关闭后。]{#emacs-file-created-on-exit explanation="退出时可能提示保存，但文件创建取决于成功保存，而不一定取决于关闭 Emacs。"}
:::

## 保存当前缓冲区

使用运行 `save-buffer` 的 `C-x C-s` 保存当前访问文件的缓冲区：

```text
C-x C-s
```

如果缓冲区没有关联文件名，Emacs 会提示输入一个。成功写入会清除缓冲区的已修改标记；失败则会在缓冲区中保留未保存数据并报告错误。

:::single-choice{#emacs-save-current-buffer}
哪个按键序列会保存当前访问文件的缓冲区？

::option[`C-x C-s`]{#emacs-save-buffer-key .correct explanation="`C-x C-s` 会对当前缓冲区运行 `save-buffer`。"}
::option[`C-x C-w`]{#emacs-write-file-key explanation="这会提示输入另一个文件名，并改变该缓冲区访问的文件。"}
::option[`C-x s`]{#emacs-save-some-key explanation="这会检查多个访问文件的缓冲区，并提示是否保存，而不只针对当前缓冲区。"}
:::

## 使用其他名称写入

使用运行 `write-file` 的 `C-x C-w`，可以提示输入路径、把缓冲区写入该处，并让缓冲区改为访问这个新文件：

```text
C-x C-w
```

这就是 Emacs 的“另存为”行为。它与只写出一份副本、但继续访问原路径不同。

:::single-choice{#emacs-write-file-as}
哪个按键序列会对当前缓冲区执行通常的“另存为”操作？

::option[`C-x C-f`]{#emacs-find-file-other explanation="这会访问文件，可能切换到另一缓冲区；它不是当前缓冲区的另存为操作。"}
::option[`C-x k`]{#emacs-write-as-kill-buffer explanation="这会提示终止缓冲区，并可能询问未保存的更改；不会用新名称保存。"}
::option[`C-x C-w`]{#emacs-write-file-answer .correct explanation="`write-file` 会写入所选路径，并让缓冲区访问该文件。"}
:::

## 审查多个已修改缓冲区

使用运行 `save-some-buffers` 的 `C-x s` 检查已修改且访问文件的缓冲区：

```text
C-x s
```

Emacs 通常会询问是否保存每个符合条件的已修改缓冲区。请阅读缓冲区名称并谨慎回答；这不是无条件的全部保存快捷键。

:::single-choice{#emacs-save-some-buffers}
`C-x s` 通常会做什么？

::option[提示是否保存已修改且访问文件的缓冲区。]{#emacs-prompt-save-some .correct explanation="`save-some-buffers` 会审查符合条件的已修改缓冲区，并询问应写入哪些。"}
::option[不显示名称，静默保存每个缓冲区。]{#emacs-silent-save-all explanation="正常的交互命令会提示，而不是无条件写入每个缓冲区。"}
::option[保存当前缓冲区后关闭所有缓冲区。]{#emacs-close-all-buffers explanation="该命令关注多个缓冲区的保存，通常不会关闭它们。"}
:::

## 从磁盘恢复

如果文件已在磁盘上改变，而你有意想丢弃缓冲区当前内容，请运行 `M-x revert-buffer` 并审查确认提示。恢复可能破坏未保存的缓冲区编辑，所以只有在确认应以哪一方为准后才使用。

决定前可以另存副本，或使用版本控制和 diff 工具比较。如果缓冲区已修改，不要把重新加载操作当成无害操作。

## 总结

现在，你可以管理文件支持的缓冲区，而不会混淆访问与写入。

1. 使用 `C-x C-f` 访问路径。
2. 只有保存缓冲区时才创建缺失文件。
3. 使用 `C-x C-s` 保存当前缓冲区。
4. 使用 `C-x C-w` 以新的访问名称保存。
5. 使用 `C-x s` 审查多个已修改缓冲区。
