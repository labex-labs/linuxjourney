---
index: 4
lang: "en"
title: "NFS"
meta_title: "NFS - Network Sharing"
meta_description: "Discover how to use the Network File System (NFS) in Linux. This lesson covers setting up an NFS client, using the mount command, and configuring automount for seamless access to network shares."
meta_keywords: "NFS, NFS client, automount, Network File System, Linux networking, mount command, Linux tutorial, beginner"
---

## Lesson Content

The most standard protocol for network file sharing in Linux is NFS, which stands for **Network File System**. NFS allows a server to share its directories and files with one or more client machines over a network, making them appear as if they were local resources.

This lesson will focus on the configuration of an **NFS client**, as setting up an NFS server can be a more complex process.

### Mounting an NFS Share

To connect to an NFS share, you first need to ensure the NFS client service is running. Then, you can use the `mount` command to attach the remote directory to a local mount point on your system.

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

In this example, `server:/directory` is the remote share you want to access, and `/mount_directory` is the local directory where the share will be mounted.

### Using Automount for NFS

If you frequently access an NFS share, you might consider making the mount permanent. While adding an entry to the `/etc/fstab` file is a common method for local drives, it can cause significant boot delays or even failures if the network connection or NFS server is unavailable during startup.

A better solution for network shares is **automount**. This service, managed by the `automount` tool or its modern implementation `amd`, dynamically mounts a filesystem on-demand. When a file or directory within a specified path is accessed, automount automatically connects to the remote server and mounts the share. This ensures seamless access when needed without impacting the system's boot process.

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What tool is used to manage mount points automatically? Please answer in English, and note that the answer is case-sensitive.

## Quiz Answer

automount
