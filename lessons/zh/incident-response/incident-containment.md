---
lesson_id: "incident-containment"
course_id: "incident-response"
lang: "zh"
order_index: 4
title: "遏制措施"
description: "从目的、影响和证据需求三个方面比较获准的遏制方案。"
meta_title: "遏制措施 - 事件响应"
meta_description: "制定范围明确的遏制措施，保留取证和维护所需的访问，并分别验证限制与服务状态。"
meta_keywords: "遏制措施, 事件响应, 服务隔离, 访问范围, 证据保全, Linux Journey"
---

**遏制**是在团队调查期间采取的短期措施，用来限制仍在发生的影响。合适的措施取决于哪些资源受到影响，以及人们还需要保留哪些访问权限。

## 明确要限制的范围

假设有人可以通过公开路径打开内部预览面板，而主页仍应对外开放。一种做法是限制预览路径，范围更大的做法则是让整个网站下线。比较两种选择分别影响哪些行为。

:::single-choice{#incident-containment-narrow-action} 要阻止公开访问预览，同时保持主页可用，哪种做法最合适？

::option[不管用途，禁用所有公开路径。]{#incident-containment-narrow-action-b explanation="这样主页也无法访问。"}
::option[限制受影响的预览路径，并验证预览和主页两条路径。]{#incident-containment-narrow-action-a .correct explanation="这针对已报告的暴露问题，也会检查必须保留的服务。"}
::option[修改预览服务的名称。]{#incident-containment-narrow-action-c explanation="改名无法阻止请求到达服务。"}
:::

## 兼顾证据与访问

参考事件响应计划，并咨询获准执行变更的人。记录谁批准了变更、预计持续多久，以及在条件允许时应当先保留哪些证据。也要考虑措施会不会中断服务日志，或者阻挡响应人员的访问。

:::single-choice{#incident-containment-action-impact} 拟议的隔离措施也可能让调查人员无法获取记录。团队应当先核查什么？

::option[需要保留哪些资料，以及怎样让获准的响应人员继续访问。]{#incident-containment-action-impact-b .correct explanation="这样既考虑遏制目标，也顾及了调查工作。"}
::option[只看配置文件的名称是否够短。]{#incident-containment-action-impact-a explanation="文件名无法保留记录，也不能保证访问。"}
::option[是否公开凭据，让所有人都能重新连接。]{#incident-containment-action-impact-c explanation="需要保护凭据，并继续控制访问范围。"}
:::

## 验证遏制措施

检查非预期的访问路径是否已经关闭。单独验证仍应开放的路径，了解措施有没有副作用。记录实施时间，以及团队应何时重新评估。遏制成功时，根本原因可能还没有查清。

:::single-choice{#incident-containment-containment-success} 公开预览路径已关闭，主页仍然正常。可以得出哪个结论？

::option[根本原因肯定已经修复。]{#incident-containment-containment-success-a explanation="测试验证了访问边界，无法证明原因已得到修复。"}
::option[已经测试了通往预览面板的所有可能路径。]{#incident-containment-containment-success-b explanation="这些检查只覆盖实际测试的特定路径。"}
::option[测试过的公开预览路径已被阻止，必须开放的主页仍可访问。]{#incident-containment-containment-success-c .correct explanation="这个说法没有超出已经验证的范围。"}
:::

## 总结

现在，你可以评估一项短期遏制措施。

1. 写明措施应该限制哪条路径或哪类访问。
2. 核对授权、证据和预期影响。
3. 分别验证预期限制与必须保留的服务。
