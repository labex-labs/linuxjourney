# mv (Move)

## Lesson Content

Used for moving files and also renaming them. Quite similar to the cp command in terms of flags and functionality.

You can rename files like this:

<pre>$ mv oldfile newfile</pre>

Or you can actually move a file to a different directory:

<pre>$ mv file2 /home/pete/Documents</pre>

And move more than one file:

<pre>$ mv file_1 file_2 /somedirectory</pre>

You can rename directories as well:

<pre>$ mv directory1 directory2</pre>

Like cp, if you mv a file or directory it will overwrite anything in the same directory. So you can use the -i flag to prompt you before overwriting anything.

<pre>mv -i directory1 directory2</pre>

Let’s say you did want to mv a file to overwrite the previous one. You can also make a backup of that file and it will just rename the old version with a ~.

<pre>$ mv -b directory1 directory2</pre>

## Exercise

Rename a file, then move that file to a different directory.

## Quiz Question

How do you rename a file called cat to dog?

## Quiz Answer

mv cat dog
