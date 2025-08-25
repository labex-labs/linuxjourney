---
index: 1
lang: "en"
title: "System Logging"
meta_title: "System Logging - Logging"
meta_description: "Learn about Linux system logging, syslog, and how to view log files in /var/log. Understand rsyslogd and monitor system events with this beginner guide."
meta_keywords: "Linux logging, syslog, rsyslogd, var log, system logs, Linux tutorial, beginner guide"
---

## Lesson Content

The services, kernel, daemons, etc., on your system are constantly doing something. This data is actually sent to be saved on your system in the form of logs. This allows us to have a human-readable journal of the events that are happening on our system. This data is usually kept in the `/var` directory; the `/var` directory is where we keep our variable data, such as logs!

How are these messages even getting received on your system? There is a service called syslog that sends this information to the system logger.

Syslog actually contains many components. One of the important ones is a daemon running called `syslogd` (newer Linux distributions use `rsyslogd`), that waits for event messages to occur and filters the ones it wants to know about. Depending on what it's supposed to do with that message, it will send it to a file, your console, or do nothing with it.

You would think that this system logger is the centralized place to manage logs, but unfortunately, it's not. You'll see many applications that write their own logging rules and generate different log files. However, in general, the format of logs should include a timestamp and the event details.

Here is an example of a line from syslog:

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Here we can see that at Jan 27 07:41:32, our cron service ran the `cron.weekly` job. You can view all the event messages that syslog collects within the `/var/log/syslog` file.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux logs and file viewing:

1. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Learn essential Linux command-line skills for efficiently viewing and navigating text files, including system logs and configuration files. Practice using commands like `cat`, `more`, and `less` to extract critical information from various file types.
2. **[Linux tail Command: File End Display](https://labex.io/labs/linux-linux-tail-command-file-end-display-214303)** - Learn the Linux `tail` command for viewing and monitoring the end of text files. This is particularly useful for real-time log analysis.
3. **[Search Text with grep in Linux](https://labex.io/labs/comptia-search-text-with-grep-in-linux-590841)** - In this lab, you will learn to search for text in files on a Linux system using the `grep` command. This is invaluable for finding specific entries within large log files.

These labs will help you apply the concepts of log file management and analysis in real scenarios and build confidence with Linux system monitoring.

## Quiz Question

What is the daemon that manages logs on newer Linux systems?

## Quiz Answer

rsyslogd
