---
index: 7
lang: "zh"
title: "电源状态"
meta_title: "电源状态 - Init"
meta_description: "了解 Linux 系统电源状态：shutdown、reboot 和 halt 命令。了解如何安全地关闭或重启您的 Linux 系统。开始学习基本命令！"
meta_keywords: "Linux shutdown, reboot 命令，halt 系统，关闭 Linux, Linux 命令，Linux 初学者，Linux 教程，系统状态"
---

## Lesson Content

我们竟然还没有讨论过如何通过命令行控制系统状态，这真是令人难以置信。在讨论 `init` 时，我们不仅讨论了启动系统的模式，还讨论了停止系统的模式。

要关闭系统：

```bash
sudo shutdown -h now
```

此命令将暂停系统（关闭电源）。您还必须指定希望何时执行此操作。您可以添加一个以分钟为单位的时间，系统将在该时间后关闭。

```bash
sudo shutdown -h +2
```

这将在两分钟内关闭您的系统。您也可以使用 `shutdown` 命令重启：

```bash
sudo shutdown -r now
```

或者直接使用 `reboot` 命令：

```bash
sudo reboot
```

## Exercise

虽然本主题没有具体的实验，但我们建议您探索全面的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

在 4 分钟内关闭系统的命令是什么？

## Quiz Answer

sudo shutdown -h +4
