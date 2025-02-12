# Privilege Levels

## Lesson Content

The next few lessons get pretty theoretical, so if you're looking for some practical stuff you can skip ahead and come back later.

Why do we have different abstraction layers for user space and kernel? Why can't you combine both powers into one layer? Well there is a very good reason why these two layers exist separately. They both operate in different modes, the kernel operates in kernel mode and the user space operates in user mode. 

In kernel mode, the kernel has complete access to the hardware, it controls everything. In user space mode, there is a very small amount of safe memory and CPU that you are allowed to access. Basically, when we want to do anything that involves hardware, reading data from our disks, writing data to our disks, controlling our network, etc, it is all done in kernel mode. Why is this necessary? Imagine if your machine was infected with spyware, you wouldn't want it to be able to have direct access to your system's hardware. It can access all your data, your webcam, etc. and that's no good. 

These different modes are called privilege levels (aptly named for the levels of privilege you get) and are often described as protection rings. To make this picture easier to paint, let's say you find out that Britney Spears is in town at your local klerb, she's protected by her groupies, then her personal bodyguards, then the bouncer outside the klerb. You want to get her autograph (because why not?), but you can't get to her because she is heavily protected. The rings work the same way, the innermost ring corresponds to the highest privilege level. There are two main levels or modes in an x86 computer architecture. Ring #3 is the privilege that user mode applications run in, Ring #0 is the privilege that the kernel runs in. Ring #0 can execute any system instruction and is given full trust. So now that we know how those privilege levels work, how are we able to write anything to our hardware? Won't we always be in a different mode than the kernel? 

The answer is with system calls, system calls allow us to perform a privileged instruction in kernel mode and then switch back to user mode.

## Exercise

No exercises for this lesson.

## Quiz Question

What ring number has the highest privileges?

## Quiz Answer

0
