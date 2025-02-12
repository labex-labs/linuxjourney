# Anatomy of a Disk

## Lesson Content

Hard disks can be subdivided into partitions, essentially making multiple block devices. Recall such examples as, /dev/sda1 and /dev/sda2, /dev/sda is the whole disk, but /dev/sda1 is the first partition on that disk. Partitions are extremely useful for separating data and if you need a certain filesystem, you can easily create a partition instead of making the entire disk one filesystem type.

<b>Partition Table</b>

Every disk will have a partition table, this table tells the system how the disk is partitioned. This table tells you where partitions begin and end, which partitions are bootable, what sectors of the disk are allocated to what partition, etc. There are two main partition table schemes used, Master Boot Record (MBR) and GUID Partition Table (GPT).

<b>Partition</b>

Disks are comprised of partitions that help us organize our data. You can have multiple partitions on a disk and they can't overlap each other. If there is space that is not allocated to a partition, then it is known as free space. The types of partitions depend on your partition table. Inside a partition, you can have a filesystem or dedicate a partition to other things like swap (we'll get to that soon).

<i>MBR</i>

<ul>
<li>Traditional partition table, was used as the standard</li>
<li>Can have primary, extended, and logical partitions</li>
<li>MBR has a limit of four primary partitions</li>
<li>Additional partitions can be made by making a primary partition into an extended partition (there can only be one extended partition on a disk). Then inside the extended partition you add logical partitions. The logical partitions are used just like any other partition. Silly I know.</li> 
<li>Supports disks up to 2 terabytes</li>
</ul>

<i>GPT</i>

<ul>
<li>GUID Partition Table (GPT) is becoming the new standard for disk partitioning</li>
<li>Has only one type of partition and you can make many of them</li>
<li>Each partition has a globally unique ID (GUID)</li>
<li>Used mostly in conjunction with UEFI based booting (we'll get into details in another course)</li> 
</ul>

<b>Filesystem Structure</b>

We know from our previous lesson that a filesystem is an organized collection of files and directories. In its simplest form, it is comprised of a database to manage files and the actual files themselves, however we're going to go into a little more detail. 

<ul>
<li>Boot block - This is located in the first few sectors of the filesystem, and it's not really used the by the filesystem. Rather, it contains information used to boot the operating system. Only one boot block is needed by the operating system. If you have multiple partitions, they will have boot blocks, but many of them are unused.</li>
<li>Super block - This is a single block that comes after the boot block, and it contains information about the filesystem, such as the size of the inode table, size of the logical blocks and the size of the filesystem.</li>
<li>Inode table - Think of this as the database that manages our files (we have a whole lesson on inodes, so don't worry). Each file or directory has a unique entry in the inode table and it has various information about the file.</li>
<li>Data blocks - This is the actual data for the files and directories.</li>
</ul>
 
Let's take a look at the different partition tables. Below is an example of a partition using the MBR partitioning table (msdos). You can see the primary, extended and logical partitions on the machine.

<pre>
pete@icebox:~$ sudo parted -l
Model: Seagate (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Number  Start   End     Size    Type      File system     Flags
 1      1049kB  6860MB  6859MB  primary   ext4            boot
 2      6861MB  21.5GB  14.6GB  extended
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
 6      7381MB  21.5GB  14.1GB  logical   xfs
</pre>


This example is GPT, using just a unique ID for the partitions.

<pre>
Model: Thumb Drive (scsi)
Disk /dev/sdb: 4041MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt

Number  Start   End     Size     File system  Name        Flags
 1      17.4kB  1000MB  1000MB                first
 2      1000MB  4040MB  3040MB                second
</pre>

## Exercise

Run <b>parted -l</b> on your machine and evaluate your results.

## Quiz Question

What partition type is used to create more than 4 partitions in the MBR partitioning scheme?

## Quiz Answer

extended
