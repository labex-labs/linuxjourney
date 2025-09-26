---
index: 5
lang: "en"
title: "Systemd Overview"
meta_title: "Systemd Overview - Init"
meta_description: "Learn Systemd basics: understand units, targets, and boot process. Discover how Systemd manages services and system states in Linux. Start your journey!"
meta_keywords: "Systemd, Systemd units, Systemd targets, Linux boot process, Linux services, beginner, tutorial, guide"
---

## Lesson Content

Systemd is the standard init system in most modern Linux distributions. If you have a `/usr/lib/systemd` directory, you're most likely using systemd.

Systemd uses goals to get your system up and running. Basically, you have a target that you want to achieve, and this target also has dependencies that need to be met. Systemd is extremely flexible and robust; it does not follow a strict sequence to get processes started. Here's what happens during a typical systemd boot:

1. First, systemd loads its configuration files, usually located in `/etc/systemd/system` or `/usr/lib/systemd/system`.
2. Then it determines its boot goal, which is usually `default.target`.
3. Systemd figures out the dependencies of the boot target and activates them.

Similar to SysV runlevels, systemd boots into different targets:

- `poweroff.target` - shutdown system
- `rescue.target` - single-user mode
- `multi-user.target` - multi-user with networking
- `graphical.target` - multi-user with networking and GUI
- `reboot.target` - restart

The default boot goal of `default.target` usually points to the `graphical.target`.

The main objects that systemd works with are known as units. Systemd doesn't just stop and start services; it can mount filesystems, monitor your network sockets, etc. Because of that robustness, it has different types of units it operates. The most common units are:

- Service units - these are the services we've been starting and stopping; these unit files end in `.service`.
- Mount units - These mount filesystems; these unit files end in `.mount`.
- Target units - These group together other units; the files end in `.target`.

For example, let's say we boot into our `default.target`. This target groups together the `networking.service` unit, `crond.service` unit, etc., so once we activate a single unit, everything below that unit gets activated as well.

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What unit is used to group together other units?

## Quiz Answer

target
