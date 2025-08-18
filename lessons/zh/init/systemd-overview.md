---
index: 5
lang: "zh"
title: "Systemd 概述"
meta_title: "Systemd 概述 - 初始化"
meta_description: "学习 Systemd 基础知识：理解单元、目标和启动过程。了解 Systemd 如何在 Linux 中管理服务和系统状态。开始您的学习之旅！"
meta_keywords: "Systemd, Systemd 单元，Systemd 目标，Linux 启动过程，Linux 服务，初学者，教程，指南"
---

## Lesson Content

Systemd 正在慢慢成为 init 的新兴标准。如果您有 `/usr/lib/systemd` 目录，那么您很可能正在使用 systemd。

Systemd 使用目标来启动和运行您的系统。基本上，您有一个想要实现的目标，并且这个目标也有需要满足的依赖项。Systemd 极其灵活和健壮；它不遵循严格的顺序来启动进程。以下是典型的 systemd 启动过程中发生的事情：

1. 首先，systemd 加载其配置文件，通常位于 `/etc/systemd/system` 或 `/usr/lib/systemd/system`。
2. 然后它确定其启动目标，通常是 `default.target`。
3. Systemd 找出启动目标的依赖项并激活它们。

类似于 SysV 运行级别，systemd 启动到不同的目标：

- `poweroff.target` - 关闭系统
- `rescue.target` - 单用户模式
- `multi-user.target` - 多用户带网络
- `graphical.target` - 多用户带网络和 GUI
- `reboot.target` - 重启

`default.target` 的默认启动目标通常指向 `graphical.target`。

Systemd 工作的主要对象被称为单元（units）。Systemd 不仅仅是停止和启动服务；它还可以挂载文件系统、监控您的网络套接字等。由于其健壮性，它有不同类型的操作单元。最常见的单元是：

- Service units - 这些是我们一直在启动和停止的服务；这些单元文件以 `.service` 结尾。
- Mount units - 这些挂载文件系统；这些单元文件以 `.mount` 结尾。
- Target units - 这些将其他单元组合在一起；这些文件以 `.target` 结尾。

例如，假设我们启动到 `default.target`。这个目标将 `networking.service` 单元、`crond.service` 单元等组合在一起，因此一旦我们激活一个单元，该单元下面的所有内容也会被激活。

## Exercise

No exercises for this lesson.

## Quiz Question

什么单元用于将其他单元组合在一起？

## Quiz Answer

target
