---
lesson_id: "web-http-requests-responses"
course_id: "web-security"
lang: "zh"
order_index: 1
title: "HTTP 请求与响应"
description: "学习阅读 HTTP 交换中的方法、路径、状态和内容类型。"
meta_title: "HTTP 请求与响应 - Web 安全"
meta_description: "读懂简单的 HTTP 请求和响应，并用 curl 检查状态码、响应头和正文。"
meta_keywords: "HTTP 请求, HTTP 响应, 状态码, Content-Type, Web 安全, Linux Journey"
---

浏览器或其他客户端通过发送 **HTTP 请求**向 Web 服务器索取内容。服务器会返回 **HTTP 响应**。对照这两条消息，就能知道客户端请求了什么，服务器又返回了什么。

## 阅读请求

下面是一条简短的 HTTP/1.1 请求。`GET` 是方法，表示客户端要求执行的操作。`/health` 是路径。`Host` 请求头标明客户端要访问哪个网站。

```http
GET /health HTTP/1.1
Host: site.example
```

**头字段**是带名称的值，用来传递关于消息的信息。方法和路径位于请求的第一行。

:::single-choice{#web-http-requests-responses-request-path} 这个客户端请求服务器返回什么？

::option[名为 HTTP/1.1 的文件。]{#web-http-requests-responses-request-path-b explanation="该部分表示协议版本。"}
::option[/health 路径上的资源。]{#web-http-requests-responses-request-path-a .correct explanation="路径位于第一行的 GET 后面。"}
::option[/site.example 路径上的资源。]{#web-http-requests-responses-request-path-c explanation="Host 请求头表示网站的主机名，不是资源路径。"}
:::

## 阅读响应

在空的练习目录中创建一个网页，再启动 Python HTTP 服务器，让它监听回环地址。重定向会把内容写入文件。让服务器留在这个终端中运行，等请求完成，再按 Ctrl+C 停止服务器。

```bash
$ mkdir web-demo
$ printf '%s\n' ready > web-demo/health.txt
$ python3 -m http.server 8094 --bind 127.0.0.1 --directory web-demo
```

在同一台机器的另一个终端中运行 `curl -i`。这个选项会在响应内容之前显示响应头。

```bash
$ curl -i http://127.0.0.1:8094/health.txt
```

响应以**状态码**开头。`200` 表示这次请求成功。响应头和正文之间有一个空行。`Content-Type` 告诉客户端如何解读正文，例如按纯文本显示。

:::single-choice{#web-http-requests-responses-response-parts} 哪一部分能帮助客户端决定如何显示内容？

::option[响应中的 Content-Type 头字段。]{#web-http-requests-responses-response-parts-b .correct explanation="它描述了响应正文的类型。"}
::option[原始请求中使用的主机名。]{#web-http-requests-responses-response-parts-a explanation="它表示客户端访问了哪个网站。"}
::option[只看路径。]{#web-http-requests-responses-response-parts-c explanation="路径用于标识资源，不能说明返回的格式。"}
:::

![LabEx 中记录的 HTTP 响应显示 200 状态码、文本内容类型和正文 ready](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-http-requests-responses/http-response.png)

## 比较两次请求的结果

`404` 表示服务器没有找到请求的资源，或者没有公开它的存在。访问一个路径可以返回 200，另一个路径则可能返回 404。比较结果时，请用确切的方法和路径。

:::single-choice{#web-http-requests-responses-health-scope} 请求 /health 返回了 200。这能说明 /welcome 的结果吗？

::option[/welcome 也返回了 200。]{#web-http-requests-responses-health-scope-a explanation="示例检查的是另一个路径。"}
::option[无法连接该主机。]{#web-http-requests-responses-health-scope-b explanation="健康检查的响应已经返回。"}
::option[需要实际请求 /welcome，才能知道它的结果。]{#web-http-requests-responses-health-scope-c .correct explanation="两条路径可以表现不同。"}
:::

要练习检查响应头和连通性，可以参阅 [在 Linux 中用 curl 测试服务器连通性](https://labex.io/tutorials/linux-how-to-test-server-connectivity-with-curl-in-linux-415082)。

## 总结

现在，你可以读懂一次简单 HTTP 交换的主要部分。

1. 从请求中找出方法、路径和主机。
2. 从响应中读出状态和内容类型。
3. 根据实际发送的那个请求描述结果。
