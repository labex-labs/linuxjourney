---
lang: "zh"
title: "电源状态"
meta_description: "学习 Linux 系统电源状态：关机、重启和暂停命令。了解如何安全地关闭或重启您的 Linux 系统。开始使用基本命令！"
meta_keywords: "Linux 关机，重启命令，暂停系统，关闭 Linux, Linux 命令，Linux 初学者，Linux 教程，系统状态"
---

## Lesson Content

很难相信我们还没有真正讨论过如何通过命令行控制系统状态。在谈论 `init` 时，我们不仅讨论启动系统的模式，还讨论停止系统的模式。

要关闭您的系统：

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

您认为当您关闭机器时，`init` 发生了什么？

## Quiz Question

在 4 分钟内关闭系统的命令是什么？

## Quiz Answer

sudo shutdown -h +4
