---
lang: "zh"
title: "修改权限"
description: "学习如何使用 chmod 命令在 Linux 中修改文件权限。了解符号模式和数字模式以进行安全的文件管理。立即开始学习！"
keywords: "chmod 命令，Linux 权限，文件权限，chmod 教程，Linux 安全，Linux 初学者，Linux 指南，chmod 数字"
---

## Lesson Content

使用 `chmod` 命令可以轻松更改权限。

首先，选择要更改的权限集：用户、组或其他。您可以使用 `+` 或 `-` 添加或删除权限。让我们看一些例子。

### Adding permission bit on a file

```bash
chmod u+x myfile
```

上面的命令解读如下：更改 `myfile` 的权限，为用户集添加可执行权限位。所以现在用户对该文件拥有可执行权限！

### Removing permission bit on a file

```bash
chmod u-x myfile
```

### Adding multiple permission bits on a file

```bash
chmod ug+w
```

还有另一种使用数字格式更改权限的方法。此方法允许您一次性更改所有权限。您将使用数字表示单个权限集，而不是使用 r、w 或 x 来表示权限。因此无需使用 `g` 指定组或使用 `u` 指定用户。

数字表示如下：

- 4: read permission
- 2: write permission
- 1: execute permission

让我们看一个例子：

```bash
chmod 755 myfile
```

您能猜出我们正在给这个文件什么权限吗？让我们分解一下：`755` 涵盖了所有权限集的权限。第一个数字 (7) 代表用户权限，第二个数字 (5) 代表组权限，最后一个 5 代表其他权限。

等等，上面没有列出 7 和 5。这些数字是从哪里来的？请记住，我们现在将所有权限组合成一个数字，因此您需要进行一些数学运算。

7 = 4 + 2 + 1，所以 7 是用户权限，它具有读取、写入和执行权限。

5 = 4 + 1，组具有读取和执行权限。

5 = 4 + 1，所有其他用户都具有读取和执行权限。

需要注意的一点是：随意更改权限不是一个好主意。您可能会将敏感文件暴露给所有人修改。但是，很多时候您确实需要更改权限；在使用 `chmod` 命令时请务必小心。

## Exercise

更改一些基本文本文件的权限，并在执行 `ls -l` 时查看权限位的变化。

## Quiz Question

使用数字格式时，哪个数字代表读取权限？

## Quiz Answer

4
