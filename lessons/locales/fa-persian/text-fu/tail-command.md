# tail

## Lesson Content

Similar to the head command, the tail command lets you see the last 10 lines of a file by default.

<pre>$ tail /var/log/syslog</pre>

Along with head you can change the number of lines you want to see.

<pre>$ tail -n 10 /var/log/syslog</pre>

Another great option you can use is the -f (follow) flag, this will follow the file as it grows. Give it a try and see what happens. 

<pre>$ tail -f /var/log/syslog</pre> 

Your syslog file will be continually changing while you interact with your system and using tail -f you can see everything that is getting added to that file.

## Exercise

Look at the man page of tail and read some of the other commands we didn't discuss. 

<pre>$ man tail</pre>

## Quiz Question

What is the flag used to follow a file in tail?

## Quiz Answer

-f