---
lesson_id: "deployment-records"
course_id: "deployment"
lang: "zh"
order_index: 6
title: "部署记录"
description: "学习从简短的发布时间线还原部署和回滚过程。"
meta_title: "部署记录 - 部署"
meta_description: "用时间线说明部署、验证和回滚的过程，留下能供同事复查的信息。"
meta_keywords: "部署记录, 发布时间线, 回滚记录, 版本核验, DevOps, Linux Journey"
---

部署记录可以帮助其他人把用户看到的结果与一次改动联系起来。先记录时间、环境、源代码版本和产物，再加上检查结果以及后续采取的措施。

## 说明改动内容

这份练习记录追踪了一次上线过程。为了方便阅读，标识都做了简写。

```text
UTC    Target   Commit   Artifact  Observation
09:00  staging  8a61e1   digest-C  version 3, home returned 200
09:12  prod     8a61e1   digest-C  version 3, home returned 503
09:18  prod     72b110   digest-B  version 2, home returned 200
```

HTTP 200 表示请求成功。HTTP 503 表示当次请求无法得到可用的服务。写实际记录时，请把检查方法和地址同结果一起保存。

:::single-choice{#deployment-records-first-prod-change} 哪一行记录了生产环境中首次观察到的 digest-C 行为？

::option[09:12 的 prod 记录。]{#deployment-records-first-prod-change-b .correct explanation="它记录了准备在生产环境运行的版本，以及失败的检查。"}
::option[09:00 的 staging 记录。]{#deployment-records-first-prod-change-a explanation="那次检查发生在另一个环境里。"}
::option[09:18 的 prod 记录。]{#deployment-records-first-prod-change-c explanation="这行记录的是回滚后的另一个产物。"}
:::

![模拟发布时间线显示预发布检查成功、生产环境返回 503，随后回滚到版本 2](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-records/release-timeline.png)

## 解释回滚

最后一行显示环境回到了 digest-B。版本检查和首页响应描述了回滚后的结果，没有解释先前失败的具体原因。原因尚无证据时，先将假设与确认的结果分开。

:::single-choice{#deployment-records-rollback-evidence} 关于 09:18 的结果，可以怎么说？

::option[09:12 的失败是数据库缺失造成的。]{#deployment-records-rollback-evidence-b explanation="记录里没有任何关于依赖项的证据。"}
::option[之后所有请求都成功了。]{#deployment-records-rollback-evidence-c explanation="一次成功检查只说明当次请求的结果。"}
::option[生产环境恢复到第 2 版，那次首页请求成功了。]{#deployment-records-rollback-evidence-a .correct explanation="这一行记录了恢复后的版本与观察到的 HTTP 响应。"}
:::

## 把记录交给下一位同事

接手的人需要按相同范围复查。请记录如何测量、带时区的时间戳，以及生成该产物的构建链接（如果有）。原因仍不明时，也要写清下一步准备检查什么。

:::single-choice{#deployment-records-handoff-detail} 哪个细节能帮助下一位审查者复现首页检查？

::option[只提供上一次发布的标识。]{#deployment-records-handoff-detail-a explanation="旧版本有助于比较，无法说明这次检查在哪儿、什么时间运行。"}
::option[检查的确切目标地址和时间。]{#deployment-records-handoff-detail-c .correct explanation="这些信息让对方可以验证同一条访问路径，并与相同时段内的其他信号对照。"}
::option[创建源代码提交的时间。]{#deployment-records-handoff-detail-b explanation="提交时间说明的是较早的事件。复查需要这次检查的时间和目标地址。"}
:::

## 记录实际运行的产物

部署说明中的标签可能在发布以后改变指向。如果服务已经报告第 2 版，应同时记下便于阅读的标签和实际运行的产物。即使仓库里的标签之后改了指向，这两个值仍能帮助别人核对本次发布。

:::single-choice{#deployment-records-final-application} 发布说明中写的是 site:2。补充哪项信息可以让之后的比较更可靠？

::option[最近拉取过 site:2 的人拿到的摘要。]{#deployment-records-final-application-c explanation="后来拉取到的内容可能与服务实际运行的版本不同。"}
::option[实际运行镜像的完整摘要。]{#deployment-records-final-application-a .correct explanation="如果标签后来指向了其他内容，摘要仍可以标识当时选定的内容。"}
::option[在另一个字段里再抄一遍标签。]{#deployment-records-final-application-b explanation="重复写标签也无法解决指向不明确的问题。"}
:::

## 总结

现在，你可以看懂发布时间线，并把它交给其他人复查。

1. 在记录中找出环境、修订版本和产物。
2. 根据观察结果描述回滚。
3. 为下一次检查保留足够的信息。
