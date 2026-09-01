---
lesson_id: "move-mv-command"
course_id: "command-line"
lang: "zh"
order_index: 11
title: "mv（移动）"
description: "学习重命名和移动文件或目录，并避免意外覆盖。"
meta_title: "mv（移动）- 命令行"
meta_description: "通过示例学习 Linux mv 命令，用于移动文件、重命名文件和目录、移动多个文件以及避免覆盖。"
meta_keywords: "linux mv 命令, mv 命令, 移动文件 linux, 重命名文件 linux, 重命名目录 linux, mv -i, mv -n, mv -t"
---

`mv` 命令用于重命名文件或目录，或将其移到其他位置。与 `cp` 不同，移动成功后不会把原路径留在原处。

基本语法是：

```bash
mv [OPTIONS] SOURCE DESTINATION
```

## 重命名文件和目录

`mv` 最常见的用途之一是重命名。语法很简单：指定旧名称和新名称。

重命名文件：

```bash
$ mv oldfile newfile
```

同样的逻辑适用于重命名目录：

```bash
$ mv old_directory_name new_directory_name
```

:::single-choice{#rename-file-with-mv} 哪个命令会把当前目录中的 `cat` 重命名为 `dog`？

::option[`mv cat dog`]{#rename-cat .correct explanation="`mv` 把 `cat` 视为源路径，把 `dog` 视为新的目标路径。"}
::option[`mv dog cat`]{#rename-dog explanation="操作数顺序颠倒了；这会尝试把现有的 `dog` 重命名为 `cat`。"}
::option[`cp cat dog`]{#copy-cat explanation="`cp` 会创建名为 `dog` 的副本并保留 `cat`，不会执行所需的重命名。"}
:::

## 把条目移动到目录

`mv` 命令的另一个核心功能是将项目从一个位置移动到另一个位置。

将单个文件移动到不同目录：

```bash
$ mv file2 /home/pete/Documents
```

你也可以一次移动多个文件。只需列出所有源文件，后跟目标目录：

```bash
$ mv file_1 file_2 somedirectory/
```

在 GNU/Linux 系统上，一个有用的选项是 `-t`，它允许你先指定目标目录。当移动许多文件时，这样更清晰。

```bash
$ mv -t somedirectory/ file_1 file_2
```

与 `cp` 命令不同，移动目录不需要递归选项。`mv` 默认支持目录。

:::single-choice{#move-multiple-files} 哪个命令会把 `file_1` 和 `file_2` 都移动到现有的 `archive/` 目录？

::option[`mv archive/ file_1 file_2`]{#target-first-without-option explanation="不使用 GNU `-t` 时，多源移动要求目标目录放在最后；这里不是标准的多源形式。"}
::option[`mv -r file_1 file_2 archive/`]{#recursive-move explanation="`mv` 移动文件或目录时不使用 `-r`；普通的多源形式已经能完成所需移动。"}
::option[`mv file_1 file_2 archive/`]{#target-last .correct explanation="存在多个源时，现有目标目录是最后一个操作数，会接收这两个文件。"}
:::

## 控制现有目标

默认情况下，如果你将文件移动到一个已存在同名文件的目标位置，`mv` 会直接覆盖而不提示。为了防止意外数据丢失，你可以使用以下选项：

- **-i（交互式）**：这是一个重要的安全功能。它会在覆盖任何已有文件前提示你确认。

  ```bash
  $ mv -i source_file destination_directory
  ```

- **-n（不覆盖）**：不覆盖现有目标。

  ```bash
  $ mv -n source_file destination_directory
  ```

- **-b（备份）**：在 GNU/Linux 上，为本来会被替换的目标创建备份。默认备份后缀通常是波浪号（`~`）。

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- **-v（详细）**：此选项使 `mv` 命令打印出正在执行的操作，显示每个被移动或重命名的文件。

```bash
$ mv -v file1 file2 somedirectory/
```

:::single-choice{#move-without-overwriting} 哪个命令只会在不覆盖现有目标的情况下把 `draft.txt` 移入 `finished/`？

::option[`mv -i draft.txt finished/`]{#interactive-draft explanation="`-i` 会在目标存在时询问操作；如果用户确认，仍可能发生覆盖。"}
::option[`mv -b draft.txt finished/`]{#backup-draft explanation="`-b` 允许替换，并保留原目标的备份，并不会阻止覆盖。"}
::option[`mv -n draft.txt finished/`]{#no-clobber-draft .correct explanation="`-n` 会跳过任何将覆盖现有目标的移动。"}
:::

## 移动目录和通配符匹配项

移动目录不需要 `-r`：

```bash
$ mv project /home/pete/Documents/
```

shell 通配符可以选择多个源：

```bash
$ ls *.txt
$ mv *.txt notes/
```

用 `ls` 预览匹配项，可以在修改多个路径前发现过于宽泛的模式。

:::single-choice{#move-directory-without-recursion} 哪个命令会把 `project/` 目录移动到 `/srv/archive/`？

::option[`mv -r project/ /srv/archive/`]{#recursive-project explanation="`mv` 不需要也不支持为此使用 `-r`；目录由普通移动操作处理。"}
::option[`mv project/ /srv/archive/`]{#move-project .correct explanation="普通 `mv` 语法无需递归标志即可把目录移入现有目标目录。"}
::option[`cp project/ /srv/archive/`]{#copy-project explanation="普通 `cp` 不会移动目录，而且复制目录还需要递归选项；原目录也会保留。"}
:::

:::single-choice{#preview-text-file-move} 你准备运行 `mv *.txt notes/`。哪个命令会预览相同通配符选中的路径？

::option[`ls '*.txt'`]{#literal-text-pattern explanation="引号会阻止 shell 展开 `*`，因此这会查找名称中真的含星号的条目，而不是预览移动集合。"}
::option[`ls *.txt`]{#list-text-matches .correct explanation="shell 会像为 `mv` 一样为 `ls` 展开 `*.txt`，使你能先检查选中的非隐藏名称。"}
::option[`mv -v *.txt notes/`]{#verbose-text-move explanation="详细模式会在移动发生时报告操作；它会真正执行移动，而不是提供只读预览。"}
:::

要练习移动和重命名条目，可以尝试以下动手实验：

1. **[Linux mv 命令：文件移动与重命名](https://labex.io/zh/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - 练习使用 `mv` 命令移动和重命名文件及目录，理解其各种选项和行为。
2. **[组织文件和目录](https://labex.io/zh/labs/linux-organizing-files-and-directories-387877)** - 在实际挑战中应用 `mv`（以及 `cp` 和 `rm`）知识，整理项目结构，移动文件并清理目录。

## 总结

现在，你可以重命名和移动文件或目录，同时保护现有目标。

1. 把源放在新的目标路径之前。
2. 把目标目录放在多个源之后。
3. 替换目标前选择询问、跳过或备份。
4. 无需递归选项即可移动目录。
5. 批量移动前预览通配符匹配项。
