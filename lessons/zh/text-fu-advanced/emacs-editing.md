---
index: 12
lang: "zh"
title: "Emacs 编辑"
meta_title: "Emacs 编辑 - 高级文本操作"
meta_description: "学习 Emacs 编辑基础：高效导航文本、剪切和粘贴。这份适合初学者的指南将帮助您掌握 Emacs 在 Linux 中的基本命令。"
meta_keywords: "Emacs, Emacs 教程，Emacs 命令，文本编辑器，Linux 编辑器，Emacs 导航，Emacs 初学者，Emacs 指南"
---

## Lesson Content

### Text Navigation

```
C-up arrow: move up one paragraph
C-down arrow: move down one paragraph
C-left arrow: move one word left
C-right arrow: move one word right
M->: move to the end of the buffer
```

在文本导航中，您的常规文本按钮（如 Home、End、Page Up、Page Down 和箭头键等）都能正常工作。

### Cutting and Pasting

要在 Emacs 中剪切 (kill) 或粘贴 (yank)，您首先需要能够选择文本。将光标移动到您想要剪切或粘贴的位置，然后按下 `C-space key`。然后您可以使用导航键选择您想要的文本。现在您可以这样剪切和粘贴：

```
C-w: cut
C-y: yank
```

## Exercise

尝试文本导航。

## Quiz Question

如何移动到缓冲区的末尾？

## Quiz Answer

M->
