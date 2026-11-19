---
lesson_id: "ci-workflow-triggers"
course_id: "continuous-integration"
lang: "zh"
order_index: 2
title: "工作流触发条件"
description: "学习根据事件和分支筛选条件，判断 GitHub Actions 工作流何时运行。"
meta_title: "工作流触发条件 - 持续集成"
meta_description: "读懂 GitHub Actions 的 push 和 pull request 触发条件，并区分它们筛选的分支。"
meta_keywords: "工作流触发条件, GitHub Actions, 持续集成, DevOps, Linux Journey"
---

工作流要有触发条件才会运行。在 GitHub Actions 中，`on` 部分列出可以触发工作流的事件。**事件**可以是向分支推送提交、更新拉取请求，也可以是其他受支持的操作。

## 查看推送事件

阅读下面的工作流片段。YAML 通过缩进表明 `branches` 是 `push` 下的配置项。

```yaml
on:
  push:
    branches:
      - main
```

如果工作流已启用，而且其他必要条件也都满足，那么向 `main` 分支推送提交时，工作流就会运行。只在本地终端提交，不会把改动发送到 GitHub。这段配置监听的是推送事件。

:::single-choice{#ci-workflow-triggers-push-filter} 哪项操作符合这个推送触发条件？

::option[在本地 main 上创建提交。]{#ci-workflow-triggers-push-filter-a explanation="触发条件监听的是 GitHub 仓库中的事件。"}
::option[向名为 draft 的分支推送提交。]{#ci-workflow-triggers-push-filter-b explanation="分支筛选条件指定的是 main。"}
::option[把提交推送到 main。]{#ci-workflow-triggers-push-filter-c .correct explanation="这个事件同时满足 push 和分支筛选条件。"}
:::

## 查看拉取请求事件

另一类事件可以在拟议改动合并之前运行检查。这个片段里的分支筛选条件针对拉取请求的目标分支。

```yaml
on:
  pull_request:
    branches:
      - main
```

从 `health-page` 合并到 `main` 的提议符合筛选条件。采用默认活动类型时，新建拉取请求，或向其源分支推送新提交，都可能触发工作流。

:::single-choice{#ci-workflow-triggers-pr-target} 有一个拉取请求要将 notes 合并到 main。这个分支筛选条件看的是哪个名称？

::option[源分支 notes。]{#ci-workflow-triggers-pr-target-b explanation="notes 包含希望合并的改动。"}
::option[目标分支 main。]{#ci-workflow-triggers-pr-target-a .correct explanation="拉取请求的分支筛选条件用于匹配接收改动的目标分支，也叫 base。"}
::option[提议中修改的文件名。]{#ci-workflow-triggers-pr-target-c explanation="这个片段按分支名称筛选。"}
:::

## 查看多个触发条件

一个文件可以在同一个 `on` 键下列出两种事件。拉取请求触发的运行可以检查合并后的预期状态。实际合并更新了 `main` 后，推送触发的运行则可以检查该分支此时的状态。请对照每次运行里记录的触发事件和修订版本来看结果。

:::single-choice{#ci-workflow-triggers-after-merge} 工作流有上面这两个触发条件。一次合并更新了 main。它符合哪个事件？

::option[推送到 main。]{#ci-workflow-triggers-after-merge-b .correct explanation="接收改动的分支已更新，符合推送事件的筛选条件。"}
::option[在新分支上发起拉取请求。]{#ci-workflow-triggers-after-merge-a explanation="题目描述的是改动合并后对 main 的更新。"}
::option[本地提交，远程仓库没有更新。]{#ci-workflow-triggers-after-merge-c explanation="题目里的 GitHub main 分支已经变化。"}
:::

## 总结

现在，你可以判断仓库中的什么事件会触发工作流。

1. 读懂推送事件和它的分支筛选条件。
2. 识别拉取请求触发条件所用的目标分支。
3. 把工作流结果与触发它的事件对应起来。
