---
lesson_id: "git-diff-command"
course_id: "git"
lang: "zh"
order_index: 3
title: "git diff"
description: "学习用 git diff 比较工作树中的文件与暂存的版本。"
meta_title: "git diff - Git"
meta_description: "用 git diff 查看具体哪些行发生了变化，并在提交前预览已暂存的改动。"
meta_keywords: "git diff, Git 差异, 工作树, 暂存区, DevOps, Linux Journey"
---

状态列表告诉你哪些文件变了。要看具体改了哪些行，可以用 `git diff`。这里仍用上一课的 `index.html`，暂存的版本里已经有 Hello 标题。

## 比较工作文件和暂存版本

修改练习文件的标题，再把工作树中的副本与暂存的副本对照一下。

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
$ git diff -- index.html
```

`--` 把命令选项和要检查的路径分开。输出中以 `-` 开头的行来自较早的版本，以 `+` 开头的行是替换后的内容。以下两行就是差异中描述这次修改的部分。

```diff
-<h1>Hello</h1>
+<h1>Welcome</h1>
```

:::single-choice{#git-diff-command-changed-heading} 工作树中的副本目前使用哪个标题？

::option[Welcome。]{#git-diff-command-changed-heading-b .correct explanation="在这个比较里，加号开头的行显示工作树中的新内容。"}
::option[Hello。]{#git-diff-command-changed-heading-a explanation="减号开头的行显示先前暂存的内容。"}
::option[两个标题都在里面。]{#git-diff-command-changed-heading-c explanation="这两行展示的是同一行改动前后的版本。"}
:::

## 比较暂存区和历史记录

用 `git diff --staged -- index.html` 把暂存的版本与最近一次提交比较。第一次提交之前，Git 以空状态为起点作比较。这里的输出会把暂存的 Hello 标题显示为新增内容。与此同时，直接运行 `git diff` 会显示后来改成 Welcome 的那次修改。

```bash
$ git diff --staged -- index.html
```

:::single-choice{#git-diff-command-preview-commit} 哪条命令能预览现在提交会包含的版本？

::option[git diff -- index.html]{#git-diff-command-preview-commit-b explanation="这条命令比较当前工作文件与暂存版本。"}
::option[git status --short]{#git-diff-command-preview-commit-c explanation="状态列表会指出哪里有改动，但不会列出具体改了哪些行。"}
::option[git diff --staged -- index.html]{#git-diff-command-preview-commit-a .correct explanation="这条命令把已选定的内容与上一个快照比较。"}
:::

![LabEx 终端比较工作树中的 Welcome 标题和暂存区中的 Hello 标题](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-diff-command/working-and-staged.png)

## 理解差异为空的原因

再次暂存当前文件，以更新暂存的副本。

```bash
$ git add index.html
$ git diff -- index.html
```

现在直接运行 `git diff` 可能没有输出，因为工作文件和暂存的副本相同。改用暂存区比较，可以看到仍待提交的改动。Git 也不会在这些常规比较中显示未跟踪的文件。拿不准改动在哪里时，先查看状态。

:::single-choice{#git-diff-command-empty-diff} 暂存修改后，直接运行 git diff 没有输出。还可以在哪里查看它与历史记录的差别？

::option[再直接运行一次 git diff。]{#git-diff-command-empty-diff-a explanation="在这个例子里，再比较一次仍是两个相同的副本。"}
::option[查看 git diff --staged 的输出。]{#git-diff-command-empty-diff-c .correct explanation="这条命令把暂存版本与历史中的基准版本比较。"}
::option[只能等到创建提交以后。]{#git-diff-command-empty-diff-b explanation="在保存提交之前，就可以检查它准备保存的内容。"}
:::

## 总结

现在，你可以根据想弄清的问题选择合适的差异比较方式。

1. 读懂差异中的删除行和新增行。
2. 比较工作文件与暂存区中的版本。
3. 在提交前预览暂存的改动。
