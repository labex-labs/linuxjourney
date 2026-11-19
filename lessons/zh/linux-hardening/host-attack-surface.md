---
lesson_id: "host-attack-surface"
course_id: "linux-hardening"
lang: "zh"
order_index: 1
title: "攻击面"
description: "学习判断 Linux 主机需要对外提供哪些资源，以及哪些访问路径值得核查。"
meta_title: "攻击面 - Linux 安全加固"
meta_description: "对照服务的预期用途和实际可访问范围，找出应优先收紧的访问路径。"
meta_keywords: "攻击面, 服务清单, 访问路径, Linux 安全加固, 网络安全, Linux Journey"
---

一台 Linux 主机可能同时提供公开网页、维护入口和后台服务。先记下每个服务的用途和应该允许哪些人访问。这样就能找出没有明确用途的访问权限。

## 列出预期的访问方式

一份简单的清单可以列出每项资源，以及需要使用它的人员或程序。下面是一台练习主机的清单。

```text
Resource           Intended access
Public homepage    Visitors
Maintenance SSH    Operations team
Preview panel      Local staff on this host only
```

**访问路径**就是用户或程序到达资源的方式。外部能够接触、也可能因此影响系统的接口，构成了系统**攻击面**的一部分。

:::single-choice{#host-attack-surface-intended-audience} 根据清单，哪项资源需要一条公众可用的网络访问路径？

::option[用于维护的 SSH。]{#host-attack-surface-intended-audience-b explanation="它面向的是运维团队。"}
::option[公开主页。]{#host-attack-surface-intended-audience-a .correct explanation="预期访问者包括主机以外的访客。"}
::option[预览面板。]{#host-attack-surface-intended-audience-c explanation="清单要求只在主机本地使用。"}
:::

## 比较预期与实际访问

假设从网络上能打开预览面板，但清单仍写着只允许本地访问。更改之前，先找负责人核实，并验证实际走的访问路径。有些服务需要运行，却没有必要接收远程请求。

:::single-choice{#host-attack-surface-mismatch} 按照清单上的规则，哪个现象需要核查？

::option[访客能访问预览面板。]{#host-attack-surface-mismatch-b .correct explanation="面板出现了供预期用户之外的人访问的路径。"}
::option[访客能打开主页。]{#host-attack-surface-mismatch-a explanation="这符合主页的预期用途。"}
::option[工作人员能在主机本地打开预览。]{#host-attack-surface-mismatch-c explanation="本地访问符合已有需求。"}
:::

## 确定优先核查的项目

首先关注没有必要、又可能造成严重影响的访问。在练习示例中，可以更改网站的预览面板，比没有重要数据的闲置服务更值得优先处理。记下预期用户、实际暴露情况，以及如何验证限制确实生效并且没有影响合法访问。

:::single-choice{#host-attack-surface-priority-check} 调整预览的访问范围之后，哪两项观察能共同证明限制达到了目标？

::option[面板仍能接收本地请求。]{#host-attack-surface-priority-check-a explanation="这验证了必要的本地访问，但还没检查非预期的远程路径。"}
::option[机器已重启，主机名不变。]{#host-attack-surface-priority-check-b explanation="这两项机器状态无法说明访问规则是否生效。"}
::option[工作人员仍能从本地访问，非预期的远程路径已经关闭。]{#host-attack-surface-priority-check-c .correct explanation="这两项检查分别验证了必要的访问和预期的限制。"}
:::

## 总结

现在，你可以判断哪些访问路径值得优先加固。

1. 说明一项资源的用途和预期使用者。
2. 对比预期访问与实际访问范围。
3. 改动后同时验证访问限制和合法使用。
