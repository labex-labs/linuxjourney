---
index: 1
lang: "zh"
title: "软件分发"
meta_title: "软件分发 - 软件包"
meta_description: "了解软件分发、包管理器以及 .deb 和 .rpm 等软件包格式，探索学习 Linux 的最佳途径。这是我们免费 Linux 认证课程的关键部分。"
meta_keywords: "linux 软件分发，包管理器，.deb, .rpm, 学习 linux 的最佳方式，免费 linux 认证课程，学习 linux 的最佳资源，学习 linux 命令行最佳方式，软件安装"
---

## Lesson Content

Linux 系统由许多软件组件构成，例如网页浏览器、文本编辑器和媒体播放器。这些组件被称为软件包（packages），通常由包管理器（package manager）管理，包管理器负责软件的安装、更新和删除。理解这个过程是学习 Linux 的基础。

### 什么是 Linux 软件包

您可能知道 Chrome 或 Firefox 这样的软件名称，但在技术层面上，它们是软件包。软件包本质上是一个文件存档，其中包含应用程序的可执行文件、配置文件和文档，所有这些都捆绑在一起。这种有组织的结构简化了软件管理。

### 软件供应链

软件软件包的旅程涉及两个关键角色：

- **上游提供者 (Upstream Providers)**：编写软件的开发者。他们编译源代码，创建安装说明，并发布新版本和更新。
- **软件包维护者 (Package Maintainers)**：当新版本准备好后，上游提供者会将软件发送给软件包维护者。这些维护者会审查、管理并将软件以针对特定 Linux 发行版的软件包形式分发给最终用户。

### 常见软件包格式

虽然您可以直接从源代码安装软件，但使用包管理器更为常见和高效。这是学习 Linux 命令进行系统管理的最有效方法之一。有两种主要的软件包格式：

- **Debian (.deb)**：由 Debian 及其衍生版（如 Ubuntu 和 Linux Mint）使用。
- **Red Hat Package Manager (.rpm)**：由 Red Hat Enterprise Linux (RHEL)、Fedora 和 CentOS 使用。

掌握管理这些软件包的工具是学习 Linux 命令行（command line）的最佳方式，也是您将持续使用的技能。这些工具是学习 Linux 系统管理资源中的佼佼者。

## Exercise

为了应用您的知识，我们推荐以下动手实验（labs）。它们提供了对本课所涵盖概念的实践经验。

1.  **[在 Linux 中使用 RPM 管理软件包](https://labex.io/zh/labs/rhel-managing-packages-with-rpm-in-linux-590868)** - 在基于 Red Hat 的系统上，获得查询软件包信息、验证完整性和检查 RPM 软件包内容的实践经验。
2.  **[在 Linux 中使用 YUM 查询和更新软件包](https://labex.io/zh/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - 学习使用 YUM 在基于 RHEL 的 Linux 系统上管理软件软件包，包括检查、更新和探索软件源。
3.  **[在 Linux 中从源代码构建软件](https://labex.io/zh/labs/comptia-build-software-from-source-code-in-linux-590853)** - 理解从源代码构建和安装软件的基本过程，这是对于无法通过包管理器获得的应用程序至关重要的技能。

这些实验将帮助您在真实场景中应用包管理和软件安装的概念，并增强您对 Linux 系统管理的信心。
