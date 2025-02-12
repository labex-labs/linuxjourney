# Users and Groups

## Lesson Content

In any traditional operating system, there are users and groups. They exist solely for access and permissions. When running a process, it will run as the owner of that process whether that is Jane or Bob. File access and ownership is also permission dependent. You wouldn't want Jane to see Bob's documents and vice versa. 

Each user has their own home directory where their user specific files get stored, this is usually located in /home/username, but can vary in different distributions. 

The system uses user ids (UID) to manage users, usernames are the friendly way to associate users with identification, but the system identifies users by their UID. The system also uses groups to manage permissions, groups are just sets of users with permission set by that group, they are identified by the system with their group ID (GID).

In Linux, you'll have users in addition to the normal humans that use the system. Sometimes these users are system daemons that continuously run processes to keep the system functioning. One of the most important users is root or superuser, root is the most powerful user on the system, root can access any file and start and terminate any process. For that reason, it can be dangerous to operate as root all the time, you could potentially remove system critical files. Luckily, if root access is needed and a user has root access, they can run a command as root instead with the sudo command. The sudo command (superuser do) is used to run a command with root access, we'll go more in depth on how a user receives root access in a later lesson.

Go ahead and try to view a protected file like /etc/shadow:

<pre>$ cat /etc/shadow</pre>

Notice how you get a permission denied error, look at the permissions with: 

<pre>$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
</pre>

We haven't gone through permissions yet, but what's happening here is that root is the owner of the file and you'll need root access or be part of the shadow group to read the contents. Now run the command with sudo:

<pre>$ sudo cat /etc/shadow</pre>

Now you'll be able to see the contents of the file!

## Exercise

No exercises for this lesson.

## Quiz Question

What command do you use to run as root?

## Quiz Answer

sudo