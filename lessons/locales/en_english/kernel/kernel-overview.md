# Overview of the Kernel

## Lesson Content

As you've learned up to this point, the kernel is the core of the operating system. We've talked about the other parts of the operating system but have yet to show how they all work together. The Linux operating system can be organized into three different levels of abstraction.

The most basic level is hardware, this includes our CPU, memory, hard disks, networking ports, etc. The physical layer that actually computes what our machine is doing.

The next level is the kernel, which handles process and memory management, device communication, system calls, sets up our filesystem, etc. The kernel's job is to talk to the hardware to make sure it does what we want our processes to do. 

And the level that you are familiar with is the user space, the user space includes the shell, the programs that you run, the graphics, etc.

In this course, we'll be focusing on the kernel and learning its intricacies.

## Exercise

No exercises for this lesson.

## Quiz Question

What level of the operating system manages devices?

## Quiz Answer

kernel
