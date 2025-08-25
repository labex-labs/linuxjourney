---
index: 4
lang: "en"
title: "Upstart Jobs"
meta_title: "Upstart Jobs - Init"
meta_description: "Learn to manage Upstart jobs in Linux using initctl commands. Understand job status, start, stop, and restart services. Improve your Linux system administration skills."
meta_keywords: "Upstart jobs, initctl, Linux services, system administration, Linux tutorial, beginner guide"
---

## Lesson Content

Upstart can trigger a lot of events and jobs to run. Unfortunately, there is no easy way to see where an event or job originated, so you'll have to poke around the job configurations in `/etc/init`. Most of the time, you won't ever need to look at the Upstart job configuration files, but you will want to control some specific jobs more easily. There are a lot of useful commands you can use in an Upstart system.

### View jobs

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

You'll see a list of Upstart jobs with different statuses applied to them. In each line, the job name is the first value, and the second field (before the `/`) is actually the goal of the job. The third value (after the `/`) is the current status. So, we see that our `shutdown` job eventually wants to stop, but it is currently in a state of waiting. The job status and goals will change as you start or stop jobs.

### View specific job

```plaintext
initctl status networking
networking start/running
```

We won't get into the details of how to write an Upstart job configuration; however, we already know that jobs are stopped, started, and restarted in these configurations. These jobs also emit events, so they can start other jobs. We'll go through the manual commands of the Upstart operation, but if you are curious, you should dig into the `.conf` files in more depth.

### Manually start a job

```bash
sudo initctl start networking
```

### Manually stop a job

```bash
sudo initctl stop networking
```

### Manually restart a job

```bash
sudo initctl restart networking
```

### Manually emit an event

```bash
sudo initctl emit some_event
```

## Exercise

Practice makes perfect! While there are no specific labs for Upstart, understanding how to schedule and manage tasks is crucial for controlling system processes. Here's a hands-on lab to reinforce your understanding of task management:

1. **[Schedule Tasks with at and cron in Linux](https://labex.io/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Practice creating, managing, and removing one-time and recurring jobs, which are fundamental concepts related to how services and tasks are managed in Linux environments like those handled by Upstart.

This lab will help you apply the concepts of task automation in real scenarios and build confidence with managing system operations.

## Quiz Question

How would I manually restart an Upstart job called `peanuts`?

## Quiz Answer

sudo initctl restart peanuts
