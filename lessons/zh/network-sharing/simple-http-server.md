---
lesson_id: "simple-http-server"
course_id: "network-sharing"
lang: "zh"
order_index: 3
title: "简单 HTTP 服务器"
description: "学习如何使用 Python HTTP 服务器临时公开一个受控目录。"
meta_title: "简单 HTTP 服务器 - 网络共享"
meta_description: "学习如何使用 Python 的 http.server 模块在 Linux 中快速设置简单 HTTP 服务器，轻松地通过网络共享文件。"
meta_keywords: "Linux 简单 HTTP 服务器, 简单 Linux Web 服务器, Python http.server, Python SimpleHTTPServer, 文件共享, 网络服务器"
---

Python 的 `http.server` 模块可以为短期测试或可信传输提供静态文件。它不是生产 Web 服务器，也不提供身份验证、授权、TLS、速率限制或针对恶意流量的强化处理。

## 准备共享目录

创建只包含打算公开文件的专用目录。启动前应检查隐藏文件、符号链接、权限和敏感元数据。不要共享主目录、仓库根目录、凭据目录或系统路径。

使用 `--directory` 明确共享根目录：

```bash
$ python3 -m http.server 8000 --directory /srv/temporary-share
```

没有索引文件时，该模块通常会生成目录列表。任何能够访问监听器的人都可能枚举并下载所提供的内容。

:::single-choice{#http-server-directory-option}
为什么使用 `--directory /srv/temporary-share`？

::option[它会自动加密每个 HTTP 响应。]{#http-server-directory-tls explanation="directory 选项不会添加 TLS。"}
::option[它会为每个下载者创建账户。]{#http-server-directory-accounts explanation="基础模块不提供用户身份验证。"}
::option[它明确指定预期文档根目录。]{#http-server-explicit-root .correct explanation="明确且经过审查的根目录可以降低意外公开工作目录中文件的风险。"}
:::

## 控制监听地址

只有同一主机需要连接时，应绑定到环回地址：

```bash
$ python3 -m http.server 8000 --bind 127.0.0.1 --directory /srv/temporary-share
```

要在可信网络上共享，应有意绑定到适当接口地址，并确认防火墙策略。不使用限制性绑定运行时通常会监听所有可用接口，可能将目录公开到预期网络之外。

:::single-choice{#http-server-loopback-bind}
谁通常可以访问绑定到 `127.0.0.1` 的服务器？

::option[同一主机上的客户端。]{#http-server-local-clients .correct explanation="环回绑定适合本地测试，或在有意配置的隧道后使用。"}
::option[公网中的任何主机。]{#http-server-public explanation="环回地址只属于同一网络命名空间，不是公网接口。"}
::option[只有通过蓝牙连接的设备。]{#http-server-bluetooth explanation="该地址与蓝牙传输无关。"}
:::

## 测试访问

在服务主机上请求一个已知文件，并检查响应：

```bash
$ curl -f http://127.0.0.1:8000/example.txt
```

进行经过授权的远程测试时，应使用所选接口地址而不是环回地址。既要确认预期文件可访问，也要确认文档根目录以外的文件不可访问。浏览器成功本身不能证明公开范围或机密性合适。

:::single-choice{#http-server-default-port-command}
`python3 -m http.server 8000` 明确选择了哪个端口？

::option[22]{#http-server-port-22 explanation="端口 22 通常与 SSH 关联，此处没有选择它。"}
::option[8000]{#http-server-port-8000 .correct explanation="位置端口操作数告诉模块在哪里监听。"}
::option[443]{#http-server-port-443 explanation="该命令没有在端口 443 配置 HTTPS。"}
:::

## 停止并清理

在受监督的终端中运行临时服务，传输完成后使用 `Ctrl-C` 停止。确认监听器已经消失：

```bash
$ ss -ltn 'sport = :8000'
```

按照数据处理策略移除临时副本，并撤销所有临时防火墙规则。对于持久、需要身份验证或面向互联网的分发，应使用配置了访问控制和 TLS、持续维护的服务器。

:::single-choice{#http-server-completion-check}
临时传输完成后应该做什么？

::option[停止服务并确认端口不再监听。]{#http-server-stop-verify .correct explanation="验证可以确认临时网络服务确实已经结束。"}
::option[保留监听器运行，以防以后有人需要。]{#http-server-leave-running explanation="授权用途结束后应移除不必要的暴露。"}
::option[将更多私有文件复制到文档根目录。]{#http-server-add-private explanation="只有有意共享的内容才应放入服务目录。"}
:::

## 总结

现在，你可以在暴露范围有限的情况下运行临时 Python HTTP 服务器。

1. 只提供专用且经过审查的目录。
2. 绑定到范围最窄的适当地址。
3. 测试预期访问和非预期边界。
4. 之后停止监听器并清理临时访问。
