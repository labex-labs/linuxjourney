# cd (Change Directory)

## Lesson Content

Now that you know where you are, let’s see if we can move around the filesystem a bit. Remember we’ll need to navigate our way using paths. There are two different ways to specify a path, with absolute and relative paths.

<ul>
<li>Absolute path: This is the path from the root directory. The root is the head honcho. The root directory is commonly shown as a slash. Every time your path starts with / it means you are starting from the root directory. For example, /home/pete/Desktop.</li>

<li>Relative path: This is the path from where you are currently in filesystem. If I was in location /home/pete/Documents and wanted to get to a directory inside Documents called taxes, I don’t have to specify the whole path from root like /home/pete/Documents/taxes, I can just go to taxes/ instead.</li>
</ul>

Now that you know how paths work, we just need something to help us change to the directory we want to. Luckily, we have cd or “change directory” to do that.

<pre>$ cd /home/pete/Pictures</pre>

So now I've changed my directory location to /home/pete/Pictures.

Now from this directory I have a folder inside called Hawaii, I can navigate to that folder with:

<pre>$ cd Hawaii</pre>

Notice how I just used the name of the folder? It’s because I was already in /home/pete/Pictures.

It can get pretty tiring navigating with absolute and relative paths all the time, luckily there are some shortcuts to help you out.

<ul>
<li>. (current directory). This is the directory you are currently in. </li>
<li>.. (previous directory). Takes you to the directory above your current.</li>
<li>~ (home directory). This directory defaults to your “home directory”. Such as /home/pete.</li>
<li>- (previous directory). This will take you to the previous directory you were just at.</li>
</ul>

<pre>$ cd .
$ cd ..
$ cd ~
$ cd -
</pre>
Give them a try!

## Exercise

<ol>
<li>Run the cd command without any flags, where does it take you?</li>
</ol>

## Quiz Question

If you are in /home/pete/Pictures and wanted to go to /home/pete, what’s a good shortcut to use?

## Quiz Answer

cd ..
