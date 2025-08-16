---
title: "用户和组"
description: "了解 Linux 用户和组，理解 UID、GID 和 root 用户。学习如何使用 sudo 命令提升权限。开始你的 Linux 之旅！"
keywords: "Linux 用户，Linux 组，sudo 命令，root 用户，Linux 权限，Linux 教程，Linux 入门，Linux 指南"
---

## Lesson Content

在任何传统的操作系统中，都有用户和组。它们的存在仅仅是为了访问和权限。当运行一个进程时，它将以该进程所有者的身份运行，无论是 Jane 还是 Bob。文件访问和所有权也依赖于权限。你不会希望 Jane 看到 Bob 的文档，反之亦然。

每个用户都有自己的主目录，其中存储了他们用户特定的文件。这通常位于`/home/username`，但在不同的发行版中可能会有所不同。

系统使用用户 ID（UID）来管理用户。用户名是关联用户身份的友好方式，但系统通过其 UID 来识别用户。系统还使用组来管理权限。组只是一组用户，其权限由该组设置；它们由系统通过其组 ID（GID）识别。

在 Linux 中，除了使用系统的普通人类用户之外，你还会拥有其他用户。有时这些用户是系统守护进程，它们持续运行进程以保持系统正常运行。其中最重要的用户是`root`或`superuser`。`root`是系统上最强大的用户；`root`可以访问任何文件并启动和终止任何进程。因此，一直以`root`身份操作可能很危险；你可能会不小心删除系统关键文件。幸运的是，如果需要`root`访问权限并且用户拥有`root`访问权限，他们可以使用`sudo`命令以`root`身份运行命令。`sudo`命令（superuser do）用于以`root`权限运行命令。我们将在后面的课程中更深入地探讨用户如何获得`root`访问权限。

继续尝试查看受保护的文件，例如`/etc/shadow`：

```bash
cat /etc/shadow
```

注意你会收到权限拒绝错误。使用以下命令查看权限：

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

我们还没有详细介绍权限，但这里发生的情况是`root`是文件的所有者，你需要`root`访问权限或属于`shadow`组才能读取内容。现在使用`sudo`运行命令：

```bash
sudo cat /etc/shadow
```

现在你将能够看到文件的内容！

## Exercise

No exercises for this lesson.

## Quiz Question

你使用什么命令以`root`身份运行？

## Quiz Answer

sudo
