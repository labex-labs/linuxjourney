---
lesson_id: "modifying-permissions"
course_id: "permissions"
lang: "zh"
order_index: 2
title: "修改权限"
description: "学习如何使用符号和八进制 `chmod` 模式更改 Linux 权限位。"
meta_title: "修改权限 - 权限管理"
meta_description: "学习如何使用 chmod 命令更改 Linux 权限。本指南涵盖符号和数字方法，帮助您安全地管理文件和目录访问。掌握 Linux 权限更改过程，以实现更好的系统管理。"
meta_keywords: "linux 更改权限，更改 linux 权限，如何在 linux 中更改权限，如何更改 linux 文件权限，chmod, 文件权限，linux 安全，符号权限，数字权限"
---

`chmod` 命令会更改文件和目录的模式位。通常，只有文件所有者或拥有必要权限的进程才能进行此更改。运行 `chmod` 前后都应使用 `ls -l` 检查当前模式。

## 使用符号模式

符号模式说明要更改哪个权限类别、如何更改以及涉及哪些权限。

- `u` 选择所有者类别。
- `g` 选择组类别。
- `o` 选择其他类别。
- `a` 选择全部三个类别。
- `+` 添加权限，`-` 移除权限，`=` 精确设置所选类别。

例如，为所有者添加执行权限：

```bash
$ chmod u+x myfile
```

移除组写入权限：

```bash
$ chmod g-w myfile
```

同时为所有者和组添加写入权限：

```bash
$ chmod ug+w myfile
```

多个子句可以用逗号分隔。以下命令把所有者设为可读写、组设为只读、其他设为没有权限：

```bash
$ chmod u=rw,g=r,o= myfile
```

如果像 `chmod +x myfile` 那样省略类别，进程 umask 会影响更改哪些类别。明确写出类别，更便于审查预期结果。

:::single-choice{#modifying-permissions-remove-group-write}
哪个符号模式会移除组写入权限，而不改变组的其他权限位？

::option[`chmod u-w myfile`]{#modifying-permissions-user-minus-write explanation="这会从所有者类别移除写入权限，而不是组类别。"}
::option[`chmod g-w myfile`]{#modifying-permissions-group-minus-write .correct explanation="`g` 选择组类别，`-` 移除权限位，`w` 指定写入权限。"}
::option[`chmod g=w myfile`]{#modifying-permissions-group-equals-write explanation="`=` 会把所选类别替换为仅可写，而不是移除写入。"}
:::

## 使用八进制模式

八进制模式用一位数字设置每个基本权限三元组。每个类别中的值相加：

- `4` 表示读取
- `2` 表示写入
- `1` 表示执行
- `0` 表示没有权限

最右侧三位依次表示所有者、组和其他。例如：

```bash
$ chmod 755 myfile
```

模式 `755` 展开如下：

- 所有者 `7` 是 `4 + 2 + 1`，即 `rwx`。
- 组 `5` 是 `4 + 1`，即 `r-x`。
- 其他 `5` 是 `4 + 1`，即 `r-x`。

与符号模式中的 `+` 或 `-` 操作不同，八进制模式会提供完整的普通权限集合。后续课程会介绍用于特殊模式位的可选首位数字。

:::single-choice{#modifying-permissions-octal-read-value}
哪个八进制值表示读取权限？

::option[`1`]{#modifying-permissions-value-one explanation="值 `1` 表示执行权限。"}
::option[`2`]{#modifying-permissions-value-two explanation="值 `2` 表示写入权限。"}
::option[`4`]{#modifying-permissions-value-four .correct explanation="读取权限为一个类别的数字贡献八进制值 `4`。"}
:::

:::single-choice{#modifying-permissions-mode-640}
`chmod 640 report` 会设置哪些普通权限？

::option[所有者读取、组写入、其他执行。]{#modifying-permissions-640-separated explanation="八进制数字是每个类别权限值的总和，而不是独立的读、写、执行列。"}
::option[所有者读取/执行、组写入、其他无权限。]{#modifying-permissions-640-wrong-sums explanation="所有者值 `6` 是读取加写入，组值 `4` 是读取。"}
::option[所有者读取/写入、组读取、其他无权限。]{#modifying-permissions-640-correct .correct explanation="这些数字展开为所有者 `6`（`rw-`）、组 `4`（`r--`）和其他 `0`（`---`）。"}
:::

## 安全应用更改

只授予用户和服务所需的访问权限。不要把 `chmod 777` 当作排查问题的快捷方式，因为它会向每个类别授予读取、写入和执行，常常在未解决所有权、目录遍历、ACL 或服务策略问题的情况下增加风险。

递归更改需要格外谨慎。使用 `chmod -R` 前，应预览目标树、考虑符号链接和挂载文件系统，并在小范围内测试。更改后应验证结果模式，而不是假设命令影响了预期对象。

:::single-choice{#modifying-permissions-least-privilege}
为什么 `chmod 777` 通常不是解决访问问题的好方法？

::option[它会移除所有者的全部权限。]{#modifying-permissions-777-removes explanation="每个 `7` 都授予读取、写入和执行，不会移除所有者权限。"}
::option[它会向所有者、组和其他授予所有基本权限。]{#modifying-permissions-777-grants-all .correct explanation="三个类别全部获得 `rwx`，通常超出实际需要的访问范围。"}
::option[它只会更改文件的组所有权。]{#modifying-permissions-777-group explanation="`chmod` 更改模式位；组所有权使用 `chgrp` 或 `chown` 等工具更改。"}
:::

要在隔离环境中动手练习，可以使用 [Linux 用户组和文件权限](https://labex.io/zh/labs/linux-linux-user-group-and-file-permissions-18002) 实验，并在更改前后检查每个模式。

## 总结

现在，你可以使用有意设计的 `chmod` 表达式更改普通 Linux 模式位。

1. 使用符号模式进行有针对性的添加、移除或赋值。
2. 用读取 `4`、写入 `2` 和执行 `1` 构建八进制数字。
3. 按所有者、组和其他的顺序读取八进制类别。
4. 验证更改，并应用所需的最小权限。
