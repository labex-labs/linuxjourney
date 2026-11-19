---
lesson_id: "ci-overview"
course_id: "continuous-integration"
lang: "zh"
order_index: 1
title: "持续集成"
description: "了解持续集成如何在小改动并入共享分支之前对其进行检查。"
meta_title: "持续集成 - 持续集成"
meta_description: "从一个网页改动出发，了解持续集成怎样检查特定版本、报告失败，以及它和部署的区别。"
meta_keywords: "持续集成, CI, 代码检查, DevOps, Linux Journey"
---

主页改动在一个人的浏览器里看着正常，换个人打开却可能出问题。**持续集成**（CI）让团队经常合并改动，并针对特定版本运行可重复的检查。

## 把改动与检查关联起来

修订版本指明正在检查哪一版文件。如果拟议改动修改了 `index.html`，CI 可以针对这个版本运行检查，并报告结果是否符合预期。比如，这个网站的检查可以寻找必需的标题。团队决定是否合并时，可以参考这个结果。

:::single-choice{#ci-overview-revision-result} 星期一的检查通过了。星期二有一次新提交修改了网页。之前通过的结果能说明什么？

::option[两个版本都符合检查要求。]{#ci-overview-revision-result-b explanation="较晚的提交需要有自己的检查结果。"}
::option[星期一的版本符合那项检查的要求。]{#ci-overview-revision-result-a .correct explanation="每个结果只对应运行检查时使用的那个版本。"}
::option[访客可以看到新网页。]{#ci-overview-revision-result-c explanation="对源文件的检查无法说明线上是否已部署。"}
:::

## 解读失败的检查

假设检查报告说找不到预期的标题。这给提交者提供了一个具体的排查起点。修改网页之前，先看清检查的要求和实际结果。有时是提交者写错了，有时是预期行为变了，检查也需要相应调整。

:::single-choice{#ci-overview-failed-action} 标题检查失败时，该先看什么？

::option[预期标题以及被检查版本中的文件。]{#ci-overview-failed-action-b .correct explanation="对照两者，就能找出这次不匹配的原因。"}
::option[先看上一次成功运行生成的产物。]{#ci-overview-failed-action-a explanation="那份产物代表更早的输出。失败的检查和当前文件能提供更直接的信息。"}
::option[访客的网络设置。]{#ci-overview-failed-action-c explanation="这项检查只读取文件，没有发出浏览器请求。"}
:::

## 区分检查和交付

一条流水线可以检查文件、构建输出，再把输出交给后续的部署环节。**构建**为后续步骤准备可用的产物，例如一组已经可以提供给用户的网页文件。**部署**是在某个环境中安装或启动某个版本。你的第一个 CI 工作流会在网页交付之前先检查它。

:::single-choice{#ci-overview-output-vs-live} 测试已通过，而且已经生成了网站归档。什么证据可以说明访客能使用这个版本？

::option[再复制一份检查日志。]{#ci-overview-output-vs-live-a explanation="日志只描述检查和构建的情况。"}
::option[网站归档已经存在。]{#ci-overview-output-vs-live-b explanation="即使文件已归档，网站也可能还没有对外提供。"}
::option[有对应的部署记录，并且访问目标网页得到成功响应。]{#ci-overview-output-vs-live-c .correct explanation="两项证据把构建版本与目标环境返回的响应联系起来。"}
:::

## 总结

现在，你可以解释 CI 在一个改动从提出到交付的过程中起什么作用。

1. 把检查结果与具体的修订版本对应起来。
2. 从失败的检查中找出应优先排查的问题。
3. 区分检查、构建和部署。
