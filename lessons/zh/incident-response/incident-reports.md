---
lesson_id: "incident-reports"
course_id: "incident-response"
lang: "zh"
order_index: 6
title: "事件报告"
description: "学习根据观测证据和待核实事项写一份简明的事件报告。"
meta_title: "事件报告 - 事件响应"
meta_description: "根据受影响路径、时间线和恢复结果写清楚已知事实、未解问题及下一步工作。"
meta_keywords: "事件报告, 事件交接, 恢复证据, 待核实事项, 事件响应, Linux Journey"
---

简短的事件报告可以帮助同事直接接手，省去重新还原整个调查过程的时间。写明受影响的服务、几个带时间戳的观测结果，以及接下来要做的事。

## 报告观测结果

下面是同一次服务事件的三条模拟记录。

```text
09:17 UTC  Deployment record: version 3 reached production
09:22 UTC  Visitor-path check: homepage returned 503
09:31 UTC  After rollback: version 2, homepage returned 200
```

这些记录依次描述了一次变更、一次失败，以及恢复后一次成功的检查。写明受影响的访问路径和时间，也要保留实际测试了什么。

:::single-choice{#incident-reports-report-claim} 哪项说法可以直接从这些记录得出？

::option[09:22 的主页检查失败，回滚后检查成功。]{#incident-reports-report-claim-b .correct explanation="这概括了观察到的结果及其先后顺序。"}
::option[第 3 版肯定破坏了数据库。]{#incident-reports-report-claim-a explanation="记录没有给出故障是如何发生的。"}
::option[整个时段内所有用户都受到了影响。]{#incident-reports-report-claim-c explanation="提供的检查结果没有涵盖每一次请求。"}
:::

![模拟事件证据显示生产环境发生变更、返回 503，之后恢复检查通过](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-reports/evidence-timeline.png)

## 说明不确定性

回滚后请求成功，说明这次部署值得调查。在证据支持某个解释之前，原因应保持未定。例如，维护人员可以比较主页请求失败时段内两个版本的服务日志。

:::single-choice{#incident-reports-uncertainty-statement} 哪句话应该写进尚未解决的问题？

::option[没有任何值得继续调查的事情。]{#incident-reports-uncertainty-statement-b explanation="发布记录和错误记录缩小了后续检查的范围。"}
::option[服务一直不可用，再也没有恢复。]{#incident-reports-uncertainty-statement-c explanation="之后的测试请求已成功，与这项说法矛盾。"}
::option[503 的原因尚未确定。]{#incident-reports-uncertainty-statement-a .correct explanation="证据记录了失败和恢复检查，仍需补充能说明原因的证据。"}
:::

## 为接手的人指定下一步

写明谁可以接手、应该查看哪些记录，以及什么结果能回答尚未解决的问题。面向较多读者的通报中，不要包含机密或个人信息。短报告可以为获准审查的人员提供指向受保护证据的链接。

:::single-choice{#incident-reports-useful-handoff} 下面哪项后续行动最符合这个案例？

::option[让人随便截一张图，不指定时间或服务。]{#incident-reports-useful-handoff-a explanation="这没有说明要为故障查找什么证据。"}
::option[请服务维护人员检查第 3 版在主页请求失败时段内的日志。]{#incident-reports-useful-handoff-c .correct explanation="它为未解问题指定了具体的数据来源和时间范围。"}
::option[只让维护人员重复已经成功的第 2 版检查。]{#incident-reports-useful-handoff-b explanation="这样可以再次确认恢复，却无法解释第 3 版为什么失败。"}
:::

## 记录恢复验证的范围

一份报告可能既要说明恢复后的观测结果，也要说明影响范围还无法估计。回滚后主页检查成功，可以说明被测试的路径已恢复。要估计受影响的访客人数，仍需检查故障时段内的请求计数或其他合适数据。

:::single-choice{#incident-reports-final-application} 哪种交接说明准确表达了这两类证据？

::option[一次请求返回 200，所以每位访客都恢复正常了。]{#incident-reports-final-application-b explanation="这次成功只验证了实际测试的路径和时刻。"}
::option[恢复检查已通过，应该把之前失败的检查从报告中删掉。]{#incident-reports-final-application-c explanation="较早的失败仍是事件证据的一部分。"}
::option[回滚后主页检查已恢复正常，受影响的请求总数仍然未知。]{#incident-reports-final-application-a .correct explanation="这样可以区分已经确认的恢复结果和尚无法由现有记录确定的总数。"}
:::

练习过数据包和主机证据后，可以试试更长的 [SOC 基础复习](https://labex.io/courses/project-soc-foundations-review)练习。

## 总结

现在，你可以把事件的事实、未解问题和下一步行动交接给别人。

1. 写清受影响的路径和已观察到的时间线。
2. 区分可能原因和已确认的证据。
3. 把后续工作落实到明确的数据来源和时段。
