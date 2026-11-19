---
lesson_id: "ci-jobs-steps-runners"
course_id: "continuous-integration"
lang: "zh"
order_index: 3
title: "作业、步骤和运行器"
description: "学习在简短的 GitHub Actions 文件中找出作业、步骤和运行器。"
meta_title: "作业、步骤和运行器 - 持续集成"
meta_description: "读懂 GitHub Actions 工作流的组成，并了解如何指定作业依赖和在作业之间传递文件。"
meta_keywords: "GitHub Actions, 作业, 步骤, 运行器, 持续集成, DevOps, Linux Journey"
---

工作流是整个自动化过程。**作业**把一组操作交给**运行器**，也就是执行这些操作的机器或环境。**步骤**是作业中的一次操作。

## 读懂一个小型工作流

这个例子在 GitHub 托管的 Ubuntu 运行器上执行一个作业。这类工作流文件放在 GitHub 仓库的 `.github/workflows/` 下。

```yaml
name: Page check
on: push
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Get the repository
        uses: actions/checkout@v6
      - name: Find the heading
        run: grep -q '<h1>Welcome</h1>' index.html
```

作业 ID 是 `check`。`runs-on` 字段选择运行环境。`uses` 调用可复用的 action，这里用于让作业可以访问仓库文件。`run` 则在运行器上执行命令。

:::single-choice{#ci-jobs-steps-runners-job-fields} 哪个字段决定 check 作业在哪种环境运行？

::option[Runs-on。]{#ci-jobs-steps-runners-job-fields-a .correct explanation="它指定了作业使用的运行器类型。"}
::option[Uses。]{#ci-jobs-steps-runners-job-fields-b explanation="这个步骤用它来调用 checkout action。"}
::option[Name。]{#ci-jobs-steps-runners-job-fields-c explanation="name 为工作流设置名称。"}
:::

## 查看步骤的执行顺序

同一个作业中的步骤默认按列出顺序执行。检查步骤要读取仓库里的文件，所以先执行 checkout。同一作业的后续步骤可以使用前面步骤写入的文件。

:::single-choice{#ci-jobs-steps-runners-step-order} 在一个全新的运行器上，如果把 checkout 移到 grep 之后，grep 这一步会缺少什么？

::option[作业的名称。]{#ci-jobs-steps-runners-step-order-a explanation="工作流已经选好了要执行的作业。"}
::option[Ubuntu 运行器本身。]{#ci-jobs-steps-runners-step-order-c explanation="运行器在执行步骤之前就已选定。"}
::option[它要读取的项目文件。]{#ci-jobs-steps-runners-step-order-b .correct explanation="checkout 会在检查之前把仓库文件准备好。"}
:::

## 区分各个作业

不同作业可能同时执行。每个使用 GitHub 托管运行器的作业都有单独的运行器。一个作业写入的文件，另一个默认看不到，除非工作流传过去。如果一个作业依赖另一个作业成功，应使用 `needs` 声明依赖，需要传文件时再使用构建产物。

:::single-choice{#ci-jobs-steps-runners-separate-jobs} 构建作业写入了 site.tar.gz，后续作业在另一台托管运行器上执行。怎样让它收到这个文件？

::option[假定文件还在原工作目录。]{#ci-jobs-steps-runners-separate-jobs-a explanation="另一台托管运行器有自己的文件系统。"}
::option[把文件作为产物传过去。]{#ci-jobs-steps-runners-separate-jobs-c .correct explanation="工作流可以在一个作业中上传文件，在另一个作业中下载。"}
::option[设置 needs，让后续作业等构建完成。]{#ci-jobs-steps-runners-separate-jobs-b explanation="needs 能安排顺序。构建文件仍需要在运行器之间另行传递。"}
:::

想在 GitHub 仓库里编写和运行工作流，可以跟着 [GitHub Actions 入门](https://labex.io/courses/github-actions-for-beginners) 练习。这个实验课程需要 GitHub 账户。

## 总结

现在，你可以读懂 CI 工作流的主要组成部分。

1. 找出作业和执行它的运行器。
2. 区分可复用的 action 和执行 shell 命令的步骤。
3. 判断什么时候需要声明作业依赖或传递文件。
