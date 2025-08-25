---
index: 1
lang: "zh"
title: "文件系统层次结构"
meta_title: "文件系统层次结构 - 文件系统"
meta_description: "了解 Linux 文件系统层次结构标准 (FHS)，并理解 /bin、/etc 和 /var 等关键目录。探索 Linux 目录结构。"
meta_keywords: "Linux 文件系统层次结构，FHS, Linux 目录结构，Linux 命令，Linux 初学者，Linux 教程，Linux 指南"
---

## Lesson Content

此时，您可能已经非常熟悉系统的目录结构了；如果还没有，很快就会熟悉。文件系统的结构可能有所不同，但在大多数情况下，它们应该符合文件系统层次结构标准。

继续执行 `ls -l /` 命令，查看根目录下列出的目录。您的目录可能与我的不同，但大多数目录应该如下所示：

- `/` - 整个文件系统层次结构的根目录；所有内容都嵌套在此目录下。
- `/bin` - 必要的即用程序（二进制文件）；包括 `ls` 和 `cp` 等最基本的命令。
- `/boot` - 包含内核引导加载程序文件。
- `/dev` - 设备文件。
- `/etc` - 核心系统配置目录；应仅包含配置文件，不包含任何二进制文件。
- `/home` - 用户的个人目录；存放您的文档、文件、设置等。
- `/lib` - 存放二进制文件可以使用的库文件。
- `/media` - 用作可移动媒体（如 USB 驱动器）的挂载点。
- `/mnt` - 临时挂载的文件系统。
- `/opt` - 可选的应用程序软件包。
- `/proc` - 有关当前运行进程的信息。
- `/root` - root 用户的家目录。
- `/run` - 自上次启动以来有关运行系统的信息。
- `/sbin` - 包含必要的系统二进制文件，通常只能由 root 运行。
- `/srv` - 由系统提供的特定站点数据。
- `/tmp` - 临时文件的存储。
- `/usr` - 这个命名不幸；它通常不包含家庭文件夹意义上的用户文件。它旨在用于用户安装的软件和实用程序；但是，这并不是说您不能在其中添加个人目录。此目录内部有 `/usr/bin`、`/usr/local` 等子目录。
- `/var` - 可变目录；它用于系统日志记录、用户跟踪、缓存等。基本上是所有经常变化的内容。

## Exercise

熟能生巧！以下是一些动手实验，以加深您对 Linux 文件系统的理解：

1. **[在 Linux 中导航文件系统](https://labex.io/zh/labs/comptia-navigate-the-filesystem-in-linux-590971)** - 练习使用 `pwd`、`cd` 和 `ls` 等基本 shell 命令在目录之间移动和探索文件系统。
2. **[在 Linux 中管理文件和目录](https://labex.io/zh/labs/comptia-manage-files-and-directories-in-linux-590835)** - 学习创建、删除、复制和移动文件和目录，并理解符号链接和硬链接。
3. **[在 Linux 中查找文件和命令](https://labex.io/zh/labs/comptia-find-files-and-commands-in-linux-590834)** - 掌握使用 `find`、`locate`、`whereis`、`which` 和 `type` 定位文件和命令的技术。

这些实验将帮助您在实际场景中应用概念，并增强对 Linux 文件系统管理的信心。

## Quiz Question

哪个目录用于存储日志？

## Quiz Answer

/var
