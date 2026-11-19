---
lesson_id: "build-release-deploy"
course_id: "deployment"
lang: "zh"
order_index: 1
title: "构建、发布与部署"
description: "学习如何根据构建、发布和部署记录追踪源代码版本。"
meta_title: "构建、发布与部署 - 部署"
meta_description: "把源代码版本与构建产物关联起来，区分发布批准和实际部署。"
meta_keywords: "构建, 发布, 部署, 构建产物, DevOps, Linux Journey"
---

同事说第 2 版已经准备好了。这可能只是说文件已经构建好了，也可能表示版本已获准发布，或者访客已经能访问它。查看各项记录，就能知道流程进行到了哪一步。

## 识别构建

构建把某个源代码版本变成可用的产物。示例把一个小网站打包成容器镜像，再将镜像保存在镜像仓库中。记录镜像引用时，一并记下构建使用的源代码提交。

```text
Build 81
Source commit: 3ab4501
Image: registry.example/journey/site:2
Result: succeeded
```

这条记录说明产出了什么。网站仍可能在运行较早的版本。

:::single-choice{#build-release-deploy-build-record} 哪条记录把打包后的镜像与源代码版本联系起来？

::option[浏览器书签。]{#build-release-deploy-build-record-b explanation="书签只记录一个访问地址，不记录文件如何构建。"}
::option[第 81 次构建。]{#build-release-deploy-build-record-a .correct explanation="它同时记录了源代码提交和生成的镜像。"}
::option[最新的本地分支名。]{#build-release-deploy-build-record-c explanation="分支所指的提交可以改变，仅凭分支名无法识别这次构建。"}
:::

## 查看发布记录

**发布**会确定一个已获准分发的版本。例如，一条发布记录可以批准把第 81 次构建生成的那个镜像用于预发布环境。这样，获得批准后还可以引用同一个产物，无需重新构建。

:::single-choice{#build-release-deploy-release-record} 第 2 版获准在预发布环境中使用。这说明什么？

::option[记录中的产物获准在该环境使用。]{#build-release-deploy-release-record-b .correct explanation="发布记录写明哪个产物可以部署到预发布环境。"}
::option[所有环境都已提供第 2 版。]{#build-release-deploy-release-record-a explanation="批准只是允许继续部署，并没有记录某个版本已经在运行。"}
::option[第 2 版的请求速率更高。]{#build-release-deploy-release-record-c explanation="发布记录不会测量流量。"}
:::

## 查明已部署的版本

**部署**是把某个确切版本放进指定环境，并在其中启动或更新服务。预发布和生产都是不同的环境，各有自己的设置和资源。成功请求报告版本的端点，可以帮助判断正在响应的是哪个版本。

```text
Staging version response: 2
Production version response: 1
```

本例中，预发布环境返回新版本，生产环境仍返回第 1 版。

:::single-choice{#build-release-deploy-running-version} 审查者想确认生产环境是否在提供第 2 版。哪项观察能直接帮助验证？

::option[预发布环境再次返回第 2 版。]{#build-release-deploy-running-version-a explanation="这检查的仍是预发布环境。"}
::option[批准这次发布的消息。]{#build-release-deploy-running-version-b explanation="批准消息不会测试实际运行中的服务。"}
::option[从生产环境地址收到的版本响应。]{#build-release-deploy-running-version-c .correct explanation="这检查的正是审查者提出的环境。"}
:::

## 总结

现在，你可以区分一次发布过程中各环节留下的记录。

1. 把构建产物与它的源代码版本关联起来。
2. 识别发布记录批准的产物。
3. 确认目标环境中实际响应的版本。
