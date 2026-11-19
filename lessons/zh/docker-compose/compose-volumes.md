---
lesson_id: "compose-volumes"
course_id: "docker-compose"
lang: "zh"
order_index: 4
title: "数据卷"
description: "了解为什么具名数据卷中的文件在容器替换后仍然存在。"
meta_title: "数据卷 - Docker Compose"
meta_description: "了解文件如何保存在具名数据卷中，并用另一个容器验证数据是否保留。"
meta_keywords: "数据卷, 具名卷, Docker Compose, 持久化, DevOps, Linux Journey"
---

容器可以在自己的可写层中写入文件。移除容器时，Docker 会一并移除这层。**具名数据卷**是由 Docker 单独管理的存储，可以挂载到替换后的容器。

## 定义练习用数据卷

把下面的独立示例保存为练习目录中的 `compose.volume.yaml`。它把名为 `notes` 的存储挂载到工具容器中的 `/data`。文件底部的 `volumes` 部分声明了这份具名存储。

```yaml
services:
  toolbox:
    image: busybox:1.36
    volumes:
      - notes:/data
volumes:
  notes:
```

服务定义决定数据卷会挂载到容器中的哪个位置。文件顶层的声明告诉 Compose 把这个数据卷作为项目资源来管理。

:::single-choice{#compose-volumes-attached-path} 工具容器中的哪个路径使用了具名数据卷？

::option[/notes。]{#compose-volumes-attached-path-b explanation="notes 是数据卷的名称，用于挂载的容器内路径是另一个值。"}
::option[/data。]{#compose-volumes-attached-path-a .correct explanation="notes:/data 的右侧是容器中的路径。"}
::option[容器内的所有路径。]{#compose-volumes-attached-path-c explanation="数据卷只覆盖配置中的那个目录。"}
:::

## 用不同容器写入和读取

`-f` 用于选择单独的配置文件，`-p` 则为它指定不同的项目名称。`run --rm` 会创建一个只运行一次的容器，并在它结束后移除它。请在独立的练习目录中运行这些命令。第一条命令会覆盖测试文件 `/data/note.txt`。

```bash
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox sh -c 'echo ready > /data/note.txt'
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox cat /data/note.txt
```

第二个容器应当输出 `ready`。它挂载了与第一个容器相同的数据卷。

:::single-choice{#compose-volumes-persistence} 第一个容器被移除后，为什么第二个容器仍能读到该文件？

::option[两个容器挂载了同一个具名数据卷。]{#compose-volumes-persistence-b .correct explanation="文件写入挂载在 /data 的独立存储中。"}
::option[两个容器都保留了第一个容器的可写层。]{#compose-volumes-persistence-a explanation="第一个容器被移除时，它的可写层也被移除了。"}
::option[BusyBox 自动把文件加到了镜像中。]{#compose-volumes-persistence-c explanation="运行容器不会改变原来的镜像。"}
:::

![两个工具容器分别向同一个具名数据卷中的文件写入和读取数据](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-volumes/persisted-note.png)

## 确认数据存放在哪里

如果 `/tmp/note.txt` 之类的文件位于挂载目录之外，而且没有其他挂载覆盖这个位置，文件就留在它所在的容器中。要确认文件是否受到保护，先看存放路径。删除数据卷本身也可能抹掉卷里的数据。备份是另外保存的副本，数据卷丢失时可以从中恢复。

:::single-choice{#compose-volumes-inside-mount} 下一个工具容器能通过这个数据卷看到哪个文件？

::option[第一个工具容器写在可写层里的 /tmp/note.txt。]{#compose-volumes-inside-mount-a explanation="这个路径不在配置的挂载目录中。"}
::option[保存在另一个具名数据卷里的文件。]{#compose-volumes-inside-mount-b explanation="新容器必须挂载那个数据卷，才能看到它里面的文件。"}
::option[第一个工具容器写入的 /data/note.txt。]{#compose-volumes-inside-mount-c .correct explanation="挂载到 /data 后，每个容器都能访问同一个文件。"}
:::

## 总结

现在，你可以解释为什么创建文件的容器已被移除，文件仍能保留。

1. 读出数据卷名称和挂载路径。
2. 用另一个容器读取文件，验证数据是否保留。
3. 区分删除数据卷和替换容器。
