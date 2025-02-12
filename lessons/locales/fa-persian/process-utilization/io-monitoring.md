# I/O Monitoring

## Lesson Content

We can also monitor CPU usage as well as monitor disk usage with a handy tool known as <b>iostat</b>

<pre>
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
</pre>

The first part is the CPU information:

<ul>
<li>%user - Show the percentage of CPU utilization that occurred while executing at the user level (application)</li>
<li>%nice - Show the percentage of CPU utilization that occurred while executing at the user level with nice priority.user CPU utilization with nice priorities</li>
<li>%system - Show the percentage of CPU utilization that occurred while executing at the system level (kernel).</li>
<li>%iowait - Show the percentage of time that the CPU or CPUs were idle during which the system had an outstanding disk I/O request.</li>
<li>%steal - Show the percentage of time spent in involuntary wait by the virtual CPU or CPUs while the hypervisor was servicing another virtual processor.</li>
<li>%idle - Show the percentage of time that the CPU or CPUs were idle and the system did not have an outstanding disk I/O request.</li>
</ul>

The second part is the disk utilization:

<ul>
<li>tps - Indicate the number of transfers per second that were issued to the device. A transfer is an I/O request to the device. Multiple logical requests can be combined into a single I/O request to the device. A transfer is of indeterminate size.</li>
<li>kB_read/s - Indicate the amount of data read from the device expressed in kilobytes per second.</li>
<li>kB_wrtn/s - Indicate the amount of data written to the device expressed in kilobytes per second.</li>
<li>kB_read - The total number of kilobytes read.</li>
<li>kB_wrtn - The total number of kilobytes written.</li>
</ul>

## Exercise

Use iostat to view your disk usage.

## Quiz Question

What command can be used to view I/O and CPU usage?

## Quiz Answer

iostat