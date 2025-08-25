---
index: 5
lang: "en"
title: "rpm and dpkg"
meta_title: "rpm and dpkg - Packages"
meta_description: "Learn to install, remove, and list packages using rpm and dpkg commands. Understand direct package management for .deb and .rpm files. Start your Linux journey!"
meta_keywords: "rpm, dpkg, Linux package management, .deb, .rpm, Linux tutorial, beginner guide, install packages"
---

## Lesson Content

Although most of this course is about package management systems (the Batmans of package management), we mustn't forget about the Robins. Although very useful and reliable, they don't come with that sweet Batmobile and utility belt.

Just like `.exe` is a single executable file, so is `.deb` and `.rpm`. You normally wouldn't see these if you use package repositories, but if you directly download packages, you will most likely get them in these popular formats. Obviously, they are exclusive to their distributions: `.deb` for Debian-based and `.rpm` for Red Hat-based.

To install these direct packages, you can use the package management commands: `rpm` and `dpkg`. These tools are used to install package files; however, they will not install the package dependencies. So, if your package had 10 dependencies, you would have to install those packages separately and then their dependencies, and so on and so forth. As you can see, that was one of the reasons that brought forth the full-blown management systems that we will discuss later.

Keep in mind that there will be countless times when you need to install, query, or verify a package with one of these tools, so remember these commands.

### Install a package

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

The `i` stands for install. You can also use the longer format of `--install`.

### Remove a package

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r` for remove
RPM: `e` for erase

### List installed packages

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l` for list
RPM: `q` for query and `a` for all

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of direct package management:

1. **[Managing Packages with RPM in Linux](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868)** - Gain hands-on experience querying package info, verifying integrity, listing dependencies, simulating removal, and inspecting RPM package contents with `rpm` and related tools.

This lab will help you apply the concepts of managing individual package files in a real scenario and build confidence with these essential Linux tools.

## Quiz Question

What is the package management tool for `.deb` files?

## Quiz Answer

dpkg
