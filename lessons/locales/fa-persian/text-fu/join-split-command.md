# join and split

## Lesson Content

The join command allows you to join multiple files together by a common field: 

Let's say I had two files that I wanted to join together:
<pre>file1.txt
1 John
2 Jane
3 Mary

file2.txt
1 Doe
2 Doe
3 Sue

$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
</pre>

See how it joined together my files? They are joined together by the first field by default and the fields have to be identical, if they are not you can sort them, so in this case the files are joined via 1, 2, 3. 

How would we join the following files? 

<pre>file1.txt
John 1
Jane 2
Mary 3

file2.txt
1 Doe
2 Doe
3 Sue
</pre>

To join this file you need to specify which fields you are joining, in this case we want field 2 on file1.txt and field 1 on file2.txt, so the command would look like this:

<pre>
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
</pre>

-1 refers to file1.txt and -2 refers to file2.txt. Pretty neat. You can also split a file up into different files with the split command: 

<pre>$ split somefile</pre>

This will split it into different files, by default it will split them once they reach a 1000 line limit. The files are named x** by default.

## Exercise

Join two files with different number of lines in each file, what happens?

## Quiz Question

What command would you use to join files named cat dog cow?

## Quiz Answer

join cat dog cow