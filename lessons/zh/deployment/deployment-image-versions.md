---
lesson_id: "deployment-image-versions"
course_id: "deployment"
lang: "zh"
order_index: 2
title: "镜像版本"
description: "区分镜像标签和摘要，并比较两个环境实际使用的镜像。"
meta_title: "镜像版本 - 部署"
meta_description: "读懂标签与摘要引用，并按平台核对两个环境实际部署的镜像。"
meta_keywords: "镜像版本, 镜像标签, 镜像摘要, 部署, DevOps, Linux Journey"
---

`site:2` 这样的标签让镜像引用容易辨认。不过，发布者推送替代镜像时，可以更改标签的指向。要识别镜像的确切内容，应记录它的**摘要**，也就是根据被引用的内容计算出的值。

## 读取标签

假设镜像仓库在不同日期显示了以下记录。这里的摘要为了演示而缩短，不能拿来拉取镜像。

```text
Monday    site:2    sha256:a1b2…
Tuesday   site:2    sha256:c3d4…
```

同一个标签现在指向不同的内容。星期一拉取镜像的机器可能仍在使用旧版。

:::single-choice{#deployment-image-versions-moving-tag} 两个环境都显示 site:2 标签。怎样确认它们各自实际拉取的是哪个镜像？

::option[只看共有的标签。]{#deployment-image-versions-moving-tag-b explanation="示例中两个不同的镜像使用了同一个标签。"}
::option[统计任一台机器上的容器数。]{#deployment-image-versions-moving-tag-c explanation="容器数量无法识别它们使用的镜像。"}
::option[查看各自记录的摘要。]{#deployment-image-versions-moving-tag-a .correct explanation="标签指向可能改变，摘要则可以识别拉取时选中的内容。"}
:::

## 读取摘要引用

镜像名后面可以加 `@` 和完整的摘要，用来向仓库请求那个确切的对象。请使用镜像仓库或构建记录里的完整摘要。缩短值适合展示示例，无法用来获取对应镜像。

:::single-choice{#deployment-image-versions-fixed-reference} 哪个写法可以选中镜像仓库中的特定对象？

::option[不带标签的镜像名。]{#deployment-image-versions-fixed-reference-a explanation="Docker 会应用默认标签，而标签指向可能改变。"}
::option[镜像名后加上完整摘要。]{#deployment-image-versions-fixed-reference-c .correct explanation="摘要指向确定的内容。"}
::option[在注释里写上构建日期。]{#deployment-image-versions-fixed-reference-b explanation="仓库无法通过注释获取对象。"}
:::

## 在相同条件下比较镜像

一个镜像引用可以对应面向不同架构的构建列表，也可以对应某个平台的单独镜像。比较两台主机实际运行的内容时，先记录它们的平台，再比较对应平台的镜像引用。发布记录中应保留原始的完整引用。

:::single-choice{#deployment-image-versions-compare-platform} 一个版本同时支持 arm64 和 amd64。核对两台 amd64 主机时，哪项比较有意义？

::option[比较两台主机选中的 amd64 镜像引用。]{#deployment-image-versions-compare-platform-b .correct explanation="这样比较的是用于同一平台的内容。"}
::option[比较为不同架构准备的镜像对象。]{#deployment-image-versions-compare-platform-a explanation="这些对象本来就对应不同的平台。"}
::option[比较两台主机的主机名。]{#deployment-image-versions-compare-platform-c explanation="主机名能标识机器，无法标识实际部署的内容。"}
:::

## 总结

现在，你可以通过摘要追踪镜像内容，而不只依赖容易辨认的标签。

1. 解释为什么同一个标签可能指向不同内容。
2. 识别包含完整摘要的镜像引用。
3. 比较对应平台的确切镜像。
