---
lang: "zh"
title: "rpm 和 dpkg"
description: "学习使用 rpm 和 dpkg 命令安装、移除和列出软件包。了解.deb 和.rpm 文件的直接包管理。开始您的 Linux 之旅！"
keywords: "rpm, dpkg, Linux 包管理，.deb, .rpm, Linux 教程，初学者指南，安装包"
---

## Lesson Content

尽管本课程的大部分内容是关于包管理系统（包管理领域的“蝙蝠侠”），但我们不能忘记“罗宾”们。虽然它们非常有用和可靠，但它们没有配备酷炫的蝙蝠车和多功能腰带。

就像`.exe`是一个单独的可执行文件一样，`.deb`和`.rpm`也是如此。如果您使用包仓库，通常不会看到这些文件，但如果您直接下载包，则很可能会以这些流行的格式获取它们。显然，它们是各自发行版独有的：`.deb`用于基于 Debian 的发行版，`.rpm`用于基于 Red Hat 的发行版。

要安装这些直接包，您可以使用包管理命令：`rpm`和`dpkg`。这些工具用于安装包文件；但是，它们不会安装包的依赖项。因此，如果您的包有 10 个依赖项，您将不得不单独安装这些包，然后安装它们的依赖项，依此类推。正如您所看到的，这是促使我们稍后将讨论的完整管理系统出现的原因之一。

请记住，您将无数次需要使用这些工具之一来安装、查询或验证包，因此请记住这些命令。

### Install a package

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

`i`代表安装。您也可以使用更长的格式`--install`。

### Remove a package

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r`代表移除
RPM: `e`代表擦除

### List installed packages

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l`代表列表
RPM: `q`代表查询，`a`代表所有

## Exercise

找到一个您想在系统上安装的程序，例如 Google Chrome，并使用其中一个命令进行安装。

## Quiz Question

`.deb`文件的包管理工具是什么？

## Quiz Answer

dpkg
