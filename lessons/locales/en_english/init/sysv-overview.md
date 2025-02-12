# System V Overview

## Lesson Content

The main purpose of init is to start and stop essential processes on the system. There are three major implementations of init in Linux, System V, Upstart and systemd. In this lesson, we're going to go over the most traditional version of init, System V init or Sys V (pronounced as 'System Five'). 

To find out if you are using the Sys V init implementation, if you have an /etc/inittab file you are most likely running Sys V. 

Sys V starts and stops processes sequentially, so let's say if you wanted to start up a service named foo-a, well before foo-b can work, you have to make sure foo-a is already running. Sys V does that with scripts, these scripts start and stop services for us, we can write our own scripts or most of the time use the ones that are already built in the operating system and are used to load essential services. 

The pros of using this implementation of init, is that it's relatively easy to solve dependencies, since you know foo-a comes before foo-b, however performance isn't great because usually one thing is starting or stopping at a time. 

When using Sys V, the state of the machine is defined by runlevels which are set from 0 to 6. These different modes will vary depending on the distribution, but most of the time will look like the following: 

<ul>
<li>0: Shutdown</li>
<li>1: Single User Mode</li>
<li>2: Multiuser mode without networking</li>
<li>3: Multiuser mode with networking</li>
<li>4: Unused</li>
<li>5: Multiuser mode with networking and GUI</li>
<li>6: Reboot</li>
</ul>

When your system starts up, it looks to see what runlevel you are in and executes scripts located inside that runlevel configuration. The scripts are located in <b>/etc/rc.d/rc[runlevel number].d/</b> or <b>/etc/init.d</b>. Scripts that start with S(start) or K(kill) will run on startup and shutdown, respectively. The numbers next to these characters are the sequence they run in. 

For example:

<pre>
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn        
</pre>

We see when we switch to runlevel 0 or shutdown mode, our machine will try to run a script to kill the updates services and then openvpn. To find out what runlevel your machine is booting into, you can see the default runlevel in the /etc/inittab file. You can also change your default runlevel in this file as well. 

One thing to note, System V is slowly getting replaced, maybe not today, or even years from now. However, you may see runlevels come up in other init implementations, this is primarily to support those services that are only started or stopped using System V init scripts. 

## Exercise

If you are running System V, change the default runlevel of your machine to something else and see what happens.

## Quiz Question

What runlevel is usually used for shutdown?

## Quiz Answer

0
