---
lesson_id: "git-branches"
course_id: "git"
lang: "zh"
order_index: 5
title: "分支"
description: "了解 Git 分支如何表示不同的开发线，以及如何把一个改动合并到 main。"
meta_title: "分支 - Git"
meta_description: "用分支开展独立工作，再通过合并把改动纳入 main。"
meta_keywords: "Git 分支, git switch, git merge, 快进合并, DevOps, Linux Journey"
---

**分支**是指向某次提交的一个名称。当你在当前分支上创建新的提交时，该分支就移到新提交的位置。其他分支仍指向原来的位置，直到你更新它们。

## 开始一条独立的开发线

在练习仓库的 `main` 分支上，新建名为 `health-page` 的分支并切换过去。`git switch` 的 `-c` 选项表示创建分支。

```bash
$ git switch -c health-page
```

起初两个名称都指向同一次提交。用 `git branch --show-current` 查看当前分支，就能知道下次提交会推动哪个分支前进。

:::single-choice{#git-branches-start-pointer} 刚执行完 git switch -c health-page 时，新分支指向哪次提交？

::option[命令新建的一次空提交。]{#git-branches-start-pointer-a explanation="这个命令只创建了一个分支名称，并把它指向已有的提交。"}
::option[其他人的仓库里的一次提交。]{#git-branches-start-pointer-c explanation="这个命令在当前仓库里创建本地分支。"}
::option[创建分支时所在的那次提交。]{#git-branches-start-pointer-b .correct explanation="两个分支起初都指向同一个快照。"}
:::

## 在分支上保存改动

在当前分支为 `health-page` 时，添加一个只有一行的状态文件并提交。

```bash
$ printf '%s\n' ready > health.txt
$ git add health.txt
$ git commit -m "Add a health page"
```

假设主页对应的提交是 A，状态页对应的提交是 B。

```text
A (main) --- B (health-page)
```

只有 `health-page` 移到了 B。在工作树干净的情况下切回 `main`，文件会恢复到提交 A 的快照。

:::single-choice{#git-branches-branch-snapshot} 合并之前，哪个分支包含状态页的提交？

::option[两个分支都包含，因为它们在同一个仓库里。]{#git-branches-branch-snapshot-a explanation="同一仓库里的分支可以指向不同的快照。"}
::option[只有 health-page。]{#git-branches-branch-snapshot-c .correct explanation="创建提交 B 时，它是当前分支。"}
::option[只有 main，因为你是从它创建分支的。]{#git-branches-branch-snapshot-b explanation="在 health-page 上提交时，main 的位置没有变化。"}
:::

## 合并到 main

先切换到要接收改动的分支，再在合并命令里指定提供改动的分支。

```bash
$ git switch main
$ git merge health-page
```

这里的 `main` 在 A 之后没有自己的新提交。Git 可以直接让它指向 B，这叫**快进合并**。如果两个分支都各自有新提交，Git 可能需要合并两边的改动。先查看结果，再确认合并是否完成。

:::single-choice{#git-branches-merge-direction} 你想让 main 接收 health-page 的改动。应当怎样运行合并？

::option[在 main 上运行，指定 health-page 为来源。]{#git-branches-merge-direction-a .correct explanation="当前分支接收合并结果。"}
::option[在 health-page 上运行，指定 main 为来源。]{#git-branches-merge-direction-b explanation="那样更新的是 health-page。"}
::option[在两边都不用的新分支上运行。]{#git-branches-merge-direction-c explanation="在 main 接收改动之前，它仍会指向原来的位置。"}
:::

## 总结

现在，你可以把改动从本地分支合并到 main。

1. 在当前提交上创建分支。
2. 在指定分支上保存改动。
3. 将改动合并到应当接收它的分支。
