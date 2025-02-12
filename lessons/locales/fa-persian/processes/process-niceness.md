# niceness

## Lesson Content

When you run multiple things on your computer, like perhaps Chrome, Microsoft Word or Photoshop at the same time, it may seem like these processes are running at the same time, but that isn't quite true. 

Processes use the CPU for a small amount of time called a time slice. Then they pause for milliseconds and another process gets a little time slice. By default, process scheduling happens in this round-robin fashion. Every process gets enough time slices until it's finished processing. The kernel handles all of these switching of processes and it does a pretty good job at it most of the time.

Processes aren't able to decide when and how long they get CPU time, if all processes behaved normally they would each (roughly) get an equal amount of CPU time. However, there is a way to influence the kernel's process scheduling algorithm with a nice value. Niceness is a pretty weird name, but what it means is that processes have a number to determine their priority for the CPU. A high number means the process is nice and has a lower priority for the CPU and a low or negative number means the process is not very nice and it wants to get as much of the CPU as possible. 

<pre>$ top</pre>

You can see a column for NI right now, that is the niceness level of a process.

To change the niceness level you can use the nice and renice commands:

<pre>$ nice -n 5 apt upgrade</pre>

The nice command is used to set priority for a new process. The renice command is used to set priority on an existing process. 

<pre>$ renice 10 -p 3245</pre>

## Exercise

What processes aren't very nice and why?

## Quiz Question

If I want a process to get more CPU priority, do I use a lower or higher nice number?

## Quiz Answer

lower
