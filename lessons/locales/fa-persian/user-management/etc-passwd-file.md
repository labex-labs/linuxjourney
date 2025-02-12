# /etc/passwd

## Lesson Content

Remember that usernames aren't really identifications for users. The system uses a user ID (UID) to identify a user. To find out what users are mapped to what ID, look at the /etc/passwd file. 

<pre>$ cat /etc/passwd</pre>

This file shows you a list of users and detailed information about them. For example, the first line in this file most likely looks like this:

<pre>root:x:0:0:root:/root:/bin/bash</pre>

Each line displays user information for one user, most commonly you'll see the root user as the first line. There are many fields separated by colons that tell you additional information about the user, let's look at them all:

<ol>
<li>Username</li>
<li>User's password - the password is not really stored in this file, it's usually stored in the /etc/shadow file. We'll discuss more in the next lesson about /etc/shadow, but for now, know that it contains encrypted user passwords. You can see many different symbols that are in this field, if you see an "x" that means the password is stored in the /etc/shadow file, a "*" means the user doesn't have login access and if there is a blank field that means the user doesn't have a password.</li>
<li>The user ID - as you can see root has the UID of 0</li>
<li>The group ID</li>
<li>GECOS field - This is used to generally leave comments about the user or account such as their real name or phone number, it is comma delimited.</li>
<li>User's home directory</li>
<li>User's shell - you'll probably see a lot of user's defaulting to bash for their shell</li>
</ol>

Normally in a user's setting page, you would expect you see just human users. However, you'll notice /etc/passwd contains other users. Remember that users are really only on the system to run processes with different permissions. Sometimes we want to run processes with pre-determined permissions. For example, the daemon user is used for daemon processes.

Also should note that you can edit the /etc/passwd file by hand if you want to add users and modify information with the <b>vipw</b> tool, however things like these are best left to the tools we will discuss in a later lesson such as useradd and userdel.

## Exercise

Look at your /etc/passwd file, take a look at some of the users and note the access they have. 

## Quiz Question

If a user doesn't have login access how is that denoted in /etc/passwd?

## Quiz Answer

*