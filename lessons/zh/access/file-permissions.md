---
lang: "zh"
title: "文件权限"
meta_description: "学习 Linux 文件权限：理解 rwx 位、用户、组和其他权限。掌握 `ls -l` 输出，适合初学者。开始你的 Linux 之旅！"
meta_keywords: "Linux 文件权限，ls -l 命令，rwx 权限，Linux 教程，文件模式，Linux 初学者，Linux 指南"
---

## Lesson Content

正如我们之前所学，文件有不同的权限或文件模式。我们来看一个例子：

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
```

文件权限有四个部分。第一部分是文件类型，由权限中的第一个字符表示。在我们的例子中，由于我们查看的是一个目录，它显示 **d** 作为文件类型。最常见的是，普通文件会显示 **-**。

文件模式的接下来的三个部分是实际的权限。权限每 3 位一组。前 3 位是用户权限，然后是组权限，然后是其他权限。我添加了管道符号以便更容易区分。

```plaintext
d | rwx | r-x | r-x
```

每个字符代表不同的权限：

- r: 可读
- w: 可写
- x: 可执行（基本上是一个可执行程序）
- -: 空

所以在上面的例子中，我们看到用户 pete 对文件拥有读、写和执行权限。组 penguins 拥有读和执行权限。最后，其他用户（所有人）拥有读和执行权限。

## Exercise

Use the `ls -l` command on multiple files and recite their permissions, user, and group.

## Quiz Question

可执行文件使用哪个权限位？

## Quiz Answer

x
