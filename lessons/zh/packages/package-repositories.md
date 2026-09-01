---
lesson_id: "package-repositories"
course_id: "packages"
lang: "zh"
order_index: 2
title: "软件包仓库"
description: "了解仓库如何发布已签名的软件包索引，以及 APT 如何发现已配置的 Debian 家族软件源。"
meta_title: "软件包仓库 - 软件包"
meta_description: "探索 Linux 软件包仓库及其在包管理中的作用。了解系统如何使用 /etc/apt/sources.list 文件等来源来查找和安装 Linux 软件包。"
meta_keywords: "Linux 软件包仓库，apt 软件源列表，/etc/apt/sources.list, Linux 软件包，Linux 入门，Linux 教程，包管理"
---

软件包仓库会同时发布软件包、索引和发行元数据。包管理器下载索引，选择与已配置发行版和架构兼容的版本，验证仓库身份，再获取所需软件包文件。

## 仓库元数据与本地目录

仓库不只是一个归档文件目录。其元数据描述可用软件包名称、版本、架构、校验和、依赖项和仓库分区。客户端缓存一份本地目录，这样无需先下载每个归档，就能搜索和解析软件包。

在 Debian 家族系统上，使用以下命令刷新已配置的元数据：

```bash
$ sudo apt update
```

该命令更新本地软件包索引，本身不会安装所有可用升级。应检查报告的软件源和身份验证错误，而不能忽略失败条目。

:::single-choice{#package-repositories-apt-update} `apt update` 主要刷新什么？

::option[无需确认就更新每个已安装软件包的二进制文件。]{#package-repositories-all-binaries explanation="安装升级与刷新元数据是不同操作。"}
::option[允许安装软件包的用户密码。]{#package-repositories-user-passwords explanation="刷新仓库索引不会修改本地身份验证凭据。"}
::option[描述已配置来源中可用软件包的本地索引。]{#package-repositories-local-indexes .correct explanation="APT 下载当前仓库元数据，使后续搜索和依赖解析使用更新后的目录。"}
:::

## APT 软件源配置

APT 会从以下两个位置读取已配置来源：

- `/etc/apt/sources.list`
- `/etc/apt/sources.list.d/` 下以 `.list` 或 `.sources` 结尾的文件

`.list` 扩展名使用传统单行格式；`.sources` 扩展名使用 deb822 风格的段落，当前 APT 文档建议新配置使用后者。发行版可以把默认来源放在任一位置，因此 `/etc/apt/sources.list` 不一定包含完整或主要配置。

Deb822 风格的软件源可能如下：

```text
Types: deb
URIs: https://deb.example.invalid/repository
Suites: stable
Components: main
Signed-By: /etc/apt/keyrings/example.gpg
```

这只是语法示例；保留的 `.invalid` 域名不是可用仓库。

:::single-choice{#package-repositories-apt-locations} APT 可以从哪里读取活动仓库定义？

::option[只能从 `/etc/apt/sources.list` 读取。]{#package-repositories-only-main-list explanation="APT 还会读取 `/etc/apt/sources.list.d/` 下受支持的源文件。"}
::option[只能从每个用户家目录内的文件读取。]{#package-repositories-only-home explanation="系统 APT 软件源配置通常位于 `/etc/apt` 下。"}
::option[从 `/etc/apt/sources.list` 和 `/etc/apt/sources.list.d/` 中受支持的文件读取。]{#package-repositories-both-locations .correct explanation="APT 会组合主文件与软件源目录中的 `.list` 和 `.sources` 定义。"}
:::

## 仓库身份验证

APT 会验证已签名的仓库发行元数据，再依据经过身份验证的元数据中的校验和检查下载的软件包文件。`Signed-By` 可以把一个软件源限定到特定密钥环，而不是让该仓库信任所有全局配置密钥。

有效签名表明元数据来自获接受签名密钥的持有者，而且没有在未被发现的情况下修改。它不能证明发布者的软件没有缺陷、没有恶意或适合当前系统。应通过独立且受信任的渠道确认密钥指纹和软件源说明。

:::single-choice{#package-repositories-signed-by} APT 软件源定义中的 `Signed-By` 有什么安全用途？

::option[加密每个已安装软件包，使 root 也无法读取。]{#package-repositories-package-encryption explanation="仓库签名提供来源和完整性检查，并不对本地管理员保密。"}
::option[把该软件源限定到选定的签名密钥。]{#package-repositories-key-scope .correct explanation="该字段把仓库验证绑定到选定密钥环，而不是不受限制的全局密钥集合。"}
::option[保证仓库中不存在有漏洞的软件。]{#package-repositories-no-vulnerabilities explanation="加密真实性不会评估软件质量或安全缺陷。"}
:::

## 谨慎添加第三方来源

仓库可以用系统权限安装软件包和生命周期脚本，因此添加仓库会扩大系统的软件信任边界。添加前：

1. 如果发行版仓库能够满足需求，应优先使用它。
2. 确认发布者、受支持版本、架构和签名密钥指纹。
3. 使用独立的软件源文件和限定范围的密钥环。
4. 安装前检查软件包名称和依赖变更。
5. 记录如何禁用软件源，以及如何迁移或移除其软件包。

不要照搬禁用签名检查的过时说明，也不要把未经审核的远程脚本通过管道送入特权 shell。

:::single-choice{#package-repositories-third-party-risk} 为什么添加第三方仓库会扩大系统的信任边界？

::option[其经过身份验证的软件包和脚本可能以系统权限安装。]{#package-repositories-privileged-install .correct explanation="信任签名来源可能授权影响操作系统的代码和生命周期操作。"}
::option[它会让 Linux 内核停止实施文件权限。]{#package-repositories-disable-permissions explanation="仓库配置不会禁用内核的常规访问控制机制。"}
::option[它会把所有原生软件包转换成源代码归档。]{#package-repositories-convert-source explanation="添加仓库会改变可用软件包来源，而不会改变现有软件包的基本格式。"}
:::

可以在[Linux 软件安装](https://labex.io/zh/labs/linux-software-installation-on-linux-18005)实验中练习通过仓库安装，或在[使用 YUM 查询和更新软件包](https://labex.io/zh/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)实验中比较 Red Hat 家族流程。准确的 APT 语法请查阅本机 `sources.list(5)` 手册。

## 总结

现在，你可以解释已配置仓库如何成为受信任的软件包元数据来源。

1. 区分仓库索引与软件包归档。
2. 使用 `apt update` 刷新本地目录。
3. 找到单行和 deb822 风格的 APT 软件源定义。
4. 限定签名密钥，并谨慎审查第三方信任。
