---
index: 8
lang: "zh"
title: "Cron 作业"
meta_title: "Cron 作业 - 进程利用率"
meta_description: "学习使用 cron 作业调度 Linux 任务。理解 crontab 语法并自动化脚本以进行日常操作。通过这份适合初学者的指南开始学习！"
meta_keywords: "cron 作业，crontab, 调度任务，Linux 自动化，Linux 命令，Linux 初学者，Linux 教程，crontab -e"
---

## Lesson Content

尽管我们一直在讨论资源利用率，但我认为现在是时候提一下 Linux 中一个很棒的工具了，它用于使用 cron 调度任务。有一个服务会按照您设定的时间为您运行程序。如果您有一个脚本想每天运行一次，并且需要为您执行某些操作，这真的非常有用。

例如，假设我有一个脚本位于 `/home/pete/scripts/change_wallpaper`。我每天早上都使用这个脚本来更改我的壁纸图片，但每天早上我必须手动执行这个脚本。相反，我可以创建一个 cron 作业，通过 cron 执行我的脚本。我可以指定我希望这个 cron 作业运行并执行我的脚本的时间。

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

字段从左到右依次是：

- 分钟 - (0-59)
- 小时 - (0-23)
- 月份中的日期 - (1-31)
- 月份 - (1-12)
- 星期几 - (0-7)。0 和 7 都表示星期日

字段中的星号表示匹配所有值。所以在我的上述示例中，我希望它在每个月的每天早上 8:30 运行。

要创建 cron 作业，只需编辑 crontab 文件：

```bash
crontab -e
```

## Exercise

熟能生巧！这里有一些动手实验来巩固您对 Linux 中任务调度的理解：

1. **[在 Linux 中使用 at 和 cron 调度任务](https://labex.io/zh/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 练习使用 `at`、`atq`、`atrm` 和 `crontab` 创建、管理和删除作业，获得自动化系统管理任务的实践经验。

本实验将帮助您在实际场景中应用这些概念，并增强任务调度的信心。

## Quiz Question

编辑 cron 作业的命令是什么？

## Quiz Answer

crontab -e
