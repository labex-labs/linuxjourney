---
lesson_id: "compose-files"
course_id: "docker-compose"
lang: "zh"
order_index: 1
title: "Compose 文件"
description: "学习从 Compose 文件中找出服务、镜像、命令和端口。"
meta_title: "Compose 文件 - Docker Compose"
meta_description: "读懂 Compose 文件的基本结构，了解服务、镜像、命令和端口各自怎么写。"
meta_keywords: "Compose 文件, Docker Compose, 服务配置, DevOps, Linux Journey"
---

用两条命令分别启动 Web 服务器和辅助工具，做一次并不难。**Compose 文件**可以把设置集中起来，让你以后启动同样的一组服务。本课程假定练习环境已经装好 Docker 和 Compose 插件，由插件提供 `docker compose` 命令。

## 定义两个服务

新建名为 `journey-compose` 的练习目录，把下面的内容存为 `compose.yaml`。**服务**描述 Compose 应怎样运行容器。这个文件定义了 Web 服务器和一个小型工具容器，后者会保持运行，方便稍后检查。

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8080:80"
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
```

使用空格缩进。`web` 下方缩进的键都属于这个服务。`ports` 下的短横线表示列表中的一项。`command` 后的方括号也表示列表，这里包含程序名及其参数。

:::single-choice{#compose-files-service-images} 哪个服务使用 BusyBox 镜像？

::option[web 服务。]{#compose-files-service-images-a explanation="web 有自己的 image 配置，指定的是 nginx。"}
::option[toolbox 服务。]{#compose-files-service-images-c .correct explanation="它的 image 字段指定了 busybox:1.36。"}
::option[两个服务都是。]{#compose-files-service-images-b explanation="两个服务分别有各自的 image 配置。"}
:::

## 读懂 Web 服务配置

Web 服务把主机的 8080 端口映射到容器的 80 端口。服务启动后，在运行 Docker 的机器上请求 `http://127.0.0.1:8080` 即可访问 Nginx。工具容器没有发布端口，它的 `sleep` 命令让它在练习期间持续运行 3,600 秒。

:::single-choice{#compose-files-mapping-owner} 配置中的哪一项决定 Docker 主机上的浏览器如何访问 Nginx？

::option[web 下方的 ports 设置。]{#compose-files-mapping-owner-a .correct explanation="这一项把主机的地址和端口映射到 Web 容器。"}
::option[toolbox 下方的镜像标签。]{#compose-files-mapping-owner-b explanation="这项设置决定工具容器用哪个镜像。"}
::option[toolbox 下方的 sleep 参数。]{#compose-files-mapping-owner-c explanation="这个参数决定该程序运行多久。"}
:::

## 查看解析后的配置

在包含文件的目录下运行这条命令。只输入 `$` 提示符后面的内容。Compose 会读取 `compose.yaml`，打印它解析出的配置。找一找 `web` 和 `toolbox` 两项。显示时，Compose 可能会把简写配置展开成完整形式。

```bash
$ docker compose config
```

:::single-choice{#compose-files-config-scope} 这条命令成功列出了两个服务。你验证了什么？

::option[两个容器都已启动。]{#compose-files-config-scope-a explanation="这条配置命令只读取并显示设置。"}
::option[浏览器已收到成功响应。]{#compose-files-config-scope-c explanation="服务启动之后，才能用请求测试。"}
::option[Compose 能读懂这两个服务定义。]{#compose-files-config-scope-b .correct explanation="启动前就可以查看解析后的配置。"}
:::

## 总结

现在，你可以识别一份简单 Compose 文件中的各个部分。

1. 读出 services 下的服务名称和镜像引用。
2. 理解服务配置如何决定容器的运行方式。
3. 用 docker compose config 查看解析后的配置。
