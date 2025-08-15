# rm (Remove)

## Lesson Content

Now I think we have too many files, let’s remove some files. To remove files you can use the rm command. The rm (remove) command is used to delete files and directories.

<pre>$ rm file1</pre>

Take caution when using rm, there is no magical trash can that you can fish out removed files. Once they are gone, they are gone for good, so be careful.

Fortunately there are some safety measures put into place, so the average joe can’t just remove a bunch of important files. Write-protected files will prompt you for confirmation before deleting them. If a directory is write-protected it will also not be easily removed.

Now if you don’t care about any of that, you can absolutely remove a bunch of files.

<pre>$ rm -f file1</pre>

-f or force option tells rm to remove all files, whether they are write protected or not, without prompting the user (as long as you have the appropriate permissions).

<pre>$ rm -i file</pre>

Adding the -i flag like many of the other commands, will give you a prompt on whether you want to actually remove the files or directories.

<pre>$ rm -r directory</pre>

You can’t just rm a directory by default, you’ll need to add the -r flag (recursive) to remove all the files and any subdirectories it may have.

You can remove a directory with the rmdir command.

<pre>$ rmdir directory</pre>

## Exercise

<ol>
<li>Create a file called -file (don't forget the dash!).</li>
<li>Remove that file.</li>
</ol>

## Quiz Question

How do you remove a file called myfile?

## Quiz Answer
