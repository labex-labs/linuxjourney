r---
title: "yum 和 apt"
description: "学习 yum 和 apt 进行 Linux 软件包管理。通过这个初学者教程，在 Debian/RPM 系统上安装、删除和更新软件。今天就开始吧！"
keywords: "yum, apt, Linux 软件包管理，apt 教程，yum 教程，Linux 命令，初学者指南，软件包安装"

---

## Lesson Content

啊，软件包管理的蝙蝠侠们！这些系统提供了所有必要的配置，使软件包的安装、删除和更改变得更容易，包括安装软件包依赖项。最流行的两个管理系统是 **yum** 和 **apt**。Yum 专属于 Red Hat 系列，而 apt 专属于 Debian 系列。

### Install a package from a repository

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Remove a package

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Updating packages for a repository

在安装和更新软件包之前，最好始终更新您的软件包仓库，使其保持最新状态。

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### Get information about an installed package

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

运行每个软件包命令，查看您收到的输出。

## Quiz Question

在 Debian 系统上，用于显示软件包信息的命令是什么？

## Quiz Answer

apt show
