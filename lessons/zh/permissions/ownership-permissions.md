---
lesson_id: "ownership-permissions"
course_id: "permissions"
lang: "zh"
order_index: 3
title: "所有权权限"
description: "学习如何检查和更改 Linux 文件系统对象的用户与组所有权。"
meta_title: "所有权权限 - 权限管理"
meta_description: "学习使用 chown 和 chgrp Linux 命令，掌握 Linux 文件所有权。本教程解释如何更改文件的用户和组所有权，这是管理 Linux 权限的关键技能。"
meta_keywords: "chown, chgrp, linux 文件所有权，更改文件所有者，更改文件组，linux 权限，linux 命令，linux 教程，linux 指南，用户所有权，组所有权"
---

每个 Linux 文件系统对象都会记录一个用户所有者和一个组所有者。这些身份决定应用所有者还是组权限三元组，但身份本身不会授予某项具体权限。使用 `ls -l` 同时检查所有权和模式。

## 更改用户所有者

使用 `chown`（change owner）指定不同的用户所有者：

```bash
$ sudo chown patty myfile
```

这会把 `myfile` 的用户所有者改为 `patty`，组保持不变。即使当前拥有该文件，更改其用户所有者通常也需要适当权限。这项限制能防止用户通过转移文件来规避配额或其他基于所有权的控制。

:::single-choice{#ownership-permissions-change-user}
哪个命令会把 `myfile` 的用户所有者改为 `patty`，同时保持组不变？

::option[`chown patty myfile`]{#ownership-permissions-user-with-chown .correct explanation="在 `chown` 所有权操作数中只提供用户名，会更改用户所有者并保留组。"}
::option[`chgrp patty myfile`]{#ownership-permissions-user-with-chgrp explanation="`chgrp` 更改组所有者，而不是用户所有者。"}
::option[`chmod patty myfile`]{#ownership-permissions-user-with-chmod explanation="`chmod` 更改模式位，不接受用户名作为新所有者。"}
:::

## 更改组所有者

使用 `chgrp` 指定不同的组所有者：

```bash
$ chgrp whales myfile
```

在典型系统上，非特权所有者只能把文件的组改为自己所属的组。特权进程可以进行更广泛的更改。等效的 `chown` 形式以冒号开头：

```bash
$ chown :whales myfile
```

之后，当内核选择组类别时会应用组模式位；更改组不会自动添加读取、写入或执行位。

:::single-choice{#ownership-permissions-change-group}
`chgrp whales myfile` 会更改什么？

::option[`myfile` 记录的用户所有者。]{#ownership-permissions-group-not-user explanation="用户所有者使用 `chown` 更改，而不是 `chgrp`。"}
::option[`whales` 组中列出的成员。]{#ownership-permissions-group-members explanation="该命令更改文件元数据，不会编辑系统组成员数据库。"}
::option[`myfile` 记录的组所有者。]{#ownership-permissions-group-owner .correct explanation="`chgrp` 会把指定组设为文件系统对象的组所有者。"}
:::

## 同时更改用户和组

向 `chown` 提供 `USER:GROUP` 可以在一次操作中更新两个字段：

```bash
$ sudo chown patty:whales myfile
```

该命令把 `patty` 设为用户所有者，把 `whales` 设为组所有者。应验证结果，而不是假设命令成功：

```bash
$ ls -l myfile
```

:::single-choice{#ownership-permissions-change-both}
哪个所有权说明会在一个 `chown` 命令中指定用户 `patty` 和组 `whales`？

::option[`patty:whales`]{#ownership-permissions-both-colon .correct explanation="冒号在组合所有权说明中分隔用户和组名称。"}
::option[`patty/whales`]{#ownership-permissions-both-slash explanation="斜杠不是本课介绍的 `chown` 用户和组操作数分隔符。"}
::option[`patty+whales`]{#ownership-permissions-both-plus explanation="加号不用于组合 `chown` 的两个所有权字段。"}
:::

## 谨慎处理递归更改

`-R` 选项会递归更改所有权，但范围过大的递归命令可能跨越意外目录树或影响服务数据。更改大型层次结构前，应确认准确目标、了解当前实现的符号链接行为、预览目录树，并在小样本上验证。不要在未审查范围的情况下，把示例中的特权所有权命令复制到真实系统上。

:::single-choice{#ownership-permissions-mode-separate}
更改文件的组所有者后，其普通组权限位会发生什么？

::option[始终自动变为可读写。]{#ownership-permissions-mode-read-write explanation="`chgrp` 不会自动选择固定的组模式。"}
::option[从所有者权限三元组复制而来。]{#ownership-permissions-mode-copied explanation="更改所有权时，所有者和组三元组仍然彼此独立。"}
::option[除非另行操作更改，否则保持原样。]{#ownership-permissions-mode-unchanged .correct explanation="所有权字段和模式位是独立元数据；更改组不会天然授予新的组权限位。"}
:::

要在隔离环境中练习，[Linux 用户组和文件权限](https://labex.io/zh/labs/linux-linux-user-group-and-file-permissions-18002) 实验涵盖检查和修改所有权及文件模式。

## 总结

现在，你可以区分所有权元数据与权限位，并有意地更改它们。

1. 使用 `chown USER FILE` 更改用户所有者。
2. 使用 `chgrp GROUP FILE` 或 `chown :GROUP FILE` 更改组所有者。
3. 使用 `chown USER:GROUP FILE` 设置两个字段。
4. 验证结果，并谨慎控制递归更改范围。
