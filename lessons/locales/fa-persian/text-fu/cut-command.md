# cut

## Lesson Content

We're gonna learn a couple of useful commands that you can use to process text. Before we get started, let's create a file that we'll be working with. Copy and paste the following command, once you do that add a TAB in between lazy and dog (hold down Ctrl-v + TAB).

<pre>$ echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt</pre>

First command we'll be learning about is the cut command. It extracts portions of text from a file. 

To extract contents by a list of characters: 

<pre>$ cut -c 5 sample.txt</pre>

This outputs the 5th character in each line of the file. In this case it is "q", note that the space also counts as a character. 

To extract the contents by a field, we'll need to do a little modification: 

<pre>$ cut -f 2 sample.txt</pre>

The -f or field flag cuts text based off of fields, by default it uses TABs as delimiters, so everything separated by a TAB is considered a field. You should see "dog" as your output.

You can combine the field flag with the delimiter flag to extract the contents by a custom delimiter: 

<pre>$ cut -f 1 -d ";" sample.txt</pre>

This will change the TAB delimiter to a ";" delimiter and since we are cutting the first field, the result should be "The quick brown".

## Exercise

What does the following command do? Why?

<pre>$ cut -c 5-10 sample.txt
$ cut -c 5- sample.txt
$ cut -c -5 sample.txt
</pre>

## Quiz Question

What command would you use to get the first character of every line in a file?

## Quiz Answer

cut -c 1