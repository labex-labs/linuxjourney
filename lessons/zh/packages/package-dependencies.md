---
lesson_id: "package-dependencies"
course_id: "packages"
lang: "zh"
order_index: 4
title: "软件包依赖关系"
description: "了解软件包元数据如何表达所需能力、版本、冲突和共享库关系。"
meta_title: "软件包依赖关系 - 软件包"
meta_description: "了解 Linux 软件包依赖项及其对软件安装至关重要的原因。本指南解释共享库以及软件包管理如何处理依赖项以防止软件损坏。"
meta_keywords: "Linux 软件包依赖项，共享库，Linux 软件包，软件包管理，Linux 软件安装，Linux 教程，Linux 入门，Linux 指南"
---

软件包依赖关系表示一个软件包在安装或运行时需要另一个软件包、某项能力或兼容版本。能够访问仓库的包管理器会使用这些元数据计算一组一致的变更，而不是孤立处理每个归档。

## 依赖关系

软件包元数据可以表达比单个必需名称更丰富的关系。根据发行版格式不同，其中可能包括：

- 必需依赖项
- 最低、最高或精确版本限制
- 备选项，即多个提供者中的任意一个可以满足要求
- 语义较弱的推荐或建议
- 冲突、破坏或替代关系
- 由多个软件包提供的虚拟能力

这些规则让求解器能够从已配置仓库、架构和已安装状态中选择一组兼容的软件包版本。一个方案可能需要升级、移除软件包或在提供者之间作出选择，因此批准前应检查建议的事务。

:::single-choice{#package-dependencies-solver-role} 能够访问仓库的依赖求解器会尝试生成什么？

::option[一组一致的软件包版本和必要变更。]{#package-dependencies-consistent-set .correct explanation="求解器会评估已安装和可用软件包之间声明的关系。"}
::option[为每个已安装应用程序创建一个新用户账户。]{#package-dependencies-user-account explanation="创建账户可能是软件包生命周期操作，但不是依赖解析的目的。"}
::option[仓库中每个文件的压缩副本。]{#package-dependencies-compressed-repository explanation="求解器选择元数据和软件包，不会归档整个仓库。"}
:::

## 作为依赖项的共享库

共享库包含可由多个程序在运行时映射的已编译代码。共享机制减少了重复实现，也让发行版能够独立更新通用库，但程序依赖兼容的应用程序二进制接口（ABI）。

在基于 ELF 的 Linux 系统上，可执行文件可以记录所需的库名称，例如 SONAME。程序启动时，动态链接器会查找匹配的已安装库。软件包元数据通常把这一要求表示为对提供兼容库的软件包或能力的依赖。

:::single-choice{#package-dependencies-shared-library} 什么是共享库？

::option[多个程序可以加载并使用的已编译代码。]{#package-dependencies-library-code .correct explanation="共享库提供可复用的二进制接口，无需在每个程序中嵌入独立实现。"}
::option[不相关发行版共同使用的仓库列表。]{#package-dependencies-shared-repository explanation="仓库配置与可执行库代码是不同概念。"}
::option[包含每个用户 shell 历史的文本文件。]{#package-dependencies-shared-history explanation="Shell 历史属于用户数据，不是程序库依赖。"}
:::

## 版本与 ABI 兼容性

只存在名称相似的库文件并不够。所需 ABI、架构、符号以及有时要求的最低版本必须匹配。即使文件名看起来正确，手动替换发行版库也可能破坏所有依赖它的程序。

软件包维护者会编码库关系，并在 ABI 变化时协调过渡。应让原生库继续受包管理器控制；需要冲突版本的软件应使用受支持的并行安装、容器、环境或构建机制。

:::single-choice{#package-dependencies-filename-insufficient} 存在名称相似的库文件时，程序为什么仍可能失败？

::option[Linux 只允许一个可执行文件使用每个库。]{#package-dependencies-one-consumer explanation="共享库的核心用途之一就是供多个进程和程序使用。"}
::option[软件包依赖只在系统第一次启动前有效。]{#package-dependencies-boot-only explanation="依赖关系在安装、升级和运行期间始终相关。"}
::option[库的 ABI 或架构可能不满足程序要求。]{#package-dependencies-abi-mismatch .correct explanation="运行时链接依赖兼容的二进制接口和机器架构，而不只是文件名。"}
:::

## 损坏的依赖状态

混用仓库、操作中断、手动安装归档、版本保持、文件被移除或第三方软件不兼容，都可能造成依赖问题。不要通过删除软件包数据库文件或盲目强制安装来处理。

应先阅读包管理器诊断信息，只刷新受信任的仓库元数据，检查被保持或固定的版本，并审查建议的修复。低层软件包安装器可以解包归档，却不一定获取所有依赖项；普通安装通常使用高层仓库工具更安全，因为它会解析完整事务。

:::single-choice{#package-dependencies-low-level-limit} 使用低层归档工具安装一个本地软件包时，常见限制是什么？

::option[它可能不会获取并求解所有缺失的仓库依赖项。]{#package-dependencies-no-repository-resolution .correct explanation="低层工具管理软件包归档和数据库，但可能把依赖获取留给高层管理器。"}
::option[它总会从源代码重新编译 Linux 内核。]{#package-dependencies-recompile-kernel explanation="安装软件包归档本身不会重新构建内核。"}
::option[它会阻止软件包包含任何共享库。]{#package-dependencies-no-libraries explanation="无论使用何种工具安装，软件包归档都可以包含库。"}
:::

可以先在[在 Linux 中管理共享库](https://labex.io/zh/labs/comptia-manage-shared-libraries-in-linux-590867)实验中检查运行时关系，再通过[在 Linux 中使用 RPM 管理软件包](https://labex.io/zh/labs/rhel-managing-packages-with-rpm-in-linux-590868)实验把它们与软件包元数据进行比较。

## 总结

现在，你可以解释软件包依赖解析的工作方式。

1. 识别必需、备选、带版本和冲突关系。
2. 把共享库软件包与运行时 ABI 要求联系起来。
3. 与架构和接口兼容性相比，文件名只是较弱的证据。
4. 应用修复前，检查完整的包管理器事务。
