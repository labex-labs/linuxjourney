---
lang: "zh"
title: "NFS"
meta_title: "NFS - 网络共享"
meta_description: "了解 Linux 中 NFS 客户端设置和自动挂载。理解如何连接到网络文件共享以及如何使用自动挂载实现无缝访问。"
meta_keywords: "NFS 客户端，自动挂载，网络文件系统，Linux 网络，mount 命令，Linux 教程，初学者"
---

## Lesson Content

Linux 最标准的网络文件共享是 NFS (Network File System)。NFS 允许服务器通过网络与一个或多个客户端共享目录和文件。

我们不会深入探讨如何创建 NFS 服务器的细节，因为它可能很复杂；但是，我们将讨论如何设置 NFS 客户端。

### 设置 NFS 客户端

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

### 自动挂载

假设您经常使用 NFS 服务器，并且希望它永久挂载。通常，您可能会认为会编辑 `/etc/fstab` 文件，但您可能并非总能连接到服务器，这可能会在启动时导致问题。相反，您需要做的是设置自动挂载，以便在需要时连接到 NFS 服务器。这可以通过 **automount** 工具或在最新版本的 Linux 中使用 **amd** 来完成。当访问指定目录中的文件时，automount 将查找远程服务器并自动挂载它。

## Exercise

阅读 NFS 的手册页以了解更多信息。

## Quiz Question

什么工具用于自动管理挂载点？

## Quiz Answer

automount
