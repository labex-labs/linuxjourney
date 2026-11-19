---
lesson_id: "web-authorization"
course_id: "web-security"
lang: "zh"
order_index: 6
title: "授权"
description: "学习如何根据应用的访问策略判断已通过身份验证的用户能否执行请求。"
meta_title: "授权 - Web 安全"
meta_description: "用角色、操作和目标资源判断应用该允许还是拒绝请求，并确认服务端实施了规则。"
meta_keywords: "授权, 角色权限, 访问策略, 服务端检查, Web 安全, Linux Journey"
---

用户即使已经登录，也可能没有权限执行某项操作。**授权**就是判断指定账户是否可以对某项资源执行某个操作。

## 读取访问规则

**角色**是一组有名称的权限。下面这套练习规则用于某个预览服务。

```text
Role       View published page   Edit draft
Reader    Yes                   No
Editor    Yes                   Yes
```

查看用户角色所在的行，以及请求操作所在的列。编辑人员可以查看已发布的页面，也可以编辑草稿。读者可以查看已发布的页面。

:::single-choice{#web-authorization-read-policy} 一位已经登录的读者请求编辑草稿。表格是怎么规定的？

::option[Reader 角色不允许执行这个操作。]{#web-authorization-read-policy-b .correct explanation="Reader 这一行在 Edit draft 列中标为 No。"}
::option[只要账户已登录，就可以执行。]{#web-authorization-read-policy-a explanation="这个操作对不同角色有不同的权限设置。"}
::option[用户必须切换到 HTTPS 才能获得编辑权限。]{#web-authorization-read-policy-c explanation="传输保护不会向应用用户分配权限。"}
:::

## 检查具体资源

许多系统会针对不同资源授予不同权限。编辑人员可能能修改自己项目里的草稿，却只能查看另一个项目的页面。检查权限时，要同时识别请求操作和目标资源。

:::single-choice{#web-authorization-target-resource} Maya 可以编辑项目 A。判断她能否编辑项目 B，要看什么证据？

::option[项目 A 的标题。]{#web-authorization-target-resource-b explanation="标题无法说明她对另一个项目拥有哪些权限。"}
::option[她已经成功登录。]{#web-authorization-target-resource-c explanation="身份验证确认的是 Maya 的账户，对具体资源的权限仍要另行判断。"}
::option[适用于 Maya 和项目 B 的权限策略。]{#web-authorization-target-resource-a .correct explanation="先前授予的权限只覆盖某项特定资源。"}
:::

## 在服务端执行规则

用户界面可以对读者隐藏编辑按钮，但服务器在收到请求时，仍需按权限策略作出判断。针对这个练习服务，使用获准的常规操作测试应该允许和应该拒绝的情况。

:::single-choice{#web-authorization-decision-location} 应用对读者隐藏了编辑按钮。还应该在哪里实施访问控制？

::option[只在浏览器决定显示哪些按钮时实施。]{#web-authorization-decision-location-a explanation="浏览器可以通过界面引导用户。真正收到请求后，由服务作出访问决定。"}
::option[在接收操作请求的服务中实施。]{#web-authorization-decision-location-c .correct explanation="服务每次都可以核对账户、操作和目标资源。"}
::option[只在列出角色的页面上实施。]{#web-authorization-decision-location-b explanation="显示角色名无法阻止受限制的操作。"}
:::

## 总结

现在，你可以判断应用应该如何处理访问请求。

1. 对照账户角色与请求执行的操作。
2. 检查时把具体目标资源也考虑进去。
3. 确认服务会在处理请求时实施访问策略。
