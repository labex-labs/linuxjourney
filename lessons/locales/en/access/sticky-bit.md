# The Sticky Bit

## Lesson Content

One last special permission bit I want to talk about is the sticky bit.

This permission bit, "sticks a file/directory" this means that only the owner or the root user can delete or modify the file. This is very useful for shared directories. Take a look at the example below:

<pre>$ ls -ld /tmp
drwxrwxrwxt 6 root root 4096 Dec 15 11:45 /tmp
</pre>

You'll see a special permission bit at the end here <b>t</b>, this means everyone can add files, write files, modify files in the /tmp directory, but only root can delete the /tmp directory.

<b>Modify sticky bit</b>

<pre>$ sudo chmod +t mydir

$ sudo chmod 1755 mydir</pre>

The numerical representation for the sticky bit is <b>1</b>

## Exercise

What other files and directories do you think have a sticky bit enabled?

## Quiz Question

What symbol represents the sticky bit?

## Quiz Answer

t
