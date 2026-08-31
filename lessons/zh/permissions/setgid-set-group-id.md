---
lesson_id: "setgid-set-group-id"
course_id: "permissions"
lang: "zh"
order_index: 6
title: "Setgid"
description: "学习 set-group-ID 如何影响可执行文件凭据和共享目录中的组继承。"
meta_title: "Setgid - 权限"
meta_description: "了解 Linux SGID（设置组 ID）权限、它们的工作原理以及如何修改它们。理解这个关键的 Linux 安全概念。"
meta_keywords: "Linux SGID, 设置组 ID, Linux 权限，chmod g+s, Linux 安全，Linux 初学者，Linux 教程"
---

set-group-ID 位通常称为 setgid 或 SGID，有两项重要用途。对于可执行普通文件，它可以改变新进程的有效组 ID；对于目录，它会让新建目录项继承该目录的组，这对协作目录树尤其有用。

## 可执行文件上的 Setgid

长列表可以在组执行位置显示 setgid：

```bash
$ ls -l /path/to/program
-rwxr-sr-x 1 root operators 24576 Jan 10 09:30 /path/to/program
```

小写 `s` 表示 setgid 和组执行都已设置。大写 `S` 表示已设置 setgid，但没有组执行。

当内核在执行时采用该位，进程会根据可执行文件的组所有者获得有效组 ID。`nosuid` 挂载等控制可以抑制该行为，不能把它当作适用于每种文件类型和环境的普遍保证。

:::single-choice{#setgid-executable-effect}
采用可执行文件上的 setgid 时，哪个凭据来自该可执行文件的组所有者？

::option[进程的有效组 ID。]{#setgid-effective-group .correct explanation="Set-group-ID 执行会把可执行文件所有者的组设为进程的有效组身份。"}
::option[进程的实际用户 ID。]{#setgid-real-user explanation="该位涉及组凭据，而不是调用者的实际用户身份。"}
::option[进程打开的每个文件的所有者。]{#setgid-opened-owner explanation="执行凭据不会重写已打开文件的所有权元数据。"}
:::

## 目录上的 Setgid

目录上的 setgid 有不同用途。新文件和子目录通常会继承目录的组，而不是创建者的默认组。在 Linux 上，新子目录也会继承 setgid 位，帮助共享项目树保持一致的组。

Setgid 本身不会授予组写入权限。目录模式、进程 umask、请求的创建模式、默认 ACL 和其他控制仍然决定访问权限。

```bash
$ sudo chgrp developers /srv/project
$ sudo chmod g+s /srv/project
$ ls -ld /srv/project
drwxr-sr-x 2 root developers 4096 Jan 10 09:30 /srv/project
```

:::single-choice{#setgid-directory-inheritance}
`/srv/project` 上的 setgid 通常会让新建文件继承什么？

::option[目录的用户所有者。]{#setgid-inherit-user explanation="目录 setgid 影响组继承，不影响新目录项的用户所有者。"}
::option[目录的完整权限模式。]{#setgid-inherit-mode explanation="创建权限仍根据请求模式、umask 和任何 ACL 计算。"}
::option[目录的组所有者。]{#setgid-inherit-group .correct explanation="新目录项通常会获得 setgid 目录的组，从而支持一致的共享所有权。"}
:::

## 设置和移除 Setgid

使用符号形式设置该位：

```bash
$ sudo chmod g+s myfile
```

使用开头的八进制 `2`，把它与普通模式位一起设置：

```bash
$ sudo chmod 2755 myfile
```

使用 `chmod g-s myfile` 可只移除该特殊位。

:::single-choice{#setgid-octal-value}
Setgid 会为开头的特殊位八进制数字贡献哪个值？

::option[`4`]{#setgid-value-four explanation="值 `4` 表示特殊位数字中的 setuid。"}
::option[`1`]{#setgid-value-one explanation="值 `1` 表示 sticky bit。"}
::option[`2`]{#setgid-value-two .correct explanation="Setgid 贡献 `2`，例如模式 `2755`。"}
:::

## 安全使用共享目录

对于协作目录，应组合预期的组所有者、setgid 和范围严格的访问位。以代表性用户测试创建操作，并用 `ls -ld` 检查结果。不要为了处理组共享问题就让目录树对所有人可写；专用组、适当的 umask 或默认 ACL，再加上 setgid 目录，通常能提供更清晰的控制。

:::single-choice{#setgid-directory-write-access}
只设置 setgid 是否会让组成员获得在目录中创建文件的权限？

::option[会；setgid 始终添加组读取、写入和执行。]{#setgid-adds-rwx explanation="该特殊位不会自动改变三个普通组权限位。"}
::option[会；setgid 会禁用针对组成员的所有检查。]{#setgid-disables-checks explanation="普通自主访问控制和其他安全检查仍然适用。"}
::option[不会；适用的写入和搜索权限也必须允许创建。]{#setgid-no-automatic-write .correct explanation="Setgid 控制组继承，普通权限和其他访问控制则管理目录写入。"}
:::

## 总结

现在，你可以区分 setgid 在可执行文件和目录上的含义。

1. 在组执行位置识别 setgid。
2. 把可执行文件 setgid 与有效组 ID 联系起来。
3. 使用目录 setgid 在共享目录树中保持组所有权。
4. 设置或移除该位，同时不要把它与普通写入访问混淆。
