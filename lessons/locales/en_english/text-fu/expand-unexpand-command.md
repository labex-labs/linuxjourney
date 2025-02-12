# expand and unexpand

## Lesson Content

In our lesson on the cut command, we had our sample.txt file that contained a tab. Normally TABs would usually show a noticeable difference but some text files don't show that well enough. Having TABs in a text file may not be the desired spacing you want. To change your TABs to spaces, use the expand command. 

<pre>$ expand sample.txt</pre>

The command above will print output with each TAB converted into a group of spaces. To save this output in a file, use output redirection like below.

<pre>$ expand sample.txt > result.txt</pre>

Opposite to expand, we can convert back each group of spaces to a TAB with the unexpand command: 

<pre>$ unexpand -a result.txt</pre>

## Exercise

What happens if you just type expand with no file input?

## Quiz Question

What command is used to convert TABs to spaces? 

## Quiz Answer

expand
