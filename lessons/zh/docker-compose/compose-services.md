---
lesson_id: "compose-services"
course_id: "docker-compose"
lang: "zh"
order_index: 2
title: "Compose 服务"
description: "学习如何启动 Compose 服务并查看相应的容器状态。"
meta_title: "Compose 服务 - Docker Compose"
meta_description: "用 Compose 启动多个服务，查看容器状态，并确认服务是否仍在运行。"
meta_keywords: "Compose 服务, Docker Compose, 容器状态, DevOps, Linux Journey"
---

继续使用上一课中包含 `web` 和 `toolbox` 的 `compose.yaml`。两个服务属于同一个 Compose **项目**，也就是用这份配置一起管理的一组资源。请在练习目录中执行命令。

## 启动项目

如果 8080 端口已被占用，请在 `compose.yaml` 中改用空闲的主机端口。例如，Docker 课程中的 `published-web` 容器只要还在运行，就会占用 8080。你可以保留这个容器，并在 8081 空闲时将 Compose 的映射改为 `127.0.0.1:8081:80`。容器一侧仍使用 80，之后从浏览器访问时，则使用你选定的主机端口。

用 `docker compose up -d` 在后台启动服务。Compose 会创建项目所需的资源，并根据服务设置创建或更新容器。

```bash
$ docker compose up -d
```

:::single-choice{#compose-services-project-start} 你在练习目录里执行 up -d。什么设置决定要启动哪些服务？

::option[Docker 主机上已有的所有镜像。]{#compose-services-project-start-a explanation="主机也可能存放与此项目无关的镜像。"}
::option[刚好处于停止状态的所有容器。]{#compose-services-project-start-c explanation="Compose 会处理指定要启动的项目。"}
::option[选定的 Compose 文件中的服务。]{#compose-services-project-start-b .correct explanation="本例中，Compose 使用的是 web 和 toolbox 的定义。"}
:::

## 读取服务列表

用 `docker compose ps` 查看这个项目。服务一列使用 YAML 文件中定义的名称。Docker 还为每个容器分配了名称，其中可能带有项目名称。

```bash
$ docker compose ps
```

找出 `web` 和 `toolbox` 并查看其状态。容器显示在运行，只能说明检查时程序还在运行。要验证 Web 服务是否返回网页，还要从浏览器发出请求。

:::single-choice{#compose-services-compose-list} Compose 显示 web 正在运行。怎样直接确认它返回了预期的网页？

::option[统计 config 输出中的服务数。]{#compose-services-compose-list-b explanation="配置中有多少服务，与 Web 服务的响应无关。"}
::option[访问已发布的 Web 地址。]{#compose-services-compose-list-a .correct explanation="实际发出请求，就能验证页面是否正常返回。"}
::option[查看另一个容器的名字。]{#compose-services-compose-list-c explanation="容器名能指明一个实例，无法测试服务。"}
:::

![Compose 状态列表显示 web 和 toolbox 正在运行，主机使用 8080 端口](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-services/project-status.png)

截图使用的是原来的主机端口 8080。如果你换了端口，就在映射的主机一侧查找你选的数字。

## 查看已停止的服务

这个工具容器只会临时运行。如果 sleep 结束或你手动停止了它，可加上 `-a`，把已停止的容器也列出来。示例中的命令会停止练习项目的工具容器，让 Web 服务继续运行。要接着做后面的练习，请再次启动工具容器。

```bash
$ docker compose stop toolbox
$ docker compose ps -a
$ docker compose start toolbox
```

:::single-choice{#compose-services-stopped-service} 停止工具容器后，应该到哪里查找它？

::option[本项目的 docker compose ps -a 输出。]{#compose-services-stopped-service-c .correct explanation="all 选项会显示项目中已经停止的容器。"}
::option[只能在镜像列表中找。]{#compose-services-stopped-service-a explanation="停止容器中的程序后，容器仍然存在，可以继续查看它。"}
::option[在另一个项目的容器列表里找。]{#compose-services-stopped-service-b explanation="工具容器属于当前项目。"}
:::

想进一步练习容器和 Compose，可以参考 [Docker 命令实验](https://labex.io/courses/docker-command-labs)。

## 总结

现在，你可以用一份 Compose 文件启动并检查一组服务。

1. 启动选定项目中的服务。
2. 找出服务名称和当前状态。
3. 排查项目时一并查看已停止的服务。
