---
lesson_id: "web-sessions-and-cookies"
course_id: "web-security"
lang: "zh"
order_index: 5
title: "会话与 Cookie"
description: "学习 Cookie 如何将浏览器的后续请求关联到 Web 会话。"
meta_title: "会话与 Cookie - Web 安全"
meta_description: "跟踪 Cookie 如何在浏览器与服务器之间传递，理解常见属性以及注销怎样结束会话。"
meta_keywords: "Web 会话, Cookie, Set-Cookie, Cookie 属性, 会话令牌, Linux Journey"
---

一次登录成功后，浏览器往往会继续发出其他请求。**会话**让应用把这些请求与已登录的账户关联起来。常见做法是把一个短标识保存在浏览器的 Cookie 中。

## 跟踪 Cookie 的传递

下面的例子经过简化。响应发出名为 `session` 的 Cookie，其中用的是演示用的假令牌。

```http
Set-Cookie: session=sample-token; Secure; HttpOnly; SameSite=Lax
```

之后，符合 Cookie 规则的请求可以带上这个 Cookie。

```http
Cookie: session=sample-token
```

服务器用令牌查找之前创建的会话。

:::single-choice{#web-sessions-and-cookies-direction} 浏览器通过哪个请求头把 Cookie 值发回服务器？

::option[Set-Cookie。]{#web-sessions-and-cookies-direction-a explanation="服务器在响应中发送这个头字段，用它设置 Cookie。"}
::option[Content-Type。]{#web-sessions-and-cookies-direction-c explanation="这个头字段描述消息正文的格式。"}
::option[Cookie。]{#web-sessions-and-cookies-direction-b .correct explanation="请求符合规则时，浏览器会发送这个请求头。"}
:::

## 读懂属性

`Secure` 会把 Cookie 的常规传输限制在 HTTPS 上。`HttpOnly` 防止页面脚本通过常用的 Cookie API 读取它。`SameSite` 控制浏览器在何种情况下会把它加入从其他网站发起的请求。三个设置分别影响浏览器的不同行为。

:::single-choice{#web-sessions-and-cookies-secure-attribute} 哪个属性指示浏览器限制这个 Cookie 只通过 HTTPS 传输？

::option[HttpOnly。]{#web-sessions-and-cookies-secure-attribute-b explanation="这个属性限制页面脚本访问 Cookie。"}
::option[Secure。]{#web-sessions-and-cookies-secure-attribute-a .correct explanation="这个属性约束 Cookie 的传输连接。"}
::option[名称 session。]{#web-sessions-and-cookies-secure-attribute-c explanation="Cookie 名称只是应用选择的标记。"}
:::

## 结束会话

用户退出登录时，服务可以在服务器上让会话失效，并要求浏览器移除已经保存的 Cookie。服务器端的失效处理很重要，因为浏览器可能会暂时保留旧值。对待真实会话令牌时，应像保护登录凭据一样保护它，避免出现在截图和共享日志中。

:::single-choice{#web-sessions-and-cookies-after-sign-out} 已经失效的会话令牌再次到达服务器时，应该怎样处理？

::option[服务器应把请求视为未通过身份验证。]{#web-sessions-and-cookies-after-sign-out-c .correct explanation="与这个值关联的服务器端会话已经失效。"}
::option[服务器应该自动恢复旧会话。]{#web-sessions-and-cookies-after-sign-out-a explanation="旧会话已经结束了。"}
::option[Cookie 还有名称，所以服务器应接受它。]{#web-sessions-and-cookies-after-sign-out-b explanation="Cookie 的名称无法使它的值重新有效。"}
:::

## 总结

现在，你可以追踪浏览器与服务之间的会话 Cookie。

1. 找出设置 Cookie 的响应头，以及发回 Cookie 的请求头。
2. 解释常见 Cookie 属性的用途。
3. 说明服务器怎样通过使会话失效来结束会话。
