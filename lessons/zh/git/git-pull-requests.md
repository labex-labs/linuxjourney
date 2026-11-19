---
lesson_id: "git-pull-requests"
course_id: "git"
lang: "zh"
order_index: 7
title: "拉取请求"
description: "学习如何阅读拉取请求，并确认代码审查或自动检查覆盖了哪些改动。"
meta_title: "拉取请求 - Git"
meta_description: "看懂拉取请求的源分支和目标分支，查阅改动，并确认自动检查对应哪个版本。"
meta_keywords: "Git 拉取请求, Pull Request, PR, 代码审查, DevOps, Linux Journey"
---

**拉取请求**（pull request，简称 PR）提出将一个分支的改动合并到另一个分支。Git 负责记录提交和分支，托管服务则围绕这些改动提供审查页面、讨论和检查结果。

## 找出源分支和目标分支

假设同事提议为网站增加状态页。审查页显示 `health-page → main`。源分支有时叫 **head**，它提供拟合并的改动。目标分支有时叫 **base**，它负责接收这些改动。

```text
Source: health-page at 3ab4501
Target: main
Changed file: health.txt
```

此时，审查页描述的是待合并的改动。等 PR 合并后，目标分支才会接收改动。

:::single-choice{#git-pull-requests-pr-direction} 合并这个 PR 后，哪个分支会收到状态页？

::option[用提交 ID 命名的分支。]{#git-pull-requests-pr-direction-a explanation="那个值是用来识别快照的，不能说明哪个分支接收改动。"}
::option[main。]{#git-pull-requests-pr-direction-b .correct explanation="目标分支是 main，因此它会收到审查过的改动。"}
::option[health-page。]{#git-pull-requests-pr-direction-c explanation="health-page 是提供改动的源分支。"}
:::

## 查看改动

打开变更文件视图，查看相对于 PR 目标分支的差异。`health.txt` 增加一行，符合新增一个简单状态页的预期。如果审查页还显示 `index.html` 有改动，就要核对该改动是否也应纳入这次 PR。应以页面上实际列出的文件为准。

:::single-choice{#git-pull-requests-unexpected-file} 标题叫 Add a health page 的 PR 还改了主页。到哪里可以核对具体改了什么？

::option[到变更文件视图查看差异。]{#git-pull-requests-unexpected-file-a .correct explanation="差异显示此次提议具体改了哪些行。"}
::option[只看标题。]{#git-pull-requests-unexpected-file-b explanation="标题概括改动目的，细节可能没有写出来。"}
::option[看分支名称。]{#git-pull-requests-unexpected-file-c explanation="分支名称表示一条开发线，无法描述其中的每项改动。"}
:::

## 查看自动检查结果

PR 发生变化时，托管平台可以自动运行测试。找到这次结果所覆盖的提交或修订版本。如果测试通过之后又推送了一次提交，应确认更新后的版本也执行了所需检查。通过的结果只适用于实际执行过的检查。

:::single-choice{#git-pull-requests-changed-revision} 有一项测试在 3ab4501 上通过了，而 PR 现在指向 78ac900。采信这个结果之前，应该确认什么？

::option[原来的提交说明写得是否清楚。]{#git-pull-requests-changed-revision-a explanation="提交说明无法表明测试是否覆盖了较新的提交。"}
::option[PR 是否仍用原来的标题。]{#git-pull-requests-changed-revision-b explanation="代码发生变化后，标题可以不变。"}
::option[检查是否针对更新后的版本运行了。]{#git-pull-requests-changed-revision-c .correct explanation="先前的结果对应的是另一个版本。"}
:::

## 总结

现在，你可以读懂 PR 提出了什么改动，以及哪些依据支持合并。

1. 找出源分支和目标分支。
2. 在变更文件视图中核对拟议改动。
3. 确认自动检查结果对应哪个版本。
