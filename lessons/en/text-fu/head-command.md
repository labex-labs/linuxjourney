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

What does the following command do and why?

```bash
head -c 15 /var/log/syslog
```

## Quiz Question

What flag would you use to change the number of lines you want to view for the `head` command?

## Quiz Answer

-n
