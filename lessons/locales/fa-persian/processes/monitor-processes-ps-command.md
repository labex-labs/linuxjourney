# ps (Processes)

## Lesson Content

Processes are the programs that are running on your machine. They are managed by the kernel and each process has an ID associated with it called the <b>process ID (PID).</b> This PID is assigned in the order that processes are created. 

Go ahead and run the ps command to see a list of running processes:

<pre>$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
</pre>

This shows you a quick snapshot of the current processes:

<ul>
<li>PID: Process ID</li>
<li>TTY: Controlling terminal associated with the process (we'll go in detail about this later)</li>
<li>STAT: Process status code</li>
<li>TIME: Total CPU usage time</li>
<li>CMD: Name of executable/command</li>
</ul>

If you look at the man page for ps you'll see that there are lots of command options you can pass, they will vary depending on what options you want to use - BSD, GNU or Unix. In my opinion the BSD style is more popular to use, so we're gonna go with that. If you are curious the difference between the styles is the amount of dashes you use and the flags.

<pre>$ ps aux</pre>

The <b>a</b> displays all processes running, including the ones being ran by other users. The <b>u</b> shows more details about the processes. And finally the <b>x</b> lists all processes that don't have a TTY associated with it, these programs will show a ? in the TTY field, they are most common in daemon processes that launch as part of the system startup.

You'll notice you're seeing a lot more fields now, no need to memorize them all, in a later course on advanced processes, we'll go over some of these again:

<ul>
<li>USER: The effective user (the one whose access we are using)</li>
<li>PID: Process ID</li>
<li>%CPU: CPU time used divided by the time the process has been running</li>
<li>%MEM: Ratio of the process's resident set size to the physical memory on the machine</li>
<li>VSZ: Virtual memory usage of the entire process</li>
<li>RSS: Resident set size, the non-swapped physical memory that a task has used</li>
<li>TTY: Controlling terminal associated with the process</li>
<li>STAT: Process status code</li>
<li>START: Start time of the process</li>
<li>TIME: Total CPU usage time</li>
<li>COMMAND: Name of executable/command</li>
</ul>

The ps command can get a little messy to look at, for now the fields we will look at the most are PID, STAT and COMMAND. 

Another very useful command is the <b>top</b> command, top gives you real time information about the processes running on your system instead of a snapshot. By default you'll get a refresh every 10 seconds. Top is an extremely useful tool to see what processes are taking up a lot of your resources. 

<pre>$ top</pre>

## Exercise

Use the ps command with different flags and see how the output changes. 

## Quiz Question

What ps flag is used to view detailed information about processes?

## Quiz Answer

u