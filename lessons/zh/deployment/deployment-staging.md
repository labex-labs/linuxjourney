---
lesson_id: "deployment-staging"
course_id: "deployment"
lang: "zh"
order_index: 3
title: "预发布环境"
description: "了解预发布环境可以验证什么，以及同一个产物在不同环境里为什么可能表现不同。"
meta_title: "预发布环境 - 部署"
meta_description: "在预发布环境中验证获准的产物，并确认上线之前需要核对的环境和行为。"
meta_keywords: "预发布环境, 部署, Staging, 发布验证, DevOps, Linux Journey"
---

一个版本快要可以发布了。可以先在**预发布环境**中运行产物。这个环境模仿用户实际依赖的服务，让你在接入生产流量之前，用贴近真实情况的设置验证版本。

## 让同一个产物进入下一环境

使用已经测试并获准的镜像。如果依赖项可能变化，重新构建就可能得到不同的产物。每次部署都应记录完整镜像引用。

```text
Environment  Artifact      Page configuration
staging      site@digest-A Internal preview
production   site@digest-A Public website
```

示例使用简写的摘要标记。两个环境中的产物相同，但设置不同。

:::single-choice{#deployment-staging-same-artifact} 什么信息表明可以把同一个打包后的版本部署到生产环境？

::option[两条部署记录中的产物引用一致。]{#deployment-staging-same-artifact-b .correct explanation="完全一致的引用可以证明两个环境指向同一次构建。"}
::option[两个环境的端口都使用相同的标签。]{#deployment-staging-same-artifact-a explanation="一个设置相同，无法证明产物相同。"}
::option[两个环境在同一天部署。]{#deployment-staging-same-artifact-c explanation="仅凭时间无法识别部署的内容。"}
:::

## 选择有代表性的检查

预发布环境应当能测试重要的行为，例如加载网页、从测试依赖项中读取数据。请使用获准的测试账户和测试数据。如果预发布检查通过，可以对被测试的场景更有把握。正式上线后，流量、数据或配置上的差异仍可能影响结果。

:::single-choice{#deployment-staging-staging-scope} 预发布页面能使用测试数据库正常加载。真正部署以后，还应该验证什么？

::option[产物以后是否不再需要版本信息。]{#deployment-staging-staging-scope-b explanation="验证与恢复时依然需要版本记录。"}
::option[生产环境中的每个请求是否一定会成功。]{#deployment-staging-staging-scope-c explanation="少量测试无法证明所有未来的请求都会成功。"}
::option[生产访问路径在获准的设置下是否有效。]{#deployment-staging-staging-scope-a .correct explanation="预发布请求并没有经过生产环境。"}
:::

## 变更前先确认目标

执行部署之前，先阅读目标环境的名称和地址。部署后用同一个地址核对新版本以及重要功能是否正常。在笔记里写清预发布和生产环境各自的信息，便于确认每个检查结果对应的环境。

:::single-choice{#deployment-staging-correct-target} 你计划部署到预发布环境，但命令里显示的是生产地址。首先该做什么？

::option[继续部署，把结果标成预发布即可。]{#deployment-staging-correct-target-a explanation="地址决定哪个服务会收到变更。"}
::option[停下来，确认预期的部署目标。]{#deployment-staging-correct-target-c .correct explanation="这样可以避免把改动部署到错误的环境。"}
::option[部署后换一个浏览器测试。]{#deployment-staging-correct-target-b explanation="在执行变更之前就应该纠正目标。"}
:::

想动手尝试 CI/CD 示例，可以参阅 [持续部署到预发布环境](https://labex.io/tutorials/cd-deployment-to-staging-636593)。

## 总结

现在，你可以在产物进入生产环境之前，用预发布环境验证它。

1. 让同一个产物在不同环境中仍可准确识别。
2. 选择能反映用户主要行为的检查。
3. 在更改之前确认目标环境。
