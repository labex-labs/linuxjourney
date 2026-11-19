---
lesson_id: "auditing-configuration-changes"
course_id: "system-auditing"
lang: "zh"
order_index: 5
title: "配置变更"
description: "学习怎样结合获准的变更、文件差异以及审计事件来核查配置。"
meta_title: "配置变更 - 系统审计"
meta_description: "对照变更工单、文件差异和审计记录，判断哪些变动符合计划，哪些还需核实。"
meta_keywords: "配置变更, 变更工单, 审计记录, 文件差异, 系统审计, Linux Journey"
---

变更工单记录计划中的操作。文件比较告诉你现在有哪些差异。审计事件描述审计范围内观测到的操作。把三者放在一起，才能判断目前可以怎样描述一次配置变更。

## 匹配预期的变更

查看下面这条模拟的维护记录。

```text
Approved: change banner.txt mode to 640
Window: 09:00–09:30 UTC
Host: web-01
```

记录写明了哪一个文件的哪项属性获准修改。其他地方出现变化，即使在同一时段，也需要另行解释。

:::single-choice{#auditing-configuration-changes-approve-scope} 哪项变化符合记录里批准的操作？

::option[web-01 上的 site.conf 内容发生了变化。]{#auditing-configuration-changes-approve-scope-b explanation="这个配置文件不在批准范围内。"}
::option[另一台主机上的 banner.txt 消失了。]{#auditing-configuration-changes-approve-scope-c explanation="记录中的操作和主机都不同。"}
::option[web-01 上的 banner.txt 权限变成 640。]{#auditing-configuration-changes-approve-scope-a .correct explanation="文件、属性、主机和获准的结果都与记录匹配。"}
:::

## 对照不同来源的观测结果

文件比较显示，横幅文件的权限发生变化，`site.conf` 的字节内容也变了。另有一条 09:15 的审计事件记录了对 `web-01` 上 `site.conf` 的写入。审计事件给出了便于调查的时间点，无法说明操作是否获准。

:::single-choice{#auditing-configuration-changes-source-comparison} 结合关于 site.conf 的两项观察，可以得出什么结论？

::option[写入发生在维护窗口内，因此已经获得授权。]{#auditing-configuration-changes-source-comparison-a explanation="工单写的是另一项操作。"}
::option[有写入记录，文件字节也变了，因此值得核查。]{#auditing-configuration-changes-source-comparison-b .correct explanation="文件比较指出了差异，审计事件则缩小了应检查的时间范围。"}
::option[修改横幅导致了这次写入。]{#auditing-configuration-changes-source-comparison-c explanation="这些观测无法证明一个操作是另一个操作的原因。"}
:::

## 编写核查说明

写清哪项差异符合计划，哪项还无法解释。记录文件、主机、时间和证据来源。下一步可以把当前配置与获准的副本比较，并检查是否还有另一项获准变更涵盖这次写入。

:::single-choice{#auditing-configuration-changes-useful-review} 交接时应该怎样描述 site.conf？

::option[写明差异，引用观测到的写入，要求提供相应的审批依据。]{#auditing-configuration-changes-useful-review-c .correct explanation="说明既保留了已有证据，也交代了待核实的问题。"}
::option[将它标为已批准，并省略路径。]{#auditing-configuration-changes-useful-review-a explanation="这会丢失目标信息，还假定存在记录中没有给出的批准。"}
::option[把这项改动归到负责横幅变更的人名下。]{#auditing-configuration-changes-useful-review-b explanation="现有记录不足以确定是谁做的。"}
:::

## 比较两条维护记录

另一张工单批准在之后编辑 site.conf。结束核查之前，要把实际观测时间、目标主机和文件与工单相互对照。即使工单批准改动的是同一个文件，也可能无法解释更早的事件。

:::single-choice{#auditing-configuration-changes-final-application} 工单允许在 09:40 到 10:00 之间修改 web-01 上的 site.conf。关于 09:15 记录到的写入，还有什么需要核实？

::option[site.conf 是否也存在于工单系统以外。]{#auditing-configuration-changes-final-application-b explanation="文件比较已经看到了该配置。"}
::option[后来的工单是否应该自动解释所有过去的写入。]{#auditing-configuration-changes-final-application-c explanation="批准只适用于规定的操作和时间。"}
::option[更早的这次写入是否有单独的批准。]{#auditing-configuration-changes-final-application-a .correct explanation="主机和路径都匹配，但记录时间不在获准的时段内。"}
:::

## 总结

现在，你可以根据不同来源梳理一次配置变更的已知情况。

1. 从获准的工单中读出变更范围。
2. 用差异报告和审计事件说明实际观察到什么。
3. 说明还缺哪些证据，并选出下一项检查。
