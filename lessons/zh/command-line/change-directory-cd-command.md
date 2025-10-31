---
index: 3
lang: "zh"
title: "cd (切换目录)"
meta_title: "cd (切换目录) - 命令行"
meta_description: "学习使用 essential cd linux 命令来更改目录。本指南涵盖了如何在命令提示符下使用 cd 命令，使用绝对路径和相对路径导航到任何 cd 文件夹，以及使用有用的快捷方式。"
meta_keywords: "cd 命令，cd linux 命令，cd 文件夹，cd 命令提示符，cd 命令 cmd, 更改目录，linux 导航，绝对路径，相对路径"
---

## Lesson Content

为了在 Linux 文件系统中移动，您将使用路径来指定目的地。主要的工具是 `cd`（更改目录）命令。理解如何使用这个 `cd linux 命令` 是在终端或 `cd 命令提示符` 中工作的基本技能。

### 理解路径

有两种指定路径的方式：绝对路径和相对路径。

- **绝对路径 (Absolute Path)**：这是从根目录 (`/`) 开始的完整路径。根目录是文件系统中的顶层目录。任何以 `/` 开头的路径都是绝对路径。例如：`/home/pete/Desktop`。

- **相对路径 (Relative Path)**：此路径相对于您在文件系统中的当前位置。如果您位于 `/home/pete/Documents` 并且想要访问名为 `taxes` 的子目录，则不需要完整路径。您可以简单地使用相对路径：`taxes/`。

### 使用 cd 命令

了解路径后，您就可以使用 `cd 命令` 来更改当前目录了。无论您是在 Linux 终端还是 Windows `cd 命令 cmd` 提示符中，更改目录的概念都是通用的，尽管语法可能略有不同。

要使用绝对路径更改到特定目录，您将输入：

```bash
cd /home/pete/Pictures
```

此命令将直接将您移动到 `Pictures` 目录。

### 导航到 cd 文件夹

如果您已经在某个目录中并想移动到子目录，您可以使用相对路径。例如，如果您的当前位置是 `/home/pete/Pictures` 并且其中包含一个名为 `Hawaii` 的 `cd 文件夹`，您可以使用以下命令导航到其中：

```bash
cd Hawaii
```

请注意，我们只使用了文件夹的名称。这是因为我们已经在其父目录 `/home/pete/Pictures` 中。

### 基本导航快捷方式

使用完整路径进行导航可能会很繁琐。幸运的是，Shell 提供了一些快捷方式，使移动速度快得多。

- `.` (当前目录)：表示您当前所在的目录。
- `..` (父目录)：将您向上移动一级到包含您当前目录的目录。
- `~` (主目录)：指向您的个人主目录（如 `/home/pete`）的快捷方式。
- `-` (前一个目录)：将您带回到您上一个所在的目录。

You can use these shortcuts with the `cd command`:

```bash
cd .
cd ..
cd ~
cd -
```

试验这些快捷方式，以提高在命令行上的效率。

## Exercise

实践造就完美！这里有一些动手实验，以加强您对 Linux 目录导航的理解：

1. **[Linux cd 命令：目录更改](https://labex.io/zh/labs/linux-linux-cd-command-directory-changing-209733)** - 学习 Linux `cd` 命令，以有效地导航文件系统，包括更改目录的各种技术、理解路径和探索文件结构。
2. **[Linux 目录导航](https://labex.io/zh/labs/linux-directory-navigation-387844)** - 通过使用基本命令在目录之间导航，来测试您的基本 Linux 命令行技能。
3. **[设置新的项目结构](https://labex.io/zh/labs/linux-setting-up-a-new-project-structure-387859)** - 通过创建特定的项目结构并使用 `mkdir` 和 `cd` 等基本命令进行导航，来练习您的 Linux 目录管理技能。

这些实验将帮助您在实际场景中应用这些概念，并建立对导航 Linux 文件系统的信心。

## Quiz Question

如果您在 `/home/pete/Pictures` 中，想要导航到父目录 (`/home/pete`)，您应该使用的完整命令是什么？请用英语回答，注意大小写和空格。

## Quiz Answer

cd ..
