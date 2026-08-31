---
lesson_id: "arch-linux"
course_id: "getting-started"
lang: "zh"
order_index: 9
title: "Arch Linux"
description: "了解 Arch Linux 如何结合滚动发布、Pacman 和由用户管理的系统配置。"
meta_title: "Arch Linux 发行版"
meta_description: "了解 Arch Linux 发行版，探索其滚动更新模式与 Pacman 软件包管理器的运作方式，以及为何 Arch Linux 受到追求系统掌控权与动手实践用户的青睐。"
meta_keywords: "Arch Linux 发行版，什么是 Arch Linux, Arch 滚动更新，Pacman 软件包管理器，Arch Linux 哲学"
---

## 什么是 Arch Linux？

Arch Linux 是一款轻量级、独立开发的 Linux 发行版，以用户控制和动手实践的理念而闻名。它深受那些希望更自主地构建系统，而非依赖繁重默认设置的用户喜爱。

与具有定期重大版本发布的发行版不同，Arch 采用滚动更新模式。这意味着系统会持续接收更新，而无需等待重大的版本跳跃。

:::single-choice{#recognize-rolling-release}
Arch Linux 的滚动发布模式意味着什么？

::option[已安装的系统会持续获得软件包升级]{#continuous-upgrades .correct explanation="Arch 通过持续的软件包升级演进，而不是发布彼此分离的主要系统版本；得到维护的安装可以长期保持最新。"}
::option[系统等待固定的多年期升级版本]{#fixed-major-editions explanation="固定的主要版本属于点发布模式；Arch 会持续更新已安装的系统。"}
::option[系统只在重新安装时替换所有软件包]{#reinstall-for-updates explanation="Arch 用户使用 Pacman 更新现有安装；重新安装不是获取每批升级的常规方式。"}
:::

## 为什么 Arch Linux 如此受欢迎

Arch Linux 之所以受欢迎，是因为它赋予了用户高度的控制权。许多人选择它并不是因为它最简单，而是因为它鼓励用户去了解安装了什么、系统是如何配置的，以及各个组件是如何协同工作的。

这使得 Arch 成为好奇的中高级用户的常见推荐，尽管在[选择 Linux 发行版](https://labex.io/zh/lesson/choosing-a-linux-distribution)时，它通常不是推荐给初学者的首选。

:::single-choice{#match-arch-user}
哪类用户最适合 Arch Linux？

::option[希望所有决定都自动完成的初学者]{#automatic-beginner explanation="Arch 有意把许多选择留给用户；带有更多预设默认值的发行版更符合全自动配置需求。"}
::option[从不想查看软件更新的用户]{#ignore-updates explanation="滚动更新的 Arch 系统需要主动维护并关注更新公告；忽略更新与这一责任相冲突。"}
::option[愿意阅读资料并维护系统的动手型学习者]{#hands-on-learner .correct explanation="Arch 面向具有自己动手态度、愿意查阅文档并负责配置和维护的用户。"}
:::

## 滚动更新

Arch 使用滚动更新模式，因此软件包会持续更新。这让用户无需为每个重大版本重新安装系统即可获得最新的软件，但也意味着更新需要比保守的点发布发行版投入更多的关注。

对于希望系统保持最新的用户来说，滚动更新是一个巨大的吸引力。对于优先考虑最大可预测性的用户，像 [Debian](https://labex.io/zh/lesson/debian) 这样的发行版可能会让他们感觉更舒适。

## Pacman 与软件包管理

Arch 使用 Pacman 作为其软件包管理器。Pacman 负责在系统上安装、更新、删除和跟踪软件，它是 Arch Linux 体验中最具辨识度的部分之一。

一个常用的命令是 `sudo pacman -Syu`，它会同步软件包数据库，并对配置的软件仓库执行完整升级。Arch 不支持部分升级，因此用户应避免只刷新软件包数据库而不完成对应的系统升级。Pacman 因其直接、快速且与 Arch 的极简主义设计紧密契合而备受推崇。

:::single-choice{#identify-pacman-role}
Pacman 在 Arch Linux 中发挥什么作用？

::option[选择桌面布局，但不管理软件]{#pacman-desktop-layout explanation="桌面配置与软件包管理是两回事；Pacman 管理能提供桌面组件的软件包。"}
::option[用固定版本取代滚动发布模式]{#pacman-fixed-releases explanation="Pacman 通过软件包升级支持 Arch 的滚动系统，并不会把 Arch 变成点发布发行版。"}
::option[安装、更新、删除和跟踪软件包]{#pacman-package-manager .correct explanation="Pacman 是 Arch Linux 的软件包管理器，负责维护已安装的软件包并与发行版仓库配合。"}
:::

:::single-choice{#avoid-partial-upgrades}
Arch 用户刷新软件包数据库后，为什么应完成一次完整升级？

::option[部分升级是保留旧库的推荐方式]{#partial-upgrades-recommended explanation="Arch 明确不支持部分升级；混用较新的库和依赖它们的旧软件包可能破坏系统。"}
::option[刷新软件包数据库会自动重装操作系统]{#refresh-reinstalls-system explanation="刷新数据库只会更新软件包信息，不会重装 Arch，但随后应执行与之对应的完整升级。"}
::option[仓库软件包作为一致的系统状态共同维护]{#consistent-system-state .correct explanation="Arch 仓库会作为滚动系统整体向前推进；完整升级能让已安装的库及依赖软件包保持一致。"}
:::

## Arch 哲学

Arch 通常与极简主义、现代性和以用户为中心联系在一起。在实践中，这意味着该发行版尽量避免不必要的抽象，并期望用户对系统的设置和维护负责。

这种哲学是 Arch 吸引忠实用户的主要原因。它不是试图尽可能地隐藏复杂性，而是试图让系统变得易于理解。

## 谁应该使用 Arch Linux？

Arch Linux 最适合那些想要动手实践 Linux 发行版，并且不介意阅读文档、手动配置系统组件以及对更新负责的用户。对于想要深入了解系统的用户来说，它是一个极佳的学习环境。

对于完全的初学者，Arch 通常作为进阶选择比作为入门选择更好。

## 延伸阅读

- [Arch Linux](https://archlinux.org/)
- [ArchWiki](https://wiki.archlinux.org/)
- [Pacman](https://wiki.archlinux.org/title/Pacman)
- [Arch Linux 安装指南](https://wiki.archlinux.org/title/Installation_guide)

为了建立 Arch Linux 所需的命令行信心，我们推荐以下 LabEx 课程：

1. **[Linux 命令在线练习](https://labex.io/zh/courses/linux-basic-commands-practice-online)** - 加强在动手实践的 Linux 环境中至关重要的命令行习惯。
2. **[Shell 初学者教程](https://labex.io/zh/courses/shell-for-beginners)** - 提高您对 Shell 和终端工作流程的熟悉程度。
3. **[Shell 脚本基础](https://labex.io/zh/courses/shell-scripting-fundamentals)** - 当您想要对 Linux 环境拥有更多控制权时，进一步深入学习。

## 总结

现在，您可以说明 Arch Linux 如何把持续升级与用户的直接责任结合起来。

1. 描述 Arch 的滚动发布模式。
2. 识别 Arch 面向的用户类型。
3. 知道 Pacman 是 Arch 的软件包管理器。
4. 说明 Arch 为什么要求执行完整系统升级。
