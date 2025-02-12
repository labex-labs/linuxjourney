# Disk Usage

## Lesson Content

There are a few tools you can used to see the utilization of your disks: 

<pre>
pete@icebox:~$ df -h
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
</pre>

The df command shows you the utilization of your currently mounted filesystems. The -h flag gives you a human readable format. You can see what the device is, and how much capacity is used and available. 

Let's say your disk is getting full and you want to know what files or directories are taking up that space, for that you can use the <b>du</b> command. 

<pre>$ du -h</pre>

This shows you the disk usage of the current directory you are in, you can take a peek at the root directory with <b>du -h /</b> but that can get a little cluttered.

Both of these commands are so similar in syntax it can be hard to remember which one to use, to check how much of your <b>disk</b> is <b>free</b> use df. To check <b>disk usage</b>, use du. 

## Exercise

Look at your disk usage and free space with both du and df. 

## Quiz Question

What command is use to show how much space is free on your disk?

## Quiz Answer

df
