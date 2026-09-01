---
lesson_id: "compile-source-code"
course_id: "packages"
lang: "zh"
order_index: 7
title: "编译源代码"
description: "学习如何验证、配置、构建、测试、暂存并跟踪从源代码编译的软件。"
meta_title: "编译源代码 - 软件包"
meta_description: "了解如何在 Linux 中从源代码编译。本指南涵盖使用 configure、make 和推荐的 checkinstall 命令构建源代码以进行干净软件包管理的基本步骤。"
meta_keywords: "如何从源代码编译，如何构建源代码，编译源代码，make install, checkinstall, Linux 编译，build-essential, configure 脚本，makefile, Linux 教程"
---

从源代码构建可以获得已配置仓库中没有的版本或功能，但这会把集成、更新和信任工作从发行版转移给你。如果受支持的发行版软件包能够满足需求，应优先使用它。

## 构建前验证并阅读

从经过身份验证的上游发布渠道获取源代码，通过受信任路径验证签名或校验和；然后先检查归档，再把它提取到非特权暂存目录。阅读 `README`、`INSTALL`、`SECURITY` 和项目构建文档等文件。

构建说明也是可执行代码。`configure` 脚本、构建定义、测试或编译器插件都可能以你的用户身份运行任意命令。不要构建不受信任的源代码，也不要用 `sudo` 运行构建本身。

:::single-choice{#compile-source-code-build-privilege} 为什么编译步骤通常不应该使用 `sudo`？

::option[编译器拒绝为 root 用户生成机器代码。]{#compile-source-code-root-compiler explanation="编译器可以由 root 运行，但这样做会不必要地增加风险。"}
::option[`sudo` 会自动删除所有生成的目标文件。]{#compile-source-code-sudo-delete explanation="提升权限本身不会移除构建输出。"}
::option[构建逻辑可以执行任意命令，而且通常不需要系统权限。]{#compile-source-code-unprivileged-build .correct explanation="保持非特权构建可以限制错误或恶意构建说明造成的损害。"}
:::

## 安装构建要求

在 Debian 家族开发系统上，常见起点是：

```bash
$ sudo apt install build-essential
```

这会安装一组基础编译器和构建工具，而不是每个项目所需的全部依赖。项目还可能需要语言运行时、生成器、构建系统工具、开发头文件或精确的库版本。应从受信任仓库安装要求，并区分构建依赖与运行时依赖。

:::single-choice{#compile-source-code-build-essential-scope} `build-essential` 在 Debian 家族系统上提供什么？

::option[一组常用的基础编译和构建工具。]{#compile-source-code-baseline-tools .correct explanation="它提供基础工具，但无法预知每个项目特有的库或生成器。"}
::option[每个源代码项目的所有依赖项。]{#compile-source-code-all-dependencies explanation="各项目还会声明额外的、有时带特定版本要求的依赖。"}
::option[下载的源代码一定可信的保证。]{#compile-source-code-trust-guarantee explanation="安装工具不会对另一份源代码发布进行身份验证。"}
:::

## 配置与构建

传统的 Autoconf 风格项目可能使用：

```bash
$ ./configure --prefix=/usr/local
$ make
```

`configure` 检查环境，并根据所选选项生成构建文件。`make` 读取通常位于 `Makefile` 中的依赖与命令规则，创建请求的目标。

这一顺序并不通用。项目可能使用 CMake、Meson、Ninja、语言专用工具或自定义脚本。应遵循准确版本的文档，不要仅仅因为熟悉就运行 `./configure`。如果构建系统支持，源代码树外的构建目录可以让生成文件保持分离。

:::single-choice{#compile-source-code-make-role} 在传统流程中，`make` 做什么？

::option[把每个输出注册到发行版软件包数据库。]{#compile-source-code-make-package-db explanation="仅编译不会创建原生软件包所有权记录。"}
::option[自动下载经过身份验证的源代码发布。]{#compile-source-code-make-download explanation="除非项目明确另有定义，源代码获取与验证发生在本地构建之前。"}
::option[执行构建描述中适用的规则。]{#compile-source-code-make-rules .correct explanation="Make 评估依赖项，并运行让选定目标达到最新状态所需的命令。"}
:::

## 安装前测试

运行项目文档指定的测试目标，例如：

```bash
$ make check
```

实际目标可能是 `test`、`check` 或一个独立命令。测试失败时应调查原因，而不是安装未经测试的输出。测试可能要求网络访问、服务、特殊硬件或隔离环境；执行前应像审查其他构建代码一样审查测试。

:::single-choice{#compile-source-code-test-failure} 文档指定的测试套件失败时，应该怎么做？

::option[立即以 root 身份运行相同安装。]{#compile-source-code-install-after-failure explanation="权限无法解决未知的正确性问题，反而会扩大后果。"}
::option[删除包管理器数据库以避免冲突。]{#compile-source-code-delete-database explanation="原生数据库与解决源代码测试失败无关，绝不能丢弃。"}
::option[安装构建前先调查失败原因。]{#compile-source-code-investigate-tests .correct explanation="测试失败可能揭示依赖不兼容、构建缺陷或环境假设。"}
:::

## 暂存并跟踪安装

`sudo make install` 可能直接把文件复制到系统前缀，却不记录到原生软件包数据库。卸载目标是可选的，可能并不完整；后续升级也可能覆盖文件或留下孤立文件。

应优先选择以下受控方法之一：

- 使用发行版打包工具构建正式原生软件包
- 在策略允许时安装到 `/usr/local` 等明确分离的前缀
- 使用 `DESTDIR` 等受支持机制把文件暂存到临时打包根目录
- 适当时使用非特权用户前缀、隔离环境或容器

`checkinstall` 可以为某些 `make install` 流程创建简单软件包，但并不通用，也无法替代经过审核的发行版质量打包配方。绝不能把它当作“始终使用”的规则。进行任何特权复制前，应检查暂存文件列表、所有权、权限、路径，以及卸载或升级计划。

:::single-choice{#compile-source-code-destdir-purpose} 受支持的 `DESTDIR` 暂存安装有什么用途？

::option[把预定安装文件放到临时根目录中，以供检查或打包。]{#compile-source-code-stage-root .correct explanation="暂存会把文件收集与立即写入活动系统前缀分开。"}
::option[把编译器变成远程软件包仓库。]{#compile-source-code-destdir-repository explanation="该变量重定向安装路径，不会发布仓库元数据。"}
::option[跳过编译，改为下载未知二进制文件。]{#compile-source-code-destdir-download explanation="暂存发生在构建后，并不替代外部二进制下载。"}
:::

可以在可丢弃环境中通过[在 Linux 中从源代码构建软件](https://labex.io/zh/labs/comptia-build-software-from-source-code-in-linux-590853)实验练习这一流程，避免把实验文件混入生产系统。

## 总结

现在，你可以把源代码构建作为受控的软件供应流程来处理。

1. 验证源代码身份，并把其说明当作可执行代码审查。
2. 从受信任仓库安装明确的构建要求。
3. 在没有不必要权限的情况下配置、构建和测试。
4. 写入系统前暂存并检查输出。
5. 使用原生打包或有意识选择的隔离前缀跟踪已安装文件。
