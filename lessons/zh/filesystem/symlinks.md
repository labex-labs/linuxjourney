---
lesson_id: "symlinks"
course_id: "filesystem"
lang: "zh"
order_index: 12
title: "符号链接"
description: "了解符号链接与硬链接在路径名解析、inode 身份和文件系统范围上的差异。"
meta_title: "符号链接 - 文件系统"
meta_description: "探索 Linux 符号链接（软链接）和硬链接。学习如何使用 ln 命令创建它们，使用 ls 命令检查 Linux 中的链接数，并理解 ls 输出中符号链接和硬链接的区别。"
meta_keywords: "Linux 符号链接，硬链接，ln 命令，软链接，ls 符号链接，Linux 链接数，ls 符号链接，ls 链接，Linux 文件系统，Linux 教程"
---

目录条目为 inode 提供名称。硬链接会为同一个 inode 创建另一个目录条目，符号链接则创建一个不同的 inode，其内容是需要解析的路径名。这项差异决定了身份、生命周期和跨文件系统行为。

## 创建并检查符号链接

使用 `ln -s TARGET LINK_NAME` 创建符号链接：

```bash
$ printf '%s\n' 'example' > myfile
$ ln -s -- myfile myfilelink
$ ls -li myfile myfilelink
151   -rw-r--r-- 1 user user 8 ... myfile
93403 lrwxrwxrwx 1 user user 6 ... myfilelink -> myfile
```

符号链接拥有自己的 inode，并存储文本 `myfile`。程序跟随 `myfilelink` 时，路径名解析会继续转向目标。使用以下命令可以显示已存储文本，而不跟随链接：

```bash
$ readlink myfilelink
```

