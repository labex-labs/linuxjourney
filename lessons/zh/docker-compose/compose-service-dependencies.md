---
lesson_id: "compose-service-dependencies"
course_id: "docker-compose"
lang: "zh"
order_index: 6
title: "服务依赖"
description: "区分依赖服务已经按顺序启动和它已经准备好响应请求。"
meta_title: "服务依赖 - Docker Compose"
meta_description: "读懂 Compose 的健康检查和依赖条件，确认服务是否已经可以响应。"
meta_keywords: "服务依赖, 健康检查, 就绪状态, Docker Compose, DevOps, Linux Journey"
---

依赖 Web 服务器的工具即使按正确的顺序启动，也可能过早发出第一条请求。**健康检查**是 Docker 运行的小型测试，用来观察服务能否完成特定操作，例如响应 HTTP 请求。

## 选择就绪检查

在这个独立示例中，检查在 Web 容器内部执行，向本地网页发出请求。请求成功说明服务器从这个位置可以正常响应，Docker 会用这一结果判断健康状态。

```yaml
services:
  web:
    image: nginx:alpine
    healthcheck:
      test: ["CMD", "wget", "-q", "-O", "/dev/null", "http://127.0.0.1/"]
      interval: 3s
      timeout: 2s
      retries: 5
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
    depends_on:
      web:
        condition: service_healthy
```

把下面的内容存为同一个练习目录下的 `compose.health.yaml`。检查会定期执行，每次都有时间限制，测试的是 Web 容器内部的本地响应。

:::single-choice{#compose-service-dependencies-check-location} 在这个健康检查中，wget 在哪儿运行？

::option[在 Web 容器里。]{#compose-service-dependencies-check-location-c .correct explanation="这里的回环 URL 是从该容器内部访问的。"}
::option[在主机上的浏览器里。]{#compose-service-dependencies-check-location-a explanation="Docker 根据 Web 服务的定义运行这条命令。"}
::option[在工具容器里。]{#compose-service-dependencies-check-location-b explanation="这个检查定义在 web 服务下。"}
:::

## 等待依赖服务达到健康状态

`service_healthy` 条件会让 Compose 等到健康检查通过后，再启动依赖它的工具容器。单有启动顺序的话，一个服务可能在它依赖的服务刚启动时就开始运行，那时第一次请求还不一定能成功。

```bash
$ docker compose -p journey-health -f compose.health.yaml up -d
$ docker compose -p journey-health -f compose.health.yaml ps
```

查看 web 是否显示健康状态，以及工具容器是否在运行。

:::single-choice{#compose-service-dependencies-ready-condition} Web 进程已启动，但容器内部的请求仍然失败。什么条件应当让工具容器再等一等？

::option[只要求按顺序启动。]{#compose-service-dependencies-ready-condition-b explanation="先启动 web，仍可能需要等一段时间它才会响应。"}
::option[选择分离模式。]{#compose-service-dependencies-ready-condition-c explanation="分离模式改变终端如何等待，不决定服务是否就绪。"}
::option[要求依赖服务处于健康状态。]{#compose-service-dependencies-ready-condition-a .correct explanation="这条依赖条件会等待健康检查的结果。"}
:::

![Compose 状态显示 Web 服务依赖已达到健康状态，工具容器正在运行](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-dependencies/healthy-dependency.png)

## 处理启动后的故障

Compose 的启动条件负责决定一开始按什么顺序启动。即使服务启动时是健康的，之后也可能停止响应。客户端要能处理请求失败，并在依赖服务恢复时重新连接。查看当前状态并直接发出请求，确认它现在如何响应。

:::single-choice{#compose-service-dependencies-later-failure} 两个服务启动一小时后，某个请求失败了。现在应该查哪些信息？

::option[只看最初的启动顺序。]{#compose-service-dependencies-later-failure-a explanation="这只能说明启动时发生了什么。"}
::option[查看当前的健康检查结果，并从依赖 Web 的服务发出请求。]{#compose-service-dependencies-later-failure-b .correct explanation="这两项观察有助于分辨服务当前的状态和客户端使用的访问路径。"}
::option[统计 Docker 缓存中的镜像数量。]{#compose-service-dependencies-later-failure-c explanation="有多少镜像，对判断运行中服务是否响应帮助不大。"}
:::

## 从两个位置检查

本地健康检查成功，说明 Web 容器从内部可以访问自己的服务。工具容器则仍需使用项目网络，并且要有一个可用的服务地址。请分别核对健康检查结果和工具容器的实际请求。

:::single-choice{#compose-service-dependencies-final-application} 健康检查显示通过，但工具容器的一个请求失败。怎样对比有助于定位问题？

::option[只查看最初的启动时间。]{#compose-service-dependencies-final-application-b explanation="启动时间无法说明现在每条路径可以访问什么。"}
::option[既然 Web 健康检查通过，就认为两个请求都成功了。]{#compose-service-dependencies-final-application-c explanation="健康检查只提供从一个位置观察到的结果。"}
::option[比较在 web 容器内部发出的请求，与从工具容器发往 web 的同一请求。]{#compose-service-dependencies-final-application-a .correct explanation="两项检查分别验证服务内部是否就绪，以及依赖它的服务实际使用的路径。"}
:::

## 总结

现在，你可以借助检查结果判断依赖服务是否就绪。

1. 辨认健康检查实际测试了什么。
2. 启动顺序不足以保证就绪时，选择基于健康状态的依赖条件。
3. 服务之后发生故障时，验证它现在的行为。
