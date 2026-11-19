---
lesson_id: "system-audit-events"
course_id: "system-auditing"
lang: "zh"
order_index: 1
title: "审计事件"
description: "学习选择能回答受保护文件相关问题的审计事件。"
meta_title: "审计事件 - 系统审计"
meta_description: "根据文件、操作、结果和审计范围，判断哪些审计记录可以回答当前问题。"
meta_keywords: "审计事件, 审计记录, 受保护文件, 审计范围, 系统审计, Linux Journey"
---

服务日志可能告诉你某个网页被加载过。**审计记录**则可以描述系统按配置观测到的特定操作，例如向服务配置文件写入数据。先确定要关注什么操作，以及核查该操作需要哪些信息。

## 明确审计问题

假设 Web 服务的配置决定谁可以打开预览，你想检查这个文件的改动。有用的记录应写明操作对象、操作、时间、账户背景和结果。每个字段都能帮助核查者还原操作的一部分。

:::single-choice{#system-audit-events-choose-object} 这次核查需要审计记录提供什么？

::option[只需要当天的 Web 请求总数。]{#system-audit-events-choose-object-b explanation="请求量反映的是另一类活动。"}
::option[被操作的目标配置文件。]{#system-audit-events-choose-object-a .correct explanation="操作对象可以让你把这次变更与对其他文件的写入区分开。"}
::option[只需要操作类型，例如写入。]{#system-audit-events-choose-object-c explanation="操作类型说明尝试做什么。目标文件才能表明这次操作与当前问题有没有关系。"}
:::

## 读取操作结果

审计记录既可能描述成功写入，也可能描述没有成功的尝试。结合操作和结果一起看。写入被拒绝仍然可以作为有人尝试过的证据，只是与写入成功支持的结论不同。

:::single-choice{#system-audit-events-operation-result} 记录显示尝试向配置文件写入，结果是被拒绝。这说明什么？

::option[记录到的写入尝试被拒绝了。]{#system-audit-events-operation-result-b .correct explanation="操作和结果共同描述了观察到的行为。"}
::option[文件肯定已经被替换。]{#system-audit-events-operation-result-a explanation="拒绝结果无法证明修改成功。"}
::option[预期网页返回了 HTTP 200。]{#system-audit-events-operation-result-c explanation="这条记录没有描述网页请求。"}
:::

## 检查审计覆盖范围

审计系统只能记录它的机制和策略能够观测到的事件。看到空结果时，先核对策略是否覆盖正确的路径、操作和时段，再决定是否据此下结论。记下你查看的是哪个数据来源。

:::single-choice{#system-audit-events-empty-audit} 选定的日志里找不到写入记录。在判断没有发生写入之前，哪项检查有用？

::option[统计安装了多少个编辑器。]{#system-audit-events-empty-audit-a explanation="安装的软件无法表明审计覆盖范围。"}
::option[只按另一个账户名搜索同一时段。]{#system-audit-events-empty-audit-b explanation="确认采集已经生效后，继续搜索可能有用。第一步是检查系统是否有机会记录相关事件。"}
::option[核对审计策略和现有记录的时间范围。]{#system-audit-events-empty-audit-c .correct explanation="如果审计没有覆盖相关活动，即使操作发生过，也可能找不到记录。"}
:::

## 总结

现在，你可以为受保护的资源选择有用的审计证据。

1. 明确要核查的操作和它的目标。
2. 把记录的结果和相应的操作一起看。
3. 把空结果当作证据前，先核对审计范围。
