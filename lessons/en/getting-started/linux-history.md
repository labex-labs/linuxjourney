---
lesson_id: "linux-history"
course_id: "getting-started"
lang: "en"
order_index: 1
title: "Linux History"
description: "Learn how UNIX, GNU, and the Linux kernel contributed to modern Linux systems."
meta_title: "Linux History - Getting Started"
meta_description: "Begin your Linux journey by exploring the history of Linux. Learn about its origins from UNIX, the GNU project, and the creation of the Linux kernel by Linus Torvalds."
meta_keywords: "history of linux, linux history, linux journey, UNIX, GNU project, Linus Torvalds, Linux kernel, beginner Linux"
---

Welcome to your **Linux Journey**! If you're ready to dive into the powerful world of Linux, you've come to the right place. My name is Penguin Pete, and I'll be your guide. To get started, let's explore a brief **history of Linux**.

## The Predecessors of Linux

To understand how Linux was created, we must go back to 1969 when Ken Thompson and Dennis Ritchie of Bell Laboratories developed the UNIX operating system. It was later rewritten in the C programming language, which made it portable and led to its widespread adoption.

![Timeline of Unix](https://file.labex.io/images/ed9c245d-e8be-4287-bf34-67750b042542.jpg)

:::single-choice{#understand-unix-portability} What was an important result of rewriting UNIX in C?

::option[It became the free kernel created for the GNU system.]{#unix-became-gnu-kernel explanation="UNIX existed before the GNU project and was not GNU's kernel. GNU later began developing a separate kernel called the Hurd."}
::option[It became easier to move across different hardware systems.]{#portable-across-hardware .correct explanation="Writing UNIX in C made it more portable. That portability helped it spread beyond its original hardware."}
::option[It became a command shell used only at Bell Labs.]{#unix-became-shell explanation="UNIX is an operating system rather than only a shell. Rewriting it in C helped adoption beyond Bell Labs."}
:::

Over a decade later, Richard Stallman initiated the GNU project. GNU is a recursive acronym for "GNU's Not UNIX," and its goal was to create a completely free and open-source UNIX-like operating system. The project produced many essential components and the GNU General Public License (GPL), but its own kernel, the GNU Hurd, was not ready for general use when Linux became available.

:::single-choice{#identify-gnu-missing-component} Which major GNU component was not ready when Linux became available?

::option[A production-ready kernel]{#gnu-kernel .correct explanation="GNU had produced many system components, but its own kernel, the GNU Hurd, was not ready for general use."}
::option[A free software license]{#gnu-license explanation="The GNU project had already produced the GNU General Public License. The missing system component was a usable kernel."}
::option[Essential system tools]{#gnu-tools explanation="GNU had already produced many essential tools. Its kernel remained the major unfinished part of the system."}
:::

## The Role of the Kernel

The kernel is the core component of an operating system. It acts as a bridge, allowing the hardware to communicate with the software. The kernel manages system resources, such as the CPU, memory, and peripheral devices. A complete operating system needs this resource-managing core in addition to the tools and applications people use.

:::single-choice{#recognize-kernel-role} Which responsibility belongs to the operating system kernel?

::option[Writing every command entered in the shell]{#write-shell-commands explanation="People or scripts provide shell commands. The kernel supplies the lower-level resources needed when programs run those commands."}
::option[Choosing the license for every installed application]{#choose-software-licenses explanation="Software authors and distributors choose application licenses. License selection is not a kernel resource-management task."}
::option[Managing the CPU, memory, and connected devices]{#manage-system-resources .correct explanation="The kernel manages hardware resources and makes them available to software. CPU time, memory, and devices are central examples."}
:::

## The Birth of the Linux Kernel

This brings us to 1991, when a Finnish student named Linus Torvalds began developing a new kernel as a personal project. This kernel became known as the Linux kernel. After Linux was released as free software in 1992, it could be combined with the nearly complete GNU system to form a complete free operating system, commonly called GNU/Linux. This milestone was a pivotal moment in the **history of Linux**.

![Linus Torvalds in 2018](https://file.labex.io/images/3e1311fd-b8ca-45e7-8d02-9aac6377bb36.jpg)

_Linus Torvalds in 2018 (Source: [Wikipedia](https://en.wikipedia.org/wiki/Linus_Torvalds))_

:::single-choice{#identify-linux-kernel-creator} Who began developing the Linux kernel in 1991?

::option[Richard Stallman]{#richard-stallman explanation="Richard Stallman initiated the GNU project. GNU supplied many system components, but Linus Torvalds began the Linux kernel."}
::option[Dennis Ritchie]{#dennis-ritchie explanation="Dennis Ritchie helped develop UNIX and the C programming language. The Linux kernel project was started later by Linus Torvalds."}
::option[Linus Torvalds]{#linus-torvalds .correct explanation="Linus Torvalds began the kernel project in 1991. That project became the Linux kernel."}
:::

To continue your **Linux journey**, try these hands-on labs to practice fundamental commands and build your confidence in the command-line environment.

1. **[Getting Started with Linux](https://labex.io/labs/linux-getting-started-with-linux-446315)** - Begin your Linux journey by learning essential terminal commands like `echo`, `date`, and basic calculations. Perfect for complete beginners.
2. **[Your First Linux Lab](https://labex.io/labs/linux-your-first-linux-lab-270253)** - This introductory lab guides you through the classic "Hello, World!" program in Linux and teaches you some fundamental commands.
3. **[Create Personalized Terminal Greeting](https://labex.io/labs/linux-create-personalized-terminal-greeting-446322)** - A quick and fun challenge to use basic Linux terminal commands to create an engaging welcome message.

## Summary

You can now explain how UNIX, GNU, and the Linux kernel contributed to modern Linux systems.

1. Describe why UNIX portability mattered.
2. Identify the kernel as GNU's major missing component.
3. Explain the kernel's role in managing system resources.
4. Identify Linus Torvalds as the creator of the Linux kernel.
