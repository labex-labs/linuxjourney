# Job Control

## Lesson Content

Let's say you're working on a single terminal window and you're running a command that is taking forever. You can't interact with the shell until it is complete, however we want to keep working on our machines, so we need that shell open. Fortunately we can control how our processes run with jobs: 

<b>Sending a job to the background</b>

Appending an ampersand (&) to the command will run it in the background so you can still use your shell. Let's see an example:

<pre>$ sleep 1000 &
$ sleep 1001 &
$ sleep 1002 &
</pre>

<b>View all background jobs</b>

Now you can view the jobs you just sent to the background.

<pre>$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &

</pre>

This will show you the job id in the first column, then the status and the command that was run. The <b>+</b> next to the job ID means that it is the most recent background job that started. The job with the <b>-</b> is the second most recent command.

<b>Sending a job to the background on existing job</b>

If you already ran a job and want to send it to the background, you don't have to terminate it and start over again. First suspend the job with Ctrl-Z, then run the <b>bg</b> command to send it to the background.

<pre>
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &

pete@icebox ~ $ jobs

[1]    Running     sleep 1000 &
[2]    Running     sleep 1001 &
[3]-   Running     sleep 1002 &
[4]+   Running     sleep 1003 &
</pre>

<b>Moving a job from the background to the foreground</b>

To move a job out of the background just specify the job ID you want. If you run fg without any options, it will bring back the most recent background job (the job with the + sign next to it)

<pre>$ fg %1</pre>

<b>Kill background jobs</b>

Similar to moving jobs out of the background, you can use the same form to kill the processes by using their Job ID.

<pre>kill %1</pre>

## Exercise

Move some jobs between the background and the foreground

## Quiz Question

What command is used to list background jobs?

## Quiz Answer

jobs
