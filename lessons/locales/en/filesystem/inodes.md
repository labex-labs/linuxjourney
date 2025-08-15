# Inodes

## Lesson Content

Remember how our filesystem is comprised of all our actual files and a database that manages these files? The database is known as the inode table.

<b>What is an inode?</b>

An inode (index node) is an entry in this table and there is one for every file. It describes everything about the file, such as:

<ul>
<li>File type - regular file, directory, character device, etc</li>
<li>Owner</li>
<li>Group</li>
<li>Access permissions</li>
<li>Timestamps - mtime (time of last file modification), ctime (time of last attribute change), atime (time of last access)</li>
<li>Number of hardlinks to the file</li>
<li>Size of the file</li>
<li>Number of blocks allocated to the file</li>
<li>Pointers to the data blocks of the file - most important!</li>
</ul>

Basically inodes store everything about the file, except the filename and the file itself!

<b>When are inodes created?</b>

When a filesystem is created, space for inodes is allocated as well. There are algorithms that take place to determine how much inode space you need depending on the volume of the disk and more. You've probably at some point in your life seen errors for out of disk space issues. Well the same can occur for inodes as well (although less common), you can run out of inodes and therefore be unable to create more files. Remember data storage depends on both the data and the database (inodes).

To see how many inodes are left on your system, use the command <b>df -i</b>

<b>Inode information</b>

Inodes are identified by numbers, when a file gets created it is assigned an inode number, the number is assigned in sequential order. However, you may sometimes notice when you create a new file, it gets an inode number that is lower than others, this is because once inodes are deleted, they can be reused by other files. To view inode numbers run <b>ls -li</b>:

<pre>
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
</pre>

The first field in this command lists the inode number.

You can also see detailed information about a file with stat, it tells you information about the inode as well.

<pre>
pete@icebox:~$ stat ~/Desktop/
  File: ‘/home/pete/Desktop/’
  Size: 6               Blocks: 0          IO Block: 4096   directory
Device: 806h/2054d      Inode: 140         Links: 2
Access: (0755/drwxr-xr-x)  Uid: ( 1000/   pete)   Gid: ( 1000/   pete)
Access: 2016-01-20 20:13:50.647435982 -0800
Modify: 2016-01-20 20:13:06.191675843 -0800
Change: 2016-01-20 20:13:06.191675843 -0800
 Birth: -
</pre>

<b>How do inodes locate files?</b>

We know our data is out there on the disk somewhere, unfortunately it probably wasn't stored sequentially, so we have to use inodes. Inodes point to the actual data blocks of your files. In a typical filesystem (not all work the same), each inode contains 15 pointers, the first 12 pointers point directly to the data blocks. The 13th pointer, points to a block containing pointers to more blocks, the 14th pointer points to another nested block of pointers, and the 15th pointer points yet again to another block of pointers! Confusing, I know! The reason this is done this way is to keep the inode structure the same for every inode, but be able to reference files of different sizes. If you had a small file, you could find it quicker with the first 12 direct pointers, larger files can be found with the nests of pointers. Either way the structure of the inode is the same.

## Exercise

Observe some inode numbers for different files, which ones are usually created first?

## Quiz Question

How do you see how many inodes are left on your system?

## Quiz Answer

df -i
