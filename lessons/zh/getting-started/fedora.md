---
lesson_id: "fedora"
course_id: "getting-started"
lang: "zh"
order_index: 6
title: "Fedora"
description: "了解 Fedora 如何通过与 Red Hat 相连的社区项目提供较新的 Linux 技术。"
meta_title: "Fedora Linux 发行版"
meta_description: "了解 Fedora Linux 发行版、Fedora 与 Red Hat 的关系、DNF 软件包管理的工作原理，以及为何 Fedora 深受开发者和桌面用户欢迎。"
meta_keywords: "fedora linux, fedora linux 发行版，什么是 fedora, fedora red hat, fedora 版本，dnf 软件包管理，linux 发行版"
---

## 什么是 Fedora？

Fedora 是一个由 Red Hat 赞助、社区驱动的 Linux 发行版。它以提供前沿技术、精致的桌面体验以及对开发者和技术用户的强大支持而闻名。

Fedora 以比保守型发行版更快的更新速度著称，同时兼顾了质量和易用性。这种平衡使其对于那些既想要现代 Linux 系统又不想从零开始构建一切的用户极具吸引力。

:::single-choice{#identify-fedora-project-model}
以下哪项正确描述了 Fedora 项目？

::option[它是已经停止维护的 Red Hat Enterprise Linux 版本]{#discontinued-rhel explanation="Fedora 是具有独立版本的活跃发行版；它位于 RHEL 上游，而不是过时的 RHEL 版本。"}
::option[它是由一家硬件制造商维护的发行版]{#hardware-maintained explanation="Fedora 会与硬件厂商合作，但其开发由社区推动，并由 Red Hat 赞助。"}
::option[它是由 Red Hat 赞助的社区项目]{#community-sponsored .correct explanation="Fedora 由社区构建，并获得 Red Hat 的赞助与支持；它仍是一个独立的社区发行版。"}
:::

## 为什么 Fedora 脱颖而出

Fedora 之所以脱颖而出，是因为它往往比以企业为中心的发行版更早采用新的 Linux 特性。这使得它对开发者、开源贡献者以及希望拥有与上游紧密联系的最新系统的桌面用户非常有吸引力。

它还以提供纯净的默认体验而闻名。Fedora Workstation 在那些需要现代桌面、最新工具以及对容器、虚拟化和其他开发工作流良好支持的开发者中尤为受欢迎。

:::single-choice{#match-fedora-user}
哪种用户目标最适合 Fedora Workstation？

::option[让一个企业版本多年保持不变]{#long-enterprise-lifecycle explanation="长期而保守的企业生命周期更符合 RHEL 的定位；Fedora 的发布和升级节奏更快。"}
::option[在完善的桌面系统中使用较新的开发工具]{#current-developer-desktop .correct explanation="Fedora Workstation 把精心设计的桌面与较新的开发、容器和虚拟化工具结合起来，正好符合这一目标。"}
::option[从源代码手动构建每个系统组件]{#fedora-manual-source explanation="Fedora 提供完整的打包系统，不要求用户构建每个组件；该目标更像一种专门的工作方式。"}
:::

## Fedora 与 Red Hat

Fedora 在 Red Hat 生态系统中扮演着重要角色。新技术和变更通常会先在 Fedora 中出现，其中一些成果随后会影响 Red Hat Enterprise Linux (RHEL)。这种关系有助于解释为什么 Fedora 感觉更前沿，而 RHEL 则更保守且专注于企业级应用。

如果您想将 Fedora 与面向企业的选项进行比较，请参阅 [Red Hat Enterprise Linux](https://labex.io/zh/lesson/red-hat-enterprise-linux)。如果您仍在比较不同的发行版系列，[选择 Linux 发行版](https://labex.io/zh/lesson/choosing-a-linux-distribution) 提供了更广泛的概述。

:::single-choice{#explain-fedora-upstream-role}
Fedora 与 RHEL 的上游关系意味着什么？

::option[RHEL 版本会在发布后原样复制到 Fedora]{#rhel-copied-to-fedora explanation="这颠倒了二者的关系；Fedora 更新更快，是上游来源，而不是 RHEL 的后续副本。"}
::option[Fedora 与 RHEL 始终提供完全相同的软件版本]{#identical-software-versions explanation="两个发行版有不同的发布目标和日程；RHEL 会选择并稳定技术，而不会与每个 Fedora 版本完全一致。"}
::option[在 Fedora 中开发的成果以后可能影响 RHEL]{#fedora-influences-rhel .correct explanation="Fedora 会较早集成新技术，其中一些成果随后会进入 Red Hat 的企业平台。"}
:::

## Fedora 版本发布

Fedora 遵循定期的发布周期，大多数年份会有两个主要版本，每个版本提供约 13 个月的支持。与更保守的发行版相比，Fedora 倾向于以更快的节奏提供更新的内核、桌面环境和开发工具。

这使得 Fedora 非常适合那些既想要最新软件，又希望使用有组织的主流 Linux 发行版，而不是手动滚动更新系统的用户。

:::single-choice{#plan-fedora-upgrades}
根据 Fedora 的发布模式，用户应该安排哪项维护？

::option[在计算机整个寿命期间都不升级版本]{#no-version-upgrades explanation="Fedora 版本的支持期有限；要持续获得支持，需要逐步升级到较新版本。"}
::option[定期升级，以继续使用受支持的版本]{#regular-release-upgrades .correct explanation="Fedora 发布节奏较快，每个版本支持约 13 个月，因此用户应规划定期的版本升级。"}
::option[不区分系统版本，持续接收软件包变化]{#no-distinct-releases explanation="Fedora 会发布明确的主要版本，并非传统滚动发行版；软件较新，但版本边界仍然重要。"}
:::

## 软件包管理

Fedora 使用 RPM 软件包格式和 DNF 软件包管理器来安装、更新和卸载软件。DNF 是 Fedora 体验的核心部分，也是用户保持系统更新所依赖的主要工具之一。

Fedora 中的软件包管理非常直观，并且与更广泛的 Red Hat 系统家族自然契合。

:::single-choice{#identify-fedora-package-tool}
Fedora 使用哪个工具进行高级软件包管理？

::option[APT]{#fedora-apt-tool explanation="APT 与 Debian 系发行版相关；Fedora 属于 RPM 软件包家族，使用 DNF。"}
::option[DNF]{#fedora-dnf-tool .correct explanation="DNF 从 Fedora 仓库安装、更新和删除软件包，底层软件包采用 RPM 格式。"}
::option[Pacman]{#fedora-pacman-tool explanation="Pacman 是 Arch Linux 使用的软件包管理器；Fedora 的高级软件包工具是 DNF。"}
:::

## 常见用途

Fedora 常用于开发者工作站、技术桌面和笔记本电脑。对于那些需要现代 Linux 环境来进行编码、容器、虚拟机和日常桌面工作的用户来说，它特别有吸引力。

虽然 Fedora 也可用于服务器，但其最显著的定位通常是一个前沿的、对开发者友好的 Linux 发行版。

## Fedora 对初学者友好吗？

Fedora 可以对初学者友好，但它通常更适合那些习惯于节奏稍快系统的用户。它比高度依赖手动配置的发行版更容易上手，但可能感觉不如 Debian 保守，也不如 Ubuntu 或 Linux Mint 那样以初学者为中心。

对于那些想要现代 Linux 发行版且不介意在实践中学习的用户来说，Fedora 是一个强有力的选择。

## 延伸阅读

- [Fedora Workstation](https://fedoraproject.org/workstation/)
- [Fedora 文档](https://docs.fedoraproject.org/)
- [Fedora 版本生命周期](https://docs.fedoraproject.org/en-US/releases/lifecycle/)
- [Fedora Workstation 工作组](https://docs.fedoraproject.org/en-US/workstation-working-group/)

为了在了解 Fedora 后构建真正的 Linux 技能，我们推荐以下 LabEx 课程：

1. **[Linux 快速入门](https://labex.io/zh/courses/quick-start-with-linux)** - 涵盖适用于多种发行版的 Linux 基础知识。
2. **[Linux 命令在线练习](https://labex.io/zh/courses/linux-basic-commands-practice-online)** - 强化日常 Linux 工作中重要的命令行习惯。
3. **[RPM 和 DNF 软件包管理](https://labex.io/zh/courses/rpm-and-dnf-package-management)** - 练习与 RPM 和 DNF 相关的软件包管理概念。

## 总结

现在，您可以说明 Fedora 作为 Red Hat 生态中较新且由社区驱动的发行版所处的位置。

1. 描述 Fedora 的社区和赞助模式。
2. 识别 Fedora Workstation 支持的用户和工作流程。
3. 说明 Fedora 与 RHEL 的上游关系。
4. 为 Fedora 的定期版本升级做好规划。
5. 知道 DNF 是 Fedora 的软件包管理工具。
