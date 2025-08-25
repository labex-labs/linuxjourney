---
index: 6
lang: "zh"
title: "内核模块"
meta_title: "内核模块 - 内核"
meta_description: "了解 Linux 内核模块：如何加载、卸载和管理它们。理解 `modprobe` 和 `lsmod` 命令以扩展内核功能。开始您的 Linux 之旅！"
meta_keywords: "Linux 内核模块，modprobe, lsmod, 内核管理，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

假设我有一辆很棒的车；我投入了大量时间和金钱。我给它加装了扰流板、拖车钩、自行车架和其他一些零碎的东西。这些组件实际上并没有改变汽车的核心功能，而且我可以非常容易地移除和添加它们。内核使用与内核模块相同的概念。

内核本身是一个庞大的软件。当我们想要添加对新型键盘的支持时，我们不会直接将这段代码写入内核代码中。就像我们不会把自行车架焊接到我们的汽车上一样（好吧，也许有些人会那样做）。内核模块是可以按需加载和卸载到内核中的代码片段。它们允许我们扩展内核的功能，而无需实际增加核心内核代码。我们还可以添加模块，并且（在大多数情况下）无需重新启动系统。

### 查看当前已加载模块列表

```bash
lsmod
```

### 加载模块

```bash
sudo modprobe bluetooth
```

`modprobe` 从 `/lib/modules/(kernel version)/kernel/drivers` 加载模块。内核模块也可能有依赖项；如果它们尚未加载，`modprobe` 会加载我们的模块依赖项。

### 移除模块

```bash
sudo modprobe -r bluetooth
```

### 开机加载

您也可以在系统启动时加载模块，而不是使用 `modprobe` 临时加载它们（这将在您重启时卸载）。只需修改 `/etc/modprobe.d` 目录并在其中添加一个配置文件，如下所示：

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

这是一个有点离谱的例子，但如果您有一个名为 `peanut_butter` 的模块，并且您想为其添加一个 `type=almond` 的内核参数，您可以使用此配置文件在启动时加载它。另外请注意，内核模块有自己的内核参数，因此您需要专门阅读有关该模块的信息以了解更多。

### 不在开机时加载

您还可以通过添加如下配置文件来确保模块不在启动时加载：

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

## Exercise

熟能生巧！这是一个动手实验，旨在巩固您对 Linux 内核模块的理解：

1. **[在 Linux 中管理内核模块](https://labex.io/zh/labs/comptia-manage-kernel-modules-in-linux-590865)** - 练习列出、检查、加载和卸载内核模块，并配置它们在启动时自动加载。本实验将帮助您在实际场景中应用这些概念，并增强您对内核模块管理的信心。

## Quiz Question

用于卸载模块的命令是什么？

## Quiz Answer

modprobe -r
