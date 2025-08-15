# Authentication Logging

## Lesson Content

Authentication logging can be very useful to look at if you are having issues logging in.

<b>/var/log/auth.log</b>

This contains system authorization logs, such as user login and the authentication method used.

Sample snippet:

<pre>
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
</pre>

## Exercise

Do some failed logins and then a successful one, look at your /var/log/auth.log and see what happened.

## Quiz Question

What log is used for user authentication?

## Quiz Answer

auth.log
