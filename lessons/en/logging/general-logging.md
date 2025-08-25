---
index: 3
lang: "en"
title: "General Logging"
meta_title: "General Logging - Logging"
meta_description: "Learn about Linux log files like /var/log/messages and syslog. Understand their differences for effective system troubleshooting. Start your Linux journey!"
meta_keywords: "Linux logs, syslog, var/log/messages, Linux troubleshooting, Linux beginner, Linux guide, system logs"
---

## Lesson Content

There are many log files you can view on your system; many important ones can be found under `/var/log`. We won't go through them all, but we'll discuss a couple of the major ones.

There are two general log files you can view to get a glimpse of what your system is doing:

### `/var/log/messages`

This log contains all non-critical and non-debug messages, including messages logged during boot-up (dmesg), auth, cron, daemon, etc. It is very useful to get a glimpse of how your machine is acting.

### `/var/log/syslog`

This logs everything except auth messages; it's extremely useful for debugging errors on your machine.

These two logs should be more than enough when troubleshooting issues with your system. However, if you just want to view a specific log component, there are also separate logs for those as well.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of viewing and analyzing log files:

1. **[Linux tail Command: File End Display](https://labex.io/labs/linux-linux-tail-command-file-end-display-214303)** - Learn the Linux `tail` command for viewing and monitoring the end of text files, essential for log analysis.
2. **[Linux head Command: File Beginning Display](https://labex.io/labs/linux-linux-head-command-file-beginning-display-214302)** - Explore the `head` command to display the initial lines of text files, useful for quickly checking log headers.
3. **[Rapid Threat Detection](https://labex.io/labs/linux-rapid-threat-detection-387930)** - Practice essential Linux command-line skills for cybersecurity analysis, using `tail` and `head` to quickly extract and analyze recent log entries.

These labs will help you apply the concepts of log file viewing in real scenarios and build confidence with system monitoring.

## Quiz Question

What log file logs everything except auth messages?

## Quiz Answer

syslog
