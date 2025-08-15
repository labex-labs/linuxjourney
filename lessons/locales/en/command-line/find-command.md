# find

## Lesson Content

With all these files we have on the system it can get a little hectic trying to find a specific one. Well there’s a command we can use for that, find!

<pre>$ find /home -name puppies.jpg</pre>

With find you’ll have to specify the directory you’ll be searching it, what you’re searching for, in this case we are trying to find a file by the name of puppies.jpg.

You can specify what type of file you are trying to find.

<pre>$ find /home -type d -name MyFolder</pre>

You can see that I set the type of file I’m trying to find as (d) for directory and I’m still searching by the name of MyFolder.

One cool thing to note is that find doesn’t stop at the directory you are searching, it will look inside any subdirectories that directory may have as well.

## Exercise

<ol>
<li>Find a file from the root directory that has the word net in it.</li>
</ol>

## Quiz Question

What option should I specify for find if I want to search by name?

## Quiz Answer

-name
