---
lang: "zh"
title: "内核模块"
meta_title: "内核模块 - 内核"
meta_description: "了解 Linux 内核模块：如何加载、卸载和管理它们。理解 `modprobe` 和 `lsmod` 命令以扩展内核功能。开始您的 Linux 之旅！"
meta_keywords: "Linux 内核模块，modprobe, lsmod, 内核管理，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

假设我有一辆很棒的车；我投入了大量时间和金钱。我加装了扰流板、拖车钩、自行车架和其他一些零碎的东西。这些组件实际上并没有改变汽车的核心功能，而且我可以非常容易地拆卸和安装它们。内核使用与内核模块相同的概念。

内核本身是一个庞大的软件。当我们想要添加对新型键盘的支持时，我们不会直接将这段代码写入内核代码中。就像我们不会把自行车架焊接到汽车上一样（好吧，也许有些人会那样做）。内核模块是可以按需加载和卸载到内核中的代码片段。它们允许我们扩展内核的功能，而无需实际增加核心内核代码。我们还可以添加模块，并且（在大多数情况下）无需重新启动系统。

### View a list of currently loaded modules

```bash
lsmod
```

### Load a module

```bash
sudo modprobe bluetooth
```

`modprobe` 从 `/lib/modules/(kernel version)/kernel/drivers` 加载模块。内核模块也可能有依赖关系；如果它们尚未加载，`modprobe` 会加载我们的模块依赖关系。

### Remove a module

```bash
sudo modprobe -r bluetooth
```

### Load on bootup

You 也可以在系统启动时加载模块，而不是使用 `modprobe` 临时加载它们（它们会在您重新启动时卸载）。只需修改 `/etc/modprobe.d` 目录并在其中添加一个配置文件，如下所示：

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

这是一个有点离谱的例子，但如果您有一个名为 `peanut_butter` 的模块，并且您想为其添加一个 `type=almond` 的内核参数，您可以使用此配置文件在启动时加载它。另外，请注意，内核模块有自己的内核参数，因此您需要专门阅读有关该模块的信息以了解更多信息。

### Do not load on bootup

You 也可以通过添加一个配置文件来确保模块在启动时不加载，如下所示：

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

## Exercise

使用 `modprobe` 卸载您的蓝牙模块，看看会发生什么。您将如何解决这个问题？

## Quiz Question

卸载模块使用什么命令？

## Quiz Answer

modprobe -r
