---
index: 4
lang: "en"
title: "CPU Monitoring"
meta_title: "CPU Monitoring - Process Utilization"
meta_description: "Learn CPU monitoring with the uptime command. Understand load average, CPU usage, and how to interpret system performance for Linux beginners."
meta_keywords: "uptime command, Linux CPU monitoring, load average, system performance, Linux tutorial, beginner guide"
---

## Lesson Content

Let's go over a useful command, **uptime**.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

We talked about uptime in the first lesson of this course, but we haven't gone over the load average field. Load averages are a good way to see the CPU load on your system. These numbers represent the average CPU load in 1, 5, and 15 minute intervals. What do I mean by CPU load? The CPU load is the average number of processes that are waiting to be executed by the CPU.

Let's say you have a single-core CPU; think of this core as a single lane in traffic. If it's rush hour on the freeway, this lane is going to be really busy, and traffic is going to be at 100% or a load of 1. Now the traffic has become so bad, it's backing up the freeway and getting the regular roads busy by twice the amount of cars; we can say that your load is 200% or a load of 2. Now let's say it clears up a bit and there are only half as many cars on the freeway lane; we can say the load of the lane is 0.5. When traffic is non-existent and we can get home quicker, the load should ideally be very low, like 2 AM traffic low. The cars in this case are processes, and these processes are just waiting to get off the freeway and get home.

Now, just because you have a load average of 1 doesn't mean your computer is slogging around. Most modern machines these days have multiple cores. If you had a quad-core processor (4 cores) and your load average is 1, it's really just affecting 25% of your CPU. Think of each core as a lane in traffic. You can view the amount of cores you have on your system with **cat /proc/cpuinfo**.

When observing load average, you have to take the number of cores into account. If you find that your machine is always using an above-average load, there could be something wrong going on.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of monitoring Linux system performance and CPU load:

1. **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with and inspecting processes, and monitoring resources with tools like `ps` and `top`, which directly relates to understanding CPU load.
2. **[Linux top Command: Real-time System Monitoring](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Learn to use the `top` command for real-time system monitoring, including sorting processes and filtering, providing a deeper dive into CPU and process activity.
3. **[Linux free Command: Monitoring System Memory](https://labex.io/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Learn to monitor and analyze system memory usage, which is often a critical factor alongside CPU load in overall system performance.

These labs will help you apply the concepts of system monitoring and resource management in real scenarios and build confidence with analyzing system performance.

## Quiz Question

What command can you use to see the load average?

## Quiz Answer

uptime
