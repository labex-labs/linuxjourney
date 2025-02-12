# Process States

## Lesson Content

Let's take a look at the ps aux command again:

<pre>$ ps aux</pre>

In the STAT column, you'll see lots of values. A linux process can be in a number of different states. The most common state codes you'll see are described below:

<ul>
<li>R: running or runnable, it is just waiting for the CPU to process it</li>
<li>S: Interruptible sleep, waiting for an event to complete, such as input from the terminal</li>
<li>D: Uninterruptible sleep, processes that cannot be killed or interrupted with a signal, usually to make them go away you have to reboot or fix the issue</li>
<li>Z: Zombie, we discussed in a previous lesson that zombies are terminated processes that are waiting to have their statuses collected</li>
<li>T: Stopped, a process that has been suspended/stopped</li>
</ul>

## Exercise

Take a look at the running processes on your system and check out their process states.

## Quiz Question

What STAT code is used to represent an uninterruptible sleep? 

## Quiz Answer

D