---
index: 6
lang: "zh"
title: "yum 和 apt"
meta_title: "yum 和 apt - 软件包"
meta_description: "学习 yum 和 apt 进行 Linux 包管理。通过这个初学者教程在 Debian/RPM 系统上安装、移除和更新软件。立即开始！"
meta_keywords: "yum, apt, Linux 包管理，apt 教程，yum 教程，Linux 命令，初学者指南，包安装"
---

## Lesson Content

啊，包管理的蝙蝠侠！这些系统配备了所有必要的工具，使包的安装、删除和更改变得更容易，包括安装包依赖项。最流行的两个管理系统是 **yum** 和 **apt**。Yum 专属于 Red Hat 系列，而 apt 专属于 Debian 系列。

### 从仓库安装软件包

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### 移除软件包

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### 更新仓库中的软件包

在安装和更新软件包之前，最好始终更新您的软件包仓库，使其保持最新。

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### 获取已安装软件包的信息

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

熟能生巧！这里有一些动手实验来巩固您对 Linux 包管理的理解：

1. **[使用 YUM 在 Linux 中查询和更新软件包](https://labex.io/zh/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - 练习使用 YUM 在基于 RHEL 的 Linux 系统上管理软件包，包括检查、更新和探索仓库。
2. **[Linux 上的软件安装](https://labex.io/zh/labs/linux-software-installation-on-linux-18005)** - 学习在 Ubuntu 系统上安装和管理软件的各种方法，包括使用 apt、dpkg 和处理 .deb 文件。
3. **[安装和移除软件包](https://labex.io/zh/labs/linux-installing-and-removing-packages-385380)** - 练习使用 `apt` 在基于 Debian 的系统上更新系统、安装和移除软件包以及优化软件配置。

这些实验将帮助您在实际场景中应用概念，并增强对 Linux 包管理的信心。

## Quiz Question

在 Debian 系统上显示软件包信息的命令是什么？

## Quiz Answer

apt show
