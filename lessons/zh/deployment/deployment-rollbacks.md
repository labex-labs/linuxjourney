---
lesson_id: "deployment-rollbacks"
course_id: "deployment"
lang: "zh"
order_index: 5
title: "回滚"
description: "学习如何选择已知可用的版本，以及如何判断只回滚应用是否足够。"
meta_title: "回滚 - 部署"
meta_description: "根据部署历史选择回滚目标，核对共享数据兼容性，并实际验证服务是否恢复。"
meta_keywords: "回滚, 部署恢复, 版本验证, 数据兼容性, DevOps, Linux Journey"
---

**回滚**是把服务恢复到之前确认可用的发布版本。可以参考部署历史选择目标。撤销改动之前，先查清这次发布是否还改变了共享数据或设置。

## 选择以前的发布版本

示例中，新版本发布后有一次请求失败。上一个验证通过的是第 2 版。下面的引用标签在真实记录中应当是完整的镜像摘要。

```text
08:50  version 2  digest-B  homepage and version check passed
09:10  version 3  digest-C  homepage check failed
```

如果第 2 版仍能与当前环境配合使用，它就是合适的回滚候选。根据记录中的产物标识找到它。

:::single-choice{#deployment-rollbacks-previous-version} 首先应该调查哪个镜像能否作为回滚目标？

::option[主机缓存中最新的镜像。]{#deployment-rollbacks-previous-version-a explanation="缓存顺序无法说明哪个版本已验证可用。"}
::option[digest-C，因为最近部署的是它。]{#deployment-rollbacks-previous-version-c explanation="记录表明这个产物的检查失败了。"}
::option[digest-B，此前通过了相关检查。]{#deployment-rollbacks-previous-version-b .correct explanation="记录将它与最近一次验证通过的版本对应起来。"}
:::

## 检查数据兼容性

应用发布也可能改变数据库或其他共享资源。启动旧镜像时，这些外部状态不会随之恢复。先确认旧应用能否读取当前的数据。如果还要恢复数据，应按团队的恢复计划操作，并考虑备份之后发生的变化。

:::single-choice{#deployment-rollbacks-external-state} 第 3 版修改了数据库格式。用第 2 版连接该数据库之前，必须核对什么？

::option[第 2 版是否通过了以前的首页检查。]{#deployment-rollbacks-external-state-b explanation="以前的检查表明第 2 版值得考虑，但不反映当前数据库格式。"}
::option[第 2 版能否使用当前的数据格式。]{#deployment-rollbacks-external-state-a .correct explanation="替换应用镜像不会还原共享数据。"}
::option[发布说明里是否提到了数据库名称。]{#deployment-rollbacks-external-state-c explanation="真正要解决的是旧代码能否使用当前数据。"}
:::

## 确认回滚结果

回滚后检查正在运行的版本，再从用户的角度重复之前失败的检查。重新查看重要的依赖项。记下时间、恢复的版本和检查结果，让别人能够区分最初的故障和后续恢复。

:::single-choice{#deployment-rollbacks-rollback-proof} 回滚命令已经结束。哪两项结果一起支持服务已经恢复的结论？

::option[端点报告第 2 版，之前失败的检查现在通过了。]{#deployment-rollbacks-rollback-proof-c .correct explanation="两项结果分别验证了回滚目标版本和原先受影响的行为。"}
::option[两次成功下载了镜像。]{#deployment-rollbacks-rollback-proof-a explanation="下载只是在准备文件，没有检查运行中的服务。"}
::option[之前截取的第 2 版截图。]{#deployment-rollbacks-rollback-proof-b explanation="截图显示的是以前的状态。"}
:::

## 总结

现在，你可以根据证据制定回滚计划。

1. 选择历史上已经验证通过的发布版本。
2. 检查共享数据和配置的兼容性。
3. 核对恢复的版本，以及用户端原本受到影响的行为。
