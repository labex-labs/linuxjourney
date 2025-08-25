---
index: 8
lang: "en"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "Learn how to use the Linux 'head' command to view the beginning of files. Understand options like -n for line count. Essential Linux command tutorial."
meta_keywords: "head command, Linux head, view file beginning, Linux tutorial, Linux commands, beginner Linux, head -n, Linux guide"
---

## Lesson Content

Let's say we have a very long file; in fact, we have many to choose from. Go ahead and `cat /var/log/syslog`. You should see pages upon pages of text. What if I just wanted to see the first couple of lines in this text file? Well, we can do that with the `head` command. By default, the `head` command will show you the first 10 lines in a file.

```bash
head /var/log/syslog
```

You can also modify the line count to whatever you choose. Let's say I wanted to see the first 15 lines instead.

```bash
head -n 15 /var/log/syslog
```

The `-n` flag stands for "number of lines."

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of viewing the beginning of files and general text file manipulation:

1. **[Linux head Command: File Beginning Display](https://labex.io/labs/linux-linux-head-command-file-beginning-display-214302)** - This lab will guide you through using the `head` command to display the initial lines of text files, including modifying the line count.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice essential Linux command-line skills for efficiently viewing and navigating text files, including system logs and configuration files, which often require commands like `head`.
3. **[Rapid Threat Detection](https://labex.io/labs/linux-rapid-threat-detection-387930)** - Apply your knowledge of `head` (and `tail`) to quickly extract and analyze recent log entries, simulating real-world cybersecurity analysis.

These labs will help you apply the concepts in real scenarios and build confidence with text file viewing and analysis in Linux.

## Quiz Question

What flag would you use to change the number of lines you want to view for the `head` command?

## Quiz Answer

-n
