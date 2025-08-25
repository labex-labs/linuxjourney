---
index: 3
lang: "en"
title: "Upstart Overview"
meta_title: "Upstart Overview - Init"
meta_description: "Learn about Upstart, its event-driven model, and how it manages services in Linux. Understand Upstart job configurations and its role as an init system."
meta_keywords: "Upstart, init system, Linux services, Ubuntu, SysV, beginner tutorial, Linux guide"
---

## Lesson Content

Upstart was developed by Canonical, so it was the init implementation on Ubuntu for a while; however, on modern Ubuntu installations, systemd is now used. Upstart was created to improve upon the issues with SysV, such as strict startup processes, blocking of tasks, etc. Upstart's event and job-driven model allow it to respond to events as they happen.

To find out if you are using Upstart, if you have a `/usr/share/upstart` directory, that's a pretty good indicator.

Jobs are the actions that Upstart performs, and events are messages that are received from other processes to trigger jobs. To see a list of jobs and their configuration:

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

Inside these job configurations, you'll find information on how and when to start jobs.

For example, in the `networking.conf` file, it could say something as simple as:

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

This means that it will start setting up networking on runlevel 2, 3, or 5 and will stop networking on runlevel 0. There are many ways to write the configuration file, and you'll discover that when you look at the different job configurations available.

The way that Upstart works is that:

1. First, it loads the job configurations from `/etc/init`.
2. Once a startup event occurs, it will run jobs triggered by that event.
3. These jobs will make new events, and then those events will trigger more jobs.
4. Upstart continues to do this until it completes all the necessary jobs.

## Exercise

Practice makes perfect! While Upstart is an older init system, understanding how processes are managed and tasks are scheduled is crucial for any Linux administrator. Here are some hands-on labs to reinforce your understanding of process management and task automation, which are foundational to how init systems operate:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with foreground and background processes, inspecting them with `ps`, monitoring resources with `top`, and terminating them with `kill`. This lab helps you understand the lifecycle of processes, which init systems like Upstart manage.
2. **[Schedule Tasks with at and cron in Linux](https://labex.io/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Learn to schedule one-time jobs with `at` and recurring tasks with `cron`. This provides practical experience with task automation, a core function that init systems facilitate for system services.

These labs will help you apply the concepts of process control and task automation in real scenarios, building confidence in managing a Linux system, regardless of the specific init system in use.

## Quiz Question

What is the init implementation that is used by Ubuntu?

## Quiz Answer

upstart
