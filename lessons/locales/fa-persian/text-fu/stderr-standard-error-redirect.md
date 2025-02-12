# stderr (Standard Error)

## Lesson Content

Let's try something a little different now, let's try to list the contents of a directory that doesn't exist on your system and redirect the output to the peanuts.txt file again.

<pre>$ ls /fake/directory > peanuts.txt </pre>

What you should see is: 

<pre>ls: cannot access /fake/directory: No such file or directory</pre>

Now you're probably thinking, shouldn't that message have been sent to the file? There is actually another I/O stream in play here called standard error (stderr). By default, stderr sends its output to the screen as well, it's a completely different stream than stdout. So you'll need to redirect its output a different way. 

Unfortunately the redirector is not as nice as using <b>&lt;</b> or <b>&gt;</b> but it's pretty close. We will have to use file descriptors. A file descriptor is a non-negative number that is used to access a file or stream. We will go in depth about this later, but for now know that the file descriptor for stdin, stdout and stderr is 0, 1, and 2 respectively. 

So now if we want to redirect our stderr to the file we can do this: 

<pre>$ ls /fake/directory 2> peanuts.txt</pre>

You should see just the stderr messages in peanuts.txt. 

Now what if I wanted to see both stderr and stdout in the peanuts.txt file? It's possible to do this with file descriptors as well: 

<pre>$ ls /fake/directory > peanuts.txt 2>&1</pre>

This sends the results of ls /fake/directory to the peanuts.txt file and then it redirects stderr to the stdout via 2>&1. The order of operations here matters, 2>&1 sends stderr to whatever stdout is pointing to. In this case stdout is pointing to a file, so 2>&1 also sends stderr to a file. So if you open up that peanuts.txt file you should see both stderr and stdout. In our case, the above command only outputs stderr.

There is a shorter way to redirect both stdout and stderr to a file:

<pre>$ ls /fake/directory &> peanuts.txt</pre>

Now what if I don't want any of that cruft and want to get rid of stderr messages completely? Well you can also redirect output to a special file call /dev/null and it will discard any input.

<pre>$ ls /fake/directory 2> /dev/null</pre>

## Exercise

What is the following command doing? 

<pre>$ ls /fake/directory >> /dev/null 2>&1</pre>

## Quiz Question

What is the redirector for stderr?

## Quiz Answer

2>
