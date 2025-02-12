# Samba

## Lesson Content

In the early days of computing, it became necessary for Windows machines to share files with Linux machines, thus the Server Message Block (SMB) protocol was born. SMB was used for sharing files between Windows operating systems (Mac also has file sharing with SMB) and then it was later cleaned up and optimized in the form of the Common Internet File System (CIFS) protocol. 

Samba is what we call the Linux utilities to work with CIFS on Linux. In addition to file sharing, you can also share resources like printers. 

<b>Create a network share with Samba</b>

Let's go through the basic steps to create a network share that a Windows machine can access:

<b>Install Samba</b>

<pre>$ sudo apt update
$ sudo apt install samba</pre>

<b>Setup smb.conf</b>

The configuration file for Samba is found at /etc/samba/smb.conf, this file should tell the system what directories should be shared, their access permissions, and more options. The default smb.conf comes with lots of commented code already and you can use those as an example to write your own configurations.

<pre>$ sudo vi /etc/samba/smb.conf</pre>

<b>Setup up a password for Samba</b>

<pre>$ sudo smbpasswd -a [username]</pre>

<b>Create a shared directory</b>

<pre>$ mkdir /my/directory/to/share</pre>

<b>Restart the Samba service</b>

<pre>$ sudo service smbd restart</pre>

<b>Accessing a Samba share via Windows</b>

In Windows, just type in the network connection in the run prompt: \\HOST\sharename.

<b>Accessing a Samba/Windows share via Linux</b>

<pre>$ smbclient //HOST/directory -U user</pre>

The Samba package includes a command line tool called <b>smbclient</b> that you can use to access any Windows or Samba server. Once you're connected to the share you can navigate and transfer files.

<b>Attach a Samba share to your system</b>

Instead of transferring files one by one, you can just mount the network share on your system.

<pre>$ sudo mount -t cifs servername:directory mountpount -o user=username,pass=password</pre>

## Exercise

Setup a Samba share, if you don't have one, open up smb.conf and familiarize yourself with the options in the config file.

## Quiz Question

What is the latest protocol used for file transfer between Windows and Linux?

## Quiz Answer

CIFS
