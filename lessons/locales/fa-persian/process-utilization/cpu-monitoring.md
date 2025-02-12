# CPU Monitoring

## Lesson Content

Let's go over a useful command, <b>uptime</b>.

<pre>
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
</pre>

We talked about uptime in the first lesson of this course, but we haven't gone over the load average field. Load averages are good way to see the CPU load on your system. These numbers represent the average CPU load in 1, 5, and 15 minute intervals. What do I mean by CPU load, the CPU load is the average number of processes that are waiting to be executed by the CPU.

Let's say you have a single-core CPU, think of this core as a single lane in traffic. If it's rush hour on the freeway, this lane is gonna be really busy and traffic is gonna be at 100% or a load of 1. Now the traffic has become so bad, it's backing up the freeway and getting the regular roads busy by twice the amount of cars, we can say that your load is 200% or a load of 2. Now let's say it clears up a bit and there are only half as many cars on the freeway lane, we can say the load of the lane is 0.5. When traffic is non-existent and we can get home quicker, the load should ideally be very low, like 2am traffic low. The cars in this case are processes and these processes are just waiting to get off the freeway and get home.

Now just because you have a load average of 1 doesn't mean your computer is slogging around. Most modern machines these days have multiple cores. If you had a quad core processor (4 cores) and your load average is 1, it's really just affecting 25% of your CPU. Think of each core as a lane in traffic. You can view the amount of cores you have on your system with <b>cat /proc/cpuinfo</b>.

When observing load average, you have to take the number of cores into account, if you find that your machine is always using an above average load, there could something wrong going on. 

## Exercise

Check the load average of your system and see what it's doing. 

## Quiz Question

What command can you use to see the load average?

## Quiz Answer

uptime
