---
index: 8
lang: "en"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "A beginner Linux guide on using the head command to view the beginning of a file. Learn how to use the head -n option to control line count, an essential skill for any Linux tutorial."
meta_keywords: "head command, Linux head, view file beginning, Linux tutorial, Linux commands, beginner Linux, head -n, Linux guide, text files, command line"
---

## Lesson Content

In Linux, you often need to inspect the contents of very large files, such as system logs. For example, if you run `cat /var/log/syslog`, you'll see pages of text scroll by, making it difficult to get a quick overview. So, what if you only want to **view the beginning of a file**? The `head` command is the perfect tool for this job.

### Default Behavior of the head Command

By default, the `head` command displays the first 10 lines of any given file. This is a fundamental part of our **beginner Linux guide** for handling text. To see it in action, simply provide a filename as an argument:

```bash
head /var/log/syslog
```

This command will output the first 10 lines from `/var/log/syslog`, allowing you to quickly check the file's initial content without opening it in an editor.

### Customizing the Line Count

The **Linux head** command is flexible. You can easily change the number of lines it displays using the `-n` flag, which stands for "number of lines". For instance, if you want to see the first 15 lines of a file, you would use the `head -n` option like this:

```bash
head -n 15 /var/log/syslog
```

This makes `head` one of the most useful **Linux commands** for quickly inspecting file headers or log entries.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of viewing the beginning of files and general text file manipulation:

1. **[Linux head Command: File Beginning Display](https://labex.io/labs/linux-linux-head-command-file-beginning-display-214302)** - This lab will guide you through using the `head` command to display the initial lines of text files, including modifying the line count.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice essential Linux command-line skills for efficiently viewing and navigating text files, including system logs and configuration files, which often require commands like `head`.
3. **[Rapid Threat Detection](https://labex.io/labs/linux-rapid-threat-detection-387930)** - Apply your knowledge of `head` (and `tail`) to quickly extract and analyze recent log entries, simulating real-world cybersecurity analysis.

These labs will help you apply the concepts in real scenarios and build confidence with text file viewing and analysis in Linux.

## Quiz Question

What flag would you use with the `head` command to change the number of lines you want to view? Please answer using only the English flag, paying attention to case sensitivity.

## Quiz Answer

-n
