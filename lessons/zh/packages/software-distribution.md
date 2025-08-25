---
index: 1
lang: "zh"
title: "软件分发"
meta_title: "软件分发 - 软件包"
meta_description: "了解 Linux 软件分发、包管理器以及 .deb 和 .rpm 等包类型。理解如何在 Linux 系统上管理软件。"
meta_keywords: "Linux 软件分发，包管理器，.deb, .rpm, Linux 软件包，Linux 初学者，Linux 教程，软件安装"
---

## Lesson Content

您的系统由许多软件包组成，例如互联网浏览器、文本编辑器、媒体播放器等。这些软件包通过包管理器进行管理，包管理器负责在您的系统上安装和维护软件。然而，并非所有软件包都通过包管理器安装；您通常可以直接从源代码安装软件包（我们很快会讲到）。但是，大多数情况下，您将使用包管理器来安装软件。最常见的软件包类型是 Debian (.deb) 和 Red Hat (.rpm)。Debian 风格的软件包用于 Debian、Ubuntu、Linux Mint 等发行版。Red Hat 风格的软件包则出现在 Red Hat Enterprise Linux、Fedora、CentOS 等发行版中。

什么是软件包？您可能知道它们是 Chrome、Photoshop 等，它们确实是，但它们真正的本质是大量文件编译成一个整体。编写这些软件的人（有时是单个人）被称为 **上游提供商**；他们编译代码并编写如何安装它。这些上游提供商致力于发布新软件和更新现有软件。当他们准备好向世界发布时，他们会将软件包发送给 **软件包维护者**，由后者负责将此软件交付给用户。这些软件包维护者以软件包的形式审查、管理和分发这些软件。

## Exercise

熟能生巧！这里有一些动手实验，可以帮助您巩固对 Linux 包管理和软件安装的理解：

1. **[在 Linux 中使用 RPM 管理软件包](https://labex.io/zh/labs/rhel-managing-packages-with-rpm-in-linux-590868)** - 获得在基于 Red Hat 的系统上查询软件包信息、验证完整性以及检查 RPM 软件包内容的实践经验。
2. **[在 Linux 中使用 YUM 查询和更新软件包](https://labex.io/zh/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - 学习使用 YUM 在基于 RHEL 的 Linux 系统上管理软件包，包括检查、更新和探索存储库。
3. **[在 Linux 中从源代码构建软件](https://labex.io/zh/labs/comptia-build-software-from-source-code-in-linux-590853)** - 了解从源代码构建和安装软件的基本过程，这是对于无法通过包管理器获取的应用程序来说至关重要的技能。

这些实验将帮助您在实际场景中应用包管理和软件安装的概念，并增强您在 Linux 系统管理方面的信心。

## Quiz Question

没有问题，继续！

## Quiz Answer
