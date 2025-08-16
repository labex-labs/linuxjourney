---
title: "Package Repositories"
description: "Learn about Linux package repositories and how they manage software. Discover how to find and add package sources like /etc/apt/sources.list for easy installation."
keywords: "Linux package repositories, apt sources list, /etc/apt/sources.list, Linux packages, beginner Linux, Linux tutorial, package management"
---

## Lesson Content

How do packages uploaded to the internet end up on our computers? Do you go to the download page of each package you want and click download and install? While you can do that, there's a better solution: package repositories. Repositories are central storage locations for packages. There are tons of repositories holding many packages, and best of all, they are all found on the internet—no silly installation disks. Your machine doesn't know where to look for these repositories unless you explicitly tell it where to look.

For example, let's say I want WackyWidgets Software on my machine. WackyWidgets manages its own repositories for its widget packages. Inside this repository are 10 packages, such as the CoolWidget package, the SuperWidget package, etc. WackyWidgets hosts this repository at a source link called: <http://download.widgets/linux/deb/>

Now, instead of going to their website to download the package directly, you can tell your machine to find WackyWidgets software from the source link.

Your distribution already comes with pre-approved sources to get packages from, and this is how it installs all the base packages you see on your system. On a Debian system, this sources file is the `/etc/apt/sources.list` file. Your machine will know to look there and check for any source repositories you added.

## Exercise

No exercises for this lesson.

## Quiz Question

Where is the sources file in a Debian system?

## Quiz Answer

/etc/apt/sources.list
