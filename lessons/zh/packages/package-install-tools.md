---
lesson_id: "package-install-tools"
course_id: "packages"
lang: "zh"
order_index: 5
title: "rpm 与 dpkg"
description: "了解 `dpkg` 和 `rpm` 如何检查并修改各自的原生软件包数据库和本地归档。"
meta_title: "rpm 与 dpkg - 软件包"
meta_description: "学习使用 rpm 和 dpkg 命令安装、移除和列出软件包。了解 .deb 和 .rpm 文件的直接软件包管理。开始您的 Linux 之旅！"
meta_keywords: "rpm, dpkg, Linux 软件包管理，.deb, .rpm, Linux 教程，初学者指南，安装软件包"
---

`dpkg` 是 Debian 家族系统上的低层软件包工具，`rpm` 在 RPM 家族系统上承担类似职责。它们会解包原生归档、运行软件包生命周期操作，并更新已安装软件包数据库。APT 和 DNF 等能够访问仓库的工具建立在这些低层机制之上。

## 安装前检查归档

软件包归档并不等同于单个可执行文件。它可以包含大量载荷文件、元数据、配置处理逻辑和以特权运行的生命周期脚本。安装前，应检查其来源、签名或经过身份验证的下载路径、元数据和内容。

```bash
Debian: $ dpkg-deb --info ./some-package.deb
Debian: $ dpkg-deb --contents ./some-package.deb
RPM:    $ rpm -qip ./some-package.rpm
RPM:    $ rpm -qlp ./some-package.rpm
```

所示 RPM 查询形式中的 `p` 表示查询软件包文件，而不是已安装数据库。查询输出有助于审查软件包，但不能证明其中的脚本或程序安全。

:::single-choice{#package-install-tools-native-format} 哪个低层工具管理 Debian `.deb` 软件包及其已安装数据库？

::option[`rpm`]{#package-install-tools-rpm-debian explanation="RPM 在 RPM 家族系统上管理自身的原生格式和数据库。"}
::option[`tar`]{#package-install-tools-tar-debian explanation="Tar 可以读取归档，但不实现 Debian 已安装软件包生命周期。"}
::option[`dpkg`]{#package-install-tools-dpkg-debian .correct explanation="Debian 家族系统使用 `dpkg` 执行低层 `.deb` 归档和软件包数据库操作。"}
:::

## 安装本地归档

直接进行低层安装时使用：

```bash
Debian: $ sudo dpkg -i ./some-package.deb
RPM:    $ sudo rpm -U ./some-package.rpm
```

`dpkg -i` 可以解包并配置指定归档，但不会获取缺失的仓库依赖项。原始 `rpm` 同样不提供常规仓库求解器流程。对于本地归档，通常优先使用高层命令，因为它可以从已配置来源解析依赖项：

```bash
Debian: $ sudo apt install ./some-package.deb
RPM:    $ sudo dnf install ./some-package.rpm
```

确认前应审查事务。前导 `./` 可以让 APT 区分本地 Debian 归档路径与仓库软件包名称。

:::single-choice{#package-install-tools-local-dependencies} 所示哪个命令可以安装本地 `.deb`，并解析仓库中可用的依赖项？

::option[`dpkg -l ./some-package.deb`]{#package-install-tools-dpkg-list-file explanation="`dpkg -l` 列出已安装软件包选择，并不是解析本地依赖的安装流程。"}
::option[`rpm -qa ./some-package.deb`]{#package-install-tools-rpm-query-deb explanation="RPM 查询语法不会安装 Debian 归档。"}
::option[`apt install ./some-package.deb`]{#package-install-tools-apt-local .correct explanation="APT 会识别明确的本地路径，并可使用已配置仓库满足声明的依赖项。"}
:::

## 移除已安装软件包

移除操作的目标是已安装软件包名称，而不是先前使用的归档文件名：

```bash
Debian: $ sudo dpkg --remove package-name
RPM:    $ sudo rpm --erase package-name
```

在 Debian 上，`--remove` 通常保留归类为 conffile 的配置文件；`--purge` 还请求移除这些文件，但仍受软件包脚本和非受管数据影响。两个命令都不保证删除用户创建的数据。高层 `apt remove` 或 `dnf remove` 通常更合适，因为它们可以评估相关软件包并呈现完整事务。

:::single-choice{#package-install-tools-remove-operand} `dpkg --remove` 期望用什么作为已安装软件包的操作数？

::option[仓库索引的 URL。]{#package-install-tools-remove-url explanation="仓库位置不是传给低层移除操作的软件包身份。"}
::option[已安装软件包名称。]{#package-install-tools-remove-name .correct explanation="移除操作针对 `example` 这样的软件包记录，而不需要原来的 `.deb` 路径。"}
::option[软件包启动进程的 PID。]{#package-install-tools-remove-pid explanation="进程 ID 与已安装软件包数据库的键无关。"}
:::

## 查询已安装状态

使用以下命令列出已安装或已知的软件包记录：

```bash
Debian: $ dpkg-query -l
RPM:    $ rpm -qa
```

进行定向检查时，应优先指定具体软件包名称；脚本要求可靠性时，应使用机器可读格式。软件包数据库描述受管理状态，但本地管理员或应用程序之后仍可修改文件，因此需要将已安装文件与记录元数据比较时，应使用验证功能。

:::single-choice{#package-install-tools-rpm-list-installed} 哪个命令查询 RPM 数据库中记录的所有已安装软件包？

::option[`rpm -qa`]{#package-install-tools-rpm-query-all .correct explanation="`-q` 选择查询模式，`-a` 将查询扩展到所有已安装软件包记录。"}
::option[`rpm -e`]{#package-install-tools-rpm-erase explanation="`-e` 请求移除软件包，而不是只读列出。"}
::option[`dpkg-deb --contents`]{#package-install-tools-deb-contents explanation="该命令检查 Debian 归档文件的载荷，不查询 RPM 已安装数据库。"}
:::

可以在隔离系统中通过[在 Linux 中使用 RPM 管理软件包](https://labex.io/zh/labs/rhel-managing-packages-with-rpm-in-linux-590868)实验练习归档查询和完整性检查。

## 总结

现在，你可以区分低层软件包操作与仓库事务。

1. 安装前检查本地归档的元数据和内容。
2. 使用 `dpkg` 执行 `.deb` 低层操作，使用 `rpm` 执行 `.rpm` 低层操作。
3. 需要解析依赖项时优先使用 APT 或 DNF。
4. 按已安装软件包名称移除，并单独验证受管理状态。
