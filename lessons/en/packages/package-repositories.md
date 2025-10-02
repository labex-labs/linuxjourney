---
index: 2
lang: "en"
title: "Package Repositories"
meta_title: "Package Repositories - Packages"
meta_description: "Learn about Linux package repositories and how they manage software. Discover how to find and add package sources like /etc/apt/sources.list for easy installation."
meta_keywords: "Linux package repositories, apt sources list, /etc/apt/sources.list, Linux packages, beginner Linux, Linux tutorial, package management"
---

## Lesson Content

How do packages uploaded to the internet end up on our computers? Do you go to the download page of each package you want and click download and install? While you can do that, there's a better solution: package repositories. Repositories are central storage locations for packages. There are tons of repositories holding many packages, and best of all, they are all found on the internet—no silly installation disks. Your machine doesn't know where to look for these repositories unless you explicitly tell it where to look.

For example, let's say I want Docker Software on my machine. Docker manages its own repositories for its container packages. Inside this repository are multiple packages, such as the docker-ce package, docker-ce-cli package, containerd.io package, etc. Docker hosts this repository at a source link called: `https://download.docker.com/linux/ubuntu`

Now, instead of going to their website to download the package directly, you can tell your machine to find Docker software from the source link.

Your distribution already comes with pre-approved sources to get packages from, and this is how it installs all the base packages you see on your system. On a Debian system, this sources file is the `/etc/apt/sources.list` file. Your machine will know to look there and check for any source repositories you added.

> **Note:** On older Debian/Ubuntu systems, repositories are configured in `/etc/apt/sources.list`, while newer Ubuntu versions (22.04+) use structured files in `/etc/apt/sources.list.d/` like `ubuntu.sources`. Both formats are supported by apt.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux package management and repositories:

1. **[Software Installation on Linux](https://labex.io/labs/linux-software-installation-on-linux-18005)** - Practice various methods to install and manage software on Ubuntu systems, including using apt and handling .deb files, directly relating to the `sources.list` concept.
2. **[Installing and Removing Packages](https://labex.io/labs/linux-installing-and-removing-packages-385380)** - Learn to update the system, install, and remove packages on a Debian-based system, solidifying your understanding of how package managers interact with repositories.
3. **[Query and Update Packages with YUM in Linux](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Explore how to manage software packages on RHEL-based Linux systems using YUM, providing a broader perspective on package management across different distributions.

These labs will help you apply the concepts of package repositories and software management in real scenarios and build confidence with system administration tasks.

## Quiz Question

Where is the sources file in a Debian system?

## Quiz Answer

/etc/apt/sources.list
