---
index: 6
lang: "zh"
title: "Setgid"
meta_title: "Setgid - 权限"
meta_description: "了解 Linux SGID（设置组 ID）权限、它们的工作原理以及如何修改它们。理解这个关键的 Linux 安全概念。"
meta_keywords: "Linux SGID, 设置组 ID, Linux 权限，chmod g+s, Linux 安全，Linux 初学者，Linux 教程"
---

## Lesson Content

类似于设置用户 ID 权限位，还有一个设置组 ID（SGID）权限位。此位允许程序以该组的成员身份运行。

我们来看一个例子：

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

我们现在可以看到权限位在组权限集中。

### 修改 SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

SGID 的数字表示是 2。

## Exercise

熟能生巧！这里有一些动手实验来巩固你对 Linux 用户、组和文件权限的理解：

1. **[Linux 用户、组和文件权限](https://labex.io/zh/labs/linux-linux-user-group-and-file-permissions-18002)** - 学习基本的 Linux 用户和组管理概念，包括创建和管理用户、探索组成员身份、理解文件权限以及操作文件所有权。
2. **[添加新用户和组](https://labex.io/zh/labs/linux-add-new-user-and-group-17987)** - 练习创建新用户帐户、设置自定义组以及管理组成员身份，模拟真实的系统管理任务。

这些实验将帮助您在实际场景中应用这些概念，并增强对 Linux 权限和用户管理的信心。

## Quiz Question

SGID 的数字表示是什么？

## Quiz Answer

2
