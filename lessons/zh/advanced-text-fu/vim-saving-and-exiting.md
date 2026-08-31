---
lesson_id: "vim-saving-and-exiting"
course_id: "advanced-text-fu"
lang: "zh"
order_index: 8
title: "Vim 保存与退出"
description: "学习如何写入、退出、另存为其他名称，或有意丢弃 Vim 缓冲区更改。"
meta_title: "Vim 保存与退出 - 高级文本技巧"
meta_description: "学习如何使用 :w 等命令在 Vim 编辑器中保存。掌握如何使用 :wq 或 ZZ 保存并退出。本指南涵盖了高效管理 Vim 文件所需的 essential linux wq 和 vi 写入并退出命令。"
meta_keywords: "vim 如何保存，linux wq, vi 写入并退出，vim 如何保存并退出，如何在 vim 编辑器中保存，保存文件 vim, 退出 vim, vim 命令"
---

写入和退出是两项独立的 Vim 操作。输入 Ex 命令前，请按 `Esc` 返回普通模式，输入 `:` 和命令，再按 Enter。不要想当然地认为写入成功，应先阅读 Vim 的状态或错误消息。

## 写入当前缓冲区

使用 `:w` 把当前缓冲区写入其关联文件，而不关闭窗口：

```vim
:w
```

如果缓冲区没有文件名、目录不可写、文件系统已满，或有其他条件阻止操作，写入可能失败。请检查 Vim 报告的消息。

使用 `:w copy.txt` 可把当前缓冲区写入另一个路径，同时保留当前缓冲区原来的名称。如果缓冲区应采用新路径名，请使用 `:saveas copy.txt`。

:::single-choice{#vim-save-without-quit}
哪个 Vim 命令会把当前缓冲区写入其关联文件而不退出？

::option[`:q`]{#vim-save-q explanation="`:q` 请求退出，并不会写入已修改的缓冲区。"}
::option[`:w`]{#vim-save-w .correct explanation="`:write` 命令保存当前缓冲区，并让编辑窗口保持打开。"}
::option[`:q!`]{#vim-save-q-force explanation="`:q!` 会放弃未保存的更改并退出，不会保存它们。"}
:::

## 退出未修改的缓冲区

如果关闭当前窗口不会放弃未保存的缓冲区更改，可以使用 `:q`：

```vim
:q
```

如果当前缓冲区已修改，退出会丢失更改，Vim 通常会拒绝并显示警告。这个保护措施让你有机会写入或重新考虑。

:::single-choice{#vim-quit-clean-buffer}
没有未保存更改会丢失时，哪个命令会退出当前 Vim 窗口？

::option[`:w`]{#vim-quit-w explanation="这会写入缓冲区，但让当前窗口保持打开。"}
::option[`:q`]{#vim-quit-q .correct explanation="当 Vim 的缓冲区修改保护允许时，普通退出命令会关闭窗口。"}
::option[`u`]{#vim-quit-u explanation="普通模式中的 `u` 会撤销更改，不会关闭编辑器窗口。"}
:::

## 丢弃未保存的更改

只有在确实想关闭当前窗口并放弃原本会阻止退出的更改时，才使用 `:q!`：

```vim
:q!
```

感叹号会覆盖未保存更改的警告。这些缓冲区更改不会写入，因此按 Enter 前应确认它们确实可以丢弃。

:::single-choice{#vim-quit-discard-changes}
当前缓冲区中有你明确不想保存的更改。哪个命令会退出当前窗口并放弃它们？

::option[`:q`]{#vim-discard-plain-q explanation="如果退出会丢失已修改缓冲区中的更改，普通 `:q` 通常会拒绝。"}
::option[`:wq`]{#vim-discard-wq explanation="`:wq` 会在退出前写入更改，行为与丢弃正好相反。"}
::option[`:q!`]{#vim-discard-q-force .correct explanation="感叹号会覆盖修改警告，在不写入未保存更改的情况下关闭窗口。"}
:::

## 同时写入和退出

如果应写入缓冲区，并在成功写入后关闭当前窗口，请使用 `:wq`：

```vim
:wq
```

如果写入失败，Vim 不会完成所请求的退出。应解决错误，不要假设数据已经写入磁盘。

:::single-choice{#vim-write-and-quit}
哪个命令会写入当前缓冲区，并在写入成功后退出当前窗口？

::option[`:wq`]{#vim-save-wq .correct explanation="它组合了写入和退出，而且退出取决于写入成功。"}
::option[`:q!`]{#vim-save-force-quit explanation="这会退出并丢弃更改，而不是写入它们。"}
::option[`:w copy.txt`]{#vim-save-copy explanation="这会写入另一个路径，但让编辑窗口保持打开。"}
:::

## 使用 :x 和 ZZ

`:x` 只在缓冲区已修改时写入，然后退出。在普通模式中，大写 `ZZ` 会执行相同的“修改后才写入并退出”行为：

```vim
:x
```

```text
ZZ
```

这与 `:wq` 有细微差别：即使缓冲区没有更改，`:wq` 也会请求写入。大写 `ZQ` 是普通模式中“不写入便退出”的对应命令，类似于 `:q!`。

:::single-choice{#vim-write-if-modified-quit}
普通模式中的哪个命令只在缓冲区已修改时写入，然后退出？

::option[`ZZ`]{#vim-save-zz .correct explanation="大写 `ZZ` 会执行与 `:x` 对应的“修改后才写入并退出”行为。"}
::option[`zz`]{#vim-center-screen explanation="小写 `zz` 会把当前行重新置于窗口中央，不会保存或退出。"}
::option[`ZQ`]{#vim-quit-zq explanation="大写 `ZQ` 会不写入便退出，因此会丢弃未保存的更改，而不是保存它们。"}
:::

涉及多个窗口或缓冲区时，一个命令可能只关闭当前窗口。`:qa`、`:wqa` 和 `:qa!` 等命令会作用于所有窗口，但使用强制作用于全部窗口的命令前，应检查每个已修改的缓冲区。

要在可丢弃文件上练习写入和退出，可以尝试以下动手实验：

1. **[在 Linux 中使用 Vim 和 Nano 编辑文本文件](https://labex.io/zh/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 使用 Vim 和 Nano 练习创建文件、编辑文本、保存文件和导航，巩固包括保存与退出在内的 Vim 基本操作。

## 总结

现在，你可以根据对未保存数据的意图选择合适的 Vim 退出命令。

1. 使用 `:w` 写入而不退出。
2. 不会丢失更改时，使用 `:q` 安全退出。
3. 使用 `:q!` 有意丢弃更改。
4. 使用 `:wq` 写入并退出。
5. 使用 `:x` 或 `ZZ` 实现修改后才写入的行为。
