---
index: 4
lang: "en"
title: "Kernel Logging"
meta_title: "Kernel Logging - Logging"
meta_description: "Learn about Linux kernel logging with dmesg and kern.log. Understand boot messages and hardware issues. Explore kernel logs for system insights."
meta_keywords: "dmesg, kern.log, Linux logging, kernel messages, boot log, Linux tutorial, beginner guide"
---

## Lesson Content

### /var/log/dmesg

On boot-time, your system logs information about the kernel ring buffer. This shows us information about hardware drivers, kernel information, and status during bootup, among other things. This log file can be found at `/var/log/dmesg` and gets reset on every boot. You may not actually see any use in it now, but if you were to ever have issues with something during bootup or a hardware issue, `dmesg` is the best place to look. You can also view this log using the `dmesg` command.

### /var/log/kern.log

Another log you can use to view kernel information is the `/var/log/kern.log` file. This logs kernel information and events on your system; it also logs `dmesg` output.

## Exercise

Look at your `dmesg` and `kern` logs. What differences do you notice?

## Quiz Question

What command can be used to view kernel bootup messages?

## Quiz Answer

dmesg
