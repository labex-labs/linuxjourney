---
lesson_id: "sticky-bit"
course_id: "permissions"
lang: "zh"
order_index: 8
title: "Sticky Bit"
description: "学习 sticky bit 如何保护 `/tmp` 等共享可写目录中的目录项。"
meta_title: "粘位 - 权限"
meta_description: "探索 Linux 和 Unix 文件权限中粘位（Sticky Bit）的用途。了解粘位如何保护 /tmp 等共享目录中的文件，以及如何使用 chmod 设置它。"
meta_keywords: "粘位，linux 粘位，unix 文件权限 粘位，chmod +t, /tmp 目录，文件权限，linux 安全"
---

可写目录通常允许获准用户删除或重命名其中的目录项，即使该用户并不拥有文件本身。Sticky bit 会增加所有权限制，让共享可写目录更安全。

## Sticky Bit 如何限制删除

目录设置 sticky bit 后，Linux 通常只允许拥有适当权限的进程、目录所有者或目录项所有者删除或重命名目录项。普通目录写入和搜索权限仍然是必要条件。

该限制针对目录项。如果文件权限原本允许，sticky bit 不会阻止文件所有者编辑文件内容，也不会让目录变为私有。

:::single-choice{#sticky-bit-removal-rule} 在设置 sticky bit 的共享目录中，哪个普通用户通常可以删除某个目录项？

::option[任何能够列出目录的用户。]{#sticky-bit-any-reader explanation="目录读取权限可能暴露名称，但不会绕过 sticky 所施加的所有权限制。"}
::option[拥有所需目录访问权限的该目录项所有者。]{#sticky-bit-entry-owner .correct explanation="目录项所有者是 sticky 目录规则通常允许的身份之一。"}
::option[只有该目录项所属组的成员。]{#sticky-bit-entry-group explanation="单凭组成员身份并不属于 sticky bit 定义的所有权例外。"}
:::

## 在 `/tmp` 上识别该位

系统临时目录是一个常见示例：

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

末尾的小写 `t` 位于其他执行位置。它表示 sticky bit 和其他执行权限都存在。大写 `T` 表示设置了 sticky bit，但没有其他执行权限。

因为 `/tmp` 通常允许所有人写入和搜索，多个用户都可以在其中创建目录项。Sticky bit 会阻止普通用户仅因为目录对所有人可写就删除其他用户的目录项。应用程序仍必须安全创建临时对象，因为可预测名称、不安全链接和宽松文件模式会带来独立风险。

:::single-choice{#sticky-bit-lowercase-t} 目录模式末尾的小写 `t` 表示什么？

::option[已设置 sticky，同时也设置了其他执行。]{#sticky-bit-t-with-execute .correct explanation="小写 `t` 组合了 sticky 特殊位和普通的其他执行位。"}
::option[已设置 sticky，但没有其他执行。]{#sticky-bit-t-without-execute explanation="这种组合显示为大写 `T`。"}
::option[已设置 setgid 和组执行。]{#sticky-bit-setgid-position explanation="Setgid 出现在组执行位置，而不是最后的其他位置。"}
:::

## 设置和移除 Sticky Bit

使用符号形式设置该位：

```bash
$ chmod +t shared-directory
```

在开头的特殊位八进制数字中，sticky 贡献 `1`：

```bash
$ chmod 1777 shared-directory
```

开头的 `1` 设置 sticky，`777` 提供普通模式。只有目录确实有意供所有本地用户共享时，这种模式才合适。对于团队目录，范围更窄的组权限可能更好。使用 `chmod -t shared-directory` 可只移除 sticky bit。

:::single-choice{#sticky-bit-octal-value} 哪个开头的八进制值表示 sticky bit？

::option[`2`]{#sticky-bit-value-two explanation="开头的 `2` 表示 setgid。"}
::option[`1`]{#sticky-bit-value-one .correct explanation="Sticky bit 为开头的特殊位数字贡献 `1`。"}
::option[`4`]{#sticky-bit-value-four explanation="开头的 `4` 表示 setuid。"}
:::

## 验证完整目录策略

Sticky 不会授予写入或搜索访问；它只会在普通权限允许修改目录后，限制删除和重命名操作。应一起验证目录的所有者、组、普通模式、ACL 和挂载上下文。请在隔离环境中使用非特权账户测试，不要修改运行中系统的 `/tmp`。

:::single-choice{#sticky-bit-access-scope} 添加 sticky bit 是否会让其他用户可以写入原本不可写的目录？

::option[会；sticky 会自动为每个类别添加写入。]{#sticky-bit-adds-write explanation="该特殊位不会重写所有者、组或其他写入位。"}
::option[会；sticky 会禁用目录的其他权限三元组。]{#sticky-bit-disables-other explanation="其他三元组仍然参与普通访问检查。"}
::option[不会；普通写入和搜索权限仍然控制访问。]{#sticky-bit-no-write-grant .correct explanation="Sticky 会缩小某些删除和重命名操作的范围，但不会添加缺少的普通权限。"}
:::

要练习，可以创建可丢弃的共享目录，设置适当的普通模式和 sticky bit，再以两个非特权用户测试目录项删除。[删除和移动文件](https://labex.io/zh/labs/linux-delete-and-move-files-7777) 实验可以巩固底层的重命名和删除操作。

## 总结

现在，你可以说明并验证共享目录上的 sticky bit。

1. 把 sticky 与删除和重命名时的所有权限制联系起来。
2. 在长列表中识别小写 `t` 和大写 `T`。
3. 使用符号形式或开头的八进制值 `1` 设置该位。
4. 把 sticky 与普通目录权限一起评估。
