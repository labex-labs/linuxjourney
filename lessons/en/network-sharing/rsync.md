# rsync

## Lesson Content

Another tool used to copy data from different hosts is rsync (short for remote synchronization). Rsync is very similar to scp, but it does have a major difference. Rsync uses a special algorithm that checks in advanced if there is already data that you are copying to and will only copy over the differences. For example, let's say that you were copying over a file and your network got interrupted, therefore your copy stopped midway. Instead of re-copying everything from the beginning, rsync will only copy over the parts that didn't get copied.

It also verifies the integrity of a file you are copying over with checksums. These small optimizations allow greater file transfer flexibility and makes rsync ideal for directory synchronization remotely and locally, data backups, large data transfers and more.

Some commonly-used rsync options:

<ul>
<li>v - verbose output</li>
<li>r - recursive into directories</li>
<li>h - human readable output</li>
<li>z - compressed for easier transfer, great for slow connections</li>
</ul>

<b>Copy/sync files on the same host</b>

<pre>$ rsync -zvr /my/local/directory/one /my/local/directory/two</pre>

<b>Copy/sync files to local host from a remote host</b>

<pre>$ rsync /local/directory username@remotehost.com:/remote/directory</pre>

<b>Copy/sync files to a remote host from a local host</b>

<pre>$ rsync username@remotehost.com:/remote/directory /local/directory</pre>

## Exercise

Use rsync to sync a directory to another directory, be sure not to overwrite an important directory!

## Quiz Question

What command would be useful for data backups?

## Quiz Answer

rsync
