---
lang: "zh"
title: "Upstart 作业"
meta_description: "学习使用 initctl 命令在 Linux 中管理 Upstart 作业。了解作业状态、启动、停止和重启服务。提升您的 Linux 系统管理技能。"
meta_keywords: "Upstart 作业，initctl, Linux 服务，系统管理，Linux 教程，初学者指南"
---

## Lesson Content

Upstart 可以触发许多事件和作业运行。不幸的是，没有简单的方法可以查看事件或作业的来源，因此您必须在 `/etc/init` 中查看作业配置。大多数时候，您根本不需要查看 Upstart 作业配置文件，但您会希望更轻松地控制某些特定作业。在 Upstart 系统中，您可以使用许多有用的命令。

### View jobs

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

您将看到一个 Upstart 作业列表，它们具有不同的状态。在每一行中，作业名称是第一个值，第二个字段（在 `/` 之前）实际上是作业的目标。第三个值（在 `/` 之后）是当前状态。因此，我们看到 `shutdown` 作业最终想要停止，但它目前处于等待状态。作业状态和目标将随着您启动或停止作业而改变。

### View specific job

```plaintext
initctl status networking
networking start/running
```

我们不会深入探讨如何编写 Upstart 作业配置的细节；但是，我们已经知道这些配置中的作业是停止、启动和重新启动的。这些作业还会发出事件，因此它们可以启动其他作业。我们将介绍 Upstart 操作的手动命令，但如果您好奇，应该更深入地研究 `.conf` 文件。

### Manually start a job

```bash
sudo initctl start networking
```

### Manually stop a job

```bash
sudo initctl stop networking
```

### Manually restart a job

```bash
sudo initctl restart networking
```

### Manually emit an event

```bash
sudo initctl emit some_event
```

## Exercise

观察您的 Upstart 作业列表。现在，使用我们今天学到的一个命令更改作业状态。之后您会注意到什么？

## Quiz Question

我将如何手动重启一个名为 `peanuts` 的 Upstart 作业？

## Quiz Answer

sudo initctl restart peanuts
