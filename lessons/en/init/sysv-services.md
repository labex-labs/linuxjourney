# System V Service

## Lesson Content

There are many command line tools you can use to manage Sys V services.

<b>List services</b>

<pre>$ service --status-all</pre>

<b>Start a service</b>

<pre>$ sudo service networking start</pre>

<b>Stop a service</b>

<pre>$ sudo service networking stop</pre>

<b>Restart a service</b>

<pre>$ sudo service networking restart</pre>

These commands aren't specific to Sys V init systems, you can use these commands to manage Upstart services as well. Since Linux is trying to move away from the more traditional Sys V init scripts, there are still things in place to help that transition.

## Exercise

Manage a couple of services and change their states, what do you observe?

## Quiz Question

What is the command to stop a service named peanut with Sys V?

## Quiz Answer

sudo service peanut stop
