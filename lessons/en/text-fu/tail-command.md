---
index: 9
lang: "en"
title: "tail"
meta_title: "tail - Text-Fu"
meta_description: "Learn how to use the `tail` command in Linux to view file ends and monitor logs. Discover `tail -f` for real-time updates. Start your Linux journey!"
meta_keywords: "tail command, Linux tail, tail -f, view logs, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Similar to the `head` command, the `tail` command lets you see the last 10 lines of a file by default.

```bash
tail /var/log/syslog
```

Along with `head`, you can change the number of lines you want to see.

```bash
tail -n 10 /var/log/syslog
```

Another great option you can use is the `-f` (follow) flag; this will follow the file as it grows. Give it a try and see what happens.

```bash
tail -f /var/log/syslog
```

Your `syslog` file will be continually changing while you interact with your system, and using `tail -f` you can see everything that is getting added to that file.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of the `tail` command and its applications:

1. **[Linux tail Command: File End Display](https://labex.io/labs/linux-linux-tail-command-file-end-display-214303)** - Learn the Linux `tail` command for viewing and monitoring the end of text files, including the `-f` option for real-time updates.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice using `tail` (along with `cat` and `more`) to efficiently view and navigate log and configuration files, which is crucial for system monitoring.
3. **[Rapid Threat Detection](https://labex.io/labs/linux-rapid-threat-detection-387930)** - Apply your knowledge of `tail` to quickly extract and analyze recent log entries, simulating rapid threat detection in a cybersecurity context.

These labs will help you apply the concepts of viewing and monitoring file content in real scenarios and build confidence with the `tail` command.

## Quiz Question

What is the flag used to follow a file in `tail`?

## Quiz Answer

-f
