---
index: 8
lang: "zh"
title: "粘滞位"
meta_title: "粘滞位 - 权限"
meta_description: "了解 Linux 粘滞位、它在 /tmp 等共享目录中的用途以及如何使用 chmod 设置它。理解这个关键的文件权限！"
meta_keywords: "Linux 粘滞位，chmod +t, /tmp 目录，Linux 权限，文件安全，Linux 教程，Linux 初学者"
---

## Lesson Content

我想谈的最后一个特殊权限位是粘滞位。

这个权限位“粘住文件/目录”，这意味着只有所有者或 root 用户才能删除或修改文件。这对于共享目录非常有用。请看下面的例子：

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

你会在这里的末尾看到一个特殊的权限位 **t**。这意味着每个人都可以在 `/tmp` 目录中添加文件、写入文件和修改文件，但只有 root 可以删除 `/tmp` 目录。

### 修改粘滞位

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

粘滞位的数字表示是 **1**。

## Exercise

熟能生巧！这里有一些动手实验，以加强您对 Linux 文件权限及其对文件和目录管理影响的理解：

1. **[Linux 用户组和文件权限](https://labex.io/zh/labs/linux-linux-user-group-and-file-permissions-18002)** - 练习创建和管理用户和组，理解文件权限，以及操作文件所有权。本实验提供了理解粘滞位等特殊权限如何运作的基础知识。
2. **[删除和移动文件](https://labex.io/zh/labs/linux-delete-and-move-files-7777)** - 学习如何在 Linux 系统中删除和移动文件。本实验将帮助您理解权限的实际含义，包括它们如何限制这些操作。
3. **[查找文件](https://labex.io/zh/labs/linux-find-a-file-17993)** - 练习定位文件和设置访问权限。本实验强调了文件权限的重要性以及它们如何控制访问和修改。

这些实验将帮助您在实际场景中应用文件权限的概念，并增强您在 Linux 中管理文件访问的信心。

## Quiz Question

什么符号代表粘滞位？

## Quiz Answer

t
