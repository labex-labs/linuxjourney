---
lang: "zh"
title: "Setgid"
description: "了解 Linux SGID（设置组 ID）权限、它们的工作原理以及如何修改它们。理解这个关键的 Linux 安全概念。"
keywords: "Linux SGID, 设置组 ID, Linux 权限，chmod g+s, Linux 安全，Linux 初学者，Linux 教程"
---

## Lesson Content

与设置用户 ID 权限位类似，还有一个设置组 ID（SGID）权限位。此位允许程序以该组成员的身份运行。

我们来看一个例子：

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

我们现在可以看到权限位位于组权限集中。

### Modifying SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

SGID 的数字表示是 2。

## Exercise

本课程没有练习。

## Quiz Question

什么数字代表 SGID？

## Quiz Answer

2
