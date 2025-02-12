# lsof and fuser

## Lesson Content

Let's say you plugged in a USB drive and starting working on some files, once you were done, you go and unmount the USB device and you're getting an error "Device or Resource Busy". How would you find out which files in the USB drive are still in use? There are actually two tools you can use for this: 

<b>lsof</b>

Remember files aren't just text files, images, etc, they are everything on the system, disks, pipes, network sockets, devices, etc. To see what is in use by a process, you can use the lsof command (short for "list open files") this will show you a list of all the open files and their associated process. 

<pre>
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
indicator 1809 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
lsof      5915 pete  cwd    DIR    8,6     4096  131 .
</pre>

Now I can see what processes are currently holding the device/file open. In our USB example, you can also kill these processes so we can unmount this pesky drive.

<b>fuser</b>

Another way to track a process is the fuser command (short for "file user"), this will show you information about the process that is using the file or the file user. 

<pre>
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  1809 ..c.. indicator-power
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
</pre>

We can see which processes are currently using our /home/pete directory. The lsof and fuser tools are very similar, familiarize yourself with these tools and try using them next time you need to track a file or process down.

## Exercise

Read the manpages for lsof and fuser, there is a lot of information that we didn't cover that allows you to have greater flexibility with these tools.

## Quiz Question

What command is used to list open files and their process information?

## Quiz Answer

lsof