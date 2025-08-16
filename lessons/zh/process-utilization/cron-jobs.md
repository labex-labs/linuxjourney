---
lang: "zh"
title: "Cron 作业"
description: "学习使用 cron 作业安排 Linux 任务。了解 crontab 语法并自动化脚本以进行日常操作。通过这份适合初学者的指南开始吧！"
keywords: "cron jobs, crontab, 安排任务，Linux 自动化，Linux 命令，Linux 初学者，Linux 教程，crontab -e"
---

## Lesson Content

尽管我们一直在讨论资源利用率，但我认为现在是时候提一下 Linux 中一个很棒的工具了，它使用 cron 来安排任务。有一个服务可以在您设定的任何时间为您运行程序。如果您有一个脚本需要每天运行一次以执行某些操作，这真的非常有用。

例如，假设我有一个脚本位于 `/home/pete/scripts/change_wallpaper`。我每天早上都使用这个脚本来更改我的壁纸图片，但每天早上我都必须手动执行这个脚本。相反，我可以创建一个 cron 作业，通过 cron 执行我的脚本。我可以指定我希望这个 cron 作业运行并执行我的脚本的时间。

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

这些字段从左到右依次是：

- 分钟 - (0-59)
- 小时 - (0-23)
- 月份中的日期 - (1-31)
- 月份 - (1-12)
- 星期几 - (0-7)。0 和 7 都表示星期日

字段中的星号表示匹配所有值。因此，在我上面的示例中，我希望它在每个月的每天上午 8:30 运行。

要创建 cron 作业，只需编辑 crontab 文件：

```bash
crontab -e
```

## Exercise

创建一个您希望在预定时间运行的 cron 作业。

## Quiz Question

编辑 cron 作业的命令是什么？

## Quiz Answer

crontab -e
