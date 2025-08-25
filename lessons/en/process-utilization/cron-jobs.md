---
index: 8
lang: "en"
title: "Cron Jobs"
meta_title: "Cron Jobs - Process Utilization"
meta_description: "Learn to schedule Linux tasks with cron jobs. Understand crontab syntax and automate scripts for daily operations. Get started with this beginner-friendly guide!"
meta_keywords: "cron jobs, crontab, schedule tasks, Linux automation, Linux commands, beginner Linux, Linux tutorial, crontab -e"
---

## Lesson Content

Although we have been talking about resource utilization, I think this would be a good point to mention a neat tool in Linux that is used to schedule tasks using cron. There is a service that runs programs for you at whatever time you schedule. This is really useful if you have a script you want to run once a day that needs to execute something for you.

For example, let's say I have a script located in `/home/pete/scripts/change_wallpaper`. I use this script every morning to change the picture I use for my wallpaper, but each morning I have to manually execute this script. Instead, what I can do is create a cron job that executes my script through cron. I can specify the time I want this cron job to run and execute my script.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

The fields are as follows from left to right:

- Minute - (0-59)
- Hour - (0-23)
- Day of the month - (1-31)
- Month - (1-12)
- Day of the week - (0-7). 0 and 7 are denoted as Sunday

The asterisk in the field means to match every value. So in my above example, I want this to run every day in every month at 8:30 AM.

To create a cron job, just edit the crontab file:

```bash
crontab -e
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of scheduling tasks in Linux:

1. **[Schedule Tasks with at and cron in Linux](https://labex.io/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Practice creating, managing, and removing jobs with `at`, `atq`, `atrm`, and `crontab`, gaining hands-on experience in automating system administration tasks.

This lab will help you apply the concepts in real scenarios and build confidence with task scheduling.

## Quiz Question

What is the command to edit your cron jobs?

## Quiz Answer

crontab -e
