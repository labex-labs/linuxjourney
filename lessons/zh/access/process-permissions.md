---
index: 7
lang: "zh"
title: "进程权限"
meta_title: "进程权限 - 权限"
meta_description: "了解 Linux 进程权限，包括真实用户 ID (Real UID)、有效用户 ID (Effective UID) 和保存用户 ID (Saved User ID)。理解 UID 如何影响安全性和命令执行。立即开始学习！"
meta_keywords: "Linux 进程权限，真实用户 ID, 有效用户 ID, 保存用户 ID, Linux 安全，passwd 命令，Linux 教程，Linux 初学者"
---

## Lesson Content

让我们稍微谈谈进程权限。还记得我告诉过你，当你运行启用了 SUID 权限位的 `passwd` 命令时，你将以 root 身份运行该程序吗？这是真的。然而，这是否意味着你暂时是 root，就可以修改其他用户的密码呢？不，幸运的是不能！

这是因为 Linux 实现了许多 UID。每个进程都关联着三个 UID：

当你启动一个进程时，它会以启动它的用户或组的相同权限运行。这被称为**有效用户 ID**。这个 UID 用于授予进程访问权限。因此，很自然地，如果 Bob 运行了 `touch` 命令，该进程将以他的身份运行，他创建的任何文件都将归他所有。

还有另一个 UID，称为**真实用户 ID**。这是启动进程的用户的 ID。它们用于跟踪启动进程的用户是谁。

最后一个 UID 是**保存用户 ID**。这允许进程在有效 UID 和真实 UID 之间切换，反之亦然。这很有用，因为我们不希望我们的进程一直以提升的权限运行；在特定时间使用特殊权限是一种良好的实践。

现在让我们再次通过 `passwd` 命令将这些概念联系起来。

运行 `passwd` 命令时，你的有效 UID 是你的用户 ID；我们暂时假设它是 500。哦，等等，记住 `passwd` 命令启用了 SUID 权限。所以当你运行它时，你的有效 UID 现在是 0（0 是 root 的 UID）。现在这个程序可以以 root 身份访问文件了。

假设你尝到了一点权力，你想修改 Sally 的密码。Sally 的 UID 是 600。嗯，你将无法成功。幸运的是，该进程还拥有你的真实 UID，在本例中是 500。它知道你的 UID 是 500，因此你无法修改 UID 为 600 的密码。（当然，如果你是机器上的超级用户，可以控制和更改所有内容，则始终可以绕过此限制）。

由于你运行了 `passwd`，它将使用你的真实 UID 启动进程，并保存文件所有者（有效 UID）的 UID，这样你就可以在两者之间切换。如果不需要，则无需以 root 权限修改所有文件。

大多数情况下，真实 UID 和有效 UID 是相同的，但在 `passwd` 命令等情况下，它们会发生变化。

## Exercise

我们还没有讨论进程，但我们仍然可以实时查看这种变化：

1. Open one terminal window and run the command: `watch -n 1 "ps aux | grep passwd"`. This will watch for the `passwd` process.
2. Open a second terminal window and run: `passwd`.
3. Look at the first terminal window; you'll see a process come up for `passwd`. The first column in the process table is the effective user ID. Lo and behold, it's the root user!

## Quiz Question

哪个 UID 决定授予什么访问权限？

## Quiz Answer

effective
