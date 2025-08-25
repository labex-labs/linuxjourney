---
index: 7
lang: "en"
title: "Power States"
meta_title: "Power States - Init"
meta_description: "Learn Linux system power states: shutdown, reboot, and halt commands. Understand how to safely power off or restart your Linux system. Get started with essential commands!"
meta_keywords: "Linux shutdown, reboot command, halt system, power off Linux, Linux commands, beginner Linux, Linux tutorial, system states"
---

## Lesson Content

It's hard to believe we haven't actually discussed ways to control your system state through the command line. When talking about `init`, we not only discuss the modes that start our system but also the ones that stop it.

To shut down your system:

```bash
sudo shutdown -h now
```

This command will halt the system (power it off). You must also specify a time when you want this to take place. You can add a time in minutes that will shut down the system in that amount of time.

```bash
sudo shutdown -h +2
```

This will shut down your system in two minutes. You can also restart with the `shutdown` command:

```bash
sudo shutdown -r now
```

Or just use the `reboot` command:

```bash
sudo reboot
```

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What is the command to power off your system in 4 minutes?

## Quiz Answer

sudo shutdown -h +4
