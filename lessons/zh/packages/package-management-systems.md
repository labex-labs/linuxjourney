---
lesson_id: "package-management-systems"
course_id: "packages"
lang: "zh"
order_index: 6
title: "yum 与 apt"
description: "了解能够访问仓库的 APT 和 DNF 如何检查、安装、移除与升级软件包。"
meta_title: "yum 与 apt - 软件包"
meta_description: "探索 yum 与 apt 之间的关键区别。本指南涵盖如何在基于 RPM 和 Debian 的 Linux 系统上使用 yum 和 apt 安装、删除和更新软件包。"
meta_keywords: "yum vs apt, yum apt, Linux 软件包管理，apt, yum, Debian, Red Hat, 安装软件包，更新软件包，Linux 命令"
---

能够访问仓库的包管理器会获取元数据、求解依赖项、验证经过身份验证的内容，并协调事务。Debian 家族系统通常使用 APT。当前 Fedora 和 Red Hat Enterprise Linux 使用 DNF；在当前 RHEL 上，`yum` 命令作为 DNF 的兼容别名保留，旧系统则使用原始 YUM 实现。

应始终遵循已安装发行版和版本的文档，不要假定一套命令适用于所有环境。

## 刷新并检查元数据

APT 把元数据刷新与软件包升级分开：

```bash
Debian family: $ sudo apt update
```

安装前先搜索并检查：

```bash
Debian family: $ apt search package-name
Debian family: $ apt show package-name
RPM family:    $ dnf search package-name
RPM family:    $ dnf info package-name
```

仓库配置决定这些命令能发现什么。应仔细阅读来源名称、架构、版本和签名错误。

:::single-choice{#package-management-systems-apt-show}
哪个命令显示 `package-name` 的 APT 软件包详情？

::option[`apt remove package-name`]{#package-management-systems-apt-remove-command explanation="`remove` 子命令会建议卸载该软件包。"}
::option[`dnf search package-name`]{#package-management-systems-dnf-search-command explanation="该命令搜索 RPM 家族仓库，不是 APT 详情命令。"}
::option[`apt show package-name`]{#package-management-systems-apt-show-command .correct explanation="`show` 子命令呈现指定二进制软件包的元数据。"}
:::

## 安装软件包

使用仓库软件包名称安装：

```bash
Debian family: $ sudo apt install package-name
RPM family:    $ sudo dnf install package-name
```

管理器会建议依赖项，以及任何冲突或替代关系。在检查软件包来源、版本、架构、下载大小、磁盘变更、移除项和新增依赖项之前，不要自动确认。

:::single-choice{#package-management-systems-dnf-install}
当前哪个命令从已配置 RPM 家族仓库安装 `package-name`？

::option[`rpm -qa package-name`]{#package-management-systems-rpm-query-command explanation="这是 RPM 已安装数据库查询，不是仓库安装请求。"}
::option[`dnf install package-name`]{#package-management-systems-dnf-install-command .correct explanation="DNF 是 Fedora 和较新 RHEL 版本当前使用的仓库感知管理器。"}
::option[`apt update package-name`]{#package-management-systems-apt-update-package explanation="APT update 刷新索引，不会安装指定的 RPM 家族软件包。"}
:::

## 移除软件包

使用以下命令请求移除：

```bash
Debian family: $ sudo apt remove package-name
RPM family:    $ sudo dnf remove package-name
```

移除可能影响依赖软件包，或留下不再使用的依赖项和配置。应审查建议的事务；在 Debian 家族系统上区分 remove 与 purge 语义，并按照应用自己的备份和保留流程保存数据。移除软件包并不承诺删除用户创建的数据。

:::single-choice{#package-management-systems-remove-review}
为什么确认前应该审查移除事务？

::option[移除总会格式化软件包所在文件系统。]{#package-management-systems-removal-format explanation="包管理器移除受管文件和状态，通常不会格式化文件系统。"}
::option[包管理器无法显示建议的变更集合。]{#package-management-systems-no-proposal explanation="交互式管理器通常会显示计划事务，目的正是供用户审查。"}
::option[其他软件包可能依赖选中的软件包，并因此受到影响。]{#package-management-systems-dependent-removal .correct explanation="依赖约束可能让请求影响最初输入的一个软件包名称之外的内容。"}
:::

## 应用更新

在 APT 系统上，元数据刷新与升级应作为两个独立的成功步骤执行和审查：

```bash
$ sudo apt update
$ apt list --upgradable
$ sudo apt upgrade
```

在 DNF 系统上，使用本地文档规定的流程检查并应用可用更新：

```bash
$ dnf check-update
$ sudo dnf upgrade
```

更新命令可能改变核心库、服务、内核和依赖项。应根据系统使用备份、维护策略、发行说明和重启规划。还要检查命令退出语义；例如，某些“检查更新”操作会用非零状态表示存在可用更新，而不是执行失败。

:::single-choice{#package-management-systems-apt-update-upgrade}
`apt update` 与 `apt upgrade` 有什么关系？

::option[`update` 移除软件包，`upgrade` 恢复其配置文件。]{#package-management-systems-apt-remove-restore explanation="这两个命令不存在这种移除和恢复关系。"}
::option[`update` 刷新元数据，`upgrade` 应用获批准的软件包升级计划。]{#package-management-systems-apt-two-steps .correct explanation="APT 把目录刷新与安装较新软件包版本分成两个阶段。"}
::option[它们是同一操作的两个名称。]{#package-management-systems-apt-identical explanation="它们执行不同阶段，应该分别检查。"}
:::

## 选择 `dnf` 还是 `yum`

当前 Fedora 和 RHEL 文档应使用 `dnf`。较新 RHEL 系统中的 `yum` 命令可能调用 DNF 兼容行为，但脚本不能仅根据可执行文件名称推断实现。在旧主机上翻译命令说明前，应核实已安装版本和受支持语法。

:::single-choice{#package-management-systems-yum-current-rhel}
在当前 RHEL 系统上，`yum` 通常表示什么？

::option[由 DNF 支持的兼容命令。]{#package-management-systems-yum-dnf-alias .correct explanation="较新 RHEL 版本使用 DNF，同时保留 yum 命令名称以提供兼容性。"}
::option[Debian 的低层 `.deb` 归档工具。]{#package-management-systems-yum-dpkg explanation="Debian 系统使用 APT 和 dpkg 等工具，而不是 YUM 管理原生软件包。"}
::option[只用于仓库元数据的压缩器。]{#package-management-systems-yum-compressor explanation="YUM 和 DNF 是包管理接口，并不是独立压缩格式。"}
:::

可以通过[安装和删除软件包](https://labex.io/zh/labs/linux-installing-and-removing-packages-385380)实验练习 APT，并通过[使用 YUM 查询和更新软件包](https://labex.io/zh/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)实验学习 DNF/YUM 家族概念。

## 总结

现在，你可以选择并审查常见的软件包仓库操作。

1. Debian 家族系统使用 APT，当前 RPM 家族系统使用 DNF。
2. 安装前检查元数据和建议的依赖变更。
3. 将移除视为依赖感知事务，而不是删除单个文件。
4. 对于分阶段操作的工具，应区分元数据刷新和升级应用。
5. 核实 `yum` 是旧版 YUM 还是 DNF 兼容命令。
