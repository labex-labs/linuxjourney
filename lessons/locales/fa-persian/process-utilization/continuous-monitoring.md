# Continuous Monitoring

## Lesson Content

These monitoring tools are good to look at when your machine is having issues, but what about machines that are having issues when you aren't looking. For those, you'll need to use a continuous monitoring tool, something that will collect, report and save your system activity information. In this lesson we will go over a great tool to use <b>sar</b>.

<b>Installing sar</b>
Sar is a tool that is used to do historical analysis on your system, first make sure you have it installed by installing the sysstat package <b>sudo apt install sysstat</b>.

<b>Setting up data collection</b>
Usually once you install sysstat, your system will automatically start collecting data, if it doesn't you can enable it by modifying the ENABLED field in /etc/default/sysstat.

<b>Using sar</b>

<pre>$ sudo sar -q</pre>

This command will list the details from the start of the day.

<pre>$ sudo sar -r</pre>

This will list the details of memory usage from the start of the day.

<pre>$ sudo sar -P</pre>

This will list the details of CPU usage. 

To see a view of a different day, you can go into /var/log/sysstat/saXX where XX is the day you want to view. 

<pre>$sar -q /var/log/sysstat/sa02</pre>

## Exercise

Install sar on your system and start collecting and analyzing your system resource utilization.

## Quiz Question

What is a good tool to use for monitoring system resources?

## Quiz Answer

sar
