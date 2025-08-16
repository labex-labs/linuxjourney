# File Permissions

## Lesson Content

As we learned previously, files have different permissions or file modes. Let's look at an example:

<pre>$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
</pre>

There are four parts to a file's permissions. The first part is the filetype, which is denoted by the first character in the permissions, in our case since we are looking at a directory it shows <b>d</b> for the filetype. Most commonly you will see a <b>-</b> for a regular file.

The next three parts of the file mode are the actual permissions. The permissions are grouped into 3 bits each. The first 3 bits are user permissions, then group permissions and then other permissions. I've added the pipe to make it easier to differentiate.

<pre>d | rwx | r-x | r-x </pre>

Each character represent a different permission:
<ul>
<li>r: readable</li>
<li>w: writable</li>
<li>x: executable (basically an executable program)</li>
<li>-: empty</li>
</ul>

So in the above example, we see that the user pete has read, write and execute permissions on the file. The group penguins has read and execute permissions. And finally, the other users (everyone else) has read and execute permissions.

## Exercise

Use the ls -l command on multiple files and recite their permissions, user and group.

## Quiz Question

What permission bit is used for executable?

## Quiz Answer

x
