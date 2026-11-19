---
lesson_id: "web-access-logs"
course_id: "web-security"
lang: "zh"
order_index: 7
title: "Web 访问日志"
description: "学习利用 HTTP 访问日志了解服务返回了什么，同时避免泄露凭据。"
meta_title: "Web 访问日志 - Web 安全"
meta_description: "读懂 HTTP 访问日志，用请求 ID 核对授权结果，并安全地分享日志片段。"
meta_keywords: "Web 访问日志, HTTP 状态码, 请求 ID, 凭据保护, Web 安全, Linux Journey"
---

Web 服务器可以为每次请求保存一条**访问日志**。日志可能包含时间、路径、响应状态码和请求 ID。调查问题时，只使用回答问题所需的字段。

## 读取请求结果

这段模拟日志给每项信息加了字段名。两个请求访问了不同的路径。

```text
t=09:18:01Z request=r31 method=GET path=/health status=200
t=09:18:04Z request=r32 method=GET path=/staff status=403
```

`403` 表示服务拒绝了请求。要与其他记录对照时，先核对准确的路径和请求 ID。

:::single-choice{#web-access-logs-log-result} 调查这次拒绝时，应追踪哪个请求？

::option[访问 /health 的 r31。]{#web-access-logs-log-result-a explanation="这行报告的是成功的健康检查请求。"}
::option[访问 /staff 的 r32。]{#web-access-logs-log-result-b .correct explanation="它的状态是 403，对应片段中被拒绝的请求。"}
::option[把两条记录视为同一个请求来追踪。]{#web-access-logs-log-result-c explanation="请求 ID 和路径可以把它们区分开。"}
:::

## 查找权限判定

访问日志记录的是服务器返回了什么，不一定解释为什么作出某项权限决定。如果应用也记录了授权结果，就按请求 ID 和时间去匹配记录。在本例中，这能帮助你确认适用了哪条规则。

:::single-choice{#web-access-logs-refusal-reason} 访问日志显示 403。哪条额外记录最能解释拒绝原因？

::option[应用对 r32 作出的权限判定。]{#web-access-logs-refusal-reason-a .correct explanation="匹配的记录可能会说明采用了哪条规则。"}
::option[另一个网站返回的成功响应。]{#web-access-logs-refusal-reason-b explanation="它与这次拒绝没有关联。"}
::option[早先对健康检查路径发出的请求。]{#web-access-logs-refusal-reason-c explanation="那是另一项操作，结果也不同。"}
:::

## 防止凭据进入日志

不要记录能让他人使用某个会话的值，例如完整的会话 Cookie 或授权令牌。请求 ID 和响应状态仍能帮助排查问题。分享日志样本时，移除敏感字段，只保留调查所需的信息。

:::single-choice{#web-access-logs-safe-fields} 哪些字段既能帮助追踪被拒绝的请求，又不会复制凭据？

::option[完整的会话 Cookie 和账户密码。]{#web-access-logs-safe-fields-a explanation="两者都是敏感值，不应放入共享日志。"}
::option[授权令牌和一个公开路径。]{#web-access-logs-safe-fields-b explanation="路径可能有用，但令牌属于私有凭据。"}
::option[请求 ID 及其响应状态。]{#web-access-logs-safe-fields-c .correct explanation="通过这些字段可以匹配相关记录，无需公开会话的值。"}
:::

## 分享必要的日志片段

假设审查者需要了解一次被拒绝的请求。如果时间、请求 ID、方法、清理后的路径和状态已经足够，就只保留这些字段。有些路径的查询字符串中可能有私密值。分享之前应检查整个片段。

:::single-choice{#web-access-logs-final-application} 哪种日志片段最适合这样的审查？

::option[默认提供完整请求及所有头字段。]{#web-access-logs-final-application-b explanation="请求可能包含凭据或不必要的个人数据。"}
::option[只保留状态码，删除所有标识。]{#web-access-logs-final-application-c explanation="仅用状态码可能很难匹配对应的授权记录。"}
::option[清除敏感信息的路径，以及请求时间、请求 ID 和响应状态。]{#web-access-logs-final-application-a .correct explanation="这样能保留关联所需字段，又不会公开会话的值。"}
:::

## 总结

现在，你可以读懂基本的访问日志，并安全保留有用的上下文。

1. 把请求 ID、路径与响应对应起来。
2. 需要查明原因时，找出相关的权限判定记录。
3. 防止凭据进入捕获和共享的日志。
