# Modifying Permissions

## Lesson Content

Changing permissions can easily be done with the <b>chmod</b> command.

First, pick which permission set you want to change, user, group or other. You can add or remove permissions with a <b>+</b> or <b>-</b>, let's look at some examples.

<b>Adding permission bit on a file</b>
<pre>$ chmod u+x myfile</pre>

The above command reads like this: change permission on myfile by adding executable permission bit on the user set. So now the user has executable permission on this file!

<b>Removing permission bit on a file</b>
<pre>$ chmod u-x myfile</pre>

<b>Adding multiple permission bits on a file</b>
<pre>$ chmod ug+w</pre>

There is another way to change permissions using numerical format. This method allows you to change permissions all at once. Instead of using r, w, or x to represent permissions, you'll use a numerical representation for a single permission set. So no need to specify the group with g or the user with u.

The numerical representations are seen below:

<ul>
<li>4: read permission</li>
<li>2: write permission</li>
<li>1: execute permission</li>
</ul>

Let's look at an example:

<pre>$ chmod 755 myfile</pre>

Can you guess what permissions we are giving this file? Let's break this down, so now 755 covers the permissions for all sets. The first number (7) represents user permissions, the second number (5) represents group permissions and the last 5 represents other permissions.

Wait a minute, 7 and 5 weren't listed above, where are we getting these numbers? Remember we are combining all the permissions into one number now, so you'll have to get some math involved.

7 = 4 + 2 + 1, so 7 is the user permissions and it has read, write and execute permissions

5 = 4 + 1, the group has read and execute permissions

5 = 4 +1, and all other users have read and execute permissions

One thing to note: it's not a great idea to be changing permissions nilly willy, you could potentially expose a sensitive file for everyone to modify, however many times you legitimately want to change permissions, just take precaution when using the chmod command.

## Exercise

Change some basic text file permissions and see the bits changing as you do an ls -l.

## Quiz Question

What number represents the read permission when using numerical format?

## Quiz Answer

4
