---
lesson_id: "docker-port-mapping"
course_id: "docker"
lang: "zh"
order_index: 5
title: "端口映射"
description: "学习如何发布容器端口，并找出本机浏览器应该访问的地址。"
meta_title: "端口映射 - Docker"
meta_description: "读懂 Docker 端口映射，区分主机端口和容器端口，排查访问地址中的端口错误。"
meta_keywords: "Docker 端口映射, 发布端口, docker run -p, 主机端口, 容器端口"
---

Web 服务器可以在容器里正常运行，但浏览器还需要有办法访问它。**端口**是一个数字，帮助机器把收到的网络请求交给相应的服务。Docker 可以发布主机端口，再把收到的请求转发到容器中的端口。

## 读懂端口映射

示例中的 Nginx 服务器在容器内的 80 端口接收 Web 请求。前面创建的 `web` 容器没有发布端口。这里另建一个容器，给它取一个新名字，并在创建时用 `-p` 设置映射。

```bash
$ docker run -d --name published-web -p 127.0.0.1:8080:80 nginx:alpine
```

`8080:80` 表示从**主机端口** 8080 转发到**容器端口** 80。浏览器连接主机端口，服务器在容器端口接收请求。`127.0.0.1` 将映射绑定到主机的回环地址，也就是机器访问自己的地址。

请在私有练习环境中操作。Docker Engine 早于 28.0.0 的版本中，同一局域网网段上的其他机器也可能访问发布到 localhost 的端口。 [Docker 端口发布文档](https://docs.docker.com/engine/network/port-publishing/)

:::single-choice{#docker-port-mapping-request-target} 在 `127.0.0.1:9090:80` 这个映射中，Docker 主机上的浏览器应连接哪个端口？

::option[主机的 9090 端口。]{#docker-port-mapping-target-outer .correct explanation="中间的数字是浏览器连接的主机端口。"}
::option[主机的 80 端口。]{#docker-port-mapping-target-inner explanation="80 是容器内的目标端口。"}
::option[容器中的 9090 端口。]{#docker-port-mapping-target-wrong-side explanation="这个例子中，服务器在容器内的 80 端口接收请求。"}
:::

## 从主机测试

在 Docker 发布端口的那台机器上，用浏览器打开 `http://127.0.0.1:8080`。如果 Docker 运行在远程机器上，在笔记本电脑里输入 `127.0.0.1`，访问的仍是笔记本电脑自身。如果用的是浏览器实验环境，请按实验环境提供的方式访问。

:::single-choice{#docker-port-mapping-local-browser} Docker 在另一台实验机器上发布了 8080 端口。在笔记本电脑的浏览器中输入 `127.0.0.1`，实际访问的是哪里？

::option[那台独立的实验机器。]{#docker-port-mapping-local-lab explanation="只有在实验机器上使用该地址时，它才指向实验机器自身。"}
::option[Docker 中的 Web 容器。]{#docker-port-mapping-local-container explanation="浏览器使用的是自身所在机器的地址。要把请求转发给容器，需要端口映射。"}
::option[你的笔记本电脑。]{#docker-port-mapping-local-laptop .correct explanation="回环地址指向浏览器运行的那台机器。"}
:::

## 检查 Docker 发布的端口

`docker ps` 的 `PORTS` 列可以显示映射。箭头从主机地址和端口指向容器端口。`/tcp` 后缀表示映射使用的网络协议。

```text
$ docker ps
STATUS         PORTS                   NAMES
Up 2 minutes   127.0.0.1:8080->80/tcp   published-web
```

有的行仅显示 `80/tcp`。没有主机地址和箭头，就看不到已发布的主机端口。

![LabEx 终端显示主机的 8080 端口转发到容器的 80 端口，并收到 HTTP 200 响应](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-port-mapping/loopback-mapping.png)

截图中的列表只显示了 `published-web`。随后在 Docker 主机上用 `curl` 请求发布的地址，验证了它能成功响应。

:::single-choice{#docker-port-mapping-read-listing} 某行只显示 `80/tcp`，没有箭头。这一项说明了什么？

::option[Docker 发布了主机的 80 端口。]{#docker-port-mapping-listing-host explanation="已发布的映射会标出主机端口，并用箭头指向容器端口。"}
::option[这里只显示容器端口，没有显示发布到主机的端口。]{#docker-port-mapping-listing-container .correct explanation="这一项只列出了容器内的 80 端口，没有主机地址或转发箭头。"}
::option[Docker 发布了主机的 8080 端口。]{#docker-port-mapping-listing-default explanation="这一项没有主机端口，Docker 不会据此推断要用 8080。"}
:::

## 选择要测试的地址

如果网页打不开，先把输入的地址与映射箭头左侧的地址和端口对照一下。`Up` 状态和箭头告诉你 Docker 在运行什么、转发到哪里。用浏览器发出请求，才能确认服务器实际有没有返回网页。

:::single-choice{#docker-port-mapping-correct-misdirected} 在 Docker 主机上访问 8080 端口，网页没有打开。列表显示的是 `127.0.0.1:8081->80/tcp`。接下来该试什么？

::option[打开 `http://127.0.0.1:80`。]{#docker-port-mapping-misdirected-80 explanation="80 是映射中容器一侧的端口。"}
::option[打开 `http://127.0.0.1:8081`。]{#docker-port-mapping-misdirected-8081 .correct explanation="使用箭头左边发布到主机的端口。"}
::option[重试 `http://127.0.0.1:8080`。]{#docker-port-mapping-misdirected-8080 explanation="列表显示的主机端口是 8081。重试 8080 无法检查这条映射。"}
:::

## 总结

现在，你可以根据端口映射，为浏览器选对访问地址。

1. 区分主机端口和容器端口。
2. 解释 `127.0.0.1` 指向哪里。
3. 在容器列表中识别已发布的端口映射。
4. 通过发布的主机端口测试服务。
