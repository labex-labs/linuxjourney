---
index: 9
lang: "en"
title: "tail"
meta_title: "tail - Text-Fu"
meta_description: "A beginner Linux guide to the tail command. Learn how to use Linux tail to view the end of files and monitor logs in real-time with the powerful tail -f option."
meta_keywords: "tail command, Linux tail, tail -f, view logs, monitor logs, Linux tutorial, beginner Linux, Linux guide, file monitoring"
---

## Lesson Content

The `tail` command is a fundamental utility for anyone learning Linux. As its name suggests, it allows you to view the "tail" or end of a file. This is particularly useful for checking the most recent entries in rapidly changing files, such as system logs.

### Viewing the End of a File

By default, the `tail` command displays the last 10 lines of a specified file. It functions as the counterpart to the `head` command.

```bash
tail /var/log/syslog
```

Just like with `head`, you can customize the number of lines you want to see by using the `-n` option. For example, to see the last 20 lines, you would use the following command:

```bash
tail -n 20 /var/log/syslog
```

This flexibility makes the `Linux tail` command an essential tool for quickly inspecting file endings without opening the entire file.

### Real-Time File Monitoring with tail -f

One of the most powerful features of the `tail` command is its ability to monitor files in real-time. This is achieved with the `-f` (follow) flag. When you use `tail -f`, the command doesn't exit after displaying the last few lines. Instead, it waits for new data to be appended to the file and prints it to the screen as it arrives.

```bash
tail -f /var/log/syslog
```

Try running this command. As you continue to use your system, you will see new lines appear in your terminal. This makes `tail -f` an indispensable tool for system administrators and developers who need to `view logs` and monitor application output as it happens.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of the `tail` command and its applications:

1. **[Linux tail Command: File End Display](https://labex.io/labs/linux-linux-tail-command-file-end-display-214303)** - Learn the Linux `tail` command for viewing and monitoring the end of text files, including the `-f` option for real-time updates.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice using `tail` (along with `cat` and `more`) to efficiently view and navigate log and configuration files, which is crucial for system monitoring.
3. **[Rapid Threat Detection](https://labex.io/labs/linux-rapid-threat-detection-387930)** - Apply your knowledge of `tail` to quickly extract and analyze recent log entries, simulating rapid threat detection in a cybersecurity context.

These labs will help you apply the concepts of viewing and monitoring file content in real scenarios and build confidence with the `tail` command.

## Quiz Question

What is the flag used to follow a file in `tail`? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

-f
