# Memory Monitoring

## Lesson Content

In addition to CPU monitoring and I/O monitoring you can monitor your memory usage with <b>vmstat</b>

<pre>
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
</pre>

The fields are as follows:

<b>procs</b>
<ul>
<li>r - Number of processes for run time</li>
<li>b - Number of processes in uninterruptible sleep</li>
</ul>

<b>memory</b>
<ul>
<li>swpd - Amount of virtual memory used</li>
<li>free - Amount of free memory</li>
<li>buff - Amount of memory used as buffers</li>
<li>cache - Amount of memory used as cache</li>
</ul>

<b>swap</b>
<ul>
<li>si - Amount of memory swapped in from disk</li>
<li>so - Amount of memory swapped out to disk</li>
</ul>

<b>io</b>
<ul>
<li>bi - Amount of blocks received in from a block device</li>
<li>bo - Amount of blocks sent out to a block device</li>
</ul>

<b>system</b>
<ul>
<li>in - Number of interrupts per second</li>
<li>cs - Number of context switches per second</li>
</ul>

<b>cpu</b>
<ul>
<li>us - Time spent in user time</li>
<li>sy - Time spent in kernel time</li>
<li>id - Time spent idle</li>
<li>wa - Time spent waiting for IO</li>
</ul>

## Exercise

Look at your memory usage with vmstat.

## Quiz Question

What tool is used to view memory utilization?

## Quiz Answer

vmstat
