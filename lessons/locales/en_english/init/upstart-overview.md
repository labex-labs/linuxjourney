# Upstart Overview

## Lesson Content

Upstart was developed by Canonical, so it was the init implementation on Ubuntu for a while, however on modern Ubuntu installations systemd is now used. Upstart was created to improve upon the issues with Sys V, such as the strict startup processes, blocking of tasks, etc. Upstart's event and job driven model allow it to respond to events as they happen. 

To find out if you are using Upstart, if you have a /usr/share/upstart directory that's a pretty good indicator. 

Jobs are the actions that Upstart performs and events are messages that are received from other processes to trigger jobs. To see a list of jobs and their configuration:

<pre>
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
</pre>

Inside these job configurations, it'll include information on how to start jobs and when to start jobs.

For example, in the networking.conf file, it could say something as simple as:
<pre>
start on runlevel [235]
stop on runlevel [0]
</pre>

This means that it will start setting up networking on runlevel 2, 3 or 5 and will stop networking on runlevel 0. There are many ways to write the configuration file and you'll discover that when you look at the different job configurations available. 

The way that Upstart works is that: 

<ol>
<li>First, it loads up the job configurations from /etc/init</li>
<li>Once a startup event occurs, it will run jobs triggered by that event.</li>
<li>These jobs will make new events and then those events will trigger more jobs</li>
<li>Upstart continues to do this until it completes all the necessary jobs</li>
</ol>

## Exercise

If you are running Upstart, see if you can make sense of the job configurations in /etc/init.

## Quiz Question

What is the init implementation that is used by Ubuntu?

## Quiz Answer

upstart
