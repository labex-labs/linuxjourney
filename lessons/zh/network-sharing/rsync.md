---
lesson_id: "rsync"
course_id: "network-sharing"
lang: "zh"
order_index: 2
title: "rsync"
description: "学习如何预览、运行并验证安全的本地或基于 SSH 的 rsync 目录同步。"
meta_title: "rsync - 网络共享"
meta_description: "了解如何在 Linux 中使用强大的 rsync 命令高效同步文件、远程传输数据和可靠备份。本指南介绍关键 rsync 命令和选项。"
meta_keywords: "rsync, Linux rsync, 文件同步, 数据备份, 远程同步, rsync 命令, Linux 文件传输, rsync 教程"
---

`rsync` 会协调文件和目录树，同时避免不必要地传输未变化的数据。高效并不意味着每次调用都安全：源语法、末尾斜杠、元数据、排除项和删除策略共同决定结果。

## 理解源与目标

在本地将 `source/` 的内容同步到 `destination/`：

```bash
$ rsync -a -- source/ destination/
```

`source/` 末尾的斜杠表示“复制该目录的内容”。如果没有斜杠，`rsync -a source destination/` 会创建或更新 `destination/source`。改变斜杠位置时，务必预览最终路径。

:::single-choice{#rsync-source-trailing-slash} `rsync -a source/ destination/` 中源末尾的斜杠表示什么？

::option[成功传输后删除源。]{#rsync-delete-source explanation="移除源需要单独的明确选项和策略。"}
::option[将 `source` 的内容复制到目标。]{#rsync-copy-contents .correct explanation="移除源斜杠会改变目标的顶层布局。"}
::option[将目标解释为远程 Windows 共享。]{#rsync-windows-share explanation="斜杠控制目录内容，而不是传输类型。"}
:::

## 理解归档模式

归档模式 `-a` 等效于一组递归和元数据保留选项，通常概括为 `-rlptgoD`。在权限和平台支持允许时，它会保留符号链接、权限、修改时间、组、所有者及设备或特殊文件。

归档模式不包括保留硬链接、ACL 或扩展属性；这些通常分别需要 `-H`、`-A` 和 `-X`。它本身也不会创建历史版本。

:::single-choice{#rsync-archive-limit} 哪项元数据不包含在单独的 `-a` 中？

::option[硬链接关系。]{#rsync-hard-links .correct explanation="保留硬链接需要单独的 -H 选项。"}
::option[目录递归。]{#rsync-archive-recursion explanation="归档模式包含递归遍历。"}
::option[修改时间。]{#rsync-archive-times explanation="归档模式包含时间保留。"}
:::

## 预览传输

在具有重要影响的同步前，使用试运行和逐项变更：

```bash
$ rsync -a --dry-run --itemize-changes -- source/ destination/
```

试运行根据当前扫描预测操作，但不能保证文件在实际命令前不会变化。保存并审查确切命令，只有确认两个端点后，才能移除 `--dry-run` 运行。

:::single-choice{#rsync-dry-run-purpose} `--dry-run --itemize-changes` 提供什么？

::option[保留在另一台设备上的永久快照。]{#rsync-dry-backup explanation="试运行不会复制数据或创建独立保留。"}
::option[保证源文件以后无法变化。]{#rsync-dry-lock explanation="预览不会锁定源目录树。"}
::option[预览 rsync 当前计划的变更。]{#rsync-dry-preview .correct explanation="逐项试运行输出会在更改前公开路径和元数据决策。"}
:::

## 通过 SSH 同步

使用熟悉的远程操作数向远程主机推送或从中拉取：

```bash
$ rsync -a -- source/ alice@example.net:/srv/data/
$ rsync -a -- alice@example.net:/srv/data/ destination/
```

现代 rsync 通常对这种形式使用 SSH，但应确认配置的远程 shell、主机密钥、账户权限以及远端是否有 rsync。`-z` 压缩可以帮助在受限链路上传输可压缩数据，但对已经压缩的数据可能浪费 CPU。

:::single-choice{#rsync-pull-direction} 哪种操作数顺序会把远程数据拉取到本地目录？

::option[`rsync -a local/ host:/data/`]{#rsync-local-first explanation="该顺序会把本地内容推送到远程目标。"}
::option[`rsync --delete host local`]{#rsync-missing-path explanation="它没有表达所示远程路径语法，还添加了无关的破坏性选项。"}
::option[`rsync -a host:/data/ local/`]{#rsync-remote-first .correct explanation="远程目录树是源，本地目录树是目标。"}
:::

## 将删除视为破坏性操作

`--delete` 会在同步范围内删除目标中存在、源中不存在的条目。因此，端点颠倒、斜杠错误或排除项错误都可能擦除有效数据。授权前，应使用测试目标预览、确保存在可恢复备份、检查挂载状态，并考虑最大删除数量限制。

实际运行后，应检查退出状态和日志、比较预期文件数及元数据，并测试代表性内容或恢复。rsync 同步本身也会镜像不必要的删除或损坏，并不是完整备份策略。

:::single-choice{#rsync-delete-effect} `--delete` 在同步期间可能做什么？

::option[使用 SSH 主机密钥加密每个传输文件。]{#rsync-delete-encrypt explanation="删除策略与文件加密无关。"}
::option[阻止目标文件系统的一切更改。]{#rsync-delete-readonly explanation="它明确授权额外的目标更改。"}
::option[移除所选源范围中不存在的目标条目。]{#rsync-delete-destination .correct explanation="该选项使目标成员关系镜像源，需要经过审查的预览和恢复计划。"}
:::

## 总结

现在，你可以预览并验证 `rsync` 操作，而不会忽略其破坏性边缘情况。

1. 使用末尾斜杠表达预期目录布局。
2. 必要时添加归档模式未覆盖的元数据选项。
3. 实际同步前审查逐项试运行输出。
4. 验证 SSH 身份和端点方向。
5. 将删除和备份保留视为明确策略。
