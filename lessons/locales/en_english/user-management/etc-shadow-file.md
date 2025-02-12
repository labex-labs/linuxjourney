# /etc/shadow

## Lesson Content

The /etc/shadow file is used to store information about user authentication. It requires superuser read permissions. 

<pre>$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
</pre>

You'll notice that it looks very similar to the contents of /etc/passwd, however in the password field you'll see an encrypted password. The fields are separated by colons as followed:

<ol>
<li>Username</li>
<li>Encrypted password</li>
<li>Date of last password changed - expressed as the number of days since Jan 1, 1970. If there is a 0 that means the user should change their password the next time they login</li>
<li>Minimum password age - Days that a user will have to wait before being able to change their password again</li>
<li>Maximum password age - Maximum number of days before a user has to change their password</li>
<li>Password warning period - Number of days before a password is going to expire</li>
<li>Password inactivity period - Number of days after a password has expired to allow login with their password</li>
<li>Account expiration date - date that user will not be able to login</li>
<li>Reserved field for future use</li>
</ol>

In most distributions today, user authentication doesn't rely on just the /etc/shadow file, there are other mechanisms in place such as PAM (Pluggable Authentication Modules) that replace authentication.

## Exercise

Take a look at the /etc/shadow file

## Quiz Question

No questions move along!

## Quiz Answer