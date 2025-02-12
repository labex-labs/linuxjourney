# head

## Lesson Content

Let's say we have a very long file, in fact we have many to choose from, go ahead and cat /var/log/syslog. You should see pages upon pages of text. What if I just wanted to see the first couple of lines in this text file? Well we can do that with the head command, by default the head command will show you the first 10 lines in a file.

<pre>$ head /var/log/syslog</pre>

You can also modify the line count to whatever you choose, let's say I wanted to see the first 15 lines instead. 

<pre>$ head -n 15 /var/log/syslog</pre>

The -n flag stands for number of lines. 

## Exercise

What does the following command do and why? 

<pre>$ head -c 15 /var/log/syslog</pre>

## Quiz Question

What flag would you use to change the number of lines you want to view for the head command?

## Quiz Answer

-n