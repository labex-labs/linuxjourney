---
lesson_id: "remove-rm-command"
course_id: "command-line"
lang: "zh"
order_index: 13
title: "rm（删除）"
description: "学习在确认目标并选择更安全的 rm 选项后删除文件和目录。"
meta_title: "rm（删除）- 命令行"
meta_description: "学习 Linux rm 命令，包含安全示例，教你如何删除文件、移除目录、使用 rm -r、rm -i 以及避免 rm -rf 错误。"
meta_keywords: "linux rm 命令, rm 命令, rm -r, rm -i, rm -f, rm -rf, 删除文件 linux, 移除目录 linux, rmdir"
---

`rm` 命令用于移除文件系统条目。命令行删除通常不会把条目送入桌面回收站，而且 `rm` 没有内置撤销功能，因此运行前应确认每个目标。

基本语法是：

```bash
rm [OPTIONS] FILE...
```

## 删除文件

要删除一个文件，只需将文件名传递给 `rm`。

```bash
$ rm file1
```

你也可以一次删除多个文件，只需依次列出它们。

```bash
$ rm notes.txt old-report.txt draft.md
```

按 Enter 前应检查拼写和位置。删除后依赖备份或版本控制副本恢复，要比指望文件系统恢复工具更可靠。

:::single-choice{#remove-one-file} 确认目标无误后，哪个命令会删除文件 `old-report.txt`？

::option[`rm old-report.txt`]{#rm-report .correct explanation="`rm` 会移除指定的文件条目；此操作通常不会把文件放入回收站。"}
::option[`rmdir old-report.txt`]{#rmdir-report explanation="`rmdir` 作用于空目录，而非普通文件；它不适合这个目标。"}
::option[`mv old-report.txt`]{#mv-report explanation="`mv` 需要目标位置，用于更改路径而不是删除；这条不完整的命令无法完成所需删除。"}
:::

## 预览通配符目标

Shell 通配符允许你匹配多个文件。例如，这条命令会删除当前目录下所有 `.tmp` 文件：

```bash
$ rm *.tmp
```

在使用带通配符的 `rm` 之前，最好先用 `ls` 预览匹配的文件。

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

shell 会在 `rm` 启动前展开模式。如果预览中出现意外文件，应修改模式，而不是继续执行。

:::single-choice{#preview-removal-pattern} 你准备删除 `*.tmp`。哪个命令会先显示该模式选中的非隐藏路径，而不删除它们？

::option[`rm -v *.tmp`]{#verbose-remove explanation="详细模式会在删除发生时报告操作，仍会删除匹配文件，并不是只读预览。"}
::option[`ls '*.tmp'`]{#quoted-pattern explanation="引号会阻止通配符展开，因此它会查找名称中真的含 `*` 的条目，而不是预览目标。"}
::option[`ls *.tmp`]{#list-temp-matches .correct explanation="shell 会为 `ls` 展开 `*.tmp`，让你在删除前查看同一组非隐藏匹配项。"}
:::

## 请求确认

为了更安全，可以使用 `-i` 选项。它会在删除每个文件前提示确认。

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

GNU `rm` 的 `-I` 是干扰更少的保护措施：当命令将删除三个以上文件或执行递归操作时，它只询问一次。

:::single-choice{#confirm-each-removal} 哪个命令会在删除每个指定文件前请求确认？

::option[`rm -i important.txt`]{#interactive-important .correct explanation="`-i` 会在每次删除前提示，让你有机会拒绝操作。"}
::option[`rm -f important.txt`]{#force-important explanation="`-f` 会抑制提示并忽略缺失操作数，减少而不是增加确认。"}
::option[`rm -v important.txt`]{#verbose-important explanation="`-v` 会报告已删除的内容，但不会事先请求批准。"}
:::

## 使用 -f 忽略缺失文件

`-f` 选项表示“强制”。它会忽略不存在的文件且不提示确认。

```bash
$ rm -f old-cache.txt
```

如果生成的文件可能已经不存在，这能让脚本清理操作保持幂等。由于它会取消确认，不要只为了压下尚未理解的错误而添加 `-f`。

## 删除目录

默认情况下，`rm` 不能删除目录。

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

要删除目录及其内部所有内容，使用 `-r` 或 `-R` 进行递归删除。

```bash
$ rm -r old-project
```

对于空目录，`rmdir` 是范围更窄的替代命令：

```bash
$ rmdir empty-directory
```

`rmdir` 会在目录非空时失败，从而保护其中内容不被递归删除。

:::single-choice{#remove-empty-directory-only} 哪个命令只在 `old-cache/` 为空时删除该目录？

::option[`rm -r old-cache/`]{#recursive-cache explanation="递归 `rm` 会删除目录及其中内容，并不强制要求目录为空。"}
::option[`rmdir old-cache/`]{#rmdir-cache .correct explanation="`rmdir` 只会对空目录成功，因此不会递归删除其中的文件。"}
::option[`rm -f old-cache/`]{#force-cache explanation="`-f` 不会让普通 `rm` 删除目录，而且它会抑制保护措施，并不检查目录是否为空。"}
:::

## 检查递归删除

递归删除可以清除整棵目录树。把 `-r` 与 `-f` 结合还会取消提示，因此使用 `rm -rf` 前必须特别仔细地验证目标。执行任何递归删除前，请检查：

- 你是否处于预期目录？使用 `pwd`。
- `ls -ld -- TARGET` 是否显示预期的顶层路径？
- 如果涉及通配符，只读预览是否准确匹配预期内容？
- 路径是绝对路径还是相对路径？`/tmp/cache` 和 `tmp/cache` 差别很大。
- 是否有意外空格？`rm -rf old-project` 和 `rm -rf old project` 指向不同路径。

如果目标可能以连字符开头，请在它之前使用 `--`，避免被解释为选项：

```bash
$ rm -- -old-name
```

不要仅因为 `rm` 报告权限错误就直接使用 `sudo`。应先确认目标，并查明当前账户为何不能修改其所在目录。提升权限的递归删除可能损坏操作系统或其他用户的数据。

需要让 `rm` 报告每次成功删除时，可以使用 `-v`：

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

:::single-choice{#remove-nonempty-tree} 确认完整目标无误后，哪个命令会删除 `old-project/` 及其下所有内容，同时仍允许正常提示？

::option[`rm old-project/`]{#plain-rm-project explanation="普通 `rm` 不会进入目录，因此不能删除非空目录树。"}
::option[`rm -r old-project/`]{#recursive-old-project .correct explanation="`-r` 会递归删除目录树；与 `rm -rf` 不同，这种形式没有用 `-f` 抑制提示。"}
::option[`rmdir old-project/`]{#rmdir-project explanation="`rmdir` 要求目录为空；项目中仍含条目时会失败。"}
:::

要在受控环境中练习删除，可以尝试以下动手实验：

1. **[Linux rm 命令：文件删除](https://labex.io/zh/labs/linux-linux-rm-command-file-removing-209741)** - 学习如何使用 `rm` 命令删除文件和目录，包括 `-r` 和 `-i` 等选项，练习安全有效的文件删除。
2. **[文件和目录的组织](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 练习基本的 Linux 文件管理技能，包括使用 `rm` 命令清理不必要的目录，通过实际挑战提升能力。

## 总结

现在，你可以删除文件系统条目，并把每个目标都视为不可撤销操作。

1. 删除前确认文件路径。
2. 使用只读命令预览通配符展开结果。
3. 使用 `-i` 或 `-I` 请求确认。
4. 目录必须为空时优先使用 `rmdir`。
5. 使用递归删除前验证整个目标。
