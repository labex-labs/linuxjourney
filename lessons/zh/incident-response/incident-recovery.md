---
lesson_id: "incident-recovery"
course_id: "incident-response"
lang: "zh"
order_index: 5
title: "恢复"
description: "学习在宣布恢复完成前，验证服务是否处于预期且获准的状态。"
meta_title: "恢复 - 事件响应"
meta_description: "核对恢复后的版本和用户访问路径，并在观测期内确认故障没有再次出现。"
meta_keywords: "服务恢复, 恢复验证, 版本核验, 观测期, 事件响应, Linux Journey"
---

**恢复**是让服务回到预期状态，并检查它能否持续正常使用。进程重新启动只是一个早期信号。团队还需要证据，确认配置、依赖服务以及用户实际体验都符合预期。

## 确认恢复后的状态

记下获准用于恢复的版本和配置。如果服务之前做过隔离，确认哪些访问仍应受限。重新开放某条访问路径可能改变遏制措施的覆盖范围。

:::single-choice{#incident-recovery-restore-target} 什么结果能说明你是否恢复到了预期版本？

::option[任意一台不相关虚拟机上的新时间戳。]{#incident-recovery-restore-target-b explanation="这无法识别被恢复的服务。"}
::option[只看可用软件包的列表。]{#incident-recovery-restore-target-c explanation="可用的软件包无法说明目前哪个版本在处理请求。"}
::option[目标服务的响应或部署记录标明了获准的版本。]{#incident-recovery-restore-target-a .correct explanation="这把实际运行的服务与团队选定的版本对应起来。"}
:::

## 重新检查最初的问题

模拟事件中，访客打开公开主页时看到了 `503`。恢复后，应从合适的测试位置请求同一条路径。核对是否得到预期的成功结果，再查看近期请求的出错情况。内部预览正常并不能验证公开路径。

:::single-choice{#incident-recovery-verify-original-path} 哪项测试最能说明用户最初看到的问题已经消失？

::option[只检查服务的可执行文件是否存在。]{#incident-recovery-verify-original-path-a explanation="文件可能存在，但并没有处理外部请求。"}
::option[从相关客户端的访问路径检查公开主页。]{#incident-recovery-verify-original-path-b .correct explanation="这重复了最初失败的那项观测。"}
::option[只检查内部预览。]{#incident-recovery-verify-original-path-c explanation="内部预览与受影响的路径不同。"}
:::

## 持续观测

约定一个简短的观测期和成功标准。查看错误、延迟和拒绝访问等相关信号。记录检查限制、未完成的事项及下一次检查时间。把恢复证据和事件记录一起保存。

:::single-choice{#incident-recovery-observation-period} 初步检查通过，但故障之前是间歇出现的。结束恢复验证前还应做什么？

::option[在观测期内继续检查约定的信号。]{#incident-recovery-observation-period-c .correct explanation="这样可以判断恢复后的状态是否稳定。"}
::option[收到一次响应就立即结束验证。]{#incident-recovery-observation-period-a explanation="一次观测可能漏掉间歇性问题。"}
::option[丢弃所有用于比较的数据。]{#incident-recovery-observation-period-b explanation="较早的结果可以说明哪些方面有所改善。"}
:::

## 总结

现在，你可以检查恢复后的服务状态和用户实际体验。

1. 确认获准的恢复版本和配置。
2. 再次测试用户能看到的故障症状。
3. 结束恢复验证前，观测约定的信号。
