---
index: 5
lang: "zh"
title: "Systemd 概述"
meta_title: "Systemd 概述 - Init 系统"
meta_description: "了解 Systemd 基础知识：理解单元 (units)、目标 (targets) 和启动过程。探索 Systemd 如何管理 Linux 中的服务和系统状态。开始您的学习之旅！"
meta_keywords: "Systemd, Systemd 单元，Systemd 目标，Linux 启动过程，Linux 服务，初学者，教程，指南"
---

## Lesson Content

Systemd 是大多数现代 Linux 发行版中的标准 init 系统。如果您有一个 `/usr/lib/systemd` 目录，那么您很可能正在使用 systemd。

Systemd 使用目标 (goals) 来使您的系统启动并运行。基本上，您有一个想要实现的目标，并且该目标也有需要满足的依赖项。Systemd 非常灵活和健壮；它不遵循严格的顺序来启动进程。以下是典型 systemd 启动过程中发生的情况：

1. 首先，systemd 加载其配置文件，这些文件通常位于 `/etc/systemd/system` 或 `/usr/lib/systemd/system` 中。
2. 然后它确定其启动目标，通常是 `default.target`。
3. Systemd 解析启动目标的依赖项并激活它们。

类似于 SysV runlevels，systemd 会启动到不同的目标：

- `poweroff.target` - 关闭系统
- `rescue.target` - 单用户模式
- `multi-user.target` - 多用户带网络
- `graphical.target` - 多用户带网络和图形界面 (GUI)
- `reboot.target` - 重启

`default.target` 的默认启动目标通常指向 `graphical.target`。

Systemd 处理的主要对象被称为单元 (units)。Systemd 不仅仅是启动和停止服务；它还可以挂载文件系统、监控网络套接字等。正因为这种健壮性，它有不同类型的单元来操作。最常见的单元是：

- Service units - 这些是我们一直在启动和停止的服务；这些单元文件以 `.service` 结尾。
- Mount units - 这些挂载文件系统；这些单元文件以 `.mount` 结尾。
- Target units - 这些将其他单元分组在一起；文件以 `.target` 结尾。

例如，假设我们启动到我们的 `default.target`。这个目标将 `networking.service` 单元、`crond.service` 单元等分组在一起，因此一旦我们激活一个单元，该单元下的所有内容也会被激活。

## Exercise

虽然此主题没有特定的实验，但我们建议探索全面的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

What unit is used to group together other units?

## Quiz Answer

target
