---
lesson_id: "git-commits"
course_id: "git"
lang: "zh"
order_index: 4
title: "提交"
description: "学习如何把暂存的快照保存为提交，并在 Git 历史中找到它。"
meta_title: "提交 - Git"
meta_description: "保存暂存区中的内容，并用提交标识在 Git 历史中找出对应的快照。"
meta_keywords: "Git 提交, 暂存区, git commit, git log, DevOps, Linux Journey"
---

一次**提交**会记录暂存区中选定的文件。它还会记录提交说明、作者，以及它与之前的提交之间的关系。使用 Git 分配的标识，可以在历史中准确找到这次提交。

## 为练习仓库设置身份

Git 会随提交记录姓名和电子邮件地址。只给这个练习仓库设置示例值即可。这些值只是写入历史的标记，不会为你授予远程服务的访问权限。

```bash
$ git config --local user.name "Journey Learner"
$ git config --local user.email "learner@example.com"
```

继续使用练习仓库，其中的 `index.html` 应已暂存。如果想核对哪些文件会进入下一次提交，可以运行 `git status`。

:::single-choice{#git-commits-identity-scope} 这里的 --local 起什么作用？

::option[登录共享的托管服务。]{#git-commits-identity-scope-b explanation="姓名与电子邮件地址是提交的元数据。远程身份验证需要另行完成。"}
::option[为当前仓库设置作者信息。]{#git-commits-identity-scope-a .correct explanation="本地设置只作用于当前仓库。"}
::option[修改已有提交中的所有作者。]{#git-commits-identity-scope-c explanation="这些设置将用于之后创建的提交。"}
:::

## 保存快照

暂存你想保存的版本后，运行 `git commit`。`-m` 选项让你直接在命令行中填写提交说明。

```bash
$ git commit -m "Set the homepage heading"
```

提交保存的是文件的暂存版本。暂存后再编辑工作树，新的修改只有再次暂存才会进入提交。

:::single-choice{#git-commits-staged-snapshot} 你暂存了 Welcome，之后在文件里改成了 Hi，却没有重新暂存。提交会保存哪个标题？

::option[Welcome，因为这是暂存的版本。]{#git-commits-staged-snapshot-c .correct explanation="提交会读取暂存的内容来创建快照。"}
::option[Hi，因为这是磁盘里最新的内容。]{#git-commits-staged-snapshot-a explanation="最新的工作副本可能与暂存版本不同。"}
::option[两个都会，因为 Git 会自动保存每次修改。]{#git-commits-staged-snapshot-b explanation="对于这个文件，暂存的快照只包含选定的那个版本。"}
:::

## 查看简短历史

用 `git log --oneline` 查看简洁的历史列表。每行先显示缩写后的提交标识，再显示提交说明。你的标识会与示例不同。

```text
$ git log --oneline
a12c345 Set the homepage heading
```

不同的提交可以使用同样的说明，所以要用标识来指明是哪次提交。列表通常从当前开发线上的最新提交开始显示。

:::single-choice{#git-commits-identify-snapshot} 两次提交的说明都叫 Set the homepage heading。怎样区分它们各自的快照？

::option[看两次提交共用的说明。]{#git-commits-identify-snapshot-a explanation="同一段文字可以出现在多次提交中。"}
::option[看两次改动涉及的文件名。]{#git-commits-identify-snapshot-c explanation="同一个文件可能出现在许多次提交中。"}
::option[看提交标识。]{#git-commits-identify-snapshot-b .correct explanation="提交标识可以指向某一条具体的历史记录。"}
:::

想在浏览器终端里练习暂存和提交，可以试试 [你的第一个 Git 实验](https://labex.io/tutorials/git-your-first-git-lab-92739)。

## 总结

现在，你可以保存已暂存的改动，并在历史中找到对应的提交。

1. 为练习仓库设置提交身份。
2. 用清楚的提交说明保存暂存的快照。
3. 在简短历史中识别一次提交。
