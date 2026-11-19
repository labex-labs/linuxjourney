---
lesson_id: "docker-logs-command"
course_id: "docker"
lang: "zh"
order_index: 6
title: "docker logs"
description: "学习如何查看 Docker 收集的容器输出，并据此选择排查步骤。"
meta_title: "docker logs - Docker"
meta_description: "查看运行中或已退出容器的日志，聚焦最新输出，并区分应用报错与容器状态。"
meta_keywords: "docker logs, 容器日志, Docker 故障排查, 启动错误, 查看最新日志"
---

名为 `preview` 的容器已经退出。容器列表会显示状态和退出码。要知道程序报告了什么，还得查看 Docker 从该容器收集到的输出。

## 选择要查看的容器

在 `docker logs` 后加上容器名称。已经停止但仍存在的容器，只要输出还保留着，也能用这个命令查看。示例中的短任务在结束前尝试读取 `/site/title.txt`。

```text
$ docker logs preview
cat: can't open '/site/title.txt': No such file or directory
```

这里是 `cat` 在尝试读取文件。消息给出了它在容器里找不到的文件路径。

:::single-choice{#docker-logs-command-read-exited} preview 和 report 用的是同一个镜像。哪条命令可以查看 preview 的输出？

::option[`docker logs report`]{#docker-logs-command-exited-report explanation="名称决定查看哪个容器。report 对应另一次运行。"}
::option[`docker logs busybox:1.36`]{#docker-logs-command-exited-image explanation="这是镜像引用。日志属于用镜像创建的某个容器。"}
::option[`docker logs preview`]{#docker-logs-command-exited-preview .correct explanation="命令指定了要查看输出的容器。"}
:::

## 结合上下文解读消息

日志里是程序自己发出的消息。一条启动消息可以告诉你程序开始监听请求，一条报错则可能指出哪个操作没有完成。示例提示 `preview` 里找不到某个路径。下一步可以核对容器中原本是否应该在这个确切位置放有文件。这条消息提供了排查起点。

:::single-choice{#docker-logs-command-error-boundary} 文件缺失的这条消息能说明什么？

::option[整个主机上的所有目录中都没有这个文件。]{#docker-logs-command-error-host-path explanation="程序查找的是容器内的路径，消息并未涉及主机上的所有文件。"}
::option[程序在 preview 内找不到指定文件。]{#docker-logs-command-error-container-path .correct explanation="这条消息记录了 preview 里运行的程序查找文件的结果。"}
::option[主机上的浏览器访问了未发布的端口。]{#docker-logs-command-error-network explanation="消息说的是文件查找，没有提供浏览器端口的信息。"}
:::

## 查看最新输出

如果容器的输出很多，可以在 `--tail` 后指定行数。Docker 会从已收集的输出末尾最多返回这么多行。可以先看少量日志。如果第一条错误出现在更早的位置，再多读一些。

```bash
$ docker logs --tail 5 web
```

![LabEx 终端显示 preview 的文件找不到报错，以及 web 的最后五行日志](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-logs-command/preview-and-tail.png)

两条命令查看的是不同的容器。在 LabEx 的运行结果中，`preview` 报告文件找不到，`web` 则报告 Nginx 已启动。

:::single-choice{#docker-logs-command-tail-choice} 只想看 web 保存的最新两行日志，哪条命令合适？

::option[`docker logs --tail 2 web`]{#docker-logs-command-tail-two .correct explanation="tail 2 会从该容器输出的末尾最多取两行。"}
::option[`docker logs --tail 5 web`]{#docker-logs-command-tail-five explanation="这条命令最多取五行，因此可能返回两行以上。"}
::option[`docker logs web`]{#docker-logs-command-tail-unlimited explanation="如果不限制行数，Docker 可以返回所有可用的输出。"}
:::

## 处理空结果

Docker 只能显示它收集到的内容。有的命令本来就没有输出，有的程序则会把消息写入 Docker 不收集的文件。如果 `docker logs` 执行成功却没有输出，可以用 `docker ps -a` 查看容器状态。日志为空并不能单独说明容器处于什么状态。

:::single-choice{#docker-logs-command-empty-result} 名为 cleanup 的任务没有留下日志。要判断它还在运行还是已经退出，该怎么查？

::option[让 Docker 多返回几行 cleanup 的日志。]{#docker-logs-command-empty-more-lines explanation="调整行数限制无法判断没有输出的程序是否已经停止。"}
::option[查找创建 cleanup 时使用的镜像。]{#docker-logs-command-empty-image explanation="镜像说明程序起初有哪些文件和设置。容器列表才会显示它现在的状态。"}
::option[在完整容器列表中查看 cleanup 的状态。]{#docker-logs-command-empty-container-state .correct explanation="完整列表会显示仍然存在的容器，包括在运行和已退出的容器。"}
:::

## 总结

现在，你可以根据容器输出决定下一步要查什么。

1. 查看指定容器收集到的输出，包括已退出的容器。
2. 根据程序消息定位报告的问题。
3. 用 `--tail` 限制输出行数。
4. 如果日志还不能回答问题，就再做有针对性的检查。
