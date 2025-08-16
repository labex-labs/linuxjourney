# device types

## Lesson Content

Before we chat about how devices are managed, let's actually take a look at some devices.

<pre>$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
</pre>

The columns are as follows from left to right:

<ul>
<li>Permissions</li>
<li>Owner</li>
<li>Group</li>
<li>Major Device Number</li>
<li>Minor Device Number</li>
<li>Timestamp</li>
<li>Device Name</li>
</ul>

Remember in the ls command you can see the type of file with the first bit on each line. Device files are denoted as the following:

<ul>
<li>c - character</li>
<li>b - block</li>
<li>p - pipe</li>
<li>s - socket</li>
</ul>

<b>Character Device</b>

These devices transfer data, but one a character at a time. You'll see a lot of pseudo devices (/dev/null) as character devices, these devices aren't really physically connected to the machine, but they allow the operating system greater functionality.

<b>Block Device</b>

These devices transfer data, but in large fixed-sized blocks. You'll most commonly see devices that utilize data blocks as block devices, such as harddrives, filesystems, etc.

<b>Pipe Device</b>

Named pipes allow two or more processes to communicate with each other, these are similar to character devices, but instead of having output sent to a device, it's sent to another process.

<b>Socket Device</b>

Socket devices facilitate communication between processes, similar to pipe devices but they can communicate with many processes at once.

<b>Device Characterization</b>

Devices are characterized using two numbers, <b>major device number</b> and <b>minor device number</b>. You can see these numbers in the above ls example, they are separated by a comma. For example, let's say a device had the device numbers: <b>8, 0</b>:

The major device number represents the device driver that is used, in this case 8, which is often the major number for sd block devices. The minor number tells the kernel which unique device it is in this driver class, in this case 0 is used to represent the first device (a).

## Exercise

Look at your /dev directory and find out what types of devices you can see.

## Quiz Question

What is the symbol for character devices in the ls -l command?

## Quiz Answer

c
