---
lesson_id: "copy-cp-command"
course_id: "command-line"
lang: "zh"
order_index: 10
title: "cp（复制）"
description: "学习复制文件和目录树，并控制覆盖行为与保留的属性。"
meta_title: "cp（复制）- 命令行"
meta_description: "通过示例学习 Linux cp 命令，了解如何复制文件、目录、多文件、通配符、备份以及 cp -r、cp -i 和 cp -p 等选项。"
meta_keywords: "linux cp 命令, cp 命令, 复制文件 linux, cp -r, cp -i, cp -p, cp -a, cp -u, 递归复制, linux 通配符"
---

`cp` 命令复制文件和目录，同时把源文件留在原处。其基本语法是：

```bash
cp [OPTIONS] SOURCE DESTINATION
```

你可以将一个文件复制到另一个文件，将一个或多个文件复制到目录，或者使用正确的选项复制整个目录树。

## 复制单个文件

要复制文件，你需要指定源文件和目标目录或路径。

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

如果 `/home/pete/Documents/cooldocs` 是现有目录，副本会以 `mycoolfile` 为名创建在其中。也可以提供新的目标文件名：

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

在第二个示例中，复制的数据会获得 `mycoolfile_backup` 这个名称。

:::single-choice{#copy-file-under-new-name} 哪个命令会把 `draft.txt` 复制为名为 `final.txt` 的文件，同时保留 `draft.txt`？

::option[`mv draft.txt final.txt`]{#move-draft explanation="`mv` 会重命名或移动原路径，不会按要求把源副本留在原处。"}
::option[`cp final.txt draft.txt`]{#copy-reversed explanation="这里颠倒了源和目标，会从 `final.txt` 复制到 `draft.txt`。"}
::option[`cp draft.txt final.txt`]{#copy-draft .correct explanation="`cp` 读取 `draft.txt` 并创建或替换 `final.txt`，同时保留源文件。"}
:::

## 将多个文件复制到目录

要将多个文件复制到同一目录，先列出所有源文件，最后写目标目录。

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

当你提供多个源文件时，最后一个参数必须是目录。

:::single-choice{#copy-multiple-files} 哪个命令会把 `a.txt` 和 `b.txt` 复制到现有的 `archive/` 目录？

::option[`cp archive/ a.txt b.txt`]{#destination-first explanation="在这种 `cp` 用法中，目标目录应放在最后；放在开头会改变操作数的解释方式。"}
::option[`cp a.txt b.txt archive/`]{#destination-last .correct explanation="存在多个源时，`cp` 会把最后一个现有目录视为前面所有文件的目标。"}
::option[`cp a.txt archive/ b.txt`]{#destination-middle explanation="所有源操作数都必须位于目标之前，现有目录应是最后一个操作数。"}
:::

## 使用通配符选择文件

通配符是特殊字符，帮助你基于模式选择多个文件，提供极大的灵活性。

- `*`：匹配任意字符序列。
- `?`：匹配任意单个字符。
- `[]`：匹配括号内的任意一个字符。

例如，要将当前目录下所有 JPEG 图片复制到 `Pictures` 目录：

```bash
$ cp *.jpg /home/pete/Pictures
```

批量复制前应预览匹配项，尤其是目标中含有重要数据时：

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

:::single-choice{#preview-copy-pattern} 复制 `*.jpg` 前，哪个命令会显示该模式当前匹配到的非隐藏名称？

::option[`cp *.jpg`]{#copy-no-destination explanation="当模式匹配多个名称时，这会尝试在没有明确目标的情况下复制，并不是预览操作。"}
::option[`ls *.jpg`]{#list-jpg-matches .correct explanation="shell 会为 `ls` 展开同一模式，让你在复制前查看匹配名称。"}
::option[`file '*.jpg'`]{#quoted-jpg-pattern explanation="引号会阻止通配符展开，因此 `file` 收到的是字面字符 `*.jpg`，不能预览正常匹配结果。"}
:::

## 复制目录树

如果你尝试使用 `cp` 复制目录而不加任何选项，会收到错误。要复制目录及其所有内容（包括子目录），必须使用 `-r`（递归）标志。

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

此命令将 `Pumpkin` 目录及其所有内容复制到你的 `Documents` 目录。

你也可能看到 `-R`，在典型 Linux 系统中它具有相同的递归作用：

```bash
$ cp -R website /home/pete/backups/
```

归档模式 `-a` 适合备份式复制。它会递归复制，同时保留链接和许多文件属性：

```bash
$ cp -a project/ project-backup/
```

:::single-choice{#archive-directory-tree} 你想对 `project/` 进行递归的备份式复制，并保留链接和许多属性。哪个命令符合要求？

::option[`cp -p project/ project-backup/`]{#preserve-directory-only explanation="`-p` 会保留选定属性，但本身不会让目录复制变为递归操作。"}
::option[`cp -u project/ project-backup/`]{#update-directory-only explanation="`-u` 根据目标状态控制何时复制，并不会单独启用递归目录复制。"}
::option[`cp -a project/ project-backup/`]{#archive-project .correct explanation="归档模式包含递归复制，并保留链接和广泛的属性，适合备份式结果。"}
:::

## 控制覆盖行为

默认情况下，如果目标位置有同名文件，`cp` 会覆盖它。为了防止意外数据丢失，可以使用 `-i`（交互式）标志，覆盖前会提示确认。

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

如果现有目标不应被覆盖，请使用 `-n`：

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

`-f` 会让 GNU `cp` 在无法打开现有目标进行写入时尝试先删除它，再重试复制。它不能替代对目标的谨慎检查。shell 别名也可能自动添加 `-i` 等选项，因此遇到意外提示时应检查配置，不要想当然。

:::single-choice{#skip-existing-destination} 哪个命令会把 `report.txt` 复制到 `backup/`，但在同名目标已存在时跳过它？

::option[`cp -n report.txt backup/`]{#no-clobber-report .correct explanation="`-n` 会阻止 `cp` 覆盖现有目标文件。"}
::option[`cp -i report.txt backup/`]{#interactive-report explanation="`-i` 会在覆盖前询问，结果取决于回答；它不会自动跳过每个现有目标。"}
::option[`cp -f report.txt backup/`]{#force-report explanation="`-f` 可帮助替换最初无法打开的目标，并不提供禁止覆盖的行为。"}
:::

## 保留属性或刷新文件

复制文件时，其元数据（如修改时间和所有权）通常会被更新。要保留这些原始属性，请使用 `-p` 选项。

```bash
$ cp -p mycoolfile /home/pete/backups/
```

`-u` 选项仅在源文件比目标文件新，或者目标文件不存在时才复制。

```bash
$ cp -u *.txt /home/pete/Documents/
```

其他常用选项包括：

- `-f`：强制覆盖，必要时先删除目标文件。
- `-v`：显示复制的每个文件。

要练习复制文件和目录树，可以尝试以下动手实验：

1. **[Linux cp 命令：文件复制](https://labex.io/zh/labs/linux-linux-cp-command-file-copying-209744)** - 练习基本用法、高级选项如递归复制、保留属性以及使用通配符高效复制文件和目录。
2. **[文件和目录的组织](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 通过使用 `cp`、`mv` 和 `rm` 命令，练习 Linux 文件管理技能，组织项目结构，移动文件，清理不必要的目录。

## 总结

现在，你可以复制文件和目录树，并控制如何处理目标。

1. 把源操作数放在目标之前。
2. 批量复制前预览通配符匹配项。
3. 递归复制目录树或使用归档模式。
4. 确认、跳过或有意识地替换现有目标。
5. 按需保留属性或只复制较新的源文件。
