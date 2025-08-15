# NFS

## Lesson Content

The most standard network file share for Linux is NFS (Network File System), NFS allows a server to share directories and files with one or more clients over the network.

We won't get into the details of how to create an NFS server as it can get complex, however we will discuss setting up NFS clients.

<b>Setting up NFS client</b>

<pre>$ sudo service nfsclient start
$ sudo mount server:/directory /mount_directory</pre>

<b>Automounting</b>

Let's say you use the NFS server quite often and you want to keep it permanently mounted, normally you think you'd edit the /etc/fstab file, but you may not always get a connection to the server and that can cause issues on bootup. Instead what you want to do is setup automounting so that you can connect to the NFS server when you need to. This is done with the <b>automount</b> tool or in recent versions of Linux <b>amd</b>. When a file is accessed in a specified directory, automount will look up the remote server and automatically mount it.

## Exercise

Read the manpage for NFS to learn more.

## Quiz Question

What tool is used to manage mount points automatically?

## Quiz Answer

automount
