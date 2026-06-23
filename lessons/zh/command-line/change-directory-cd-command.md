---
index: 3
lang: "zh"
title: "cd（切换目录）"
meta_title: "cd（切换目录）- 命令行"
meta_description: "通过示例学习 Linux cd 命令，包括绝对路径、相对路径、主目录快捷方式、父目录和上一个目录的导航。"
meta_keywords: "cd 命令, linux cd 命令, 切换目录, cd 父目录, cd 主目录, cd 上一个目录, 绝对路径, 相对路径"
---

## Lesson Content

在 Linux 文件系统中移动时，你需要使用路径来指定目标位置。主要工具是 `cd` 命令，意为切换目录。它会更改 shell 当前的工作目录。

基本语法是：

```bash
cd [DIRECTORY]
```

### 理解路径

指定路径有两种方式：绝对路径和相对路径。

- **绝对路径**：从根目录（`/`）开始的完整路径。例如：`/home/pete/Desktop`。

- **相对路径**：基于你当前所在位置的路径。如果你在 `/home/pete/Documents`，想访问名为 `taxes` 的子目录，可以使用 `taxes/`。

### 使用 cd 命令

要使用绝对路径切换到特定目录，输入：

```bash
$ cd /home/pete/Pictures
```

此命令会直接切换到 `Pictures` 目录。

你可以用 `pwd` 确认你的位置：

```bash
$ pwd
/home/pete/Pictures
```

### 进入子目录

如果你已经在某个目录，想进入子目录，可以使用相对路径。例如，当前目录是 `/home/pete/Pictures`，其中有一个名为 `Hawaii` 的文件夹，你可以这样进入：

```bash
$ cd Hawaii
```

注意我们只用了文件夹名，因为我们已经在它的父目录 `/home/pete/Pictures` 中。

### 重要的导航快捷方式

使用完整路径导航可能很繁琐。幸运的是，shell 提供了几个快捷方式，让移动更快。

- `.`（当前目录）：表示你当前所在的目录。
- `..`（父目录）：向上一级，进入包含当前目录的目录。
- `~`（主目录）：指向你的个人主目录，比如 `/home/pete`。
- `-`（上一个目录）：返回你之前所在的目录。

你可以和 `cd` 一起使用这些快捷方式：

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

多练习这些快捷方式，可以让你在命令行中更高效。

### 实用 cd 示例

进入你的主目录：

```bash
$ cd
```

向上两级：

```bash
$ cd ../..
```

进入包含空格的目录名，使用引号：

```bash
$ cd "Vacation Photos"
```

返回上一个目录：

```bash
$ cd -
/home/pete/Documents
```

### 常见问题

**为什么 cd 提示“没有那个文件或目录”？** 路径在你当前的位置不存在，或者名字输入错误。使用 `ls` 列出可用目录。

**为什么 cd 提示“权限被拒绝”？** 你没有权限进入该目录。

**运行 cd 不带参数会怎样？** 它会带你进入你的主目录。

**cd 可以用来进入文件吗？** 不可以。`cd` 只能进入目录，不能进入普通文件。

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux directory navigation:

1. **[Linux cd Command: Directory Changing](https://labex.io/zh/labs/linux-linux-cd-command-directory-changing-209733)** - Learn the Linux `cd` command to efficiently navigate your file system, including various techniques for changing directories, understanding paths, and exploring the file structure.
2. **[Linux Directory Navigation](https://labex.io/zh/labs/linux-directory-navigation-387844)** - Put your basic Linux command-line skills to the test by navigating through directories using essential commands.
3. **[Setting Up a New Project Structure](https://labex.io/zh/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts in real scenarios and build confidence with navigating the Linux filesystem.

## Quiz Question

如果你当前在 `/home/pete/Pictures`，想切换到父目录（`/home/pete`），你应该使用什么完整命令？请用英文回答，注意大小写和空格。

## Quiz Answer

cd ..
