---
lesson_id: "ubuntu"
course_id: "getting-started"
lang: "zh"
order_index: 5
title: "Ubuntu"
description: "了解 Ubuntu 如何在 Debian 基础上提供易用的桌面、服务器和版本选择。"
meta_title: "Ubuntu Linux 操作系统"
meta_description: "了解什么是 Ubuntu Linux，为什么 Ubuntu 如此受欢迎，以及它的发布模式、软件包管理机制，及其在桌面、笔记本电脑和服务器上的广泛应用。"
meta_keywords: "ubuntu linux, ubuntu 发行版，什么是 ubuntu, ubuntu 版本发布，ubuntu 软件包管理，基于 debian 的 ubuntu, linux 发行版"
---

## 什么是 Ubuntu？

Ubuntu 是最广泛使用的 Linux 发行版之一。它由 Canonical 公司开发，基于 Debian 构建，以其易用的设计、庞大的用户社区以及广泛的硬件和软件支持而闻名。

对于那些希望学习 Linux 但又不想从手动配置或高级设置开始的人来说，Ubuntu 已成为一个常见的起点。它被应用于个人电脑、开发系统、云平台和服务器，其覆盖范围是其他发行版难以企及的。

:::single-choice{#identify-ubuntu-base} 哪个发行版为 Ubuntu 提供了基础？

::option[Debian 发行版]{#debian-base .correct explanation="Ubuntu 基于 Debian 构建，并继承了 Debian 的许多软件包管理方式；在此基础上，Ubuntu 又加入自己的版本、默认设置和支持模式。"}
::option[Fedora 发行版]{#ubuntu-fedora-base explanation="Fedora 属于 Red Hat 生态系统，并不是 Ubuntu 的基础；Ubuntu 属于 Debian 家族。"}
::option[Arch 发行版]{#ubuntu-arch-base explanation="Arch Linux 是具有独立软件包系统和发布方式的另一发行版；Ubuntu 基于 Debian。"}
:::

## 为什么 Ubuntu 如此受欢迎

Ubuntu 之所以受欢迎，是因为它致力于让 Linux 在日常使用中变得实用。它提供了完善的安装程序、强大的文档、可预测的发布周期，以及庞大的教程和第三方支持生态系统。对于许多用户而言，这些组合使 Ubuntu 成为最容易上手的 Linux 发行版之一。

Ubuntu 备受瞩目的另一个原因是它适用于多种环境。你可以在笔记本电脑、台式机、虚拟机、服务器以及各种云平台上看到它的身影。这种广泛的采用巩固了它作为通用 Linux 发行版的声誉。

:::single-choice{#recognize-beginner-support} Ubuntu 的哪项特性最能直接帮助初学者解决问题？

::option[每个安装的程序都必须手动编译]{#manual-compilation explanation="Ubuntu 通常提供打包好的软件，不要求手动编译每个程序；额外的构建工作并不会让故障排查更简单。"}
::option[丰富的文档和庞大的用户社区]{#documentation-community .correct explanation="文档和社区讨论为初学者提供了许多查找解释和排障帮助的渠道，从而降低了学习门槛。"}
::option[只有资深管理员才能获得的有限指导]{#limited-guidance explanation="Ubuntu 的知名度部分来自面向不同水平用户的丰富资料；把帮助限制给专家会削弱其初学者友好性。"}
:::

## Ubuntu 与 Debian

Ubuntu 是一个基于 Debian 的发行版，这意味着它继承了 Debian 的大部分软件包管理模型和软件打包方式。如果你学会了如何在 Ubuntu 中使用 `apt`，这些知识也将帮助你理解其他基于 Debian 的系统。

同时，Ubuntu 不仅仅是“带有桌面的 Debian”。它拥有自己的发布计划、默认设置、支持模型和生态系统。如果你想将其与其他选项进行比较，请参阅 [选择 Linux 发行版](https://labex.io/zh/lesson/choosing-a-linux-distribution) 或了解更多关于 [Debian](https://labex.io/zh/lesson/debian) 的信息。

## Ubuntu 发布版本

Ubuntu 使用两种主要的发布类型。它每六个月发布一个新版本，每两年会有一个版本成为长期支持（LTS）版本。LTS 版本通常是需要更稳定基础的台式机、工作站和服务器的首选。

这种发布模式有助于解释 Ubuntu 的吸引力。想要可靠基础的用户通常会选择 LTS，而想要新功能的用户则可以使用更新频率更快的过渡版本。

:::single-choice{#choose-ubuntu-lts} 如果系统需要寿命较长且可预测的基础，哪类 Ubuntu 版本最合适？

::option[过渡版本]{#interim-release explanation="过渡版本发布得更频繁，能更早提供新功能，但较短的支持期并不符合这里的需求。"}
::option[LTS 版本]{#lts-release .correct explanation="LTS 版本旨在提供较长期的支持，通常用于优先考虑可靠基础的系统。"}
::option[软件包更新]{#package-update explanation="软件包更新会改变已安装版本中的软件，并不是 Ubuntu 的两类操作系统版本之一。"}
:::

## 软件包管理

作为基于 Debian 的系统，Ubuntu 使用 `.deb` 软件包格式和 `apt` 软件包管理器来安装、更新和删除软件。这使用户能够访问庞大的软件生态系统，并获得熟悉的命令行工作流程。

软件包管理是 Ubuntu 的实用优势之一，因为它将成熟的 Debian 工具与广泛且文档齐全的软件环境结合在了一起。

:::single-choice{#identify-ubuntu-package-tool} 在 Ubuntu 上安装软件时使用的软件包管理工具是哪一项？

::option[`.deb`]{#deb-format explanation="`.deb` 表示 Debian 系系统使用的软件包格式，而不是命令行软件包管理工具。"}
::option[`LTS`]{#lts-label explanation="LTS 表示长期支持版本，并不负责安装或管理软件包。"}
::option[`apt`]{#ubuntu-apt-tool .correct explanation="Ubuntu 使用 `apt` 安装、更新和删除软件包；该工具管理以 Debian `.deb` 格式打包的软件。"}
:::

## 桌面与服务器使用

Ubuntu 同时用于桌面和服务器系统。在桌面端，它以完善的基于 GNOME 的体验和相对平易近人的默认设置而闻名。在服务器端，它被广泛部署在开发、Web 基础设施和云环境中。

这种广泛的适用性使得 Ubuntu 对那些希望拥有一种既能从笔记本电脑学习入门，又能运行生产工作负载的 Linux 发行版的用户极具吸引力。

## 为什么初学者选择 Ubuntu

Ubuntu 常被推荐给初学者，因为它比许多其他 Linux 发行版更容易安装和排查故障。庞大的用户群意味着当出现问题时，有大量的教程、论坛帖子和指南可供参考。

对于那些既想要对初学者友好，又不愿放弃长期灵活性的用户来说，Ubuntu 仍然是最稳妥的起点之一。

## 延伸阅读

- [Ubuntu Desktop](https://ubuntu.com/desktop)
- [Ubuntu Server](https://ubuntu.com/server)
- [Ubuntu 发布周期](https://ubuntu.com/releaseendoflife)
- [Ubuntu 发布文档](https://documentation.ubuntu.com/project/release-team/ubuntu-releases/)

为了在完成 Ubuntu 介绍后继续学习，我们推荐以下 LabEx 课程：

1. **[Linux 快速入门](https://labex.io/zh/courses/quick-start-with-linux)** - 通过引导式动手实践建立 Linux 基础和命令行技能。
2. **[Linux 新手教程](https://labex.io/zh/courses/linux-for-noobs)** - 遵循对初学者友好的路径，逐步理解 Linux 基础。
3. **[成为初级系统管理员](https://labex.io/zh/courses/become-a-junior-system-administrator)** - 在掌握基础知识后，继续学习实用的 Linux 系统管理技能。

## 总结

现在，你可以说明 Ubuntu 如何以 Debian 为基础，同时提供自己的版本和用户体验。

1. 知道 Debian 是 Ubuntu 的基础。
2. 识别能帮助初学者的支持条件。
3. 比较 Ubuntu 的 LTS 版本和过渡版本。
4. 使用 `apt` 作为 Ubuntu 的软件包管理工具。
