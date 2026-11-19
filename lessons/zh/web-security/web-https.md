---
lesson_id: "web-https"
course_id: "web-security"
lang: "zh"
order_index: 2
title: "HTTPS"
description: "学习判断 Web 请求的哪一段受到 HTTPS 保护。"
meta_title: "HTTPS - Web 安全"
meta_description: "沿浏览器、代理和内部服务器之间的请求路径，判断 TLS 在哪里起作用。"
meta_keywords: "HTTPS, TLS, 加密连接, 代理, Web 安全, Linux Journey"
---

HTTP 规定浏览器与服务器交换什么样的消息。HTTPS 通过 **TLS** 传输同样的消息。TLS 是一种保护连接并帮助浏览器验证服务器身份的协议。

## 找出受到保护的连接

假设浏览器连接到 `https://site.example`。TLS 连接建立后，浏览器和服务器可以交换加密的 HTTP 消息。即使有人观察这段网络通信，也不能直接读取 HTTP 正文，或在不被发现的情况下修改正文。

```text
Browser  ===== HTTPS connection =====  Website server
```

浏览器仍然需要验证服务器出示的身份。

:::single-choice{#web-https-protected-hop} 在这个简单的例子里，HTTPS 保护什么？

::option[浏览器已经显示出来的网页。]{#web-https-protected-hop-b explanation="浏览器读取的是解密后的响应。"}
::option[网站存储的所有备份。]{#web-https-protected-hop-c explanation="保护备份需要另外的措施。"}
::option[通过受保护连接发送的 HTTP 消息。]{#web-https-protected-hop-a .correct explanation="TLS 保护其两个端点之间正在传输的消息。"}
:::

## 读取多段访问路径

代理可以接收浏览器请求，再把它转发到另一台服务器。如果 TLS 在代理处终止，代理在转发前能够读取请求。到下一台服务器的连接需要自己的保护。应分别检查每一段连接。

```text
Browser  === HTTPS ===  Proxy  --- HTTP ---  Internal server
```

图中的外部连接使用 TLS，内部连接使用的是普通 HTTP。

:::single-choice{#web-https-inner-hop} 哪一段连接需要单独改动，才能获得 TLS 保护？

::option[浏览器到代理。]{#web-https-inner-hop-a explanation="这一段已经显示使用 HTTPS。"}
::option[代理到内部服务器。]{#web-https-inner-hop-b .correct explanation="图中的内部连接使用普通 HTTP。"}
::option[一个从未访问这个网站的浏览器标签页。]{#web-https-inner-hop-c explanation="这个标签页在图中没有连接。"}
:::

## 单独判断访问权限

安全连接有效时，可以帮助你验证服务器身份，也能保护传输中的消息。哪个账户可以阅读网页或更改设置，仍由应用决定。即使一个私密页面使用了强有力的 TLS 保护，也需要应用层的访问策略。

:::single-choice{#web-https-access-vs-transport} 返回私人账户页面之前，服务应该核对什么？

::option[已通过身份验证的账户是否有权读取该页面。]{#web-https-access-vs-transport-c .correct explanation="由应用的授权规则决定账户可访问哪些内容。"}
::option[只核对是否启用了 TLS。]{#web-https-access-vs-transport-a explanation="HTTPS 保护通信过程，服务还需要判断访问权限。"}
::option[只核对证书是否涵盖请求使用的主机名。]{#web-https-access-vs-transport-b explanation="证书帮助验证服务器身份。私密页面的访问仍由应用控制。"}
:::

## 总结

现在，你可以沿着 Web 请求的路径说明 HTTPS 保护哪些连接。

1. 找出 TLS 连接从哪里开始、在哪里结束。
2. 代理转发请求时，逐段检查连接。
3. 说明应用为什么仍需做访问控制。
