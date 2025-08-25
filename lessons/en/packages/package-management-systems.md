---
index: 6
lang: "en"
title: "yum and apt"
meta_title: "yum and apt - Packages"
meta_description: "Learn yum and apt for Linux package management. Install, remove, and update software on Debian/RPM systems with this beginner tutorial. Get started today!"
meta_keywords: "yum, apt, Linux package management, apt tutorial, yum tutorial, Linux commands, beginner guide, package install"
---

## Lesson Content

Ah, the Batmans of package management! These systems come with all the fixings to make package installation, removal, and changes easier, including installing package dependencies. Two of the most popular management systems are **yum** and **apt**. Yum is exclusive to the Red Hat family, and apt is exclusive to the Debian family.

### Install a package from a repository

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Remove a package

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Updating packages for a repository

It's always best practice to update your package repositories so they are up to date before you install and update a package.

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### Get information about an installed package

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux package management:

1. **[Query and Update Packages with YUM in Linux](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Practice managing software packages on RHEL-based Linux systems using YUM, including inspecting, updating, and exploring repositories.
2. **[Software Installation on Linux](https://labex.io/labs/linux-software-installation-on-linux-18005)** - Learn various methods to install and manage software on Ubuntu systems, including using apt, dpkg, and handling .deb files.
3. **[Installing and Removing Packages](https://labex.io/labs/linux-installing-and-removing-packages-385380)** - Practice updating the system, installing and removing packages, and optimizing software configuration on a Debian-based system using `apt`.

These labs will help you apply the concepts in real scenarios and build confidence with Linux package management.

## Quiz Question

What command is used to show package information on a Debian system?

## Quiz Answer

apt show
