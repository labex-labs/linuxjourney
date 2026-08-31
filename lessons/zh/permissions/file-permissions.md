---
lesson_id: "file-permissions"
course_id: "permissions"
lang: "zh"
order_index: 1
title: "文件权限"
description: "学习如何读取 Linux 文件类型，以及所有者、组和其他用户的权限位。"
meta_title: "文件权限 - 权限设置"
meta_description: "我们完整 Linux 教程的关键部分。了解 Linux 文件权限，包括用户、组和其他的 rwx 位。掌握 `ls -l` 输出并理解文件模式。"
meta_keywords: "文件权限，Linux 文件权限，学习 Linux 的最佳方式，完整 Linux 教程，rwx 权限，ls -l 命令，文件模式，Linux 指南"
---

Linux 通过类似文件的接口表示许多资源，每个文件系统对象都有控制访问的元数据。学会阅读这些元数据，是安全处理文件和目录的基础。

## 阅读长列表

使用 `ls -l` 显示长列表：

```bash
$ ls -ld Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 Desktop/
```

第一个字段 `drwxr-xr-x` 由一个文件类型字符和九个权限字符组成。列表还表明 `pete` 是所有者，`penguins` 是与该目录关联的组。

第一个字符描述对象类型。常见值包括：

- `-` 表示普通文件
- `d` 表示目录
- `l` 表示符号链接

还有其他特殊文件类型。剩余九个字符是访问权限：

```text
d | rwx | r-x | r-x
```

:::single-choice{#file-permissions-type-character}
在 `drwxr-xr-x` 中，第一个 `d` 表示什么？

::option[该对象是符号链接。]{#file-permissions-type-link explanation="符号链接通常在文件类型位置显示为 `l`。"}
::option[该对象是目录。]{#file-permissions-type-directory .correct explanation="第一个字符是文件类型，`d` 标识目录。"}
::option[所有者拥有删除权限。]{#file-permissions-type-delete explanation="Linux 模式字符串不使用 `d` 表示删除权限；第一个位置描述对象类型。"}
:::

## 理解 `r`、`w` 和 `x`

每个权限三元组使用以下字符：

- `r` 授予读取权限。
- `w` 授予写入权限。
- `x` 授予执行权限。
- `-` 表示没有该权限。

对于普通文件，读取允许访问内容，写入允许修改内容，执行允许内核尝试把它作为程序运行。如果文件格式、解释器行、挂载选项或其他安全控制不允许，执行仍可能失败。

对于目录，这些含义针对目录项：

- 读取允许列出目录中的名称。
- 写入允许创建或删除目录项，通常还需结合执行权限。
- 执行也称搜索权限，允许遍历目录并按名称访问目录项。

删除文件主要受父目录权限控制，而不是文件自身的写入位。

:::single-choice{#file-permissions-directory-execute}
目录的执行权限主要允许什么？

::option[运行目录中存储的每个普通文件。]{#file-permissions-directory-run-files explanation="目录的执行位不会授予其中每个文件执行权限。"}
::option[更改目录中每个文件的内容。]{#file-permissions-directory-edit-files explanation="写入文件内容取决于文件权限和其他访问控制。"}
::option[遍历目录并按名称访问目录项。]{#file-permissions-directory-search .correct explanation="目录执行权限，也称搜索权限，允许通过该目录进行路径名遍历。"}
:::

## 所有者、组和其他类别

九个模式字符按固定顺序组成三个三元组：

1. **所有者**：当进程的有效用户 ID 与文件所有者匹配时使用的权限。
2. **组**：当适用的进程组 ID 与文件组匹配时使用的权限。
3. **其他**：前两个类别都不匹配时使用的权限。

内核会选择一个适用类别，不会组合三个三元组来寻找最宽松的结果。访问控制列表、挂载选项、capabilities 或强制访问控制等其他机制还可能影响最终决策。

在示例中，所有者三元组是 `rwx`，组和其他都是 `r-x`。所有者可以读取、写入和搜索目录。组和其他类别可以读取及搜索，但不能通过普通模式位创建或删除目录项。

:::single-choice{#file-permissions-triplet-order}
在文件类型字符之后，三个权限三元组按什么顺序出现？

::option[组、所有者、其他。]{#file-permissions-order-group-first explanation="组三元组排在第二，而不是第一。"}
::option[其他、组、所有者。]{#file-permissions-order-other-first explanation="其他三元组排在最后，所有者三元组排在第一。"}
::option[所有者、组、其他。]{#file-permissions-order-owner-first .correct explanation="九个权限字符始终按所有者、组和其他的顺序显示三元组。"}
:::

:::single-choice{#file-permissions-example-group}
在 `drwxr-xr-x` 中，组类别具有哪些普通权限？

::option[读取和写入。]{#file-permissions-group-read-write explanation="组三元组为 `r-x`，所以写入位置是 `-`。"}
::option[写入和执行。]{#file-permissions-group-write-execute explanation="组三元组的第一个位置是 `r`，而不是 `w`。"}
::option[读取和执行。]{#file-permissions-group-read-execute .correct explanation="中间的三元组为 `r-x`，授予读取和执行，但不授予写入。"}
:::

要在隔离环境中巩固这些概念，可以尝试 [Linux 用户组和文件权限](https://labex.io/zh/labs/linux-linux-user-group-and-file-permissions-18002) 实验。它提供读取模式以及更改所有权和权限的练习。

## 总结

现在，你可以解释 Linux 长列表中的基本权限字段。

1. 把文件类型字符与九个权限位分开。
2. 根据对象是文件还是目录来解释 `r`、`w` 和 `x`。
3. 把模式分成所有者、组和其他三元组。
4. 把三元组与 `ls -l` 显示的所有者和组联系起来。
