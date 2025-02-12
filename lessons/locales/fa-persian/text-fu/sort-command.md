# sort

## Lesson Content

The sort command is useful for sorting lines.

<pre>
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
</pre>

You can also do a reverse sort: 

<pre>$ sort -r file1.txt
elephant
dog
cow
cat
bird
</pre>

And also sort via numerical value: 

<pre>$ sort -n file1.txt
bird
cat
cow
elephant
dog
</pre>

## Exercise

The real power of sort comes with its ability to be combined with other commands, try the following command and see what happens?

<pre>$ ls /etc | sort -rn</pre>

## Quiz Question

What flag do you use to do a reverse sort?

## Quiz Answer

-r
