---
lesson_id: "linux-history"
course_id: "getting-started"
lang: "zh"
order_index: 1
title: "Linux 历史"
description: "了解 UNIX、GNU 与 Linux 内核如何共同促成了现代 Linux 系统。"
meta_title: "Linux 历史 - 入门指南"
meta_description: "开启您的 Linux 之旅，探索 Linux 的发展历史。了解其从 UNIX 和 GNU 项目的起源，以及林纳斯·托瓦兹创建 Linux 内核的过程。"
meta_keywords: "Linux 历史，Linux 发展史，Linux 之旅，UNIX, GNU 项目，林纳斯·托瓦兹，Linux 内核，Linux 入门"
---

欢迎开启您的 **Linux 之旅**！如果您已准备好探索强大的 Linux 世界，那么您来对地方了。我叫企鹅皮特（Penguin Pete），将担任您的向导。首先，让我们简要回顾 **Linux 的历史**。

## Linux 的前身

要理解 Linux 如何诞生，需要回到 1969 年。当时，贝尔实验室的肯·汤普森（Ken Thompson）和丹尼斯·里奇（Dennis Ritchie）开发了 UNIX 操作系统。UNIX 后来用 C 语言重写，因此更容易移植到不同硬件上，并由此得到广泛采用。

![Unix 时间轴](https://file.labex.io/images/ed9c245d-e8be-4287-bf34-67750b042542.jpg)

:::single-choice{#understand-unix-portability}
用 C 语言重写 UNIX 带来了什么重要结果？

::option[它成为了为 GNU 系统创建的自由内核。]{#unix-became-gnu-kernel explanation="UNIX 早于 GNU 项目出现，并不是 GNU 的内核；GNU 后来另行开发了名为 Hurd 的内核。"}
::option[它更容易移植到不同的硬件系统。]{#portable-across-hardware .correct explanation="用 C 语言编写让 UNIX 具有更好的可移植性，这也帮助它走出最初的硬件平台并得到推广。"}
::option[它成为了仅供贝尔实验室使用的命令 shell。]{#unix-became-shell explanation="UNIX 是操作系统，而不只是 shell；用 C 语言重写反而促进了它在贝尔实验室之外的采用。"}
:::

十多年后，理查德·斯托曼（Richard Stallman）发起了 GNU 项目。GNU 是“GNU's Not UNIX”的递归缩写，目标是创建一个完全自由且开源的类 UNIX 操作系统。该项目开发了许多关键组件，并制定了 GNU 通用公共许可证（GPL）；但当 Linux 出现时，GNU 自己的内核 GNU Hurd 还无法供人们普遍使用。

:::single-choice{#identify-gnu-missing-component}
Linux 出现时，GNU 的哪个主要组件还没有准备就绪？

::option[可用于生产环境的内核]{#gnu-kernel .correct explanation="GNU 已经开发了许多系统组件，但自己的内核 GNU Hurd 当时还无法供人们普遍使用。"}
::option[自由软件许可证]{#gnu-license explanation="GNU 项目当时已经制定了 GNU 通用公共许可证；缺少的是可用的内核。"}
::option[关键的系统工具]{#gnu-tools explanation="GNU 已经开发了许多关键工具，仍未完成的主要系统组件是内核。"}
:::

## 内核的作用

内核是操作系统的核心组件。它像一座桥梁，让硬件能够与软件通信。内核负责管理 CPU、内存和外围设备等系统资源。除了人们使用的工具和应用程序，一套完整的操作系统还需要这个管理资源的核心。

:::single-choice{#recognize-kernel-role}
以下哪项职责属于操作系统内核？

::option[编写用户在 shell 中输入的每条命令]{#write-shell-commands explanation="shell 命令由用户或脚本提供；程序执行这些命令时，内核负责提供底层资源。"}
::option[为每个已安装的应用程序选择许可证]{#choose-software-licenses explanation="应用程序许可证由软件作者和发行者选择，这不是内核管理系统资源的职责。"}
::option[管理 CPU、内存和连接的设备]{#manage-system-resources .correct explanation="内核管理硬件资源并把它们提供给软件使用，CPU 时间、内存和设备都是典型例子。"}
:::

## Linux 内核的诞生

时间来到 1991 年，芬兰学生林纳斯·托瓦兹（Linus Torvalds）开始以个人项目的形式开发一种新内核，它后来被称为 Linux 内核。Linux 于 1992 年以自由软件形式发布后，便可以与接近完成的 GNU 系统结合，组成一套完整的自由操作系统，通常称为 GNU/Linux。这是 **Linux 历史**上的关键里程碑。

![2018 年的林纳斯·托瓦兹](https://file.labex.io/images/3e1311fd-b8ca-45e7-8d02-9aac6377bb36.jpg)

_2018 年的林纳斯·托瓦兹（来源：[维基百科](https://en.wikipedia.org/wiki/Linus_Torvalds)）_

:::single-choice{#identify-linux-kernel-creator}
1991 年是谁开始开发 Linux 内核？

::option[理查德·斯托曼]{#richard-stallman explanation="理查德·斯托曼发起了 GNU 项目；GNU 提供了许多系统组件，但 Linux 内核由林纳斯·托瓦兹开始开发。"}
::option[丹尼斯·里奇]{#dennis-ritchie explanation="丹尼斯·里奇参与开发了 UNIX 和 C 语言；Linux 内核项目后来由林纳斯·托瓦兹发起。"}
::option[林纳斯·托瓦兹]{#linus-torvalds .correct explanation="林纳斯·托瓦兹于 1991 年发起了这个内核项目，它后来成为 Linux 内核。"}
:::

要继续您的 **Linux 之旅**，可以尝试以下动手实验，练习基础命令并建立使用命令行环境的信心。

1. **[Linux 入门](https://labex.io/zh/labs/linux-getting-started-with-linux-446315)** - 学习 `echo`、`date` 等基本终端命令和简单计算，适合没有基础的初学者。
2. **[您的第一个 Linux 实验](https://labex.io/zh/labs/linux-your-first-linux-lab-270253)** - 在 Linux 中完成经典的“Hello, World!”程序，并学习一些基础命令。
3. **[创建个性化终端问候语](https://labex.io/zh/labs/linux-create-personalized-terminal-greeting-446322)** - 使用基本 Linux 终端命令创建有趣的欢迎信息。

## 总结

现在，您可以说明 UNIX、GNU 和 Linux 内核如何共同促成了现代 Linux 系统。

1. 说明 UNIX 的可移植性为何重要。
2. 指出内核是 GNU 当时缺少的主要组件。
3. 解释内核在管理系统资源方面的作用。
4. 知道 Linux 内核由林纳斯·托瓦兹创建。
