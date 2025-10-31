---
index: 8
lang: "zh"
title: "Cron 作业"
meta_title: "Cron 作业 - 进程利用率"
meta_description: "了解如何使用 cron 作业在 Linux 中调度任务和自动化脚本。本指南涵盖 crontab 语法、crontab -e 等基本命令以及适合初学者的实用示例。"
meta_keywords: "cron 作业，crontab, 调度任务，Linux 自动化，Linux 命令，Linux 入门，Linux 教程，crontab -e, cron"
---

## Lesson Content

虽然进程利用率很重要，但现在也是介绍一个强大的`Linux自动化`工具——`cron`守护进程的好时机。这个后台服务允许您在特定时间或时间间隔自动`调度任务`运行。这些被调度的任务通常被称为`cron作业`。这对于自动化日常操作非常有用，例如每晚运行备份脚本或每周清理一次临时文件。

### 什么是 Cron 作业

想象一下，您在`/home/pete/scripts/change_wallpaper`有一个脚本，您每天早上运行它来设置新的桌面背景。与其每天手动运行它，不如创建一个`cron作业`来为您执行它。通过定义时间表，您可以确切地告诉`cron`服务何时运行您的脚本，使其成为一个真正的“设置好就不用管了”的解决方案。

### 理解 Crontab 语法

要创建`cron作业`，您需要指定时间表和要运行的命令。时间表由五个字段定义，后跟命令。

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

从左到右，这五个时间和日期字段分别是：

- **分钟 (Minute)**: 0-59
- **小时 (Hour)**: 0-23（24 小时制）
- **月份中的日期 (Day of the month)**: 1-31
- **月份 (Month)**: 1-12
- **星期几 (Day of the week)**: 0-7（其中 0 和 7 都代表星期日）

字段中的星号（`*`）用作通配符，表示“每”。在上面的示例中，时间表 `30 08 * * *` 告诉`cron`在每天的 8:30 运行该命令，即每月的每一天、每一年、每一周的每一天。

### 使用 Crontab 管理 Cron 作业

您使用`crontab`命令来管理您的个人`cron作业`，该命令允许您编辑特定于用户的 crontab 文件。该文件保存了您调度的所有`cron作业`。

要添加或编辑您的`cron作业`，请使用`-e`（编辑）标志。这将以您的默认文本编辑器打开您的 crontab 文件。

```bash
crontab -e
```

添加作业定义并保存文件后，`cron`将自动读取新的时间表。您也可以使用`crontab -l`列出活动的`cron作业`，或使用`crontab -r`删除所有作业。使用`cron作业`是任何对`Linux自动化`感兴趣的人的一项基本技能。

## Exercise

熟能生巧！这个实践实验室将帮助您巩固对如何在 Linux 中`调度任务`的理解。

1.  **[在 Linux 中使用 at 和 cron 调度任务](https://labex.io/zh/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 练习使用 `at`、`atq`、`atrm` 和 `crontab` 创建、管理和删除作业，获得自动化系统管理任务的实践经验。

此实验室将帮助您在真实场景中应用本课程中的概念，并增强您对`Linux自动化`的信心。

## Quiz Question

编辑个人 cron 作业的命令是什么？（请使用完全相同的小写命令及其选项作答。）

## Quiz Answer

crontab -e
