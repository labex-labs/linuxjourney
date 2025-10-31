---
index: 5
lang: "en"
title: "Systemd Overview"
meta_title: "Systemd Overview - Init"
meta_description: "Learn the fundamentals of the systemd init system. This guide covers how systemd (or system d) uses units and targets to manage the Linux boot process and system services. Understand the core concepts of the modern standard for Linux initialization."
meta_keywords: "systemd, system d, init system, systemd units, systemd targets, linux boot process, linux services, system management, beginner, tutorial"
---

## Lesson Content

### What is Systemd?

Systemd is the default init system and service manager for most modern Linux distributions. It is responsible for initializing the system in the correct order after the kernel is loaded. A simple way to check if your system uses it is to see if the `/usr/lib/systemd` directory exists. If it does, you are likely running a system managed by **systemd**.

### The Systemd Boot Process

Instead of rigid sequential scripts, **systemd** uses the concept of "goals" to bring your system to a functional state. It identifies a primary goal, or `target`, and works to satisfy its dependencies. This approach allows for greater flexibility and parallelization during startup. A typical boot process managed by **systemd** follows these steps:

1.  **systemd** first loads its configuration files from directories like `/etc/systemd/system` and `/usr/lib/systemd/system`.
2.  It then identifies the default boot goal, which is typically a symbolic link named `default.target`.
3.  Finally, **systemd** resolves all dependencies for this target and activates the necessary units to achieve the desired system state.

### Understanding Systemd Targets

Targets in **systemd** are analogous to runlevels in the older SysV init system. They represent different states the system can be in. Common targets include:

- `poweroff.target`: Shuts down the system.
- `rescue.target`: Boots into a single-user shell for maintenance.
- `multi-user.target`: A standard multi-user environment with networking but no graphical interface.
- `graphical.target`: A full multi-user environment with networking and a graphical user interface (GUI).
- `reboot.target`: Restarts the system.

The `default.target` is a symbolic link that points to the target the system will boot into by default, often `graphical.target` on desktop systems.

### Core Concept: Systemd Units

The fundamental objects that **systemd** manages are called "units." A unit is a configuration file that describes a resource or service. The power of the **system d** architecture lies in its ability to manage various types of resources, not just services. Each unit type is identified by its file extension. The most common types are:

- **Service units (`.service`):** These manage system daemons or services, such as a web server or a database.
- **Mount units (`.mount`):** These control filesystem mount points.
- **Target units (`.target`):** These are used to group other units together, creating synchronization points during boot-up.

For instance, when the system boots into `graphical.target`, that target unit ensures that all its dependencies, such as `multi-user.target` and various service units like `network.service`, are started first.

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What unit is used to group together other units? Please answer in a single lowercase English word.

## Quiz Answer

target
