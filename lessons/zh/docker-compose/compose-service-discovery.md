---
lesson_id: "compose-service-discovery"
course_id: "docker-compose"
lang: "zh"
order_index: 3
title: "服务发现"
description: "了解 Compose 服务如何按名称互相访问，以及主机如何通过发布的端口访问服务。"
meta_title: "服务发现 - Docker Compose"
meta_description: "区分 Compose 网络内的服务地址和主机上的访问地址，了解为什么替换容器后仍可使用同一服务名。"
meta_keywords: "服务发现, Compose 网络, 主机端口, 容器端口, DevOps, Linux Journey"
---

Docker 主机上的浏览器会通过发布的地址访问 Web 服务。同一项目中的另一个容器则走不同的路径。Compose 通常让同一项目的服务共享网络，各服务可在这个网络里按名称查找彼此。

## 在工具容器内请求网页

回到包含 `compose.yaml` 的练习目录。如果工具容器在上一课之后已退出，可以用 `docker compose start toolbox` 重新启动它。两个服务都在运行后，用 `docker compose exec` 在现有的 toolbox 服务中运行命令。BusyBox 中的 `wget` 可以请求网页。`-q` 隐藏进度消息，`-O -` 把网页输出到终端。

```bash
$ docker compose exec -T toolbox wget -q -O - http://web:80/
```

`-T` 表示不分配交互式终端。URL 使用 Web 服务的名称和容器端口。请求成功会返回 Nginx 页面对应的 HTML。

:::single-choice{#compose-service-discovery-sibling-url} 位于同一 Compose 网络中的另一个服务，应该通过哪个地址访问 Web 容器？

::option[http://web:80/]{#compose-service-discovery-sibling-url-c .correct explanation="共享网络把 web 解析到目标服务，80 端口对应服务监听的位置。"}
::option[http://127.0.0.1:8080/]{#compose-service-discovery-sibling-url-a explanation="从该服务内部使用回环地址，会指向它自己的网络环境。"}
::option[http://web:8080/]{#compose-service-discovery-sibling-url-b explanation="在这个示例中，Web 程序在网络内部监听的是 80 端口。"}
:::

![在工具容器中用服务名请求 Web 服务后返回的 HTML](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-discovery/internal-request.png)

## 从主机访问时选择哪个地址

如果保留了原来的映射，就在 Docker 主机上打开 `http://127.0.0.1:8080/`。如果上一课改了主机端口，把浏览器地址换成那个端口。工具容器仍然使用 `http://web:80/`，因为它在 Compose 网络内部连接，可以使用服务名 `web`。

:::single-choice{#compose-service-discovery-host-url} 假设把映射的主机端口改成了 8081，示例中的哪个地址也需要改？

::option[工具容器使用 web 和 80 端口的 URL。]{#compose-service-discovery-host-url-b explanation="这条连接仍然直接访问容器所监听的端口。"}
::option[两个地址都改。]{#compose-service-discovery-host-url-c explanation="变化的只有主机一侧的端口。"}
::option[主机上浏览器使用的地址。]{#compose-service-discovery-host-url-a .correct explanation="浏览器要通过新发布的主机端口连接。"}
:::

## 使用稳定的服务名称

替换容器时，容器的网络地址可能变化，但 Compose 服务名保持不变。客户端可以重新解析该名称并重连。原先连到被替换容器的连接可能会断开。

:::single-choice{#compose-service-discovery-replacement} Web 容器已重新创建，地址变了。工具容器下次请求可以使用什么？

::option[从旧容器复制的地址。]{#compose-service-discovery-replacement-a explanation="新实例可能会得到不同的网络地址。"}
::option[原来的 web 服务名和容器端口。]{#compose-service-discovery-replacement-b .correct explanation="在项目网络内，该名称可以解析到现在的容器。"}
::option[工具容器自己的名称。]{#compose-service-discovery-replacement-c explanation="那个名称指向运行命令的工具容器。"}
:::

## 总结

现在，你可以根据请求的发起位置，选择正确的服务地址。

1. 在项目网络内用服务名和容器端口访问。
2. 在主机上通过发布的地址用浏览器访问。
3. 替换容器后重新解析服务名。
