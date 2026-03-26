---
index: 8
lang: "zh"
title: "Gentoo"
meta_title: "Gentoo Linux 发行版"
meta_description: "了解 Gentoo Linux 发行版、Portage 包管理器的运作方式，以及为何 Gentoo 能够吸引追求基于源代码定制与控制的高级用户。"
meta_keywords: "Gentoo 发行版，Gentoo Linux 发行版，什么是 Gentoo, Portage 包管理器，Gentoo 基于源代码，高级 Linux 发行版"
---

## Lesson Content

### 什么是 Gentoo？

Gentoo 是一个专为希望深度掌控系统构建方式的用户而设计的 Linux 发行版。与大多数主流发行版不同，Gentoo 以其基于源代码的特性而闻名，软件通常在本地机器上编译，而不是简单地安装预构建的二进制文件。

这种设计使得 Gentoo 对那些喜欢深入调整、学习和定制系统的进阶用户特别有吸引力。

### 为什么 Gentoo 与众不同

Gentoo 的独特之处在于它将定制化视为发行版的核心部分，而非附加功能。用户可以对可选功能、依赖项和构建行为做出详细选择，这是大多数 Linux 发行版无法直接提供的。

这使得 Gentoo 功能强大，但也意味着它对用户有更高的要求。它并非旨在成为进入 Linux 世界的最简单途径。

### Portage

Gentoo 的核心是其软件包管理系统 **Portage**。Portage 负责软件的安装和维护，并与 Gentoo 基于源代码的设计紧密相连。

Portage 最显著的特性之一是使用 **USE 标志 (USE flags)**，它允许用户在构建软件之前启用或禁用可选功能。这赋予了用户对最终系统极高水平的控制权。

### 基于源代码的定制

由于软件通常在本地构建，Gentoo 可以根据特定需求和偏好进行精细调整。那些希望剔除不必要功能或针对特定工作流程进行优化的用户通常会发现这一点特别有吸引力。

这种基于源代码的模式也使 Gentoo 成为一个具有教育意义的发行版。与许多主流发行版相比，它能让用户更深入地了解依赖关系、编译过程和系统设计。

### 性能与控制

Gentoo 常与性能和效率联系在一起，但其更大的优势在于控制力。能够从细节层面塑造系统，通常比单纯追求微小的性能提升更为重要。

对于重视这种控制水平的用户来说，Gentoo 可以带来极大的成就感。

### 谁应该使用 Gentoo？

Gentoo 最适合那些喜欢详细配置、不介意在设置和维护上花费更多时间的进阶用户和专注的学习者。如果您想要一个更温和的起点，[Ubuntu](https://labex.io/zh/lesson/ubuntu) 或 [Linux Mint](https://labex.io/zh/lesson/linux-mint) 等发行版通常更容易上手。如果您想要一个动手实践性强但编译工作较少的发行版，[Arch Linux](https://labex.io/zh/lesson/arch-linux) 可能更适合您。

### 延伸阅读

- [Gentoo](https://www.gentoo.org/)
- [Gentoo 手册](https://wiki.gentoo.org/wiki/Handbook:Main_Page)
- [Portage](https://wiki.gentoo.org/wiki/Portage)
- [USE 标志](https://wiki.gentoo.org/wiki/USE_flag)

## Exercise

为了准备 Gentoo 通常涉及的更深入的技术工作，我们推荐以下 LabEx 课程：

1. **[Linux 命令在线练习](https://labex.io/zh/courses/linux-basic-commands-practice-online)** - 加强在动手实践的 Linux 环境中至关重要的命令行习惯。
2. **[Shell 脚本基础](https://labex.io/zh/courses/shell-scripting-fundamentals)** - 通过 Shell 自动化实现对环境的更多控制。
3. **[成为初级系统管理员](https://labex.io/zh/courses/become-a-junior-system-administrator)** - 建立更广泛的 Linux 基础，这有助于使用像 Gentoo 这样的进阶发行版。

## Quiz Question

Gentoo 使用什么软件包管理系统？（您的回答应为英文，并注意大小写。）

## Quiz Answer

Portage
