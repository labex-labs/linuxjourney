# route

## Lesson Content

We've already discussed viewing our routing tables with the route command, if you wanted to add or remove routes you can do so manually.

<b>Add a new route</b>

<pre>
$ sudo route add -net 192.168.2.1/23 gw 10.11.12.3
</pre>

<b>Delete a route</b>

<pre>
$ sudo route del -net 192.168.2.1/23
</pre>

You can also perform these changes with the <b>ip</b> command:

<b>To add a route</b>
<pre>
$ ip route add 192.168.2.1/23 via 10.11.12.3
</pre>

<b>To delete a route</b>
<pre>
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
</pre>

## Exercise

There are no exercises for this lesson but you can read more information on commands discussed here in the man pages

<pre>$ man route</pre>

<pre>$ man ip-route</pre>

## Quiz Question

What is the command flag to delete a route?

## Quiz Answer

del
