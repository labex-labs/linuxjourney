# Upstart Jobs

## Lesson Content

Upstart can trigger a lot of events and jobs to run, unfortunately there is no easy way to see where an event or job originated, so you'll have to poke around the job configurations in /etc/init. Most of the time, you won't ever need to look at the Upstart job configuration files, but you will want to control some specific jobs more easily. There are a lot of useful commands you can use in an Upstart system. 

<b>View jobs</b>

<pre>initctl list

shutdown stop/waiting
console stop/waiting
...
</pre>

You'll see a list of Upstart jobs with different statuses applied to them. In each line, the job name is the first value and the second field (before the /) is actually the goal of the job, the third value (after the /) is the current status. So we see that our shutdown job eventually wants to stop, but it is currently in a state of waiting. The job status and goals will change as you start or stop jobs. 

<b>View specific job</b>

<pre>initctl status networking
networking start/running
</pre>

We won't get into the details of how to write an Upstart job configuration, however we already know that jobs are stopped, started and restarted in these configurations. These jobs also emit events, so they can start other jobs. We'll go through the manual commands of the Upstart operation, but if you are curious, you should dig into the .conf files in more depth.

<b>Manually start a job</b>

<pre>$ sudo initctl start networking</pre>

<b>Manually stop a job</b>

<pre>$ sudo initctl stop networking</pre>

<b>Manually restart a job</b>

<pre>$ sudo initctl restart networking</pre>

<b>Manually emit an event</b>

<pre>$ sudo initctl emit some_event</pre>

## Exercise

Observe your list of Upstart jobs, now change the job state with one of the commands we learned today. What do you notice afterwards?

## Quiz Question

How would I manually restart an Upstart job called peanuts?

## Quiz Answer

sudo initctl restart peanuts
