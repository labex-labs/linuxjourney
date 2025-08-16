# Authentication Logging

## Lesson Content

Authentication logging can be very useful to look at if you are having issues logging in.

**/var/log/auth.log**

This file contains system authorization logs, such as user logins and the authentication methods used.

Sample snippet:

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

## Exercise

Perform some failed login attempts, and then a successful one. Afterward, examine your `/var/log/auth.log` file to see what occurred.

## Quiz Question

What log file is used for user authentication?

## Quiz Answer

`auth.log`
