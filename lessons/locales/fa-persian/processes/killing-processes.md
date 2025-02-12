# kill (Terminate)

## Lesson Content

You can send signals that terminate processes, such a command is aptly named the kill command. 

<pre>$ kill 12445</pre>

The 12445 is the PID of the process you want to kill. By default it sends a TERM signal. The SIGTERM signal is sent to a process to request its termination by allowing it to cleanly release its resources and saving its state. 

You can also specify a signal with the kill command: 

<pre>$ kill -9 12445</pre>

This will run the SIGKILL signal and kill the process. 

<b>Differences between SIGHUP, SIGINT, SIGTERM, SIGKILL, SIGSTOP?</b>

These signals all sound reasonably similar, but they do have their differences. 

<ul>
<li>SIGHUP - Hangup, sent to a process when the controlling terminal is closed. For example, if you closed a terminal window that had a process running in it, you would get a SIGHUP signal. So basically you've been hung up on</li>
<li>SIGINT - Is an interrupt signal, so you can use Ctrl-C and the system will try to gracefully kill the process</li>
<li>SIGTERM - Kill the process, but allow it to do some cleanup first</li>
<li>SIGKILL - Kill the process, kill it with fire, doesn't do any cleanup</li>
<li>SIGSTOP - Stop/suspend a process</li>
</ul>

## Exercise

Kill some processes using different signals.

## Quiz Question

What is the signal name for the default kill command?

## Quiz Answer

SIGTERM