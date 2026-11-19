---
lesson_id: "docker-run-command"
course_id: "docker"
lang: "zh"
order_index: 3
title: "docker run"
description: "学习如何用 docker run 从镜像创建并启动容器。"
meta_title: "docker run - Docker"
meta_description: "读懂 docker run 命令，给容器命名，并区分在前台执行的短任务与在后台运行的服务器。"
meta_keywords: "docker run, 运行 Docker 容器, 容器名称, 前台运行, 后台运行"
---

你已经有了一个 Web 服务器镜像。要启动服务器，可以用 `docker run` 从镜像创建并启动容器。先运行一个很快就会结束的命令，看看什么时候能继续在终端里输入命令。

## 运行短任务

BusyBox 是一个小型镜像，提供基本的 Linux 命令。下面的例子用 `echo` 输出一条消息。先写镜像引用，再写要在容器里运行的命令。如果本地没有镜像，Docker 通常会先下载。`$` 表示终端提示符。Docker 需要先拉取镜像时，终端可能会先显示下载信息。

```text
$ docker run busybox:1.36 echo Hello
Hello
```

命令的输出会出现在终端中。`echo` 执行完毕后，容器停止，终端重新显示提示符。

:::single-choice{#docker-run-command-short-task} 这个例子中，容器里运行的是什么？

::option[作为 shell 命令运行的 `busybox:1.36`。]{#docker-run-command-short-image explanation="BusyBox 是提供工具的镜像。镜像引用后面才是要运行的命令。"}
::option[借助镜像中的工具执行的 `echo Hello`。]{#docker-run-command-short-echo .correct explanation="镜像引用后面的内容让容器运行 echo，并指定要输出的文本。"}
::option[容器内部再次执行的 `docker run`。]{#docker-run-command-short-docker explanation="docker run 在你的终端中执行，负责启动容器里的命令。"}
:::

## 给容器命名

在镜像引用之前加上 `--name`，可以给容器起一个容易辨认的名字。这条命令把执行短任务的容器命名为 `report`。

```bash
$ docker run --name report busybox:1.36 echo Ready
```

容器即使已经停止，仍会保留自己的名称。在同一个 Docker 环境里创建另一个容器时，需要使用尚未被占用的名称。

:::single-choice{#docker-run-command-name-choice} report 已经执行完毕，但容器仍然存在。你想用同一个镜像再创建一个容器，可以改什么？

::option[保留镜像引用，给新容器换一个名字。]{#docker-run-command-name-new .correct explanation="使用尚未被占用的名称，Docker 就能从同一镜像创建另一个容器。"}
::option[改镜像标签，保留原来的容器名称。]{#docker-run-command-name-change-tag explanation="换成另一个镜像也不会释放原容器占用的名称。"}
::option[改要输出的消息，保留原来的容器名称。]{#docker-run-command-name-change-message explanation="消息只是 echo 的输入，不会释放 report 这个名字。"}
:::

## 在后台启动服务器

镜像可以指定启动容器时默认执行的命令。使用 `nginx:alpine` 且未指定命令时，容器会启动 Web 服务器。加上 `-d` 可以用**分离模式**运行容器。服务器在后台继续运行，你则可以在终端里接着输入命令。

```bash
$ docker run -d --name web nginx:alpine
```

Docker 会打印容器 ID，也就是刚启动的容器的一串标识符。下一课会检查服务器是否还在运行。

![LabEx 终端显示 Docker 短任务输出的 Hello 和 Ready，以及后台服务器的容器 ID](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-run-command/foreground-and-detached.png)

短任务直接在终端输出消息。在后台启动服务器时，终端显示的是容器 ID。

:::single-choice{#docker-run-command-detach-meaning} Docker 打印出 ID，终端重新显示提示符。分离模式让你可以做什么？

::option[等服务器停止后再使用终端。]{#docker-run-command-detach-wait explanation="服务器继续运行时，分离模式就会把终端交还给你。"}
::option[跳过启动服务器，只准备好镜像。]{#docker-run-command-detach-skip explanation="分离模式下 Docker 仍会启动容器。"}
::option[在服务器运行期间继续使用终端。]{#docker-run-command-detach-continue .correct explanation="启动容器后，分离模式会把控制权交还给终端。"}
:::

## 判断是否创建了新容器

每次成功执行 `docker run` 都会创建一个新容器。再次使用同一个服务器镜像，并指定尚未被占用的名字，Docker 就会创建第二个容器。第一个容器的名称和状态不变。

:::single-choice{#docker-run-command-second-instance} web 仍在运行。如果 demo 这个名字尚未被占用，`docker run -d --name demo nginx:alpine` 会做什么？

::option[把正在运行的 web 容器改名为 demo。]{#docker-run-command-second-rename explanation="docker run 会创建新容器。原来的 web 容器仍使用原名。"}
::option[给镜像添加一个名为 demo 的标签。]{#docker-run-command-second-tag explanation="该选项是给容器命名，镜像引用仍是 nginx:alpine。"}
::option[另外启动一个名为 demo 的容器。]{#docker-run-command-second-new .correct explanation="Docker 会用这个镜像创建一个新容器，并将它命名为 demo。"}
:::

想亲手启动容器并观察输出，可以试试 [你的第一个 Docker 实验](https://labex.io/labs/docker-your-first-docker-lab-92719)。

## 总结

现在，你可以读懂 docker run 命令，并判断 Docker 会创建什么。

1. 识别镜像引用以及容器内可选的运行命令。
2. 用 `--name` 为容器命名，方便之后查找。
3. 描述短任务执行完毕后会发生什么。
4. 用 `-d` 让服务器在后台运行，同时继续使用终端。
