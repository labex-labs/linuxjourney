---
index: 2
lang: "zh"
title: "软件包仓库"
meta_title: "软件包仓库 - 软件包"
meta_description: "了解 Linux 软件包仓库及其如何管理软件。探索如何查找和添加软件包源，例如 /etc/apt/sources.list，以便轻松安装。"
meta_keywords: "Linux 软件包仓库，apt 源列表，/etc/apt/sources.list, Linux 软件包，Linux 初学者，Linux 教程，软件包管理"
---

## Lesson Content

上传到互联网的软件包是如何最终出现在我们的电脑上的呢？您是否会访问您想要的每个软件包的下载页面，然后点击下载并安装？虽然您可以这样做，但有一个更好的解决方案：软件包仓库。仓库是软件包的集中存储位置。有大量的仓库包含许多软件包，最棒的是，它们都可以在互联网上找到——没有那些麻烦的安装盘。您的机器不知道在哪里寻找这些仓库，除非您明确告诉它去哪里寻找。

例如，假设我想要在我的机器上安装 Docker 软件。Docker 为其容器软件包管理自己的仓库。这个仓库中包含多个软件包，例如 docker-ce 软件包、docker-ce-cli 软件包、containerd.io 软件包等。Docker 将此仓库托管在一个源链接上，即：`https://download.docker.com/linux/ubuntu`

现在，您无需访问他们的网站直接下载软件包，而是可以告诉您的机器从源链接查找 Docker 软件。

您的发行版已经预设了批准的软件包来源，这就是它安装您系统上所有基本软件包的方式。在 Debian 系统上，这个源文件是 `/etc/apt/sources.list` 文件。您的机器会知道去那里查找并检查您添加的任何源仓库。

## Exercise

熟能生巧！以下是一些动手实验，以加深您对 Linux 软件包管理和仓库的理解：

1. **[Linux 上的软件安装](https://labex.io/zh/labs/linux-software-installation-on-linux-18005)** - 练习在 Ubuntu 系统上安装和管理软件的各种方法，包括使用 apt 和处理 .deb 文件，这与 `sources.list` 概念直接相关。
2. **[安装和删除软件包](https://labex.io/zh/labs/linux-installing-and-removing-packages-385380)** - 学习在基于 Debian 的系统上更新系统、安装和删除软件包，巩固您对软件包管理器如何与仓库交互的理解。
3. **[使用 YUM 在 Linux 中查询和更新软件包](https://labex.io/zh/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - 探索如何在基于 RHEL 的 Linux 系统上使用 YUM 管理软件包，从而提供对不同发行版之间软件包管理的更广阔视角。

这些实验将帮助您在实际场景中应用软件包仓库和软件管理的概念，并增强您在系统管理任务中的信心。

## Quiz Question

Debian 系统中的源文件在哪里？

## Quiz Answer

/etc/apt/sources.list
