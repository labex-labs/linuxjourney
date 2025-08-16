# Memory Monitoring

## Lesson Content

In addition to CPU monitoring and I/O monitoring, you can monitor your memory usage with **vmstat**.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

The fields are as follows:

**procs**

- r - Number of processes for run time
- b - Number of processes in uninterruptible sleep

**memory**

- swpd - Amount of virtual memory used
- free - Amount of free memory
- buff - Amount of memory used as buffers
- cache - Amount of memory used as cache

**swap**

- si - Amount of memory swapped in from disk
- so - Amount of memory swapped out to disk

**io**

- bi - Amount of blocks received in from a block device
- bo - Amount of blocks sent out to a block device

**system**

- in - Number of interrupts per second
- cs - Number of context switches per second

**cpu**

- us - Time spent in user time
- sy - Time spent in kernel time
- id - Time spent idle
- wa - Time spent waiting for IO

## Exercise

Look at your memory usage with vmstat.

## Quiz Question

What tool is used to view memory utilization?

## Quiz Answer

vmstat
