---
lesson_id: "git-status-command"
course_id: "git"
lang: "zh"
order_index: 2
title: "git status"
description: "用 git status 区分未跟踪、已暂存和已修改的文件。"
meta_title: "git status - Git"
meta_description: "学习如何用 git status 查看工作树，并判断哪些改动已选入下一次提交。"
meta_keywords: "git status, Git 状态, 暂存区, 未跟踪文件, DevOps, Linux Journey"
---

在仓库中工作时，`git status` 会告诉你工作树里有哪些变化，以及你已经选定哪些内容准备保存。继续使用上一课创建的空仓库 `journey-git`。

## 找到新文件

先创建一个小网页，再用简短格式查看状态，这样输出更容易读。

```bash
$ printf '%s\n' '<h1>Hello</h1>' > index.html
$ git status --short
```

这里的 `>` 会把内容写入指定文件。如果文件已存在，就会覆盖原来的内容。新文件的简短状态是 `?? index.html`。Git 把这种文件称为**未跟踪文件**。文件已经存在，但还没有被选入要保存的快照。

:::single-choice{#git-status-command-untracked-file} Git 在新文件旁显示两个问号。这说明什么？

::option[该文件已经在上次保存的快照里。]{#git-status-command-untracked-file-a explanation="上次的快照中没有未跟踪文件的记录。"}
::option[文件已经从工作树中删除。]{#git-status-command-untracked-file-c explanation="Git 能在工作树里看到这个文件。"}
::option[文件存在，但还没被选入下一次快照。]{#git-status-command-untracked-file-b .correct explanation="你可以选择把这个文件加入暂存区。"}
:::

![Git 的简短状态显示 index.html 从未跟踪变为已暂存](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-status-command/staged-file.png)

## 查看已暂存的改动

用 `git add` 选定文件当前的内容，准备纳入下一个快照，也就是**提交**。选定的内容放在**暂存区**。简短状态的第一列现在显示 `A`，表示新增内容已经选好，等待保存。

```bash
$ git add index.html
$ git status --short
```

:::single-choice{#git-status-command-staged-new} 执行 git add 后，选定的 index.html 版本在哪里？

::option[已经在一次新提交里了。]{#git-status-command-staged-new-a explanation="git add 为下次提交做准备，不会创建提交。"}
::option[在暂存区里。]{#git-status-command-staged-new-c .correct explanation="Git 选定的是你运行 git add 时的文件内容。"}
::option[在其他人的仓库里。]{#git-status-command-staged-new-b explanation="该操作只会改变你本地的暂存区。"}
:::

## 区分两种改动

简短状态在文件名前有两列。第一列表示已暂存的改动，第二列表示暂存之后工作树中又发生的变化。比如 `AM index.html` 表示 Git 已暂存这个新文件，而你之后又修改了工作树里的副本。如果更喜欢按标题查看，直接运行 `git status`，它会分组给出详细信息。

:::single-choice{#git-status-command-two-columns} index.html 旁边显示 AM。在提交前该检查什么？

::option[确认暂存的版本是否包含你想保存的修改。]{#git-status-command-two-columns-a .correct explanation="第二列的 M 表示工作树里的副本还有更新的修改。"}
::option[查找仓库里是否还有一个叫 AM 的文件。]{#git-status-command-two-columns-b explanation="AM 是 index.html 的两个状态标记。"}
::option[检查文件是否已经从磁盘删除。]{#git-status-command-two-columns-c explanation="M 表示文件在工作树中被修改了。"}
:::

## 总结

现在，你可以查看 Git 下一次会保存哪些改动。

1. 识别新建的未跟踪文件。
2. 用 git add 暂存文件。
3. 分别查看暂存区和工作树中的改动。
