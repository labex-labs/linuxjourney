---
index: 13
lang: "zh"
title: "rm（删除）"
meta_title: "rm（删除）- 命令行"
meta_description: "学习 Linux rm 命令，包含安全示例，教你如何删除文件、移除目录、使用 rm -r、rm -i 以及避免 rm -rf 错误。"
meta_keywords: "linux rm 命令, rm 命令, rm -r, rm -i, rm -f, rm -rf, 删除文件 linux, 移除目录 linux, rmdir"
---

## Lesson Content

在 Linux 中，积累不再需要的文件是很常见的。要删除它们，你可以使用 `rm`（remove）命令，这是管理文件系统的基本工具。基本语法是：

```bash
rm [OPTIONS] FILE...
```

`rm` 命令从文件系统中移除目录项。通俗来说，它就是删除文件。与许多桌面环境不同，命令行删除通常不会将文件移动到回收站，因此在按下回车前应仔细检查命令。

### 删除单个文件

要删除一个文件，只需将文件名传递给 `rm`。

```bash
$ rm file1
```

你也可以一次删除多个文件，只需依次列出它们。

```bash
$ rm notes.txt old-report.txt draft.md
```

这对于快速清理很有用，但也意味着输入错误可能会删除比预期更多的文件。

### 使用通配符删除文件

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

记住，shell 会在 `rm` 运行前展开 `*.tmp`。如果模式匹配的文件比预期多，`rm` 仍会接收所有这些文件。

### 使用 -i 进行交互式删除

为了更安全，可以使用 `-i` 选项。它会在删除每个文件前提示确认。

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

当从共享目录删除文件、清理大量文件或首次学习该命令时，使用 `rm -i` 是个好习惯。

### 使用 -f 强制删除

`-f` 选项表示“强制”。它会忽略不存在的文件且不提示确认。

```bash
$ rm -f old-cache.txt
```

这在脚本中很有用，即使文件已经不存在，清理操作也能继续。

```bash
$ rm -f build.log
```

请小心：`-f` 也会屏蔽一些安全提示，可能掩盖错误。

### 使用 -r 删除目录

默认情况下，`rm` 不能删除目录。

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

要删除目录及其内部所有内容，使用 `-r` 或 `-R` 进行递归删除。

```bash
$ rm -r old-project
```

递归删除会遍历目录树，删除文件、子目录及其内容。

### rm -rf 的危险

命令 `rm -rf` 结合了递归删除和强制删除。

```bash
$ rm -rf old-project
```

该命令适合删除生成的文件夹（如构建输出），但很危险，因为它会无提示地删除整个目录树。务必检查：

- 你是否在预期的目录？使用 `pwd` 确认。
- 通配符是否正确展开？用 `ls` 预览。
- 路径是绝对路径还是相对路径？`/tmp/cache` 和 `tmp/cache` 差别很大。
- 是否有意外空格？`rm -rf old-project` 和 `rm -rf old project` 是不同的路径。

### 使用 rmdir 删除空目录

作为更安全的替代方案，可以用 `rmdir` 删除空目录。

```bash
$ rmdir empty-directory
```

`rmdir` 只有在目录完全为空时才会成功，因此比 `rm -r` 更安全，适合清理任务。

### 常用 rm 选项

以下是你最常见的选项：

- `-i`：删除前逐个提示确认。
- `-I`：删除超过三个文件或递归删除时，提示一次确认。
- `-f`：强制删除，忽略不存在的文件。
- `-r` 或 `-R`：递归删除目录及其内容。
- `-v`：显示删除了什么。

例如，你可以组合使用选项：

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

### 常见问题

**我可以撤销 rm 吗？** 通常不行。一旦用 `rm` 删除了文件，没有内置的撤销命令。备份、版本控制和文件系统恢复工具才是真正的安全保障。

**为什么 rm 提示“Permission denied”？** 你没有权限删除该文件或修改包含它的目录。用 `ls -l` 检查所有权和权限。

**为什么 rm 提示“No such file or directory”？** 该路径下不存在文件，或者你所在目录不是预期的。用 `pwd` 和 `ls` 确认。

**我应该用 sudo 执行 rm 吗？** 只有在完全理解要删除的路径时才使用。`sudo rm -r` 可能删除系统文件，普通用户账户无法操作的文件也会被删除。

## Exercise

实践是关键。以下是一些动手练习，帮助你巩固 Linux 中删除文件和目录的知识：

1. **[Linux rm 命令：文件删除](https://labex.io/zh/labs/linux-linux-rm-command-file-removing-209741)** - 学习如何使用 `rm` 命令删除文件和目录，包括 `-r` 和 `-i` 等选项，练习安全有效的文件删除。
2. **[文件和目录的组织](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 练习基本的 Linux 文件管理技能，包括使用 `rm` 命令清理不必要的目录，通过实际挑战提升能力。

这些实验将帮助你在真实场景中应用这些概念，增强对 `linux rm command` 的信心。

## Quiz Question

如何删除名为 `myfile` 的文件？请用英文回答，且使用准确、区分大小写的命令。

## Quiz Answer

rm myfile
