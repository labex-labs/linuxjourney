# Ownership Permissions

## Lesson Content

In addition to modifying permissions on files, you can also modify the group and user ownership of the file as well.

<b>Modify user ownership</b>

<pre>$ sudo chown patty myfile</pre>

This command will set the owner of myfile to patty.

<b>Modify group ownership</b>

<pre>$ sudo chgrp whales myfile</pre>

This command will set the group of myfile to whales.

<b>Modify both user and group ownership at the same time</b>
If you add a colon and groupname after the user you can set both the user and group at the same time.

<pre>$ sudo chown patty:whales myfile</pre>

## Exercise

Modify the group and user of some test files. Afterwards take a look at the permissions with ls -l.

## Quiz Question

What command do you use to change user ownership?

## Quiz Answer

chown
