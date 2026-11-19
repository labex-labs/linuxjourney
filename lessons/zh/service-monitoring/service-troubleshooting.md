---
lesson_id: "service-troubleshooting"
course_id: "service-monitoring"
lang: "zh"
order_index: 7
title: "服务故障排查"
description: "遇到服务停止、依赖报错或请求缓慢时，学习如何选择下一项检查。"
meta_title: "服务故障排查 - 服务监控"
meta_description: "根据用户报告的症状，对照进程状态、请求日志和延迟指标，找出下一项检查。"
meta_keywords: "服务排查, 容器日志, 依赖服务, 请求延迟, 服务监控, Linux Journey"
---

先从一个具体症状入手，例如主页请求失败。然后对照相近时间的观测结果，并确保至少有一项检查来自用户真正访问服务的位置。

## 服务器停止时

第一种情况是浏览器报告连接被拒绝，容器显示 `Exited (1)`。这两项观察表明值得查查程序为何停止。查看容器保留的日志，要与其他事件比较时，先留意程序退出的时间。

:::single-choice{#service-troubleshooting-stopped-case} 哪项检查最有可能解释进程为什么停止？

::option[再次请求同一个主页，获取较新的状态。]{#service-troubleshooting-stopped-case-a explanation="重试能核实症状，保留的日志则可能解释程序为什么退出。"}
::option[读取该容器最后几行可用的日志。]{#service-troubleshooting-stopped-case-b .correct explanation="启动或退出消息可能指出程序在哪一步停止。"}
::option[查看使用相同镜像的另一个运行中容器的日志。]{#service-troubleshooting-stopped-case-c explanation="另一个容器有自己的运行历史，可能从未碰到这次错误。"}
:::

## 依赖服务失败时

第二种情况是 Web 进程正在运行，但页面返回服务器错误。Web 日志显示，请求 `r17` 在调用目录服务时超时。接下来应当查看依赖服务里同一个请求的记录。第一跳正常，并不能说明后续服务都正常。

:::single-choice{#service-troubleshooting-dependency-case} 接下来应该为 r17 找什么证据？

::option[目录服务在当时处理这个请求的记录。]{#service-troubleshooting-dependency-case-a .correct explanation="它能说明调用依赖服务时发生了什么。"}
::option[归档的 Docker 镜像大小。]{#service-troubleshooting-dependency-case-b explanation="镜像大小无法描述这次实际调用。"}
::option[昨天一次无关的成功主页检查。]{#service-troubleshooting-dependency-case-c explanation="那是另一个时间的检查，无法解释这次请求。"}
:::

## 请求变慢时

第三个样本中，大部分请求正常响应，但用户说等得久了。延迟上升的同时，工作队列也在增长。判断原因前，先检查请求量和工作单元的活动。如果做了改动，之后要重复面向用户的检查，再看同一组信号有没有变化。

:::single-choice{#service-troubleshooting-slow-case} 怎样对比最能检验改动有没有帮助？

::option[对比改动前后源代码仓库的截图。]{#service-troubleshooting-slow-case-a explanation="这些截图不测量请求耗时或排队情况。"}
::option[拿缓存大小与部署的分支数量相比。]{#service-troubleshooting-slow-case-b explanation="这两项都无法说明用户报告的等待时间。"}
::option[比较改动前后可比的用户请求耗时和工作队列。]{#service-troubleshooting-slow-case-c .correct explanation="这样可以同时检查原先的症状和疑似瓶颈。"}
:::

## 解读不一致的检查结果

假设本地探测成功，但用户仍能看到错误。记下每项检查使用的访问路径。本地探测可以证明主机上的进程能响应，而客户端请求可能发现到达这台主机的路径有问题。

:::single-choice{#service-troubleshooting-final-application} 要继续调查受影响的用户，哪项结果最合适？

::option[从这些用户所在的位置，沿他们使用的路径执行检查。]{#service-troubleshooting-final-application-a .correct explanation="这样可以观测用户报告问题时实际访问的部分。"}
::option[只看主机本地检查的结果。]{#service-troubleshooting-final-application-b explanation="本地结果有助于缩小范围，但没有测试外部的访问路径。"}
::option[镜像仓库当前的容量。]{#service-troubleshooting-final-application-c explanation="镜像仓库能提供镜像时，用户使用的访问路径仍可能有别的问题。"}
:::

## 总结

现在，你可以根据手上的证据，选择下一项检查。

1. 用进程状态和日志调查程序停止的原因。
2. 沿着失败的请求追查依赖服务。
3. 对照原本用户可见的症状，验证改动是否改善了结果。
