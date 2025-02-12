# Process Details

## Lesson Content

Before we get into more practical applications of processes, we have to first understand what they are and how they work. This part can get confusing since we are diving into the nitty gritty, so feel free to come back to this lesson if you don't want to learn about it now. 

A process like we said before is a running program on the system, more precisely it's the system allocating memory, CPU, I/O to make the program run. A process is an instance of a running program, go ahead and open 3 terminal windows, in two windows, run the <b>cat</b> command without passing any options (the cat process will stay open as a process because it expects stdin). Now in the third window run: <b>ps aux | grep cat</b>. You'll see that there are two processes for cat, even though they are calling the same program.

The kernel is in charge of processes, when we run a program the kernel loads up the code of the program in memory, determines and allocates resources and then keeps tabs on each process, it knows: 

<ul>
<li>The status of the process</li>
<li>The resources the process is using and receives</li>
<li>The process owner</li>
<li>Signal handling (more on that later)</li>
<li>And basically everything else</li>
</ul>

All processes are trying to get a taste of that sweet resource pie, it's the kernel's job to make sure that processes get the right amount of resources depending on process demands. When a process ends, the resources it used are now freed up for other processes.

## Exercise

No exercises for this lesson.

## Quiz Question

What manages and controls processes?

## Quiz Answer

kernel