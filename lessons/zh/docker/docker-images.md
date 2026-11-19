---
lesson_id: "docker-images"
course_id: "docker"
lang: "zh"
order_index: 2
title: "镜像"
description: "学习如何读懂镜像引用，并查看对应镜像是否已在本地。"
meta_title: "镜像 - Docker"
meta_description: "认识 Docker 镜像的名称和标签，了解镜像仓库和拉取操作，并区分镜像列表与容器列表。"
meta_keywords: "Docker 镜像, 镜像标签, 镜像仓库, docker pull, docker image ls"
---

Docker 镜像打包了程序、程序所需的文件和默认设置。Docker 以镜像为基础创建容器。这一课，你会学习怎样读懂镜像名称，并找出 Docker 已经有哪些镜像。

## 读懂镜像名称和标签

在 `nginx:alpine` 中，`nginx` 是镜像名称，`alpine` 是**标签**，用来选择某个版本或变体。这里选择的是基于 Alpine Linux 构建的变体。冒号把镜像名称和标签分开。`nginx:alpine` 和 `nginx:latest` 的镜像名称相同，但引用不同。

:::single-choice{#docker-images-read-reference} 在 `busybox:1.36` 中，哪一部分是标签？

::option[`busybox`]{#docker-images-reference-name explanation="BusyBox 是镜像名称，位于冒号前面。"}
::option[`busybox:1.36`]{#docker-images-reference-whole explanation="这是完整的引用，包含镜像名称和标签。"}
::option[`1.36`]{#docker-images-reference-tag .correct explanation="冒号后面是标签，用它来选择镜像。"}
:::

## 选择标签

如果只写 `nginx` 这样的镜像名称，Docker 会使用 `latest`。这是约定俗成的标签名。发布者决定标签指向哪个镜像，之后也可以修改它。写成 `nginx:alpine` 可以明确选择 Alpine 变体，这个标签也可能随发布而更新。

:::single-choice{#docker-images-default-tag} 同事使用 `nginx` 时没有指定标签，以为 Docker 会选择最新发布的版本。这个引用实际选中了什么？

::option[latest 标签当前指向的镜像。]{#docker-images-default-latest .correct explanation="省略标签时会使用 latest。具体指向哪个镜像由发布者决定。"}
::option[最近发布的 Nginx 镜像。]{#docker-images-default-newest explanation="Docker 直接使用名为 latest 的标签，不会按发布时间排序。"}
::option[体积最小的 Nginx 镜像。]{#docker-images-default-smallest explanation="默认标签与镜像大小无关。要选用某个变体，应明确写出对应标签。"}
:::

## 下载镜像

**镜像仓库**存放镜像并提供下载。像 `nginx:alpine` 这样的引用，Docker 默认会去 Docker Hub 查找。使用 `docker pull` 可以把镜像下载到当前连接的 Docker 环境中。下载镜像也叫**拉取镜像**。

```bash
$ docker pull nginx:alpine
```

命令成功后，就可以在当前 Docker 环境使用这个镜像了。启动容器是另一步操作。终端示例中的 `$` 是提示符。

:::single-choice{#docker-images-pull-result} 成功拉取镜像后，Docker 完成了什么？

::option[启动了一个可以响应网页请求的容器。]{#docker-images-pull-started explanation="需要另行运行容器。拉取只会让镜像可供使用。"}
::option[让镜像可以在当前环境中使用。]{#docker-images-pull-available .correct explanation="现在可以用下载好的镜像来创建容器。"}
::option[向镜像仓库上传了一份镜像。]{#docker-images-pull-uploaded explanation="拉取的方向是从镜像仓库到 Docker 的本地存储。"}
:::

## 查看本地镜像

使用 `docker image ls` 查看已有镜像。下面只列出名称和标签两列。Docker 将镜像名称这一列标为 `REPOSITORY`。

```text
$ docker image ls
REPOSITORY   TAG
nginx        alpine
busybox      1.36
```

第一行显示的是 `nginx:alpine`。这张表列出有哪些镜像，不显示用这些镜像创建的容器处于什么状态。

![LabEx 终端显示 docker pull 的执行结果，以及 docker image ls 中的镜像名称和标签](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-images/pull-and-list.png)

截图中的列表经过筛选，只保留了本课使用的两个镜像引用。

:::single-choice{#docker-images-local-list} 以下哪个引用出现在列表中？

::option[`busybox:latest`]{#docker-images-local-busybox-latest explanation="BusyBox 那一行的标签是 1.36。示例中没有带 latest 标签的 BusyBox 镜像。"}
::option[`busybox:1.36`]{#docker-images-local-busybox .correct explanation="把同一行 REPOSITORY 列的 busybox 与 TAG 列的 1.36 合起来。"}
::option[`nginx:1.36`]{#docker-images-local-nginx-mixed explanation="名称和标签必须取自同一行。这里的 1.36 在 BusyBox 那一行。"}
:::

## 总结

现在，你可以读懂镜像引用，并检查它是否出现在本地镜像列表中。

1. 识别镜像引用中的名称和标签。
2. 解释省略标签时会发生什么。
3. 用 `docker pull` 从镜像仓库下载镜像。
4. 读懂 `docker image ls` 的名称列和标签列。
