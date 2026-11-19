---
lesson_id: "docker-containers"
course_id: "docker"
lang: "zh"
order_index: 1
title: "容器"
description: "了解 Docker 容器里运行着什么，以及容器与运行 Docker 的机器有什么关系。"
meta_title: "容器 - Docker"
meta_description: "通过一个小型 Web 服务器认识容器，了解主程序启动或停止后会发生什么。"
meta_keywords: "Docker 容器, 容器基础, Docker 主机, 容器进程, Web 服务器"
---

浏览器打开了由 Docker 中的 Web 服务器提供的网页。服务器在哪里运行？它停下来后，网页还能打开吗？先看看是谁在响应浏览器。

## 容器里运行的程序

**Web 服务器**是接收网页请求并作出响应的程序。假设你的浏览器和名为 `web` 的小型 Web 服务器都在同一台机器上。Docker 把服务器放在**容器**中运行，让程序看到一套独立的文件和其他资源。课程准备好了示例，可以直接跟着读，无需安装 Docker。

:::single-choice{#docker-containers-page-request} 浏览器请求网页时，谁负责返回网页内容？

::option[容器中运行的 Web 服务器。]{#docker-containers-page-server .correct explanation="服务器程序接收请求，再把网页发回浏览器。"}
::option[描述如何启动容器的文件。]{#docker-containers-page-files explanation="这些文件用来定义运行环境。实际响应请求的是正在运行的程序。"}
::option[Docker 中的容器列表。]{#docker-containers-page-list explanation="容器列表能告诉你 Docker 在运行什么，网页由服务器提供。"}
:::

## 容器与主机

运行容器的机器称为**主机**。当 Docker 在 Linux 上运行 Linux 容器时，容器里的程序就是该 Linux 主机上的进程。**进程**是正在运行的程序。多个容器可以共用一台主机，每个容器只能看到一部分资源。使用 Docker Desktop 时，Linux 容器运行在 Docker 管理的 Linux 虚拟机中。

:::single-choice{#docker-containers-shared-host} 两个 Linux 容器运行在同一台 Linux 主机上。由此可以得出什么结论？

::option[两个容器中的程序必定看到相同的文件。]{#docker-containers-host-shared-files explanation="即使共用一台主机，每个容器也可以看到不同的文件。"}
::option[两个容器中的程序可以作为独立的进程在主机上运行。]{#docker-containers-host-separate-processes .correct explanation="同一台主机可以运行多个彼此独立的容器进程。"}
::option[每个容器都必须启动一台单独的 Linux 机器。]{#docker-containers-host-separate-machines explanation="多个 Linux 容器可以在同一台主机上运行，无需为每个容器启动一台机器。"}
:::

## 从镜像创建容器

Docker 根据**镜像**创建容器。镜像打包了程序和它需要的文件。你可以用同一个 Web 服务器镜像创建 `web` 和 `demo`。启动后，两个容器各自运行同一个服务器程序的一个进程，可以分别停止。

:::single-choice{#docker-containers-two-from-image} web 仍在运行时，你停止了 demo。web 会怎样？

::option[暂停，直到 demo 再次启动。]{#docker-containers-two-paused explanation="两个容器各自运行自己的程序。在这个例子中，停止 demo 不会暂停 web。"}
::option[需要根据镜像重新创建。]{#docker-containers-two-recreate explanation="web 容器是单独创建的，可以继续运行。"}
::option[仍在自己的容器中运行。]{#docker-containers-two-independent .correct explanation="两个容器以同一镜像为起点，运行时彼此独立。"}
:::

## 比较服务停止前后的响应

假设浏览器已经能向 `web` 发送请求。停止容器前，浏览器可以收到网页。停止之后，再发一次请求就收不到这个服务器返回的网页了。镜像仍可用来创建其他容器。要让服务器提供网页，程序必须在运行，浏览器也必须能访问它。后面的课会介绍如何让浏览器连到容器。

:::single-choice{#docker-containers-stopped-server} 镜像还在，但 web 已停止。要让 web 恢复响应，需要做什么？

::option[重新运行容器里的服务器程序。]{#docker-containers-stopped-program .correct explanation="镜像提供程序所需的文件，新的请求要由正在运行的服务器处理。"}
::option[给镜像换一个名字。]{#docker-containers-stopped-rename explanation="重命名镜像不会启动已经停止的服务器。"}
::option[给浏览器再提供一份服务器镜像。]{#docker-containers-stopped-browser-image explanation="浏览器只负责发送请求，服务器程序在容器里运行。"}
:::

![LabEx 终端显示容器停止前收到 HTTP 200，停止后连接失败](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-containers/server-response.png)

在这个 LabEx 示例中，名为 `page-demo` 的容器提供网页。第一次用 `curl` 请求时，服务器返回 HTTP 200。容器停止后，再次请求失败。由于没有收到 HTTP 响应，curl 显示 `000`。

## 总结

现在，你可以解释容器如何在主机上运行程序。

1. 找出负责响应浏览器请求的程序。
2. 解释多个容器如何共用一台主机。
3. 说明如何用同一个镜像创建多个容器。
4. 重新发送请求，检查原先能访问的服务器是否仍有响应。
