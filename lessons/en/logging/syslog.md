---
index: 2
lang: "en"
title: "syslog"
meta_title: "syslog - Logging"
meta_description: "Learn about syslog and rsyslog in Linux, how to manage system logs, and use the logger command. Get started with this beginner-friendly tutorial!"
meta_keywords: "syslog, rsyslog, Linux logs, logger command, /var/log/syslog, Linux tutorial, beginner Linux, system logging"
---

## Lesson Content

The syslog service manages and sends logs to the system logger. Rsyslog is an advanced version of syslog; most Linux distributions should be using this new version. The output of all the logs the syslog service collects can be found at `/var/log/syslog` (every message except authentication messages).

To find out what files are maintained by our system logger, look at the configuration files in `/etc/rsyslog.d`:

```plaintext
pete@icebox:~$ less /etc/rsyslog.d/50-default.conf
# First some standard log files.  Log by facility.
#
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog
#cron.*                         /var/log/cron.log
#daemon.*                       -/var/log/daemon.log
kern.*                          -/var/log/kern.log
#lpr.*                          -/var/log/lpr.log
mail.*                          -/var/log/mail.log
#user.*                         -/var/log/user.log
```

These rules for log files are denoted by the selector on the left column and the action on the right column. The action tells us where to send the log information: to a file, console, etc. Remember, not every application and service uses rsyslog to manage their logs, so if you want to know specifically what is logged, you'll have to look inside this directory.

Let's actually see logging in action; you can manually send a log with the `logger` command:

```bash
logger -s Hello
```

Now look inside your `/var/log/syslog`, and you should see this entry in your logs.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux logging and file viewing:

1. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice essential Linux command-line skills for efficiently viewing and navigating text files, including system logs and configuration files.
2. **[Linux tail Command: File End Display](https://labex.io/labs/linux-linux-tail-command-file-end-display-214303)** - Learn the Linux `tail` command for viewing and monitoring the end of text files, which is particularly useful for real-time log analysis.
3. **[Search Text with grep in Linux](https://labex.io/labs/comptia-search-text-with-grep-in-linux-590841)** - Learn to search for specific text patterns within files, an invaluable skill for sifting through log entries to find critical information.

These labs will help you apply the concepts of log management and file inspection in real scenarios and build confidence with Linux system administration.

## Quiz Question

What command can you use to manually log a message?

## Quiz Answer

logger
