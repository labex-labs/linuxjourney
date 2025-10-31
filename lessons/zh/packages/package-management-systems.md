---
index: 6
lang: "zh"
title: "yum 和 apt"
meta_title: "yum 和 apt - 包管理"
meta_description: "探索 yum 与 apt 之间的关键区别。本指南涵盖了如何在基于 RPM 和 Debian 的 Linux 系统上使用 yum 和 apt 来安装、删除和更新软件包。"
meta_keywords: "yum vs apt, yum apt, Linux 包管理，apt, yum, Debian, Red Hat, 安装软件包，更新软件包，Linux 命令"
---

## Lesson Content

包管理器是 Linux 中必不可少的工具，它简化了软件的安装、更新和删除。它们会自动处理依赖关系，确保所有必需的库和组件都正确安装。Yum 和 apt 是两个最著名的包管理系统。

### Yum 与 Apt

这两个系统的主要区别在于它们所服务的 Linux 发行版。`yum`（Yellowdog Updater, Modified）包管理器用于基于 RPM 的发行版，如 Red Hat、CentOS 和 Fedora。相比之下，`apt`（Advanced Package Tool）是基于 Debian 的发行版（包括 Ubuntu）的标准。虽然 `yum` 和 `apt` 都能实现相同目标，但它们的命令语法不同。

### 安装和删除软件包

要从仓库安装新软件，您需要使用 `install` 命令。

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

要删除软件包，命令也很直接。`apt` 使用 `remove`，而 `yum` 使用 `erase`。

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### 更新和检查软件包

最佳实践是在安装或升级软件之前更新本地包索引。这可确保您获得最新版本。

对于 Debian 系统，这是一个两步过程：`apt update` 刷新包列表，`apt upgrade` 安装新版本。对于 RPM 系统，`yum update` 用一个命令处理这两个操作。

```bash
Debian: $ apt update; apt upgrade
RPM: $ yum update
```

如果您需要获取有关特定软件包的更多详细信息，您可以使用以下命令显示其版本、大小和描述等信息。

```bash
Debian: $ apt show package_name
RPM: $ yum info package_name
```

## Exercise

实践出真知！以下是一些实践实验，以加强您对 Linux 包管理的理解：

1.  **[在 Linux 中使用 YUM 查询和更新软件包](https://labex.io/zh/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - 练习使用 YUM 在基于 RHEL 的 Linux 系统上管理软件包，包括检查、更新和浏览仓库。
2.  **[Linux 上的软件安装](https://labex.io/zh/labs/linux-software-installation-on-linux-18005)** - 学习在 Ubuntu 系统上安装和管理软件的各种方法，包括使用 apt、dpkg 和处理 .deb 文件。
3.  **[安装和删除软件包](https://labex.io/zh/labs/linux-installing-and-removing-packages-385380)** - 练习使用 `apt` 在基于 Debian 的系统上更新系统、安装和删除软件包以及优化软件配置。

这些实验将帮助您在实际场景中应用这些概念，并建立对 Linux 包管理的信心。

## Quiz Question

在 Debian 系统上，用于显示软件包信息使用的命令是什么？请用英语回答，注意区分大小写。

## Quiz Answer

apt show
