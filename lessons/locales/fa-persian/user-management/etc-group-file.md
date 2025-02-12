# /etc/group

## Lesson Content

Another file that is used in user management is the /etc/group file. This file allows for different groups with different permissions. 

<pre>$ cat /etc/group

root:*:0:pete
</pre>

Very similar to the /etc/password field, the /etc/group fields are as follows:

<ol>
<li>Group name</li>
<li>Group password - there isn't a need to set a group password, using an elevated privilege like sudo is standard. A "*" will be put in place as the default value.</li>
<li>Group ID (GID)</li>
<li>List of users - you can manually specify users you want in a specific group</li>
</ol>

## Exercise

Run the command <b>groups</b>. What do you see?

## Quiz Question

What is the GID of root?

## Quiz Answer

0