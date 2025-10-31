---
index: 6
lang: "en"
title: "Systemd Goals"
meta_title: "Systemd Goals - Init"
meta_description: "Explore systemd goals and learn to manage Linux services using essential systemctl commands. This guide covers systemd unit file basics, how to start, stop, and enable services, and view their status."
meta_keywords: "systemd, systemctl, Linux services, unit files, systemd goals, service management, systemd units, beginner, tutorial, guide, Linux commands"
---

## Lesson Content

This lesson provides a foundational overview of systemd unit files and how to manage them with `systemctl`, the primary tool for controlling the init system. We will cover the basic structure of a unit file and the essential commands for managing Linux services.

### Understanding a Systemd Unit File

A systemd unit file is a plain text file that describes a service, a mount point, a device, or another resource that systemd can manage. Here is a basic example of a service unit file named `foobar.service`:

```
[Unit]
Description=My Foobar Service
After=network.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

This simple service file is divided into sections:

- **[Unit]**: This section contains metadata and dependency information. The `Description` provides a human-readable name for the unit. Directives like `After` and `Before` control the startup order, ensuring this unit starts after the network is available.
- **[Service]**: This section defines how to manage the service. The `ExecStart` directive is crucial, as it specifies the command to execute to start the service. Other directives like `ExecStop` and `ExecReload` can define how to stop or reload the service.
- **[Install]**: This section defines the behavior of the unit when it is enabled or disabled with `systemctl`. The `WantedBy` directive tells systemd to start this service as part of a specific target, such as the `multi-user.target` for a standard non-graphical boot.

This is just a glimpse into systemd unit files. For more advanced configurations, further reading on the topic is highly recommended.

### Essential Systemctl Commands

Now, let's explore the essential `systemctl` commands you'll use to interact with systemd units and manage Linux services.

### Listing Systemd Units

To see all active units that systemd is currently managing, use the `list-units` command.

```bash
systemctl list-units
```

### Checking a Unit's Status

To view the detailed status of a specific unit, including whether it's active, enabled, and its latest log entries, use the `status` command.

```bash
systemctl status networking.service
```

### Managing Service States

You can control the runtime state of a service using `start`, `stop`, and `restart`.

To start a service immediately:

```bash
sudo systemctl start networking.service
```

To stop a running service:

```bash
sudo systemctl stop networking.service
```

To stop and then start the service again:

```bash
sudo systemctl restart networking.service
```

### Enabling and Disabling Services

Enabling a service creates a symbolic link that hooks it into the boot process, ensuring it starts automatically. Disabling it removes that link.

To enable a service to start on boot:

```bash
sudo systemctl enable networking.service
```

To disable a service from starting on boot:

```bash
sudo systemctl disable networking.service
```

These commands are the building blocks for service management on modern Linux systems. Mastering them is a key step in your Linux journey.

## Exercise

Practice is key to mastering new skills. This hands-on lab will help reinforce your understanding of managing processes, which are often controlled by systemd services:

1.  **[Manage and Monitor Linux Processes](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practice interacting with foreground and background processes, inspecting them with `ps`, monitoring resources with `top`, adjusting priority with `renice`, and terminating them with `kill`. This lab will give you practical experience with the runtime effects of systemd unit management.

This lab will help you apply these concepts in a real-world scenario and build confidence with process management in Linux.

## Quiz Question

What is the command to start a service named peanut.service? Please answer in English. The answer is case-sensitive.

## Quiz Answer

sudo systemctl start peanut.service
