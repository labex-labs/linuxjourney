---
index: 2
lang: "en"
title: "lsof and fuser"
meta_title: "lsof and fuser - Process Utilization"
meta_description: "Explore the lsof and fuser commands in Linux to identify which processes are using specific files. Learn to resolve 'Device or Resource Busy' errors, compare fuser vs lsof, and use options like fuser -k to manage open files effectively."
meta_keywords: "lsof, fuser, fuser command, linux fuser, fuser vs lsof, lsof vs fuser, fuser -k linux, open files, process management, device busy, Linux commands"
---

## Lesson Content

Have you ever tried to unmount a USB drive and received a "Device or Resource Busy" error? This common issue occurs when a process is still using a file or directory on the device. To solve this, you need to find out which process is holding the resource. Two powerful utilities for this task are `lsof` and `fuser`.

### Using lsof to List Open Files

In Linux, almost everything is treated as a file, including disks, pipes, network sockets, and devices. The `lsof` command (short for "list open files") shows you a detailed list of all open files and the processes using them.

To see which processes are using the current directory (`.`), you can run:

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
```

The output shows the command (`COMMAND`), process ID (`PID`), and user (`USER`) associated with each open file. With this information, you can identify the processes preventing you from unmounting a device.

### The fuser Command

Another excellent tool is the `fuser` command (short for "file user"). This utility identifies which processes are using specific files, sockets, or filesystems. The `linux fuser` command is a quick way to see the PIDs of processes accessing a particular resource.

Using the `-v` (verbose) option provides more detailed output:

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

Here, we can clearly see which processes are using our current directory. The `ACCESS` column shows how the file is being used (e.g., `c` for current directory).

### Terminating Processes with fuser

A key feature of the `fuser` command is its ability to terminate processes that are using a resource. The `fuser -k` option sends a `SIGKILL` signal to every process accessing the specified file or filesystem. This is particularly useful for unmounting a busy device.

For example, to kill all processes using a mount point at `/mnt/usb`, you would run:

```bash
sudo fuser -k /mnt/usb
```

Using `fuser -k` in Linux is a fast and effective way to free up a resource.

### fuser vs lsof

So, when should you use `fuser` vs `lsof`?

- **`lsof`** is great for detailed investigation. It provides extensive information about all open files, making it ideal for complex troubleshooting.
- **`fuser`** is more direct. It's perfect for quickly identifying and, if needed, terminating processes on a specific file or mount point. The `fuser command` is often the faster choice for resolving "Device or Resource Busy" errors.

Both tools are essential for any Linux user. Familiarize yourself with them to efficiently manage files and processes.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of managing processes and troubleshooting resource conflicts:

1.  **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with foreground and background processes, inspecting them with `ps`, monitoring resources with `top`, and terminating them with `kill`. This lab will help you identify and manage processes that might be holding onto resources, like files on a USB drive.

This lab will help you apply these concepts in real-world scenarios and build confidence with identifying and managing system processes.

## Quiz Question

What command is used to list open files and their associated process information? (Please answer in English, using only lowercase letters.)

## Quiz Answer

lsof
