---
lesson_id: "umask"
course_id: "permissions"
lang: "zh"
order_index: 4
title: "Umask"
description: "学习进程 umask 如何限制新建文件和目录所请求的权限位。"
meta_title: "Umask - 权限"
meta_description: "了解如何使用 `umask` 命令控制 Linux 中的默认文件权限。理解数字权限并轻松管理新文件访问。"
meta_keywords: "umask, linux 权限，文件权限，linux 命令，linux 初学者，linux 教程，默认权限"
---

进程的文件创建掩码（umask）会阻止该进程创建文件系统对象时设置选定的权限位。它是掩码，不是一套完整默认模式：应用程序先请求一个模式，内核再移除 umask 禁止的权限位。

从概念上说：

```text
结果模式 = 请求模式 AND NOT umask
```

访问控制列表和应用程序行为还可能增加更多细节，因此准确权限很重要时应检查结果。

## 查看和设置 Umask

运行不带操作数的 `umask`，显示当前 shell 的掩码，通常采用八进制形式：

```bash
$ umask
0022
```

为当前 shell 及之后由该 shell 启动的进程设置它：

```bash
$ umask 027
```

每个八进制位置分别对应所有者、组和其他。掩码位会移除相应的已请求权限：`2` 掩蔽写入，`4` 掩蔽读取，`1` 掩蔽执行。

:::single-choice{#umask-command-purpose}
`umask 027` 会在当前 shell 中更改什么？

::option[每个已经存在的文件的权限。]{#umask-existing-files explanation="umask 影响创建请求，不会追溯性地对现有对象运行 `chmod`。"}
::option[之后从该 shell 启动的命令所继承的掩码。]{#umask-current-shell-mask .correct explanation="shell 会设置自己的进程 umask，子进程通常继承该值。"}
::option[新文件中存储的所有者和组名称。]{#umask-owner-group explanation="掩码会筛选权限位，不会选择所有权身份。"}
:::

## 计算新文件和目录模式

许多普通程序为新普通文件请求 `0666`，因为默认创建可执行文件并不安全。它们通常为新目录请求 `0777`，目录需要执行权限才能遍历。

使用 umask `0022` 时：

```text
普通文件：0666 由 0022 掩蔽 -> 0644 (rw-r--r--)
目录：    0777 由 0022 掩蔽 -> 0755 (rwxr-xr-x)
```

umask 只会移除已请求的权限位。如果应用程序没有请求执行权限，它不能添加该权限。应用程序也可以请求更严格的起始模式，从而产生更严格的结果。

:::single-choice{#umask-file-mode-022}
如果程序为普通文件请求模式 `0666`，umask 为 `0022`，结果是哪种模式？

::option[`0666`]{#umask-file-0666 explanation="`0666` 请求的组和其他写入位会被掩码 `0022` 移除。"}
::option[`0755`]{#umask-file-0755 explanation="普通文件没有请求执行位，因此 umask 无法添加它们。"}
::option[`0644`]{#umask-file-0644 .correct explanation="从 `0666` 移除组和其他写入后，会留下所有者读写以及组和其他只读。"}
:::

:::single-choice{#umask-directory-mode-027}
如果程序为目录请求 `0777`，umask 为 `0027`，结果是哪种模式？

::option[`0777`]{#umask-directory-0777 explanation="非零掩码会筛掉已请求的组写入和其他权限。"}
::option[`0640`]{#umask-directory-0640 explanation="该结果还移除了掩码 `0027` 并未从所有者或组移除的执行位。"}
::option[`0750`]{#umask-directory-0750 .correct explanation="掩码会移除组写入和其他的全部权限，留下 `rwxr-x---`。"}
:::

## 作用范围和持久性

在一个 shell 中更改 umask，不会改变其父进程或无关会话。该值适用于该 shell 及其后代之后创建的对象；现有文件会保留自身模式。

要持久使用首选值，应在适合当前环境的登录、shell、PAM、服务管理器或应用程序配置中设置它。正确位置各不相同，服务也可能自行设置 umask。不要假设编辑一个交互式 shell 文件就能控制系统中的每个进程。

:::single-choice{#umask-existing-file-effect}
设置新的 umask 时，现有文件会发生什么？

::option[其当前模式保持不变。]{#umask-existing-unchanged .correct explanation="新 umask 会筛选之后的创建请求，不会修改已经存储在文件系统对象上的模式。"}
::option[其模式会根据 `0666` 重新计算。]{#umask-existing-recalculated explanation="现有对象不会被重新创建，也不会自动通过新掩码处理。"}
::option[其所有者会立即失去被掩蔽的权限。]{#umask-existing-owner-loss explanation="更改进程 umask 不是针对现有文件元数据的操作。"}
:::

要动手练习，请在隔离环境中使用不同掩码创建文件和目录，再用 `ls -ld` 比较模式。[Linux 用户组和文件权限](https://labex.io/zh/labs/linux-linux-user-group-and-file-permissions-18002) 实验提供了合适的权限工作区。

## 总结

现在，你可以预测 umask 如何限制新请求的权限。

1. 使用 `umask` 查看或设置当前 shell 的掩码。
2. 从应用程序请求的模式中移除被掩蔽的位。
3. 区分普通文件常请求的 `0666` 和目录常请求的 `0777`。
4. 把 umask 的作用范围和持久性视为特定于进程及环境的行为。