:::single-choice{#symlinks-create-symbolic}
哪个命令创建名为 `myfilelink`、目标文本为 `myfile` 的符号链接？

::option[`ln -s -- myfile myfilelink`]{#symlinks-ln-s .correct explanation="`-s` 选项请求创建符号链接，后面依次是目标和新链接名称。"}
::option[`ln -- myfile myfilelink`]{#symlinks-ln-hard explanation="没有 `-s` 时，`ln` 请求为现有 inode 创建硬链接。"}
::option[`readlink myfile myfilelink`]{#symlinks-readlink-create explanation="Readlink 用于检查符号链接，不会创建链接。"}
:::

## 相对与绝对符号链接目标

绝对目标从 `/` 开始。相对目标相对于符号链接所在目录解析，而不是相对于将来某个程序打开它时 shell 的当前目录解析。

```bash
$ mkdir -p tree/data tree/current
$ printf '%s\n' 'value' > tree/data/item
$ ln -s ../data/item tree/current/item
```

整体移动 `tree` 层次仍能保持这一相对关系；只移动链接或目标则可能破坏关系。符号链接允许保存不存在的目标，此时称为悬空链接或断链。

:::single-choice{#symlinks-relative-resolution}
相对符号链接目标从哪里开始解析？

::option[创建它的用户的家目录。]{#symlinks-creator-home explanation="创建者身份不会成为永久解析基准。"}
::option[第一次列出它的 shell 的当前目录。]{#symlinks-listing-shell explanation="列出时的上下文不会重写已存储的目标关系。"}
::option[包含该符号链接的目录。]{#symlinks-containing-directory .correct explanation="路径遍历会在符号链接所在位置替换其保存的相对文本。"}
:::

## 创建硬链接

不使用 `-s`，可以为现有普通文件创建另一个名称：

```bash
$ ln -- myfile myhardlink
$ ls -li myfile myhardlink
151 -rw-r--r-- 2 user user 8 ... myfile
151 -rw-r--r-- 2 user user 8 ... myhardlink
```

两个名称都映射到同一个文件系统和 inode 编号，链接数变为 2。任何一个名称都不是天然的“原件”；通过其中一个名称修改内容会改变共享对象，删除其中一个名称则保留另一个。

硬链接不能跨越文件系统边界，因为 inode 编号只在其文件系统中有意义。Linux 还会限制普通用户为目录创建硬链接，也可能限制为不属于自己的文件创建链接，以防止循环和安全问题。

:::single-choice{#symlinks-hard-link-inode}
指向一个普通文件的两个硬链接共享什么？

::option[只有相似文件名，但文件数据彼此独立。]{#symlinks-separate-data explanation="这描述的是独立副本，而不是硬链接。"}
::option[存储在另一个符号链接 inode 中的路径名。]{#symlinks-stored-path explanation="保存路径文本是符号链接的定义机制。"}
::option[同一个 inode 和文件内容。]{#symlinks-same-inode .correct explanation="每个目录条目都为同一个文件系统对象命名。"}
:::

## 生命周期与删除

删除符号链接会删除链接对象，而不是其目标：

```bash
$ rm -- myfilelink
```

删除一个硬链接名称会减少共享 inode 的链接数。只有链接数归零，而且没有打开的文件描述或其他文件系统引用让对象保持有效时，文件系统才能回收该对象。

删除指向目录的符号链接时应避免末尾斜杠，因为根据命令不同，末尾斜杠路径解析可能会遵循目录语义。先用 `ls -ld -- LINK` 检查，再明确删除链接名称。

:::single-choice{#symlinks-remove-symbolic}
删除符号链接本身时通常会发生什么？

::option[符号链接 inode 和名称被删除，目标保持不变。]{#symlinks-remove-link-only .correct explanation="取消符号链接不会操作其保存的目标文本所指向的对象。"}
::option[目标及其所有硬链接都会自动被删除。]{#symlinks-remove-target explanation="符号链接是独立文件系统对象，并不拥有其目标。"}
::option[删除前目标会复制到符号链接中。]{#symlinks-copy-target explanation="删除操作不会在链接中保留目标内容。"}
:::

## 安全地跟随链接

符号链接可能把特权程序重定向到预期目录之外，也可能在验证与使用之间发生变化。安全程序应避免“先检查、再打开”的路径名竞态，并根据语言和操作系统使用相对于目录、禁止跟随或限制解析范围的接口。

日常检查可以使用：

- `ls -ld LINK` 显示链接本身。
- `readlink LINK` 打印其中保存的目标文本。
- 在 GNU coreutils 中，`stat LINK` 通常报告链接元数据，`stat -L LINK` 则跟随链接。
- `find -L` 会跟随链接并可能遇到循环，只能有意识地使用。

`lrwxrwxrwx` 显示的权限并不是通用访问授权。访问由目录遍历、链接跟随策略和目标权限共同决定；在某些受保护目录规则中，符号链接所有权也很重要。

:::single-choice{#symlinks-readlink-output}
`readlink LINK` 默认打印什么？

::option[符号链接中保存的路径名文本。]{#symlinks-readlink-target-text .correct explanation="它检查链接对象，而不会读取目标文件的内容。"}
::option[目标普通文件的完整字节内容。]{#symlinks-readlink-file-content explanation="要读取目标内容，应在有意识解析后使用文件读取命令。"}
::option[文件系统中任意位置的所有硬链接。]{#symlinks-readlink-all-hard explanation="发现硬链接需要能够识别 inode 的文件系统搜索，与符号链接目标文本无关。"}
:::

可以在[在 Linux 中管理文件和目录](https://labex.io/zh/labs/comptia-manage-files-and-directories-in-linux-590835)实验中，使用可丢弃文件练习链接并比较 inode 编号。

## 总结

现在，你可以选择并检查正确的文件系统链接类型。

1. 使用 `ln -s TARGET LINK` 创建基于路径名的符号链接。
2. 从链接所在目录解析相对目标。
3. 使用 `ln EXISTING LINK` 为同一文件系统中的 inode 创建另一个名称。
4. 区分取消符号链接与取消硬链接。
5. 在特权或递归操作中避免不安全地跟随链接。
