# General Logging

## Lesson Content

There are many log files you can view on your system; many important ones can be found under `/var/log`. We won't go through them all, but we'll discuss a couple of the major ones.

There are two general log files you can view to get a glimpse of what your system is doing:

**`/var/log/messages`**

This log contains all non-critical and non-debug messages, including messages logged during boot-up (dmesg), auth, cron, daemon, etc. It is very useful to get a glimpse of how your machine is acting.

**`/var/log/syslog`**

This logs everything except auth messages; it's extremely useful for debugging errors on your machine.

These two logs should be more than enough when troubleshooting issues with your system. However, if you just want to view a specific log component, there are also separate logs for those as well.

## Exercise

Look at your `/var/log/messages` and `/var/log/syslog` files and see what the differences are.

## Quiz Question

What log file logs everything except auth messages?

## Quiz Answer

syslog
