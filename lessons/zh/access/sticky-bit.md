---
index: 8
lang: "zh"
title: "粘滞位"
meta_title: "粘滞位 - 权限"
meta_description: "了解 Linux 粘滞位、它在 /tmp 等共享目录中的用途，以及如何使用 chmod 设置它。理解这个关键的文件权限！"
meta_keywords: "Linux 粘滞位，chmod +t, /tmp 目录，Linux 权限，文件安全，Linux 教程，Linux 初学者"
---

## Lesson Content

我想谈论的最后一个特殊权限位是粘滞位（sticky bit）。

这个权限位“粘住一个文件/目录”，这意味着只有所有者或 root 用户才能删除或修改该文件。这对于共享目录非常有用。请看下面的例子：

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

你会在这里的末尾看到一个特殊的权限位 **t**。这意味着每个人都可以在 `/tmp` 目录中添加文件、写入文件和修改文件，但只有 root 用户才能删除 `/tmp` 目录。

### Modify sticky bit

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

粘滞位的数字表示是 **1**。

## Exercise

你认为还有哪些文件和目录启用了粘滞位？

## Quiz Question

什么符号代表粘滞位？

## Quiz Answer

t
