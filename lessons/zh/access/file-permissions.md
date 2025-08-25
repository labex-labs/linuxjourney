---
index: 1
lang: "zh"
title: "文件权限"
meta_title: "文件权限 - 权限"
meta_description: "学习 Linux 文件权限：理解 rwx 位、用户、组和其他权限。掌握 `ls -l` 输出，适合初学者。开始您的 Linux 之旅！"
meta_keywords: "Linux 文件权限, ls -l 命令, rwx 权限, Linux 教程, 文件模式, Linux 初学者, Linux 指南"
---

## Lesson Content

正如我们之前所学，文件有不同的权限或文件模式。让我们看一个例子：

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
```

文件权限有四个部分。第一部分是文件类型，由权限中的第一个字符表示。在我们的例子中，由于我们正在查看一个目录，它显示 **d** 表示文件类型。最常见的是，您会看到 **-** 表示一个普通文件。

文件模式的接下来三个部分是实际的权限。权限每3位一组。前3位是用户权限，然后是组权限，然后是其他权限。我添加了竖线以便于区分。

```plaintext
d | rwx | r-x | r-x
```

每个字符代表不同的权限：

- r: 可读
- w: 可写
- x: 可执行（基本上是一个可执行程序）
- -: 空

因此在上面的例子中，我们看到用户 pete 对文件拥有读、写和执行权限。组 penguins 拥有读和执行权限。最后，其他用户（所有人）拥有读和执行权限。

## Exercise

熟能生巧！这里有一些动手实验来巩固您对 Linux 文件权限、用户和组的理解：

1. **[Linux 用户组和文件权限](https://labex.io/zh/labs/linux-linux-user-group-and-file-permissions-18002)** - 学习基本的 Linux 用户和组管理概念，包括创建用户、探索组成员身份、理解文件权限和操作文件所有权。
2. **[添加新用户和组](https://labex.io/zh/labs/linux-add-new-user-and-group-17987)** - 练习创建新用户帐户、设置自定义组和管理组成员身份，模拟真实的系统管理任务。
3. **[查找文件](https://labex.io/zh/labs/linux-find-a-file-17993)** - 应用您对文件权限的知识，查找特定文件并设置其访问权限，确保您是唯一授权用户。

这些实验将帮助您在实际场景中应用这些概念，并增强您在 Linux 中管理权限和用户的信心。

## Quiz Question

哪个权限位用于可执行？

## Quiz Answer

x
