---
lang: "en"
title: "Boot Process Overview"
description: "Learn the Linux boot process stages: BIOS, bootloader, kernel, and init. Understand how Linux starts from power-on to login. Essential Linux beginner guide."
keywords: "Linux boot process, BIOS, bootloader, kernel, init, Linux tutorial, Linux guide, beginner"
---

## Lesson Content

Now that we've gotten a pretty good grasp of some of the important components of Linux, let's piece them all together by learning about how the system boots. When you turn on your machine, it does some neat things like show you the logo screen, run through some different messages, and then at the end, you're prompted with a login window. Well, there is actually a ton of stuff happening between when you push the power button to when you log in, and we'll discuss those in this course.

The Linux boot process can be broken down into 4 simple stages:

### 1. BIOS

The BIOS (stands for "Basic Input/Output System") initializes the hardware and makes sure with a Power-on Self-Test (POST) that all the hardware is good to go. The main job of the BIOS is to load the bootloader.

### 2. Bootloader

The bootloader loads the kernel into memory and then starts the kernel with a set of kernel parameters. One of the most common bootloaders is GRUB, which is a universal Linux standard.

### 3. Kernel

When the kernel is loaded, it immediately initializes devices and memory. The main job of the kernel is to load the init process.

### 4. Init

Remember, the init process is the first process that gets started. Init starts and stops essential service processes on the system. There are three major implementations of init in Linux distributions. We will go over them briefly and then dive into them in another course.

There it is, the (very) simple explanation of the Linux boot process. We will go into more detail about these stages in the next lessons.

## Exercise

Reboot your system and see if you can spot each step as your machine boots up.

## Quiz Question

What is the last stage in the Linux boot process?

## Quiz Answer

init
