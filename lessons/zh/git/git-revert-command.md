---
lesson_id: "git-revert-command"
course_id: "git"
lang: "zh"
order_index: 8
title: "git revert"
description: "学习怎样用 git revert 记录一次撤销，同时保留原来的提交。"
meta_title: "git revert - Git"
meta_description: "用一个新的提交撤销已经共享的改动，并核对撤销后的文件、历史和工作树。"
meta_keywords: "git revert, Git 撤销, Git 历史, DevOps, Linux Journey"
---

已经共享的改动也可以撤销。用 `git revert` 可以创建一个新提交，应用与原改动相反的变更。这样，历史里既保留原来的改动，也记录后来撤销的决定。

## 找到要撤销的改动

练习仓库的 `main` 包含主页和状态页的提交。用简短历史核对最新一条记录。下面的提交标识仅作示例。

```text
$ git log --oneline
3ab4501 Add a health page
a12c345 Set the homepage heading
```

`HEAD` 指向当前检出的提交。先确认它正是你想撤销的改动。继续之前，用 `git status` 检查工作树是否干净。

:::single-choice{#git-revert-command-newest-commit} 在这个例子中，撤销 HEAD 会撤销哪项改动？

::option[较早的主页标题改动。]{#git-revert-command-newest-commit-b explanation="改标题的是上一次提交。"}
::option[同时撤销两项改动。]{#git-revert-command-newest-commit-c explanation="这里的 HEAD 只指向一次提交，撤销针对的是这次提交。"}
::option[新增状态页。]{#git-revert-command-newest-commit-a .correct explanation="HEAD 指向这个分支上列表中的最新提交。"}
:::

## 记录撤销

在工作树干净的练习仓库中，撤销状态页的提交。该命令会修改工作树中的文件并创建一次提交。用 `--no-edit` 保留 Git 自动生成的撤销说明。

```bash
$ git revert --no-edit HEAD
```

本例中会删除状态文件，因为原来的提交添加了它。如果后来的改动碰到了相同的行，Git 可能会暂停，要求你处理冲突。继续之前先查看状态。

:::single-choice{#git-revert-command-undo-effect} 示例中的撤销成功之后，应该看到哪个文件变化？

::option[主页文件和状态页文件都被删除。]{#git-revert-command-undo-effect-a explanation="较早的主页提交仍然有效。"}
::option[状态页文件被删除。]{#git-revert-command-undo-effect-b .correct explanation="撤销反转了指定提交添加文件的改动。"}
::option[又新增了一次状态页。]{#git-revert-command-undo-effect-c explanation="revert 应用相反的变更，不会重复添加文件。"}
:::

![Git 历史显示新的撤销记录和原来的状态页提交](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-revert-command/recorded-undo.png)

## 撤销后核对历史

再运行一次 `git log --oneline`，原状态页提交上方应该出现一条新的撤销记录。用 `git status --short` 查看是否还有本地改动。这个新提交可以像其他改动一样接受审查，再共享出去。

:::single-choice{#git-revert-command-history-after-revert} 在新的撤销记录下方，仍应该看到什么？

::option[原来的状态页提交。]{#git-revert-command-history-after-revert-c .correct explanation="这两条记录分别保存了原始改动和撤销。"}
::option[只剩最初修改标题的提交。]{#git-revert-command-history-after-revert-a explanation="原来的状态页提交仍然保留在历史中。"}
::option[没有任何提交。]{#git-revert-command-history-after-revert-b explanation="revert 会新增提交，不会替换分支的历史。"}
:::

## 保留其他改动

假设历史中有三项独立改动。先添加了状态文件，然后修正了主页上的错别字，这两项改动都已经共享。撤销添加状态文件的那次提交，可以移除该文件，同时保留无关的错别字修正。选择要撤销的提交之前，先查阅历史和相关文件。

:::single-choice{#git-revert-command-final-application} 怎么确认撤销保留了你希望留下的改动？

::option[添加状态文件的提交从日志里消失了。]{#git-revert-command-final-application-b explanation="revert 会把原记录保留在历史里。"}
::option[主页中的错别字修正也消失了。]{#git-revert-command-final-application-c explanation="错别字修正是另一项改动，应当保留下来。"}
::option[状态文件已经移除，主页仍保留修正，历史中新增了撤销记录。]{#git-revert-command-final-application-a .correct explanation="这些观察分别确认了预期的撤销、无关改动得以保留，以及历史中新增了记录。"}
:::

## 总结

现在，你可以撤销已经提交的改动，并保留改动与撤销的记录。

1. 找准要撤销的那一次提交。
2. 在干净的工作树中执行撤销。
3. 在历史中核对原始提交与撤销提交。
