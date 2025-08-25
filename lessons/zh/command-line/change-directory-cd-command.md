---
index: 3
lang: "zh"
title: "cd (更改目录)"
meta_title: "cd (更改目录) - 命令行"
meta_description: "学习如何在 Linux 中使用 'cd' 命令导航目录。了解绝对路径、相对路径和有用的快捷方式。开始您的 Linux 之旅！"
meta_keywords: "cd 命令，更改目录，Linux 路径，绝对路径，相对路径，Linux 教程，Linux 初学者，Linux 导航"
---

## Lesson Content

既然您知道自己身在何处，那么让我们在文件系统中稍微移动一下。请记住，我们需要使用路径来导航。有两种不同的方法来指定路径：绝对路径和相对路径。

- 绝对路径：这是从根目录开始的路径。根目录是最高级的。根目录通常显示为斜杠 (`/`)。每当您的路径以 `/` 开头时，都意味着您从根目录开始。例如，`/home/pete/Desktop`。

- 相对路径：这是从您当前在文件系统中的位置开始的路径。如果我在 `/home/pete/Documents` 位置，并且想进入 `Documents` 内部一个名为 `taxes` 的目录，我不需要指定从根目录开始的完整路径，例如 `/home/pete/Documents/taxes`；我可以直接进入 `taxes/`。

既然您知道路径是如何工作的，我们只需要一个工具来帮助我们更改到我们想要的目录。幸运的是，我们有 `cd` 或“change directory”来完成这项工作。

```bash
cd /home/pete/Pictures
```

所以现在我已将我的目录位置更改为 `/home/pete/Pictures`。

现在从这个目录中，我有一个名为 `Hawaii` 的文件夹。我可以使用以下命令导航到该文件夹：

```bash
cd Hawaii
```

注意到我只使用了文件夹的名称吗？那是因为我已经在 `/home/pete/Pictures` 中了。

一直使用绝对路径和相对路径导航可能会很累。幸运的是，有一些快捷方式可以帮助您。

- `.` (当前目录)：这是您当前所在的目录。
- `..` (上级目录)：将您带到当前目录的上一级目录。
- `~` (家目录)：此目录默认为您的“家目录”，例如 `/home/pete`。
- `-` (上一个目录)：这将带您回到您刚刚所在的上一个目录。

```bash
cd .
cd ..
cd ~
cd -
```

试试看吧！

## Exercise

熟能生巧！以下是一些动手实验，以加强您对 Linux 目录导航的理解：

1. **[Linux cd 命令：目录切换](https://labex.io/zh/labs/linux-linux-cd-command-directory-changing-209733)** - 学习 Linux `cd` 命令以高效地导航您的文件系统，包括各种更改目录的技术、理解路径和探索文件结构。
2. **[Linux 目录导航](https://labex.io/zh/labs/linux-directory-navigation-387844)** - 通过使用基本命令导航目录来测试您的基本 Linux 命令行技能。
3. **[设置新项目结构](https://labex.io/zh/labs/linux-setting-up-a-new-project-structure-387859)** - 通过创建特定的项目结构并使用 `mkdir` 和 `cd` 等基本命令导航它来练习您的 Linux 目录管理技能。

这些实验将帮助您在实际场景中应用概念，并增强您导航 Linux 文件系统的信心。

## Quiz Question

如果您在 `/home/pete/Pictures` 中，想去 `/home/pete`，有什么好的快捷方式可以使用？

## Quiz Answer

cd ..
