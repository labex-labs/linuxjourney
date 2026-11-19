---
lesson_id: "deployment-health-checks"
course_id: "deployment"
lang: "zh"
order_index: 4
title: "健康检查"
description: "学习部署后如何结合进程检查、服务检查和客户端请求来验证结果。"
meta_title: "健康检查 - 部署"
meta_description: "检查进程状态、版本端点和用户访问路径，判断部署后各项结果分别说明什么。"
meta_keywords: "部署验证, 健康检查, 版本端点, 用户访问, DevOps, Linux Journey"
---

程序刚启动就可能显示正在运行，此时却还没准备好处理请求。分阶段检查服务，才能说清每项通过的指标具体代表什么。

## 检查进程

容器列表可以显示主程序是否在运行。这是检查新部署的重要第一步，但不能据此判断程序是否完成初始化，或者浏览器是否能访问它。

:::single-choice{#deployment-health-checks-process-scope} 新容器显示 Up。这支持哪项结论？

::option[访客一定能看到新网页。]{#deployment-health-checks-process-scope-a explanation="容器状态无法说明访客请求的结果。"}
::option[检查时，容器的主程序正在运行。]{#deployment-health-checks-process-scope-b .correct explanation="Up 报告的是进程状态。"}
::option[所有依赖都已通过检查。]{#deployment-health-checks-process-scope-c explanation="这里没有列出任何依赖项的检查结果。"}
:::

## 检查服务端点

**端点**是服务能够处理的地址和路径。请选择能验证目标行为的路径。要在本地练习，请使用空的练习目录。重定向会把内容写入版本文件。让 Python 服务器继续在这个终端中监听回环地址，练习结束后按 Ctrl+C 停止它。

```bash
$ mkdir site
$ printf '%s\n' 2 > site/version.txt
$ python3 -m http.server 8091 --bind 127.0.0.1 --directory site
```

在第二个终端中请求版本文件。curl 的 `-f` 会把 HTTP 错误响应报告为失败，`-sS` 则隐藏进度，但仍显示错误。

```bash
$ curl -fsS http://127.0.0.1:8091/version.txt
```

练习的预期结果是 `2`。成功请求版本文件只能验证一小部分行为，远不等于测试了整个网站。

:::single-choice{#deployment-health-checks-endpoint-mismatch} 请求成功，但打印的是 1。应该查什么？

::option[哪个版本正在这个地址上响应。]{#deployment-health-checks-endpoint-mismatch-a .correct explanation="网络访问成功了，但观察到的版本不是预期版本。"}
::option[为什么 curl 完全连不上。]{#deployment-health-checks-endpoint-mismatch-b explanation="返回的值说明连接和响应都成功了。"}
::option[服务名称中是否有数字。]{#deployment-health-checks-endpoint-mismatch-c explanation="服务名称无法说明响应里的版本。"}
:::

![LabEx 练习服务器的回环端点返回版本 2](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-health-checks/version-response.png)

## 从客户端的位置检查

如果在服务主机上请求成功，再从用户平时连接的位置进行安全检查。负载均衡器、代理或网络规则都可能改变访问路径。记录你检查的地址及其返回结果。如果结果与发布记录不符，就继续调查部署情况。

:::single-choice{#deployment-health-checks-user-path} 本地请求返回 2，但公共测试地址返回 1。接下来哪项检查最有用？

::option[数一下本地请求打印了几行。]{#deployment-health-checks-user-path-a explanation="行数无法说明哪个版本在响应公共地址。"}
::option[只重复相同的本地检查。]{#deployment-health-checks-user-path-b explanation="本地路径已经返回了版本 2。"}
::option[查看公共访问路径选中了哪个服务版本。]{#deployment-health-checks-user-path-c .correct explanation="两条路径得到了不同的响应。"}
:::

## 总结

现在，你可以分辨部署后的每项检查分别验证了什么。

1. 确认主程序正在运行。
2. 请求报告预期版本的端点。
3. 单独验证用户实际使用的访问路径。
