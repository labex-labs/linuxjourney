---
lesson_id: "docker-ps-command"
course_id: "docker"
lang: "zh"
order_index: 4
title: "docker ps"
description: "学习如何列出 Docker 容器，并区分正在运行和已经退出的容器。"
meta_title: "docker ps - Docker"
meta_description: "读懂 docker ps 的输出，用 docker ps -a 找出已停止的容器，并理解容器名称和退出码。"
meta_keywords: "docker ps, 列出 Docker 容器, 已停止的容器, docker ps -a, 容器状态, 退出码"
---

你在 Docker 中启动的 Web 服务器还在运行吗？用 `docker ps` 查一查。Docker 镜像打包了程序和所需文件，容器则是根据镜像创建的实例。这条命令显示执行时的容器列表。

## 列出正在运行的容器

默认情况下，`docker ps` 只列出正在运行的容器。下面的示例取自准备好的 Docker 环境，只保留了几列。不用搭建环境也能跟着读。如果在终端练习，请输入 `$` 提示符后面的命令。

```text
$ docker ps
IMAGE         STATUS         NAMES
nginx:alpine  Up 4 minutes   web
nginx:alpine  Up 30 seconds  demo
```

如果 Docker 只显示列标题，说明运行中的容器列表为空。这个环境里仍可能有已经停止的容器。

:::single-choice{#docker-ps-running-list} 执行 `docker ps` 后，Docker 只显示列标题。从中能得出什么结论？

::option[没有可供运行容器的镜像。]{#docker-ps-running-list-images explanation="这条命令列出的是容器。没有运行中的容器时，镜像仍可能存在。"}
::option[列表中没有正在运行的容器。]{#docker-ps-running-list-empty .correct explanation="默认列表只显示运行中的容器。已经停止的容器可能仍然存在。"}
::option[没有已停止的容器可供检查。]{#docker-ps-running-list-stopped explanation="默认列表不包含已停止的容器。空列表无法说明这些容器是否存在。"}
:::

## 查看名称和状态

先看 `NAMES` 列，找到要检查的容器。两行的 `IMAGE` 列显示同一个镜像 `nginx:alpine`。在最右侧找到 `web`，再读同一行的 `STATUS`。`Up 4 minutes` 表示这个容器已经运行了大约四分钟。

:::single-choice{#docker-ps-name-column} 哪一行的容器已经运行了大约 30 秒？

::option[名称为 `demo` 的那一行。]{#docker-ps-name-demo .correct explanation="在 STATUS 列找到 Up 30 seconds，再看同一行的 NAMES，显示的是 demo。"}
::option[名称为 `web` 的那一行。]{#docker-ps-name-web explanation="web 那一行显示 Up 4 minutes。两个容器用了同一个镜像，但启动时间不同。"}
::option[镜像为 `nginx:alpine` 的两行。]{#docker-ps-name-image-reference explanation="每个容器都有自己的状态。使用同一个镜像不代表启动时间相同。"}
:::

## 一并查看已退出的容器

如果没看到想找的容器，可以试试 `docker ps -a`。`-a` 是 `--all` 的简写，会把已经停止但仍存在的容器也列出来。这个例子还加入了一个预先准备好的任务 `preview`。

```text
$ docker ps -a
IMAGE         STATUS                         NAMES
nginx:alpine  Up 4 minutes                   web
nginx:alpine  Up 30 seconds                  demo
busybox:1.36  Exited (0) 2 minutes ago       report
busybox:1.36  Exited (1) About a minute ago  preview
```

容器运行一个主程序，例如 Web 服务器或脚本。`Exited` 表示这个程序已经停止。括号里的数字是**退出码**，即程序停止时给出的结果。0 通常表示成功，非零退出码通常表示发生了错误。任务 `report` 显示 `Exited (0)`，符合任务成功结束的正常表现。

![LabEx 终端列出运行中和已退出的容器，report 的退出码为 0，preview 的退出码为 1](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-ps-command/running-and-exited.png)

LabEx 截图只展示了四个示例容器的名称和状态。运行时长会随查看时间而变化。

:::single-choice{#docker-ps-exit-code-reading} 仅根据退出码，你会先检查哪一行是否出错？

::option[`report`，因为它已经退出。]{#docker-ps-exit-code-report explanation="短任务执行完毕后也会退出。退出码 0 通常表示任务成功。"}
::option[`demo`，因为它是运行中的容器里启动最晚的一个。]{#docker-ps-exit-code-demo explanation="Up 显示的是程序已经运行了多久。这一行没有退出码。"}
::option[`preview`，因为它的退出码是 1。]{#docker-ps-exit-code-preview .correct explanation="preview 显示 Exited (1)，值得进一步检查。单凭状态还无法判断原因。"}
:::

## 选择下一步检查

退出码可以帮助你决定下一步查什么。要看 `preview` 有没有报错，在 `docker logs` 后加上容器名称。这会显示 Docker 收集到的容器输出。

```bash
$ docker logs preview
```

对于正在运行的 Web 服务器，也可以检查访问者能不能打开网页。要确认这一点，请在需要访问服务的那台电脑上打开网页。`Up` 描述的是容器内程序的状态。在浏览器中成功打开网页，则表明从测试的电脑可以访问它。

:::single-choice{#docker-ps-check-visitor-access} 在运行 Docker 的电脑上能打开网页。同事需要从另一台电脑访问。怎样才能确认对方可以访问？

::option[在同事的电脑上打开网页。]{#docker-ps-next-check-visitor-browser .correct explanation="从同事的电脑发出请求，就能验证对方实际使用的连接。"}
::option[在运行 Docker 的电脑上再执行一次 `docker ps`。]{#docker-ps-next-check-status-again explanation="列表能确认 web 是否仍在运行，但能不能从同事的电脑访问，需要从那里用浏览器测试。"}
::option[在运行 Docker 的电脑上再打开一次网页。]{#docker-ps-next-check-host-browser explanation="这只是从原来的电脑重复测试。同事的连接结果可能不同。"}
:::

## 总结

现在，你可以用容器列表找到目标容器、读懂状态，并判断下一步该检查什么。

1. 用 `docker ps` 列出正在运行的容器。
2. 按名称找到容器并查看它的状态。
3. 用 `docker ps -a` 查看包括已退出容器在内的列表。
4. 通过日志或浏览器请求，检查容器状态无法说明的问题。
