---
index: 2
lang: "en"
title: "lsof and fuser"
meta_title: "lsof and fuser - Process Utilization"
meta_description: "Learn how to use lsof and fuser commands in Linux to identify processes using files. Understand 'Device or Resource Busy' errors and manage open files effectively."
meta_keywords: "lsof, fuser, Linux commands, open files, process management, Linux tutorial, beginner guide, device busy"
---

## Lesson Content

Let's say you plugged in a USB drive and started working on some files. Once you were done, you tried to unmount the USB device and received an error: "Device or Resource Busy." How would you find out which files on the USB drive are still in use? There are two tools you can use for this:

### lsof

Remember, files aren't just text files, images, etc.; they are everything on the system: disks, pipes, network sockets, devices, etc. To see what is in use by a process, you can use the `lsof` command (short for "list open files"). This will show you a list of all open files and their associated processes.

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
indicator 1809 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
lsof      5915 pete  cwd    DIR    8,6     4096  131 .
```

Now I can see which processes are currently holding the device/file open. In our USB example, you can also kill these processes so you can unmount this pesky drive.

### fuser

Another way to track a process is with the `fuser` command (short for "file user"). This will show you information about the process that is using the file or the file user.

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  1809 ..c.. indicator-power
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

We can see which processes are currently using our `/home/pete` directory. The `lsof` and `fuser` tools are very similar. Familiarize yourself with these tools and try using them next time you need to track a file or process.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of managing processes and troubleshooting resource conflicts:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with foreground and background processes, inspecting them with `ps`, monitoring resources with `top`, and terminating them with `kill`. This lab will help you identify and manage processes that might be holding onto resources, like files on a USB drive.

This lab will help you apply the concepts in real scenarios and build confidence with identifying and managing system processes.

## Quiz Question

What command is used to list open files and their process information?

## Quiz Answer

lsof
