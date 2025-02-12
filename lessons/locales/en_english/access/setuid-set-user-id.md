# Setuid

## Lesson Content

There are many cases in which normal users need elevated access to do stuff. The system administrator can't always be there to enter in a root password every time a user needed access to a protected file, so there are special file permission bits to allow this behavior. The Set User ID (SUID) allows a user to run a program as the owner of the program file rather than as themselves.

Let's look at an example: 

Let's say I want to change my password, simple right? I just use the passwd command:

<pre>$ passwd</pre>

What is the password command doing? It's modifying a couple of files, but most importantly it's modifying the /etc/shadow file. Let's look at that file for a second: 

<pre>$ ls -l /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
</pre>

Oh wait a minute here, this file is owned by root? How is it possible that we are able to modify a file owned by root? 

Let's look at another permission set, this time of the command we ran: 

<pre>$ ls -l /usr/bin/passwd

-rwsr-xr-x 1 root root 47032 Dec 1 11:45 /usr/bin/passwd
</pre>

You'll notice a new permission bit here <b>s</b>. This permission bit is the SUID, when a file has this permission set, it allows the users who launched the program to get the file owner's permission as well as execution permission, in this case root. So essentially while a user is running the password command, they are running as root.

That's why we are able to access a protected file like /etc/shadow when we run the passwd command. Now if you removed that bit, you would see that you will not be able to modify /etc/shadow and therefore change your password. 

<b>Modifying SUID</b>

Just like regular permissions there are two ways to modify SUID permissions. 

<i>Symbolic way:</i>
<pre>$ sudo chmod u+s myfile</pre>

<i>Numerical way:</i>
<pre> sudo chmod 4755 myfile</pre>

As you can see the SUID is denoted by a 4 and pre-pended to the permission set. You may see the SUID denoted as a capital <b>S</b> this means that it still does the same thing, but it does not have execute permissions.

## Exercise

Look at the permission for /etc/passwd in detail, do you notice anything else? Files with SUID enabled are also easily distinguishable.

## Quiz Question

What number represents the SUID?

## Quiz Answer

4
