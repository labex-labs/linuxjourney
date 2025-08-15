# dd

## Lesson Content

The dd tool is super useful for converting and copying data. It reads input from a file or data stream and writes it to a file or data stream.

Consider the following command:

<pre>$ dd if=/home/pete/backup.img of=/dev/sdb bs=1024 </pre>

This command is copying the contents of backup.img to /dev/sdb. It will copy the data in blocks of 1024 bytes until there is no more data to be copied.

<ul>
<li>if=file - Input file, read from a file instead of standard input</li>
<li>of=file - Output file, write to a file instead of standard output</li>
<li>bs=bytes - Block size, it reads and writes this many bytes of data at a time. You can use different size metrics by denoting the size with a k for kilobyte, m for megabyte, etc, so 1024 bytes is 1k</li>
<li>count=number - Number of blocks to copy.</li>
</ul>

You will see some dd commands that use the count option, usually with dd if you want to copy a file that is 1 megabyte, you'll usually want to see that file as 1 megabyte when it's done being copied. Let's say you run the following command:

<pre>$ dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2</pre>

Our backup.img file is 10M, however, we are saying in this command to copy over 1M 2 times, so only 2M is being copied, leaving our copied data incomplete. Count can come in handy in many situations, but if you are just copying over data, you can pretty much omit count and even bs for that matter. If you really want to optimize your data transfers, then you'll want to start using those options.

dd is extremely powerful, you can use it to make backups of anything, including whole disk drives, restoring disks images, and more. Be careful, that powerful tool can come at a price if you aren't sure what you are doing.

## Exercise

Use the dd command to make a backup of your drive and set the output to a .img file.

## Quiz Question

What is the dd option for block size?

## Quiz Answer

bs
