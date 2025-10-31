---
index: 2
lang: "zh"
title: "软件包仓库"
meta_title: "软件包仓库 - 软件包"
meta_description: "探索 Linux 软件包仓库及其在包管理中的作用。了解您的系统如何使用 /etc/apt/sources.list 文件等来源来查找和安装 Linux 软件包。"
meta_keywords: "Linux 软件包仓库，apt 软件源列表，/etc/apt/sources.list, Linux 软件包，Linux 入门，Linux 教程，包管理"
---

## Lesson Content

数量庞大的在线 Linux 软件包是如何进入我们电脑的？虽然你可以访问每个软件的下载页面，但存在一个更有效率的解决方案：软件包存储库（Package Repositories）。

### 什么是软件包存储库

软件包存储库是软件的中央存储位置。这些存储库托管在互联网上的服务器上，包含经过筛选的 Linux 软件包集合，无需手动下载和安装。这个系统是现代 Linux 软件包管理的一个基石，提供了一种精简且安全的方式来管理软件。

### 存储库如何工作

系统的软件包管理器需要知道在哪里可以找到这些存储库。你为其提供一个源链接，它会处理其余的事情。

例如，要安装 Docker，你不会直接从其网站下载。相反，你会配置软件包管理器使用 Docker 的官方存储库，该存储库托管在类似 `https://download.docker.com/linux/ubuntu` 的 URL 上。配置完成后，你的系统就可以访问该存储库中的所有软件包，例如 `docker-ce`、`docker-ce-cli` 和 `containerd.io`。

### 配置存储库源

你的 Linux 发行版已经预先配置了一组存储库，用于你系统上的所有基础软件包。在基于 Debian 的系统（如 Ubuntu）上，这些源的主要配置是通过 `apt sources list`（apt 源列表）管理的。

传统上，这个列表是一个单一文件：`/etc/apt/sources.list`。你机器上的软件包管理器会读取此文件，以了解应检查哪些存储库以获取可用软件和更新。

将新的存储库配置添加到 `/etc/apt/sources.list.d/` 目录中也是一种常见做法。较新的 Ubuntu 版本（22.04+）甚至默认使用此目录，将源组织到结构化的 `.sources` 文件中。这种方法将第三方存储库与系统的默认源分开，使软件包管理更清晰、更有条理。`apt` 软件包管理器会同时使用 `/etc/apt/sources.list` 和 `/etc/apt/sources.list.d/` 中的文件。

## Exercise

熟能生巧！以下是一些实践实验，以加强你对 Linux 软件包管理和存储库的理解：

1.  **[在 Linux 上安装软件](https://labex.io/zh/labs/linux-software-installation-on-linux-18005)** - 练习在 Ubuntu 系统上安装和管理软件的各种方法，包括使用 apt 和处理.deb 文件，这与 `sources.list` 的概念直接相关。
2.  **[安装和删除软件包](https://labex.io/zh/labs/linux-installing-and-removing-packages-385380)** - 学习在基于 Debian 的系统上更新系统、安装和删除软件包，巩固你对软件包管理器如何与存储库交互的理解。
3.  **[使用 YUM 在 Linux 中查询和更新软件包](https://labex.io/zh/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - 探索如何使用 YUM 在基于 RHEL 的 Linux 系统上管理软件包，从而对不同发行版之间的软件包管理有更广泛的认识。

这些实验将帮助你在实际场景中应用软件包存储库和软件管理的概念，并增强你对系统管理任务的信心。

## Quiz Question

在传统的 Debian 系统上，列出软件包存储库的主文件的完整路径是什么？请使用完整的文件路径回答。

## Quiz Answer

/etc/apt/sources.list
