---
lesson_id: "ci-workflow-permissions"
course_id: "continuous-integration"
lang: "zh"
order_index: 7
title: "工作流权限"
description: "学习只为常规 CI 检查授予它所需的仓库访问权限。"
meta_title: "工作流权限 - 持续集成"
meta_description: "为检查和发布作业分别设置权限，并了解如何保护凭据、记录有助于排查的日志。"
meta_keywords: "工作流权限, CI 权限, GitHub Actions, 最小权限, 持续集成, DevOps, Linux Journey"
---

CI 作业可以运行命令，也可能接收到凭据。**权限**规定这些凭据可以读取或更改什么。只检查网页的作业通常只需读取源文件。

## 让检查作业能够读取仓库

这段 GitHub Actions 配置把工作流内置令牌的权限限制为只读仓库内容。

```yaml
permissions:
  contents: read
```

检出步骤和本地测试都可以读取仓库。发布软件包的作业需要在另一种资源上执行其他操作。因此，只给实际需要发布的作业授予相应权限。

:::single-choice{#ci-workflow-permissions-choose-permission} 一个作业读取网页并运行 grep。它需要什么仓库内容权限？

::option[写权限，因为测试会向终端写入输出。]{#ci-workflow-permissions-choose-permission-a explanation="向终端输出不需要更改仓库内容的权限。"}
::option[读权限。]{#ci-workflow-permissions-choose-permission-c .correct explanation="作业只要取出内容，没有需要编辑的仓库文件。"}
::option[写权限，因为源文件在 Git 仓库里。]{#ci-workflow-permissions-choose-permission-b explanation="题目描述的检查只需要读取源文件。"}
:::

## 处理敏感值

**机密**是需要保护的值，例如私有令牌。获得授权的作业确实需要机密时，可以使用平台的机密存储。把普通网页配置和机密分开。针对本地示例运行的常规检查无需公开任何凭据。

:::single-choice{#ci-workflow-permissions-secret-needed} 哪个值应放入受控的机密存储？

::option[用于上传软件包的私有凭据。]{#ci-workflow-permissions-secret-needed-a .correct explanation="凭据可能授予对另一个系统的访问权限。"}
::option[测试用到的 Welcome 文本。]{#ci-workflow-permissions-secret-needed-b explanation="这是公开的示例内容。"}
::option[输出目录名 dist。]{#ci-workflow-permissions-secret-needed-c explanation="目录名只是普通配置。"}
:::

## 让日志易于排查

工作流日志可能会共享给其他人。可以报告做了什么、结果如何，但别打印机密值。发生失败时，可以说明缺少必要凭据或访问被拒绝。向维护者提供作业名和修订版本，方便排查。凭据的值不要写在消息中。

:::single-choice{#ci-workflow-permissions-safe-diagnostic} 发布作业无法通过身份验证。哪种日志消息既有助于审查，又不会泄露凭据？

::option[打印完整的凭据，方便复制。]{#ci-workflow-permissions-safe-diagnostic-a explanation="任何能访问日志的人都可以看到打印出来的凭据。"}
::option[打印全部环境变量来展示作业状态。]{#ci-workflow-permissions-safe-diagnostic-c explanation="直接输出所有环境变量可能泄露敏感值。"}
::option[报告哪个发布步骤失败，以及访问返回了什么结果。]{#ci-workflow-permissions-safe-diagnostic-b .correct explanation="审查者可以据此找到失败位置，再单独核对访问配置。"}
:::

## 审查新增的作业

有人提议让工作流在拉取请求中运行网页检查，并增加一个发布软件包的作业。两种作业的权限需求不同。检查作业只需要读取权限。经批准的发布权限，应只给真正执行发布的作业。

:::single-choice{#ci-workflow-permissions-final-application} 哪种修改最符合两个作业的需要？

::option[给两个作业都授予仓库写权限。]{#ci-workflow-permissions-final-application-b explanation="检查只需要读取源文件，而且发布软件包所需的权限也可能与仓库写权限无关。"}
::option[在所有步骤中共用一个上传凭据，让重新运行时行为一致。]{#ci-workflow-permissions-final-application-c explanation="只有执行发布的作业才需要上传凭据。"}
::option[让检查保持只读，并且只给发布作业授予必要的软件包访问权限。]{#ci-workflow-permissions-final-application-a .correct explanation="这样可让两个作业各自得到完成工作所需的权限，同时减少其他地方的权限。"}
:::

## 总结

现在，你可以判断一个小型 CI 流水线需要什么样的访问权限。

1. 根据作业职责选择仓库权限。
2. 通过受控的输入提供私有凭据。
3. 记录有助于排查的错误，同时保护凭据的值。
