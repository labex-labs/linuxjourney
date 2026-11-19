---
lesson_id: "git-repositories"
course_id: "git"
lang: "zh"
order_index: 1
title: "仓库"
description: "了解 Git 仓库保存什么，并为一个小网站创建空仓库。"
meta_title: "仓库 - Git"
meta_description: "创建一个空的 Git 仓库，认识工作树和 .git 目录，并区分初始化与克隆。"
meta_keywords: "Git 仓库, 工作树, git init, git clone, DevOps, Linux Journey"
---

一个网站可以从几个文件开始。Git 可以记录这些文件在不同时间点的样子。项目文件和它们的历史一起组成了本地 Git 工作区。

## 创建仓库

从一个可以新建文件夹的练习目录开始。下面的命令只需要运行一次。美元符号是 shell 提示符，输入时只敲它后面的命令。

```bash
$ mkdir journey-git
$ cd journey-git
$ git init --initial-branch=main
```

新建的文件夹是**工作树**，你会在这里编辑项目文件。Git 会在里面创建隐藏目录 `.git` 来保存历史和设置。新仓库里还没有保存过任何修改。Git 把这条初始开发分支命名为 `main`。

:::single-choice{#git-repositories-empty-history} 你在已经有 index.html 的目录中初始化仓库。这个文件的历史会怎样？

::option[Git 立即把这个文件记录为第一次提交。]{#git-repositories-empty-history-b explanation="初始化不会保存任何项目文件。"}
::option[可以在之后的提交中记录这个文件。]{#git-repositories-empty-history-a .correct explanation="初始化会准备好仓库。保存快照需要另做一次操作。"}
::option[Git 会把这个文件移进隐藏目录。]{#git-repositories-empty-history-c explanation="项目文件仍然留在工作树里，可以继续编辑。"}
:::

![LabEx 终端显示已初始化空 Git 仓库，并将练习目录报告为仓库根目录](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-repositories/init-and-root.png)

## 识别工作树

用 `git rev-parse --show-toplevel` 输出当前仓库的根目录。在练习文件夹里运行，应当看到以 `journey-git` 结尾的路径。工作树里的子目录也属于同一个仓库，除非它里面另有一个独立的仓库。

```bash
$ git rev-parse --show-toplevel
```

:::single-choice{#git-repositories-find-root} 你进入 journey-git 中名为 images 的子目录。Git 会把哪个目录报告为顶层目录？

::option[journey-git 目录。]{#git-repositories-find-root-b .correct explanation="Git 会从当前位置向上找到仓库根目录。"}
::option[images 子目录。]{#git-repositories-find-root-a explanation="即使终端当前位于子目录，顶层目录也仍是仓库的根目录。"}
::option[隐藏的 .git 目录。]{#git-repositories-find-root-c explanation="这条命令显示的是存放项目文件的工作树根目录。"}
:::

## 从已有历史开始

已经有一个仓库需要复制时，可以用 `git clone`。普通克隆会创建新的本地工作树，并导入现有仓库的历史。如果要在本地开始记录一个新项目的历史，则用 `git init`。后面的课会继续使用 `journey-git`。

:::single-choice{#git-repositories-choose-start} 同事给了你一个仓库地址，你需要其中的历史记录。应该怎么开始？

::option[创建空文件夹，再初始化仓库。]{#git-repositories-choose-start-a explanation="新建仓库不会带有同事仓库的历史。"}
::option[只复制看得到的网站文件。]{#git-repositories-choose-start-b explanation="这些文件只能给你当时的一个版本，仓库历史不会一同复制。"}
::option[克隆同事的仓库。]{#git-repositories-choose-start-c .correct explanation="克隆会复制共享的历史，并为你创建本地工作树。"}
:::

## 总结

现在，你可以根据项目情况选择如何建立本地 Git 仓库。

1. 识别工作树和 Git 的隐藏目录。
2. 从子目录中找出仓库根目录。
3. 用初始化开始记录新历史，或用克隆获取已有历史。
