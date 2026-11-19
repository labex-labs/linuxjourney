---
lesson_id: "compose-environment-variables"
course_id: "docker-compose"
lang: "zh"
order_index: 5
title: "环境变量"
description: "区分 Compose 读取文件时替换进去的值，与传入容器的值。"
meta_title: "环境变量 - Docker Compose"
meta_description: "了解 Compose 如何先解析变量，再把选定的值传给容器中的程序。"
meta_keywords: "环境变量, 变量替换, Docker Compose, 容器配置, DevOps, Linux Journey"
---

环境变量是程序可以读取的带名称的值。Compose 可以在两个环节用到变量：读取文件时用变量的值替换表达式，也可以给容器里的程序传入值。

## 在文件中替换变量

把下面的内容存为练习目录中的 `compose.env.yaml`。其中的 `${PAGE_MODE:-demo}` 表示：如果 `PAGE_MODE` 已设置且不为空，就使用它的值，否则使用 `demo`。

```yaml
services:
  toolbox:
    image: busybox:1.36
    environment:
      PAGE_MODE: "${PAGE_MODE:-demo}"
```

Compose 会在创建容器之前解析这个表达式，这个过程叫**变量插值**。其他配置文件也可能用相同的方法选择主机端口或镜像标签。

:::single-choice{#compose-environment-variables-interpolate-default} 如果没有设置 PAGE_MODE，展开后的配置会出现什么值？

::option[文件中写下的原始表达式。]{#compose-environment-variables-interpolate-default-a explanation="Compose 读取文件时会解析表达式。"}
::option[自动生成的容器名称。]{#compose-environment-variables-interpolate-default-c explanation="容器命名和环境变量取值是两个不同的设置。"}
::option[demo，也就是默认值运算符后面的值。]{#compose-environment-variables-interpolate-default-b .correct explanation="这个表达式指定 demo 作为回退值。"}
:::

## 查看解析出来的值

在命令前面为变量赋值，可以只为这次运行设置变量。用这个方法看看换一个值会有什么效果。`config` 命令会显示解析后的配置，不会创建容器。

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml config
```

在服务的环境变量设置中查找 `PAGE_MODE: review`。`review` 只是演示值。不要把机密信息写进示例配置，也不要在输出里打印机密信息。

:::single-choice{#compose-environment-variables-config-scope} 展开后的配置显示 review。现在已经发生了什么？

::option[服务已经用这个值启动。]{#compose-environment-variables-config-scope-b explanation="展开配置文件与启动容器是两步不同的操作。"}
::option[Compose 在读取配置时替换成了这个值。]{#compose-environment-variables-config-scope-a .correct explanation="config 会在启动任何容器之前显示解析后的配置。"}
::option[所有已有容器现在都使用这个值。]{#compose-environment-variables-config-scope-c explanation="这次运行没有更改正在运行的容器。"}
:::

## 把值传入容器

`environment` 部分会把解析出的设置传入新容器。用 `printenv` 让这个一次性容器里的程序输出变量值。

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml run --rm toolbox printenv PAGE_MODE
```

预期输出是 `review`。变量插值选出了这个值，环境变量配置又把这个值传入容器。如果变量只用来选择主机端口，它不会自动出现在程序的环境变量中。

:::single-choice{#compose-environment-variables-actual-value} 用什么操作可以确认工具容器里的程序收到了哪个值？

::option[在容器内打印 PAGE_MODE。]{#compose-environment-variables-actual-value-c .correct explanation="程序自己的环境变量才能说明它实际收到了什么值。"}
::option[只看原始文件中写的默认值。]{#compose-environment-variables-actual-value-a explanation="可能有其他值覆盖文件中的默认值。"}
::option[找出工具容器的 IP 地址。]{#compose-environment-variables-actual-value-b explanation="地址无法反映程序的设置。"}
:::

## 总结

现在，你可以区分环境变量的两种用途。

1. 读懂 Compose 文件中的默认值表达式。
2. 启动容器前查看解析后的配置。
3. 检查已启动程序的环境变量值。
