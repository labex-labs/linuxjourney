---
index: 2
lang: "zh"
title: "软件包仓库"
meta_title: "软件包仓库 - 软件包"
meta_description: "了解 Linux 软件包仓库以及它们如何管理软件。探索如何查找和添加软件包源，例如 /etc/apt/sources.list，以便轻松安装。"
meta_keywords: "Linux 软件包仓库，apt 源列表，/etc/apt/sources.list, Linux 软件包，Linux 初学者，Linux 教程，软件包管理"
---

## Lesson Content

上传到互联网的软件包是如何最终进入我们的电脑的呢？你是否会访问每个你想要的软件包的下载页面，然后点击下载和安装？虽然你可以这样做，但有一个更好的解决方案：软件包仓库。仓库是软件包的中央存储位置。有大量的仓库存储着许多软件包，最棒的是，它们都可以在互联网上找到——没有那些麻烦的安装盘。你的机器不知道去哪里寻找这些仓库，除非你明确地告诉它去哪里寻找。

例如，假设我想在我的机器上安装 WackyWidgets 软件。WackyWidgets 为其小部件软件包管理自己的仓库。这个仓库里有 10 个软件包，例如 CoolWidget 软件包、SuperWidget 软件包等。WackyWidgets 将这个仓库托管在一个源链接上，叫做：<http://download.widgets/linux/deb/>

现在，你无需直接去他们的网站下载软件包，而是可以告诉你的机器从源链接中查找 WackyWidgets 软件。

你的发行版已经预设了获取软件包的批准来源，这就是它安装你系统上所有基本软件包的方式。在 Debian 系统上，这个源文件是 `/etc/apt/sources.list` 文件。你的机器会知道去那里查找并检查你添加的任何源仓库。

## Exercise

No exercises for this lesson.

## Quiz Question

在 Debian 系统中，源文件在哪里？

## Quiz Answer

/etc/apt/sources.list
