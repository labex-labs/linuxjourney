---
lesson_id: "git-remotes"
course_id: "git"
lang: "zh"
order_index: 6
title: "远程仓库"
description: "了解 Git 的远程地址如何连接两个仓库，以及拉取远程信息和推送有什么不同。"
meta_title: "远程仓库 - Git"
meta_description: "用本地裸仓库模拟 Git 远程仓库，练习设置远程地址、推送提交和获取更新。"
meta_keywords: "Git 远程仓库, git remote, git fetch, git push, DevOps, Linux Journey"
---

Git 的**远程仓库**是一个有名称的地址，本地仓库可以用它联系另一个仓库。对方仓库可以位于托管服务上，也可以在同一台机器的另一个目录。这次练习使用单独的本地目录，无需托管服务账户。

## 添加远程地址

在练习仓库中运行命令，另建一个**裸仓库**。裸仓库保存历史和引用，没有可编辑项目文件的工作树。它可以接收你从工作区发出的提交。第一次练习时，需要一个尚未被占用的 `journey-remote.git` 目录。

```bash
$ git init --bare --initial-branch=main ../journey-remote.git
$ git remote add origin ../journey-remote.git
$ git remote -v
```

`origin` 是约定俗成的远程名称。远程仓库列表会显示名称对应的地址。

:::single-choice{#git-remotes-add-address} 运行 git remote add 后，你在列表里看到 origin。Git 做了什么？

::option[为另一个仓库保存了一个名称。]{#git-remotes-add-address-b .correct explanation="之后可以在命令里用 origin 代表该地址。"}
::option[上传了本地所有提交。]{#git-remotes-add-address-a explanation="添加远程只会记录地址。上传提交需要执行 push。"}
::option[把另一个工作树克隆到你的项目中。]{#git-remotes-add-address-c explanation="原有的工作树仍在原位置。"}
:::

## 推送分支

用 `git push` 发送本地提交，并请求远程仓库更新它的分支。`-u` 会把远程分支设为上游分支，之后 Git 可以通过这个关联找到本地分支对应的远程分支。

```bash
$ git push -u origin main
```

这次推送只会发往另一个练习目录。共享的远程仓库可能要求授权，也可能拒绝更新。请查看它的响应，再确认推送是否成功。

:::single-choice{#git-remotes-push-direction} 哪条命令会把本地 main 的新提交推送到这个远程仓库？

::option[git fetch origin]{#git-remotes-push-direction-b explanation="fetch 把远程的信息取回本地仓库。"}
::option[git remote -v]{#git-remotes-push-direction-c explanation="这条命令显示 origin 对应的地址。"}
::option[git push origin main]{#git-remotes-push-direction-a .correct explanation="push 发送远程端所需的提交，并请求更新分支。"}
:::

## 获取更新

用 `git fetch origin` 刷新本地对远程历史的记录。Git 使用**远程跟踪分支**记录上次得到的信息，例如 `origin/main`。你可以用 `git log --oneline origin/main` 查看它。只执行 fetch 时，工作树仍对应当前检出的本地分支。

```bash
$ git fetch origin
$ git log --oneline origin/main
```

:::single-choice{#git-remotes-after-fetch} 执行 fetch 后，origin/main 前进了，本地 main 却没有动。哪种说法符合这个结果？

::option[fetch 重写了你正在编辑的文件。]{#git-remotes-after-fetch-a explanation="fetch 更新的是本地保存的远程分支状态。"}
::option[Git 获取了远程变化。是否合并，是另外一步。]{#git-remotes-after-fetch-c .correct explanation="即使 origin/main 前进了，本地分支也可以留在原来的位置。"}
::option[执行 fetch 时，你的推送更新了远程仓库。]{#git-remotes-after-fetch-b explanation="fetch 的数据方向是从远程到本地。"}
:::

## 总结

现在，你可以判断不同的 Git 命令会影响哪个仓库。

1. 添加并查看远程仓库地址。
2. 推送分支并识别它的上游分支。
3. 在保持已检出文件不变的情况下获取新的远程历史。
