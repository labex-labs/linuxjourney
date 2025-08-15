# Setgid

## Lesson Content

Similar to the set user ID permission bit, there is a set group ID (SGID) permission bit. This bit allows a program to run as if it was a member of that group.

Let's look at one example:

<pre>$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
</pre>

We can see now that the permission bit is in the group permission set.

<b>Modifying SGID</b>

<pre>$ sudo chmod g+s myfile
$ sudo chmod 2555 myfile
</pre>

The numerical representation for SGID is 2.

## Exercise

No exercises for this lesson.

## Quiz Question

What number represents the SGID?

## Quiz Answer

2
