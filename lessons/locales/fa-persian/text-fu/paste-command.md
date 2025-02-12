# paste

## Lesson Content

The paste command is similar to the cat command, it merges lines together in a file. Let's create a new file with the following contents: 

<pre>
sample2.txt
The
quick
brown
fox
</pre>

Let's combine all these lines into one line: 

<pre>$ paste -s sample2.txt</pre>

The default delimiter for paste is TAB, so now there is one line with TABs separating each word.

Let's change this delimiter (-d) to something a little more readable: 

<pre>$ paste -d ' ' -s sample2.txt</pre>

Now everything should be on one line delimited by spaces.

## Exercise

Try to paste multiple files together, what happens?

## Quiz Question

What flag do you use with paste to make everything go on one line? 

## Quiz Answer

-s