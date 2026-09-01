---
lesson_id: "software-distribution"
course_id: "packages"
lang: "zh"
order_index: 1
title: "软件发行"
description: "了解上游项目、发行版维护者、软件包和软件包格式如何构成 Linux 软件供应链。"
meta_title: "软件发行 - 软件包"
meta_description: "通过了解软件发行、包管理器以及 .deb 和 .rpm 等包格式，探索学习 Linux 的最佳途径。这是我们免费 Linux 认证课程的关键部分。"
meta_keywords: "linux 软件发行，包管理器，.deb, .rpm, 学习 linux 的最佳方式，免费 linux 认证课程，学习 linux 的最佳资源，学习 linux 命令行最佳方式，软件安装"
---

Linux 软件通常以软件包形式交付，并由发行版特有的工具管理。软件包把可安装文件与元数据组合起来，使系统能够跟踪版本、依赖关系、所有权、校验和及生命周期操作。

## 软件包包含什么

二进制软件包可以包含可执行文件、库、文档、默认配置、服务定义和其他资源，还会携带以下元数据：

- 软件包名称和版本
- 目标架构和发行版环境
- 声明的依赖项与冲突
- 文件列表和完整性信息
- 生命周期操作期间使用的可选脚本或触发器

并非每个软件包都是交互式应用程序。软件包也可以提供库、内核组件、语言数据、字体、调试符号，或依赖其他一组软件包的元数据。

:::single-choice{#software-distribution-package-metadata} 哪项信息通常属于软件包元数据，而不是应用程序可执行文件？

::option[实现应用程序的 CPU 指令。]{#software-distribution-executable-code explanation="编译后的指令属于软件包载荷内容，而不是依赖元数据。"}
::option[声明的依赖关系。]{#software-distribution-dependencies .correct explanation="软件包描述必需或冲突的软件包，使管理工具能够推理安装方案。"}
::option[用户当前在内存中打开且尚未保存的文档。]{#software-distribution-user-document explanation="运行时用户数据不属于发行软件包的元数据。"}
:::

## 上游与发行版的角色

上游项目开发并发布原始源代码。Linux 发行版维护者再把选定版本适配到该发行版。工作可能包括审核许可证、应用集成或安全补丁、定义构建说明、拆分输出软件包、声明依赖项、运行测试和维护更新。

发行版构建基础设施会为受支持的版本和架构生成软件包。仓库工具发布客户端可以验证的元数据和签名。具体职责有所不同：某些上游项目自行发布软件包，而发行版也可能独立从源代码构建。

:::single-choice{#software-distribution-maintainer-role} 哪项任务通常属于发行版软件包维护者？

::option[把上游源代码适配到发行版的构建和依赖规则。]{#software-distribution-maintainer-integrates .correct explanation="维护者使软件符合发行版策略、构建、依赖和受支持环境。"}
::option[选择每个用户的本地账户密码。]{#software-distribution-maintainer-passwords explanation="本地身份验证数据与软件包维护无关。"}
::option[把每个已安装进程调度到 CPU 上。]{#software-distribution-maintainer-scheduler explanation="安装后由运行中的内核调度器负责 CPU 执行。"}
:::

## 常见原生软件包格式

两种广泛使用的原生格式是：

- `.deb`：Debian 及其衍生发行版使用，包括 Ubuntu 和 Linux Mint
- `.rpm`：Fedora、Red Hat Enterprise Linux 和许多相关发行版使用

此外还存在其他原生和跨发行版格式。仅有匹配的文件扩展名并不能保证兼容性；还要考虑软件包架构、发行版版本、库版本、策略、签名和依赖项。

:::single-choice{#software-distribution-debian-format} Debian 和 Ubuntu 使用哪种原生软件包格式？

::option[`.deb`]{#software-distribution-format-deb .correct explanation="Debian 家族的软件包工具使用 `.deb` 归档格式。"}
::option[`.rpm`]{#software-distribution-format-rpm explanation="RPM 是 Fedora、RHEL 和相关发行版家族的原生格式。"}
::option[`.tar`]{#software-distribution-format-tar explanation="Tar 是通用归档容器，本身不提供 Debian 软件包元数据和生命周期语义。"}
:::

## 受管理发行的重要性

包管理器会记录已安装状态，并协调跨软件包变更。从受信任的发行版仓库安装，通常能获得一致的依赖解析、签名验证、安全更新和干净卸载。手动复制二进制文件或从源代码安装有时也合适，但不会自动进入这一受管理生命周期。

信任仍取决于仓库配置和签名密钥。加密签名有效只能证明软件包与受信任密钥关联，并不能证明任意第三方软件一定安全或适合当前系统。应尽可能优先使用发行版仓库，并在授予安装权限前评估任何外部来源。

:::single-choice{#software-distribution-package-manager-benefit} 通过受信任软件包仓库安装有什么优势？

::option[管理器可以跟踪版本并解析声明的依赖项。]{#software-distribution-managed-lifecycle .correct explanation="仓库元数据和已安装状态记录支持协调安装、更新和卸载。"}
::option[每个已安装程序都会免疫所有安全漏洞。]{#software-distribution-no-vulnerabilities explanation="软件包管理支持更新，但无法保证软件没有缺陷。"}
::option[所有发行版的软件包都会变得可以互换。]{#software-distribution-universal-compatibility explanation="原生软件包仍受格式、发行版版本、架构和依赖环境约束。"}
:::

可以通过[在 Linux 中使用 RPM 管理软件包](https://labex.io/zh/labs/rhel-managing-packages-with-rpm-in-linux-590868)实验检查软件包元数据和完整性，或通过[在 Linux 中从源代码构建软件](https://labex.io/zh/labs/comptia-build-software-from-source-code-in-linux-590853)实验比较源代码流程与受管理软件包。

## 总结

现在，你可以识别 Linux 软件发行的主要组成部分。

1. 区分软件包载荷文件与软件包元数据。
2. 区分上游开发与发行版集成。
3. 把 `.deb` 和 `.rpm` 与相应的发行版家族联系起来。
4. 评估兼容性与信任时，不能只看文件扩展名。
