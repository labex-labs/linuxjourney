---
lang: "zh"
title: "cd (更改目录)"
meta_title: "cd (更改目录) - 命令行"
meta_description: "学习如何在 Linux 中使用'cd'命令来导航目录。理解绝对路径、相对路径和有用的快捷方式。开始您的 Linux 之旅！"
meta_keywords: "cd 命令，更改目录，Linux 路径，绝对路径，相对路径，Linux 教程，Linux 初学者，Linux 导航"
---

## Lesson Content

既然您知道自己身在何处，那么让我们看看是否可以在文件系统中移动一下。请记住，我们需要使用路径来导航。有两种不同的方式来指定路径：使用绝对路径和相对路径。

- 绝对路径：这是从根目录开始的路径。根目录是最高级的。根目录通常显示为斜杠（`/`）。每当您的路径以`/`开头时，都意味着您从根目录开始。例如，`/home/pete/Desktop`。

- 相对路径：这是从您当前在文件系统中的位置开始的路径。如果我在`/home/pete/Documents`位置，并且想进入`Documents`内部一个名为`taxes`的目录，我不需要指定从根目录开始的完整路径，例如`/home/pete/Documents/taxes`；我可以直接进入`taxes/`。

既然您知道路径是如何工作的，我们只需要一个能帮助我们更改到所需目录的工具。幸运的是，我们有`cd`或“change directory”来完成这项工作。

```bash
cd /home/pete/Pictures
```

现在我已将我的目录位置更改为`/home/pete/Pictures`。

现在从这个目录中，我有一个名为`Hawaii`的文件夹。我可以使用以下命令导航到该文件夹：

```bash
cd Hawaii
```

注意我是如何只使用了文件夹的名称？那是因为我已经在`/home/pete/Pictures`中了。

一直使用绝对路径和相对路径进行导航可能会很累。幸运的是，有一些快捷方式可以帮助您。

- `.` (current directory)：这是您当前所在的目录。
- `..` (previous directory)：带您到当前目录的上一级目录。
- `~` (home directory)：此目录默认为您的“主目录”，例如`/home/pete`。
- `-` (previous directory)：这将带您到您刚才所在的上一个目录。

```bash
cd .
cd ..
cd ~
cd -
```

试试看吧！

## Exercise

1. Run the `cd` command without any flags. Where does it take you?

## Quiz Question

如果您在`/home/pete/Pictures`并想去`/home/pete`，有什么好的快捷方式可以使用？

## Quiz Answer

cd ..
