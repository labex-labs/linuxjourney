---
lesson_id: "dockerfile"
course_id: "docker"
lang: "zh"
order_index: 7
title: "Dockerfile"
description: "学习如何用 Dockerfile 将网页和基础镜像打包成可重复使用的 Web 服务器镜像。"
meta_title: "Dockerfile - Docker"
meta_description: "读懂简短 Dockerfile 中的 FROM、COPY 和 CMD，区分构建镜像与运行容器。"
meta_keywords: "Dockerfile, Docker 构建, FROM, COPY, CMD, 构建上下文"
---

前面用现成的 Web 服务器镜像启动过容器。如果想提供自己的网页，可以构建一个已经包含该网页的镜像。**Dockerfile** 就是写明如何构建镜像的文本文件。

## 从基础镜像开始

**基础镜像**提供起步所需的文件和程序。下面的 Dockerfile 以 Nginx 镜像为基础，加入一个网页，并指定容器默认执行的命令。把 Dockerfile 和名为 `index.html` 的文件放在同一个示例目录中。网页内容只写一行 `<h1>Hello from Docker</h1>` 就够了。

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
CMD ["nginx", "-g", "daemon off;"]
```

`FROM nginx:alpine` 选用指定的镜像作为基础，其中已经包含 Nginx 程序。Docker 构建新镜像时会用到它。

:::single-choice{#dockerfile-base-image-purpose} 添加网页前，哪一行提供了 Nginx？

::option[`COPY index.html /usr/share/nginx/html/index.html`]{#dockerfile-base-image-copy explanation="COPY 负责添加网页，服务器由基础镜像提供。"}
::option[`FROM nginx:alpine`]{#dockerfile-base-image-from .correct explanation="FROM 选择已经包含服务器程序的基础镜像。"}
::option[以 `CMD` 开头的那一行。]{#dockerfile-base-image-cmd explanation="CMD 设置默认启动命令，服务器程序来自基础镜像。"}
:::

## 添加文件

`COPY` 从交给 Docker 构建的文件中读取 `index.html`，再把它写到指令右侧的路径。这个版本的 Nginx 镜像会用该路径提供默认网页。以后修改了本地网页，需要重新构建镜像才能打包新内容。

:::single-choice{#dockerfile-copy-after-edit} 构建之后，你修改了本地 index.html 的标题。怎样让新镜像包含这处修改？

::option[用当前镜像再启动一个容器。]{#dockerfile-copy-edit-run explanation="这个容器使用的仍是已有镜像中打包的网页。"}
::option[只给现有容器换个名字。]{#dockerfile-copy-edit-rename explanation="容器名称不会改变镜像里打包的文件。"}
::option[用更新后的网页重新构建镜像。]{#dockerfile-copy-edit-rebuild .correct explanation="构建时，COPY 会读取当前的本地文件，并把它放进新镜像中。"}
:::

## 设置启动命令

`CMD` 为新容器设置默认命令。在这个例子中，它让 Nginx 在容器内以前台方式持续运行。同时，你仍可用 `docker run -d` 让容器在终端后台运行。

:::single-choice{#dockerfile-cmd-start-time} 示例中的默认 CMD 什么时候生效？

::option[容器使用默认命令启动时。]{#dockerfile-cmd-when-start .correct explanation="Docker 在容器启动时使用镜像中的默认命令。"}
::option[Docker 把网页复制到镜像中时。]{#dockerfile-cmd-when-copy explanation="COPY 在构建期间添加网页，不会运行服务器。"}
::option[Docker 写完镜像时。]{#dockerfile-cmd-when-build explanation="构建只会记录启动命令，供之后使用。"}
:::

## 构建镜像并运行容器

在同时包含两个文件的目录中执行构建命令。`-t` 选项为镜像指定引用 `journey-web:1`。命令末尾的点表示使用当前目录作为构建文件的来源。

```bash
$ docker build -t journey-web:1 .
$ docker run -d --name custom-web -p 127.0.0.1:8082:80 journey-web:1
```

第二条命令启动容器。如果 8082 端口可用，就可以在 Docker 主机的浏览器中打开 `http://127.0.0.1:8082`，查看自己的网页。

:::single-choice{#dockerfile-build-versus-run} 构建已经成功，还没有运行第二条命令。此时哪些东西已经就绪？

::option[镜像已经生成，可以用它创建容器。]{#dockerfile-build-ready-image .correct explanation="构建产出了镜像。接下来的命令会用它启动容器。"}
::option[指定名称的容器已经在提供你的网页。]{#dockerfile-build-ready-container explanation="运行镜像启动容器后，服务器才会启动。"}
::option[Docker 已经为这个镜像发布了浏览器访问端口。]{#dockerfile-build-ready-port explanation="端口映射是 docker run 的选项，构建时不会设置这条连接。"}
:::

![LabEx 终端显示镜像构建、容器启动，以及自定义网页返回的 HTML](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/dockerfile/build-and-run.png)

最后一个请求取回了构建时打包进镜像的网页。你在自己的环境中看到的构建进度和镜像 ID 可能不同。

## 总结

现在，你可以读懂简单的 Dockerfile，并了解本地网页如何一步步变成可访问的服务。

1. 从 `FROM` 指令中找出基础镜像。
2. 说明 `COPY` 从哪里读取文件，又把文件写到哪里。
3. 识别 `CMD` 设置的容器默认启动命令。
4. 构建镜像，再用它启动容器。
