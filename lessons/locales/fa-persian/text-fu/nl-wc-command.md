# wc and nl

## Lesson Content

The wc (word count) command shows the total count of words in a file. 

<pre>$ wc /etc/passwd
 96     265    5925 /etc/passwd
</pre>

It display the number of lines, number of words and number of bytes, respectively.

To just see just the count of a certain field, use the -l, -w, or -c respectively. 

<pre>$ wc -l /etc/passwd
96</pre>

Another command you can use to check the count of lines on a file is the nl (number lines) command. 

<pre>
file1.txt
i
like
turtles
</pre>

<pre>$ nl file1.txt
1. i
2. like
3. turtles
</pre>

## Exercise

How would you get the total count of lines by using the nl file without searching through the entire output? Hint: Use some of the other commands you learned in this course.

## Quiz Question

What command would you use to get the total number of words in a file and just the words?

## Quiz Answer

wc -w