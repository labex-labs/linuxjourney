---
lang: "zh"
title: "Emacs 缓冲区导航"
description: "学习 Emacs 缓冲区导航命令。通过这个适合初学者的 Emacs 教程，高效地切换、关闭和分割缓冲区。提升您的工作效率！"
keywords: "Emacs 缓冲区导航，Emacs 命令，C-x b, C-x k, Linux 教程，Emacs 指南，Emacs 初学者"
---

## Lesson Content

要在缓冲区（或您正在访问的文件）之间移动，请使用以下命令：

### 切换缓冲区

```
C-x b - switch buffer
C-x right arrow - right-cycle through buffer
C-x left arrow - left-cycle through buffer
```

### 关闭缓冲区

```
C-x k
```

### 分割当前缓冲区

```
C-x 2
```

这允许您在一个屏幕上看到多个缓冲区。要在这些缓冲区之间移动，请使用：C-x o

### 将单个缓冲区设置为当前屏幕

```
C-x 1
```

如果您曾使用过 `screen` 或 `tmux` 等终端复用器，那么这些缓冲区命令会感觉非常熟悉。

## Exercise

Play around with buffers.

## Quiz Question

如何终止一个缓冲区？

## Quiz Answer

C-x k
